# Historial de cambios

## 0.10.0 — 2026-10-17
- Cuarto SRT aportado por usuario: Hablando Huevadas, T10, 655 pistas / 1:21:17.
- 11 observaciones textuales de conversación con público, escucha, contradicción, dúo, chistes que no se entendieron y callbacks.
- Nueva guía para separar sketch, stand-up, chiste breve y crowdwork.
- 21 videos catalogados, 4 con análisis solo de subtítulos, 17 pendientes; ninguno visionado.
- Pruebas editoriales actualizadas para casos con cantidades distintas de observaciones.


## 0.9.0 — 2026-10-17
- Tercer SRT aportado por usuario: *Los mejores momentos de El Especial del Humor*, 88 pistas, 11:38, aproximadamente 830 palabras.
- Ocho observaciones textuales con confianza editorial y tiempos, enfatizando sátira, inversión irónica, discurso solidario exagerado, celos contraproducentes y ventas hiperbólicas.
- Catálogo pasa a **20 enlaces**: 3 con SRT analizado, 17 aún sin material, ninguno visionado.
- La recopilación se trató como escenas distintas; se excluyeron segmentos no inteligibles y no se copiaron las transcripciones.
- Actualizada prueba automática de consistencia del catálogo y estado de evidencia.


## 0.8.0 — 2026-10-17
- Segundo sketch con archivo SRT aportado por el usuario: *Jaime no puede vivir sin Cristian*, 86 bloques, 12:27, aproximadamente 1159 palabras.
- Ocho observaciones textuales sobre objetivos contrapuestos, malentendido espacial, insinuación sostenida, melodrama paródico y callback de objeto.
- Catálogo actualizado a **19 enlaces**, 2 con análisis textual y 17 pendientes; ningún video marcado como visionado.
- La ficha distingue metáfora y doble sentido de estereotipos; no publica subtítulos completos ni atribuye gestos, silencios o risas no comprobados.
- Prueba editorial de consistencia del catálogo, estado y dos fichas basadas en subtítulos.


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
