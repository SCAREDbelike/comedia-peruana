---
name: comedia-peruana
description: Skill general de humor peruano para stand-up, sketches, cómicos ambulantes, improvisación, sátira, creación de personajes, diálogos, anécdotas, juegos de palabras y remates. Actívala para escribir, analizar, mejorar o practicar comedia en cualquier contexto.
version: 0.5.0
---

# Comedia Peruana

## Misión
Generar y explicar **comedia original** en español, con picardía, chispa oral y vocabulario peruano cuando encaje, sin confundir «ser sano» con «tener un buen remate» ni «decir lisuras» con «hacer un chiste». Trabajar en diversos escenarios: stand-up, calle, teatro, sketches, conversación, redes sociales, radio, escritura, actuaciones e improvisación. **No convertir esta skill en un generador especializado en videojuegos o Kick.**

Referencias de estudio: humor popular peruano, comedia ambulante y parodia televisiva —incluido *El Especial del Humor*— como contextos históricos para investigar **mecanismos**, no para reproducir artistas.

## Calibración por crítica real — v0.5.0 (2026-10-11)

**Feedback explícito de una prueba:** los tres chistes anteriores (stand-up sobre contacto, cómico ambulante cobrando salida y sketch del soltero) obtuvieron **0/3** en preferencia. Se reportó baja claridad y humor excesivamente sano frente a referencias de comedia criolla.

### Reglas correctivas, en orden de prioridad
1. **Se entiende a la primera**: contexto cotidiano, conflicto directo y una consecuencia visible. Si el final introduce un abogado, personaje o premisa sin preparar, NO funciona.
2. **Banter con motor**: dos voces que tienen objetivos opuestos y se lanzan réplicas. A veces uno insulta y el otro se lo devuelve. Nadie debe hablar como manual corporativo.
3. **Grosería dosificada**: usar lisuras peruanas en registro natural **como reacción emocional**, no como única sorpresa. Entre 0 y 3 por mini-escena normalmente basta; no es una cuota obligatoria.
4. **Doble sentido claro**: el público debe reconocer ambas lecturas antes del final; insinuación adulta ligera cuando corresponda, sin forzar sexualidad por obligación.
5. **Juego de estatus**: el presumido pierde piso, el supuesto ingenuo gana, la víctima se defiende con ingenio; dejar que el estatus cambie durante la escena.
6. **Remate en acción**: elegir un objeto o consecuencia concreta (una cuenta, un recibo, un reclamo, una frase repetida) antes que jerga abstracta.
7. **No sobreactuar Perú**: jerga cuando sea creíble; no prefijos «MIS ÑAÑOS» ni mayúsculas por defecto.
8. **La audiencia decide**: nadie sabe si una rutina es graciosa hasta probarla; preferir feedback humano antes que autocalificaciones inventadas.

### Dónde encontrar ejemplos y ejercicios
- [datasets/humor-picaro-v05.jsonl](datasets/humor-picaro-v05.jsonl) — originales, no testeados.
- [tests/humor-con-filo.md](tests/humor-con-filo.md) — pruebas para validar claridad y picardía.
- [referencias/diagnostico-v04.md](referencias/diagnostico-v04.md) — análisis honesto del fallo anterior.

## El motor cómico
- **Premisa**: una tensión, contradicción, detalle concreto o comportamiento absurdo.
- **Expectativa**: qué creerá la audiencia que viene.
- **Giro**: cambia de significado, jerarquía, contexto o intensidad.
- **Remate**: llega lo más tarde posible; la palabra más reveladora queda al final.
- **Pausa**: en escena, no pisar las risas ni explicar el chiste.
- **Actitud**: voz o personaje con una opinión clara, distinta del narrador neutro.

## Técnicas reutilizables
1. **Incongruencia controlada**: cruzar un entorno familiar con una lógica incompatible pero comprensible.
2. **Falsa autoridad**: persona insignificante que se comporta como funcionario supremo.
3. **Reversión de estatus**: quien aparenta tener el poder termina pidiendo permiso.
4. **Regla de tres**: dos casos orientan la expectativa; el tercero la rompe.
5. **Escalada**: cada nueva réplica agrava la misma premisa sin volverse aleatoria.
6. **Literalismo**: aplicar literalmente una frase que normalmente se usa en sentido figurado.
7. **Analogía imposible pero precisa**: comparación sorprendente anclada en un detalle real.
8. **Callback**: recuperar una idea previa, modificada por lo que acaba de pasar.
9. **Malentendido funcional**: los personajes tienen objetivos claros y entienden cosas distintas.
10. **Contraste de registro**: ceremonial/administrativo frente a cotidiano/callejero.
11. **Act-out**: representar brevemente una voz, gesto, intención o situación con ritmo.
12. **Autoironía**: dejar que el personaje se desacredite con sus propias decisiones.
13. **Economía**: cada frase sostiene situación, carácter o sorpresa; suprimir explicaciones sobrantes.
14. **Cambio súbito de marco**: el público interpreta una escena en un contexto y el remate revela otro.
15. **Tensión y liberación**: dosificar la incertidumbre; evitar confusión y crueldad gratuita.

Ver [referencias/mecanismos-comicos.md](referencias/mecanismos-comicos.md).

## Estilos / formatos

### Stand-up
Hablar con opinión propia y registro oral reconocible: «oye», «oe», «pe», «causa», «mi vieja», sin usarlos todos en una sola frase. Permitir que la historia tenga vergüenza, picardía, conflictos domésticos, contradicciones, algún carajo oportuno y un punto de vista claro. Proponer una opinión particular sobre algo cotidiano, luego 3–5 observaciones cada vez más específicas. Alternar setup → punchline → tag → callback; imaginar ritmo oral y permitir espacios para risas. Evitar escribir párrafos que suenan a conferencia.

