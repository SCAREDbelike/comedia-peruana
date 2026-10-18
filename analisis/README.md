# Motor de investigación audiovisual de Comedia Peruana (v0.7.0)

## Qué existe y qué no existe todavía

- **18 videos catalogados**: por ahora enlaces y metadatos. Uno cuenta con análisis textual de subtítulos; **ninguno se marca como visionado**.
- **Transcripción opcional local**: `scripts/transcribir_audio.py` convierte un archivo audiovisual propio o autorizado en SRT con Faster Whisper. La transcripción automática puede confundir voces, acentos y lisuras.
- **Análisis temporal local**: `scripts/analizar_subtitulos.py` extrae pistas SRT/VTT con marcas de tiempo y propone fragmentos para revisar. **No detecta remates ni risas con certeza**, y no ve gestos, pausas acústicas ni actuaciones.
- **Conocimiento público editorial**: se publica solo una ficha breve con conclusiones comprobadas y redactadas en palabras propias; nunca transcripciones completas, audio ni videos de terceros.

## Ejecución de extremo a extremo

Requiere Python 3.10+ y, para **transcribir audio/video local autorizado**, instalar opcionalmente Faster Whisper:

```bash
python -m pip install faster-whisper
python scripts/transcribir_audio.py medios-locales/fragmento-autorizado.mp4 --modelo small --out transcripciones-locales/fragmento.srt
```

O empieza con un SRT/VTT que ya tengas derecho a utilizar. No necesitas instalar nada para el analizador:

```bash
python scripts/analizar_subtitulos.py --video-id eh-molina-01 --subtitulos transcripciones-locales/fragmento.srt
```

Esto creará `analisis-locales/eh-molina-01.json` (ignorado por Git). Para excluir vistas previas de subtítulos:

```bash
python scripts/analizar_subtitulos.py --video-id eh-molina-01 --subtitulos transcripciones-locales/fragmento.srt --sin-texto
```

Revisa el JSON: las entradas incluyen rango temporal, puntuación heurística y **señales**, no chistes probados. Después abre el video y verifica el fragmento.

## Qué buscan las heurísticas

| Señal de subtítulos | Lo que permite proponer | Lo que **NO** demuestra |
| --- | --- | --- |
| Hueco entre pistas >= 1.2 s | Pausa textual tras una frase | Silencio acústico, intención del actor |
| Pregunta | Posible preparación de réplica | Setup cómico o inversión de estatus |
| Exclamación | Cambio textual de intensidad | Grito, timbre ni tono emocional |
| Lisura reconocida | Posible fenómeno de registro | Que la expresión sea graciosa o esté bien dicha |
| Etiqueta `[risas]` | El subtítulo describe una reacción | Que el público se haya reído en realidad |

**Falso positivo esperado:** una pregunta, insulto o pausa puede no ser un chiste. **Falso negativo esperado:** un remate gestual o seco puede no dejar indicio textual alguno.

## Qué revisar manualmente tras las propuestas

1. Abrir el video referenciado en `videos/catalogo.json` y buscar el intervalo propuesto.
2. Confirmar si se escucha lo transcrito; identificar hablantes solo con evidencia.
3. Describir con palabras propias **situación → expectativa → información escondida → giro → remate**.
4. Registrar pausas audibles, gestos, entonación y risas solo si efectivamente están presentes.
5. Describir el papel de jerga/lisura en el **contexto de quién habla y a quién**, no de forma aislada.
6. Crear **un ejemplo nuevo** con otro tema y personajes; evitar copiar la rutina.
7. Pasar hallazgos comprobados a una ficha pública en `analisis/fichas/`, cambiando su estado a `video_revisado` solo con intervalo verificado.

Se puede trabajar solo con subtítulos sin el video, pero el estado es `transcripcion_analizada_sin_visionado` y no puede sostener observaciones visuales o de actuación.

## Primer caso con archivo SRT real (2026-10-17)

- [Marisol y Christian](fichas/eh-marisol-christian.md): **147 bloques / 19:20**, ocho observaciones textuales, enlazadas a su fuente en [JSON estructurado](observaciones/eh-marisol-christian.json).
- Esta extracción carece de signos interrogativos y exclamativos y tiene **0 huecos entre bloques**; las pausas de los intérpretes son desconocidas.
- Un fragmento marcado con `[Aplausos]` en SRT no equivale a una reacción comprobada; la voz, las identidades hablantes y el ritmo requieren visionado.
- La anotación contiene **paráfrasis originales**, no el SRT de terceros.

## Primeros dos casos priorizados

- [Las viejas pitucas de La Molina #01](fichas/eh-molina-01.md): estudio de personajes, estatus y registros.
- [Chino Risas Vol.1](fichas/ca-chino-vol1.md): interacción, pausas y remates en comedia de plaza.

Ambas fichas son **protocolos de análisis pendientes**, NO hallazgos de escenas vistas. Tampoco es una escena vista el caso de Marisol y Christian: sus observaciones provienen solamente del subtítulo.

## Fuentes y acceso

YouTube advierte que el reconocimiento automático puede fallar con acentos, audio de mala calidad y voces simultáneas: https://support.google.com/youtube/answer/6373554 . El acceso automatizado a subtítulos ajenos no está garantizado y la API oficial tiene controles de titularidad/permisos: https://developers.google.com/youtube/v3/docs/captions/download .

**No usar la automatización para eludir restricciones.** El proyecto procesa medios o subtítulos obtenidos de manera autorizada y preserva originales solo en directorios locales excluidos por `.gitignore`.

## Pruebas

```bash
python -m unittest discover -s tests -v
```

Prueba parseo SRT/VTT, tiempos, preservación de estados, pistas duplicadas y señales. No certifica resultados humorísticos ni disponibilidad de YouTube.
