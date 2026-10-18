# Comedia Peruana — Laboratorio abierto de humor (v0.9.0)

**Skill de escritura, análisis e improvisación humorística con identidad peruana.** Investiga las técnicas de los **cómicos ambulantes**, el humor de barrio, los sketches televisivos (como *El Especial del Humor*), el **stand-up**, la sátira cotidiana, los diálogos cómicos y la creación de personajes.

**Propósito:** guiar al asistente a comprender por qué funciona un remate y aplicar ese conocimiento para producir **comedia original** en cualquier formato, sin copiar rutinas ni personajes ajenos.

> No es una colección de chistes robados ni un modelo reentrenado. Es una skill con biblioteca de referencias, reglas de generación, ejemplos originales y pruebas de calidad.

## Explorar

| Recurso | Para qué sirve |
| --- | --- |
| [SKILL.md](SKILL.md) | Instrucciones principales, mecanismos cómicos, improvisación y formatos |
| [analisis/README.md](analisis/README.md) | **Motor de subtítulos y revisión audiovisual** con pasos ejecutables |
| [analisis/estado.json](analisis/estado.json) | Estado de 20 referencias, tres estudiadas desde SRT, ninguna visionada |
| [scripts/analizar_subtitulos.py](scripts/analizar_subtitulos.py) | Candidatos temporales de pausas, preguntas, reacciones descritas y registros |
| [scripts/transcribir_audio.py](scripts/transcribir_audio.py) | Transcripción local opcional de medios autorizados con Faster Whisper |
| [referencias/pragmatica-lisuras.md](referencias/pragmatica-lisuras.md) | Uso contextual de lisuras, sin convertirlas en el remate |
| [videos/README.md](videos/README.md) | **Videoteca con enlaces reales**, procedencia y estados de verificación |
| [videos/catalogo.json](videos/catalogo.json) | Catálogo estructurado con **20 enlaces** y estados de verificación |
| [videos/guia-de-visionado.md](videos/guia-de-visionado.md) | Ruta de estudio de programas, sketches y shows callejeros |
| [referencias/taller-remates-personajes.md](referencias/taller-remates-personajes.md) | Remates, picardía, doble sentido, personajes y actuación |
| [referencias/contexto-cultural-y-fuentes.md](referencias/contexto-cultural-y-fuentes.md) | Fuentes académicas y periodísticas; Víctor Vich |
| [referencias/protocolo-generacion.md](referencias/protocolo-generacion.md) | **Instrucciones operativas para que la IA genere y mejore comedia** |
| [referencias/especial-del-humor.md](referencias/especial-del-humor.md) | Hipótesis de análisis de sketches de televisión |
| [referencias/comicos-ambulantes.md](referencias/comicos-ambulantes.md) | Mecánicas de humor callejero y relación con la audiencia |
| [referencias/mecanismos-comicos.md](referencias/mecanismos-comicos.md) | Herramientas aplicables a stand-up, escena y conversación |
| [plantillas/ficha-video.md](plantillas/ficha-video.md) | Plantilla reproducible para observar escenas |
| [datasets/ejemplos-originales.jsonl](datasets/ejemplos-originales.jsonl) | Material original etiquetado por formato y técnica |
| [tests/casos.md](tests/casos.md) | Banco de pruebas de humor de distintos formatos |
| [scripts/extraer_transcripcion.py](scripts/extraer_transcripcion.py) | Limpieza local de SRT/VTT/TXT autorizados |

## Referencias iniciales

La videoteca reúne **20 referencias enlazadas**, entre ellas:
- *El Especial del Humor*: dos programas de 2004, «Las viejas pitucas de La Molina» y «El Diván con Karla Casos» en dos partes.
- Otros sketches referenciados por una nota periodística (estos enlaces **no se han comprobado mediante visionado**).
- *Los Reyes de la Risa Vol. 2*, El Chino Risas, Los Herederos de la Risa y Los Marcianitos.

[Ir al catálogo de videos →](videos/README.md)

**Ninguna ficha nueva se presenta como video visionado ni contiene transcripciones ajenas.**

## Qué hace la skill

Al activarla, el asistente emplea las referencias y el [protocolo de generación](referencias/protocolo-generacion.md) para idear premisas, construir personajes, proponer cierres alternativos y corregir errores antes de mostrarte su respuesta. Su finalidad es **producir mejores chistes, sketches, diálogos o análisis**, no asignarte tareas de entrenamiento.

## Investigación audiovisual (nuevo en v0.6)

