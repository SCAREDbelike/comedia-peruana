#!/usr/bin/env python3
"""Propone fragmentos de estudio a partir de subtítulos SRT/VTT locales autorizados.

No detecta chistes ni emociones con certeza y nunca modifica el catálogo público.
La salida incluye fragmentos de texto exclusivamente en una carpeta local ignorada.
"""
import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARCA = re.compile(
    r"(?P<inicio>(?:\d{2}:)?\d{2}:\d{2}[.,]\d{3})\s*-->\s*"
    r"(?P<fin>(?:\d{2}:)?\d{2}:\d{2}[.,]\d{3})"
)
LISURAS = re.compile(
    r"\b(?:chucha|carajo|mierda|huev[oó]n(?:a|es|as)?|cojudo(?:s|as)?|puta(?:s)?)\b",
    re.IGNORECASE
)
REACCION = re.compile(
    r"\[(?:risas?|carcajadas?|aplausos?|laughter|laughs|applause)\]"
    r"|\((?:risas?|carcajadas?|aplausos?)\)",
    re.IGNORECASE
)


def segundos(marca):
    partes = marca.replace(",", ".").split(":")
    if len(partes) == 2:
        m, s = partes
        return round(int(m) * 60 + float(s), 3)
    h, m, s = partes
    return round(int(h) * 3600 + int(m) * 60 + float(s), 3)


def tiempo(valor):
    mil = round(valor * 1000)
    h, resto = divmod(mil, 3600000)
    m, resto = divmod(resto, 60000)
    s, ms = divmod(resto, 1000)
    return f"{h:02}:{m:02}:{s:02}.{ms:03}"


def limpiar_linea(linea):
    linea = html.unescape(linea.strip())
    linea = re.sub(r"<[^>]*>", "", linea)
    linea = re.sub(r"\{\\[^}]*\}", "", linea)
    return " ".join(linea.split())


def extraer_cues(contenido):
    """Devuelve intervalos con texto de un SRT/VTT. No infiere hablantes."""
    contenido = contenido.replace("\ufeff", "").replace("\r\n", "\n")
    cues = []
    for bloque in re.split(r"\n\s*\n", contenido):
        lineas = bloque.splitlines()
        for i, linea in enumerate(lineas):
            m = MARCA.search(linea)
            if not m:
                continue
            ini, fin = segundos(m["inicio"]), segundos(m["fin"])
            if fin <= ini:
                break
            texto = " ".join(
                x for x in (limpiar_linea(l) for l in lineas[i + 1:])
                if x and not x.startswith(("NOTE ", "STYLE ", "REGION "))
            )
            if not texto:
                break
            cue = {"inicio": ini, "fin": fin, "texto": texto}
            # Las pistas móviles VTT a veces repiten el texto de la pista anterior.
            if cues and cues[-1]["texto"] == texto and ini <= cues[-1]["fin"] + 0.25:
                cues[-1]["fin"] = max(fin, cues[-1]["fin"])
            else:
                cues.append(cue)
            break
    return sorted(cues, key=lambda c: (c["inicio"], c["fin"]))


