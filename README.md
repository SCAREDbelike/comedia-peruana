# Comedia Peruana — Laboratorio abierto de humor (v0.5.0 — propuesta)

**Skill de escritura, análisis e improvisación humorística con identidad peruana.** Investiga las técnicas de los **cómicos ambulantes**, el humor de barrio, los sketches televisivos (como *El Especial del Humor*), el **stand-up**, la sátira cotidiana, los diálogos cómicos y la creación de personajes.

**Propósito:** comprender por qué funciona un remate y aplicar ese conocimiento para producir **comedia original** en cualquier formato, sin copiar rutinas ni personajes ajenos.

> No es una colección de chistes robados ni un modelo reentrenado. Es una skill con biblioteca de referencias, ejercicios, ejemplos nuevos y pruebas de calidad.

## Nueva orientación: humor con picardía (v0.5.0, pendiente de revisión)

Tras una prueba en conversación, el usuario rechazó los tres intentos de la v0.4 por baja claridad y tono demasiado sano. Ahora se priorizan **escenas comprensibles, diálogos que se pican, lisuras naturales en contexto, doble sentido ligero y un remate que dependa de la premisa**.

La lisura no es el chiste. Se permite el vocabulario criollo —«huevón», «cojudo», «carajo», «qué chucha»— si sube la tensión cómica. Ni groserías de relleno ni insultos contra identidades protegidas.

- [Diagnóstico honesto de v0.4](referencias/diagnostico-v04.md)
- [Nuevos ejemplos originales con filo](datasets/humor-picaro-v05.jsonl)
- [Pruebas de claridad y picardía](tests/humor-con-filo.md)

**Estos ejemplos todavía no han pasado pruebas con audiencia.** La mejora es una hipótesis basada en feedback, no una afirmación de éxito.

## Explorar

| Recurso | Para qué sirve |
| --- | --- |
| [SKILL.md](SKILL.md) | Instrucciones principales, mecanismos cómicos, improvisación y formatos |
| [videos/README.md](videos/README.md) | **Videoteca con enlaces reales**, procedencia y estados de verificación |
| [videos/catalogo.json](videos/catalogo.json) | Catálogo legible por programas, con temas para investigar |
| [referencias/especial-del-humor.md](referencias/especial-del-humor.md) | Hipótesis de análisis de sketches de televisión |
| [referencias/comicos-ambulantes.md](referencias/comicos-ambulantes.md) | Mecánicas de humor callejero y relación con la audiencia |
| [referencias/mecanismos-comicos.md](referencias/mecanismos-comicos.md) | Herramientas aplicables a stand-up, escena y conversación |
| [plantillas/ficha-video.md](plantillas/ficha-video.md) | Plantilla reproducible para observar escenas |
| [datasets/ejemplos-originales.jsonl](datasets/ejemplos-originales.jsonl) | Material original etiquetado por formato y técnica |
| [tests/casos.md](tests/casos.md) | Banco de pruebas de humor de distintos formatos |
| [tests/humor-con-filo.md](tests/humor-con-filo.md) | Verificación específica de comprensión y picardía |
| [scripts/extraer_transcripcion.py](scripts/extraer_transcripcion.py) | Limpieza local de SRT/VTT/TXT autorizados |

## Referencias iniciales

La videoteca ya incorpora referencias enlazadas a:
- *El Especial del Humor*: un programa completo de 2004 y sketches relacionados con «Las viejas pitucas de La Molina».
- Otros sketches referenciados por una nota periodística (estos enlaces **no se han comprobado mediante visionado**).
- *Los Reyes de la Risa Vol. 2*: presentación larga con varios cómicos ambulantes.

[Ir al catálogo de videos →](videos/README.md)

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
