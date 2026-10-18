# Historial de cambios

## 0.7.0 — 2026-10-17
- Primer SRT real aportado por usuario: *El Especial del Humor, Marisol y Christian*, 147 bloques hasta 19:20.
- Ocho observaciones textuales con intervalos, evidencias numeradas, mecanismos propuestos y limitaciones. **No se considera visionado.**
- Nuevo elemento del catálogo: **18 videos**; uno con análisis textual y 17 aún sin material.
- Analizador preparado para subtítulos continuos sin signos, con etiquetas de contraste o repetición como pistas, no como diagnóstico de humor.
- Nuevos tests del análisis heurístico de subtítulos sin puntuación.
- Sin subir subtítulos completos ajenos al repositorio. Las observaciones evitan reproducir violencia y estereotipos de la obra.


## 0.6.0 — 2026-10-17
- Implementación de un **motor local de análisis de subtítulos** SRT/VTT para generar candidatos temporales, con señales y límites explícitos.
- Nuevo transcriptor opcional de medios locales autorizados con Faster Whisper.
- Estado de los **17 videos** separado de evidencias; 2 fichas preliminares priorizadas para revisión audiovisual real.
- Guía reproducible del flujo archivo → subtítulos → candidatos → visionado → ficha → regla cómica.
- Referencia de pragmática del habla peruana a partir de corrección conversacional, expresamente no atribuida a un video.
- Se conservan originales y vistas previas en rutas ignoradas por Git; no se publican transcripciones completas.
- Tests de parseo, detección heurística, temporalidad y estado pendiente.


## 0.5.1 — 2026-10-17
- Corregido el alcance: **skill para generar humor con IA, no entrenamiento del usuario**.
- Eliminado el plan de 14 días.
- Añadido protocolo del agente: tipos de solicitudes, selección de giros, edición y reparación de chistes.
- Actualizados SKILL, README y taller de remates para no imponer prácticas ni clases.


## 0.5.0 — 2026-10-17
- Videoteca ampliada de **8 a 17 videos** (+9 enlaces indexados con metadatos, origen y objetivos de estudio).
- Más televisión: programa de 2004 y *El Diván con Karla Casos*, partes 1 y 2.
- Más plaza: El Chino Risas, Los Herederos de la Risa y Los Marcianitos.
- Guía de visionado sin inventar análisis ni tiempos; separación clara entre índice de publicador y evidencia observada.
- Taller de remates, estatus, doble sentido, personajes, lisuras expresivas y corrección de chistes débiles.
- Guía cultural con obra académica de Víctor Vich y enlaces a las fuentes.
- Programa de entrenamiento de 14 días, grabaciones, pruebas humanas y modo interactivo de la skill.


## 0.4.0 — 2026-10-11
- Proyecto **generalizado**: stand-up, cómicos ambulantes, sketches, improvisación, sátira, personajes y humor conversacional.
- README y SKILL reescritos; gaming/Kick dejan de ser el foco.
- Catálogo con **8 enlaces concretos a videos**, fuentes, etiquetas y advertencias de validación.
- Nuevas referencias de cómicos ambulantes y 15 mecanismos para escritura y escena.
- Banco de 12 pruebas de humor en 4 familias de formatos.
- Ejemplos originales de distintos géneros, etiquetados como no evaluados.
- Pruebas automáticas de integridad del catálogo y ejemplos.
- No se afirma haber visionado material no reproducido ni entrenado pesos del modelo.

## 0.3.0 — 2026-10-11
- Primera publicación.
- Skill inicial de humor peruano, script para subtítulos y pruebas locales.
