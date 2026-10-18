#!/usr/bin/env python3
"""Transcribe AUDIO/VIDEO LOCAL con autorización, a SRT para analizar en otra fase.

Dependencia opcional: pip install faster-whisper (el modelo se descarga al primer uso).
No descarga videos desde YouTube ni publica el audio o el SRT.
"""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def marca_srt(segundos):
    ms = round(segundos * 1000)
    hh, ms = divmod(ms, 3600000)
    mm, ms = divmod(ms, 60000)
    ss, ms = divmod(ms, 1000)
    return f"{hh:02}:{mm:02}:{ss:02},{ms:03}"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("medio", type=Path, help="Archivo propio o utilizado con autorización")
    p.add_argument("--modelo", default="small", help="Modelo Faster Whisper: tiny/base/small/medium")
    p.add_argument("--idioma", default="es")
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    if not args.medio.exists():
        p.error("El archivo multimedia local no existe")
    destino = args.out or (ROOT / "transcripciones-locales" / (args.medio.stem + ".srt"))
    permitido = (ROOT / "transcripciones-locales").resolve()
    if destino.resolve() != permitido and permitido not in destino.resolve().parents:
        p.error("--out debe quedar dentro de transcripciones-locales/")
    if args.medio.resolve() == destino.resolve():
        p.error("No se puede sobrescribir el archivo original")
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        p.error("Instala la dependencia opcional: pip install faster-whisper")
    model = WhisperModel(args.modelo, device="cpu", compute_type="int8")
    fragmentos, _info = model.transcribe(str(args.medio), language=args.idioma, vad_filter=True)
    salida = []
    for i, s in enumerate(fragmentos, start=1):
        salida.append(
            f"{i}\n{marca_srt(s.start)} --> {marca_srt(s.end)}\n{s.text.strip()}\n"
        )
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text("\n".join(salida), encoding="utf-8")
    print(f"Subtítulos provisionales para corregir manualmente: {destino}")


if __name__ == "__main__":
    main()
