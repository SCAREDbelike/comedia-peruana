#!/usr/bin/env python3
"""Limpia subtítulos SRT/VTT/TXT solo para análisis local y autorizado."""
import argparse
import html
import re
from pathlib import Path

def limpiar(texto: str) -> str:
    salida = []
    anterior = None
    for raw in texto.replace("\ufeff", "").splitlines():
        line = raw.strip()
        if (not line or line.upper() == "WEBVTT" or line.isdigit()
            or "-->" in line or line.startswith(("NOTE ", "STYLE", "REGION"))):
            continue
        line = html.unescape(re.sub(r"<[^>]+>", "", line))
        line = re.sub(r"\{\\[^}]*\}", "", line).strip()
        if line and line != anterior:
            salida.append(line)
        anterior = line
    return "\n".join(salida) + ("\n" if salida else "")

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("archivo", type=Path)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if args.archivo.suffix.lower() not in {".txt", ".vtt", ".srt"}:
        p.error("Formato admitido: .txt, .vtt, .srt")
    if args.archivo.resolve() == args.out.resolve():
        p.error("La salida debe ser distinta de la entrada")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(limpiar(args.archivo.read_text(encoding="utf-8-sig")), encoding="utf-8")
    print(f"Texto de análisis local: {args.out}")

if __name__ == "__main__":
    main()