def seleccionar_candidatos(cues, max_candidatos=12, incluir_texto=True):
    """Sugiere dónde mirar. Las señales NO prueban que exista un remate."""
    propuestas = []
    for i, cue in enumerate(cues):
        txt = cue["texto"]
        siguiente = cues[i + 1] if i + 1 < len(cues) else None
        separacion = round(max(0, siguiente["inicio"] - cue["fin"]), 3) if siguiente else 0
        etiquetas = []
        puntaje = 0
        if separacion >= 1.2 and siguiente:
            etiquetas.append("pausa_posterior_en_subtitulos")
            puntaje += 2
        if "?" in txt or "¿" in txt:
            etiquetas.append("pregunta_textual")
            puntaje += 1
        if "!" in txt or "¡" in txt:
            etiquetas.append("exclamacion_textual")
            puntaje += 1
        if LISURAS.search(txt):
            etiquetas.append("lisura_textual_contextualizar")
            puntaje += 1
        if REACCION.search(txt):
            etiquetas.append("reaccion_descrita_en_subtitulos_no_verificada_en_audio")
            puntaje += 2
        if not etiquetas:
            continue
        propuesta = {
            "inicio": tiempo(max(0, cue["inicio"] - 3)),
            "fin": tiempo(cue["fin"] + 3),
            "score_heuristico": puntaje,
            "indicios": etiquetas,
            "segundos_hasta_siguiente_subtitulo": separacion,
            "estado": "candidato_sin_revision",
            "mecanismo_comico_confirmado": False
        }
        if incluir_texto:
            propuesta["vista_previa_local"] = txt[:160]
        propuestas.append(propuesta)
    propuestas.sort(key=lambda x: (-x["score_heuristico"], x["inicio"]))
    seleccionadas = propuestas[:max_candidatos]
    return sorted(seleccionadas, key=lambda x: x["inicio"])


def analizar(contenido, video_id, catalogo, max_candidatos=12, incluir_texto=True):
    registro = next((v for v in catalogo["videos"] if v["id"] == video_id), None)
    if registro is None:
        raise ValueError(f"El ID '{video_id}' no existe en videos/catalogo.json")
    cues = extraer_cues(contenido)
    if not cues:
        raise ValueError("No hay marcas de tiempo legibles. Usa SRT o VTT con tiempos.")
    return {
        "video_id": video_id,
        "url": registro["url"],
        "titulo": registro["titulo"],
        "origen": "subtitulos_locales_proporcionados_por_usuario",
        "revision": "pendiente_de_revision_humana",
        "subtitulos_intervalos": len(cues),
        "duracion_ultimo_subtitulo": tiempo(max(x["fin"] for x in cues)),
        "candidatos": seleccionar_candidatos(cues, max_candidatos, incluir_texto),
        "advertencias": [
            "Los candidatos son heurísticos; NO son remates verificados.",
            "Las pausas son huecos entre subtítulos, NO silencios acústicos.",
            "Las voces, gestos, entonación y risas requieren revisión audiovisual.",
            "Si faltan lisuras podría ser censura o error de reconocimiento."
        ]
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--video-id", required=True, help="ID existente en videos/catalogo.json")
    p.add_argument("--subtitulos", required=True, type=Path, help="SRT o VTT con permiso de uso")
    p.add_argument("--out", type=Path, help="JSON LOCAL, por defecto en analisis-locales/")
    p.add_argument("--max-candidatos", type=int, default=12)
    p.add_argument("--sin-texto", action="store_true", help="Omite vistas previas del JSON")
    args = p.parse_args()
    if args.subtitulos.suffix.lower() not in {".srt", ".vtt"}:
        p.error("Usa subtítulos con tiempo (.srt o .vtt)")
    if args.max_candidatos < 1 or args.max_candidatos > 100:
        p.error("--max-candidatos debe estar entre 1 y 100")
    salida = args.out or (ROOT / "analisis-locales" / (args.video_id + ".json"))
    carpeta_permitida = (ROOT / "analisis-locales").resolve()
    # Evitar publicar accidentalmente textos completos de los subtítulos.
    if salida.resolve() != carpeta_permitida and carpeta_permitida not in salida.resolve().parents:
        p.error("--out debe quedar dentro de analisis-locales/")
    if args.subtitulos.resolve() == salida.resolve():
        p.error("La salida no puede sobrescribir la entrada")
    cat = json.loads((ROOT / "videos" / "catalogo.json").read_text(encoding="utf-8"))
    try:
        informe = analizar(
            args.subtitulos.read_text(encoding="utf-8-sig"),
            args.video_id, cat, args.max_candidatos, not args.sin_texto
        )
    except (ValueError, UnicodeError) as e:
        p.error(str(e))
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(json.dumps(informe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Revisión pendiente: {len(informe['candidatos'])} posibles fragmentos -> {salida}")


if __name__ == "__main__":
    main()
