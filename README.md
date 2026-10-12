# 🇵🇪 Comedia Peruana — Skill abierta (v0.3.0)

Repositorio de técnicas para generar humor peruano **original**, improvisación, diálogos de barrio, respuestas para directos, biografías de Kick y sketches. La meta es mejorar el *mecanismo* del chiste, no copiar comediantes.

## Qué contiene

- [SKILL.md](SKILL.md) — reglas de personalidad cómica, sorpresa, oralidad y control de clichés.
- [referencias/especial-del-humor.md](referencias/especial-del-humor.md) — primera ficha documental e hipótesis para estudiar *El Especial del Humor*. **No se ha hecho visionado directo validado de episodios.**
- [plantillas/ficha-video.md](plantillas/ficha-video.md) — cómo documentar un sketch.
- [datasets/ejemplos-originales.jsonl](datasets/ejemplos-originales.jsonl) — material original, sin diálogos copiados.
- [scripts/extraer_transcripcion.py](scripts/extraer_transcripcion.py) — limpieza local de subtítulos con permiso.
- [tests/casos.md](tests/casos.md) y [tests/test_transcripcion.py](tests/test_transcripcion.py) — evaluaciones.

## Cómo usar

Copia `SKILL.md` en un agente que acepte skills o instrucciones y pide: «Comedia Peruana, nivel 3, humor de barrio; dame tres remates distintos para un directo, sin clichés».

## Cómo estudiar nuevos videos

1. Elegir un video concreto y guardar enlace, creador y fragmento.
2. Revisar el material directamente y documentar contexto, giro, ritmo, voces y pausas en palabras propias.
3. Generalizar la técnica sin reproducir guiones ni muletillas protegidas.
4. Crear un ejemplo original y pasarlo por pruebas.
5. Documentar el cambio en `CHANGELOG.md`.

**Nota legal:** los videos y transcripciones de terceros no están incluidos en la licencia MIT. No subir transcripciones completas sin autorización.

## Procesar subtítulos localmente

```bash
python scripts/extraer_transcripcion.py video_autorizado.srt --out transcripciones-locales/video.txt
python -m unittest discover -s tests -v
```

Añadir referencias **no reentrena el modelo**; fortalece el contexto y las instrucciones. Si luego se quisiera un fine-tuning auténtico harían falta un modelo compatible, datos utilizables legalmente y una evaluación adecuada.

## Cómo colaborar

Aporta fichas verificables, no copias textuales; puedes proponer situaciones de otras regiones del Perú y calificar ejemplos por sorpresa, naturalidad y ritmo. Lee [CONTRIBUTING.md](CONTRIBUTING.md).

## Estado de avance

v0.3.0 es una primera versión publicada. Los análisis audiovisuales concretos de segmentos y las calificaciones humanas quedan pendientes.