### Cómicos ambulantes / humor callejero
Entender la audiencia como parte del ritmo: convocatoria, juego verbal, réplica **con filo**, estatus improvisado, pausa y remate. Los personajes pueden picarse, discutir, interrumpirse y soltar «oe, huevón», «no seas cojudo», «qué chucha» o «carajo» **cuando suene natural y aporte al conflicto**. Usar personajes ficticios o bromas consentidas; nunca hostigar a una persona real. No limitarse a gritar lisuras ni acumular jerga.

### Sketches
Los personajes se contestan, se pican, interpretan mal, se aprovechan o se desafían. El remate debe depender de la situación y ser comprensible sin explicar la lógica del mundo. Elegir objetivo y falla de cada personaje, definir una única regla cómica y subir sus consecuencias en 3 golpes. Terminar antes de repetir el mismo chiste. Evitar copiar personajes existentes.

### Improvisación y conversación
Responder a **lo que acaba de ocurrir**. Buscar una conexión concreta que sorprenda, crear como máximo una o dos frases y detenerse. Si no hay remate, reaccionar genuinamente. No hacer chistes cada cinco segundos.

### Parodia y sátira
Parodiar las contradicciones del **formato, la situación, las decisiones o el poder**, no asumir que insultar personas equivale a escribir comedia. Los referentes históricos sirven para estudiar estructura; no son voces que se deban clonar.

### Humor escrito / contenido breve
Un solo punto de vista por pieza, mínimo relleno, remate que funcione sin mayúsculas ni emojis.

## Intensidades
- **1 / familiar**: sorpresa sin ataque.
- **2 / pícaro**: doble lectura ligera y observación de barrio.
- **3 / criollo con filo**: sarcasmo, doble sentido entendible, ironía, choteo recíproco y lisuras casuales («huevón», «cojudo», «carajo», «qué mierda») si el contexto las pide. El chiste no depende de la lisura.
- **4 / irreverente**: escalada más desfachatada, insultos situacionales, picardía y giros arriesgados. No convertirlo en acoso ni discriminación; no confundir volumen con sorpresa.

Elige intensidad y contexto explícitos del usuario. Si no los da, 2–3 por defecto.

## Cultura y voces
«Causa», «pe», «mano» y otras palabras solo si cuadran con quien habla. Hay variedades distintas de español peruano; no presentar Lima como sinónimo de todo el Perú. Partir de vida cotidiana, trabajos, familia, relaciones, barrio, burocracia o expectativas sociales **cuando sirvan a la premisa**. No convertir la procedencia, acento, clase o rasgos de una persona en blanco automático de burla.

## Flujo obligatorio de composición
1. Determinar formato, público, grado de picardía y duración.
2. Anotar **tres premisas realmente diferentes**.
3. Para cada premisa, calcular cuál será la expectativa.
4. Escribir al menos **dos giros alternativos**, uno por incongruencia y otro por estatus/contradicción.
5. Elegir el giro más claro e inesperado; probar ritmo oral.
6. **Prueba de claridad**: identifica quién habla, qué quería cada personaje, cuál es el problema y por qué la réplica es un giro. Si no se entiende sin explicación, reescribir desde la premisa.
7. **Prueba de picardía**: comprobar si el diálogo permite una respuesta con personalidad, mala leche juguetona o doble sentido. Las lisuras se sitúan donde subirían la tensión; no son adorno.
8. Recortar explicación, muletillas sobrantes y cliché.
9. Verificar que el material no replica chistes ni personajes identificables.
10. Entregar solo lo pedido (si es humor conversacional, no mostrar todas las etapas).

## Lista negra de soluciones fáciles
No abusar de «soy malo jugando», «mi mamá me manda a trabajar», «el internet falló», «bienvenidos al caos», «risas garantizadas», «SUNAT me investiga», «me dejó mi ex» ni «esto parece un trámite» sin un giro verdaderamente nuevo. Evitar insultos por defecto **pero NO censurar las lisuras cuando el usuario pide picardía y éstas sirven al conflicto**. Rechazar remates reciclados, exageraciones vacías y cierres explicativos.

## Control de calidad
Puntuar 0–5: **claridad, sorpresa, especificidad, naturalidad oral, remate y originalidad**. Reescribir si dos parámetros caen por debajo de 3. La puntuación del modelo es una hipótesis; validar con audiencia humana. Usar [tests/casos.md](tests/casos.md).

## Estudio de videos
Consultar [videos/README.md](videos/README.md), [videos/catalogo.json](videos/catalogo.json) y fichas en [referencias/](referencias/). Separa siempre:
- **Enlace documental verificado**: la fuente publica el enlace, título y contexto.
- **Video observado**: realmente se examinó el material con momento identificable.
- **Hipótesis**: técnica que se propone investigar, no prueba de que aparezca en un video.
- **Transcripción autorizada**: texto con permiso legal para reutilizarlo.

No afirmar que se visionó un sketch, que se obtuvo toda la transcripción, ni que hubo entrenamiento del modelo sin evidencia. No publicar material audiovisual ajeno en el repositorio.

## Evolución
Añadir observaciones propias y ejemplos etiquetados; preparar ejercicios y medir reacciones. El repositorio actualiza reglas y datos de referencia, **no los pesos del modelo**.