La videoteca tiene 20 enlaces y ahora hay un motor que **procesa SRT/VTT locales** y genera candidatos con marcas temporales para revisión. Opcionalmente se puede transcribir un archivo audiovisual obtenido legítimamente con Faster Whisper. No se descargan videos de YouTube automáticamente, no se guardan transcripciones completas en GitHub ni se finge visionado.

```bash
# Si tienes subtítulos autorizados
python scripts/analizar_subtitulos.py --video-id eh-molina-01 --subtitulos transcripciones-locales/fragmento.srt
# Salida local ignorada por Git: analisis-locales/eh-molina-01.json
```

Guía: [analisis/README.md](analisis/README.md). Prioridad editorial inicial: *Las viejas pitucas de La Molina #01* y *El Chino Risas Vol.1*. Las dos fichas iniciales son **hipótesis**. Las tres fichas, [Marisol y Christian](analisis/fichas/eh-marisol-christian.md), [Jaime y Cristian](analisis/fichas/eh-jaime-cristian.md) y [Los mejores momentos](analisis/fichas/eh-mejores-momentos-3cfl.md), contienen ocho observaciones **solo textuales** cada una, todavía sin visionado.

### Casos con subtítulos aportados por el usuario

[El Especial del Humor: Marisol y Christian](analisis/fichas/eh-marisol-christian.md) ofrece **8 observaciones textuales con rangos de tiempo** y reglas cómicas originales derivadas: malentendidos que escalan, personaje que se contradice, metahumor televisivo, dobles sentidos y cierre que cambia de marco. La lectura se basa exclusivamente en un SRT aportado por el usuario, con reconocimiento imperfecto; no se ha visto el video, ni se ha subido el SRT a GitHub.

[El Especial del Humor: Jaime no puede vivir sin Cristian](analisis/fichas/eh-jaime-cristian.md) incorpora **8 observaciones textuales** (86 bloques, 12:27) sobre hospitalidad excesiva, objetivos contrapuestos, equívoco espacial, doble sentido sostenido y callback mediante un objeto. El SRT es imperfecto; faltan tono, gestos y verificación visual.

[Los mejores momentos de El Especial del Humor](analisis/fichas/eh-mejores-momentos-3cfl.md) incorpora **8 observaciones textuales** (88 pistas, 11:38) sobre inversión irónica, discursos contradictorios, celos contraproducentes y ventas de artículos aparentemente milagrosos. Al ser una recopilación, las escenas se tratan como fragmentos separados; el SRT no permite inferir actuaciones.

## Uso rápido

Si tu agente admite skills, incluye [SKILL.md](SKILL.md) en sus instrucciones, y prueba:

```text
Usa Comedia Peruana (nivel 3). Escribe una apertura de stand-up de 60 segundos
sobre tener que hacer trámites en Perú. Alterna premisa, observación,
escalada y un remate final sorprendente. Nada de clichés ni imitaciones.
```

Otros usos: improvisación en público, sketches, bromas conversacionales, sátira de situaciones, diálogos, humor absurdo, guiones, juegos de palabras y creación de personajes. **Gaming es una aplicación entre muchas**, no el foco principal.

## Método de estudio

1. Registrar enlace, canal y procedencia del video.
2. Si el video se observó, anotar fragmentos y tiempos; si no, etiquetarlo como **pendiente de visionado**.
3. Describir en palabras propias premisa, expectativas, interrupciones, pausas y remate.
4. Convertir la observación en una **regla técnica general**, sin repetir diálogos memorables ni imitaciones.
5. Crear un ejemplo completamente nuevo y someterlo a pruebas humanas de sorpresa, naturalidad y ritmo.

**Derechos:** enlazamos contenidos de terceros sin alojarlos; no subir videos ni transcripciones completas protegidas sin autorización. El material propio del proyecto puede tener licencia MIT, pero esa licencia no cubre obras externas.

## Ejecutar pruebas de subtítulos

```bash
python scripts/extraer_transcripcion.py material_autorizado.srt --out transcripciones-locales/material.txt
python -m unittest discover -s tests -v
```

La videoteca enseña a **analizar técnicas**, no modifica los parámetros del modelo. Cada propuesta deberá evaluarse con personas reales; un generador no puede garantizar que su propio chiste dé risa.

## Colaboración

Mira [CONTRIBUTING.md](CONTRIBUTING.md). Las fichas deben distinguir datos documentados, observación directa e hipótesis y evitar caricaturizar regiones o colectivos. Se aceptan estilos muy diferentes del humor peruano.
