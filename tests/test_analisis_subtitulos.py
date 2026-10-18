"""Tests de heurísticas. Validan estructura, NO calidad de humor ni visionado."""
import unittest

from scripts.analizar_subtitulos import analizar, extraer_cues, seleccionar_candidatos, tiempo, segundos
from scripts.transcribir_audio import marca_srt

CATALOGO = {"videos": [{"id": "eh-molina-01", "titulo": "Referencia",
                          "url": "https://www.youtube.com/watch?v=CSHVcaZ6Os0"}]}

SRT = """1
00:00:01,000 --> 00:00:02,000
¿Y qué pasó?

2
00:00:04,000 --> 00:00:04,900
Oe chucha, ¿qué fue?

3
00:00:06,600 --> 00:00:07,000
[risas]
"""

VTT = """WEBVTT

00:00:01.000 --> 00:00:02.000
<b>Hola</b> causa

00:00:01.500 --> 00:00:03.000
<b>Hola</b> causa

00:00:04.000 --> 00:00:05.000
¿Ves?
"""


class TestsAnalisis(unittest.TestCase):
    def test_tiempos(self):
        self.assertEqual(segundos("01:02:03,500"), 3723.5)
        self.assertEqual(segundos("02:03.250"), 123.25)
        self.assertEqual(tiempo(3723.5), "01:02:03.500")
        self.assertEqual(marca_srt(63.25), "00:01:03,250")

    def test_extraer_srt(self):
        cues = extraer_cues(SRT)
        self.assertEqual(len(cues), 3)
        self.assertEqual(cues[1]["inicio"], 4)
        self.assertEqual(cues[2]["texto"], "[risas]")

    def test_vtt_cues_repetidos(self):
        cues = extraer_cues(VTT)
        self.assertEqual(len(cues), 2)
        self.assertEqual(cues[0]["fin"], 3)
        self.assertEqual(cues[0]["texto"], "Hola causa")

    def test_indicios_no_son_conclusiones(self):
        cues = extraer_cues(SRT)
        candidatos = seleccionar_candidatos(cues)
        self.assertGreater(len(candidatos), 0)
        self.assertTrue(all(c["mecanismo_comico_confirmado"] is False for c in candidatos))
        self.assertTrue(any("lisura_textual_contextualizar" in c["indicios"] for c in candidatos))
        self.assertTrue(any("reaccion_descrita_en_subtitulos_no_verificada_en_audio" in c["indicios"] for c in candidatos))

    def test_modo_sin_texto(self):
        analisis = analizar(SRT, "eh-molina-01", CATALOGO, incluir_texto=False)
        self.assertEqual(analisis["revision"], "pendiente_de_revision_humana")
        self.assertTrue(all("vista_previa_local" not in c for c in analisis["candidatos"]))

    def test_rechaza_video_desconocido(self):
        with self.assertRaisesRegex(ValueError, "no existe"):
            analizar(SRT, "no-existe", CATALOGO)

    def test_rechaza_sin_tiempos(self):
        with self.assertRaisesRegex(ValueError, "No hay marcas"):
            analizar("texto sin horas", "eh-molina-01", CATALOGO)


if __name__ == "__main__":
    unittest.main()
