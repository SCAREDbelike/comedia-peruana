import unittest
from scripts.extraer_transcripcion import limpiar

class TestsSubtitulos(unittest.TestCase):
    def test_srt(self):
        srt = "1\n00:00:01,000 --> 00:00:03,000\nHola, causa\n\n2\n00:00:04,000 --> 00:00:05,000\nHola, causa\n¿Todo bien?"
        self.assertEqual(limpiar(srt), "Hola, causa\n¿Todo bien?\n")

    def test_vtt(self):
        self.assertEqual(limpiar("WEBVTT\n\n00:00:01.000 --> 00:00:02.000\n<b>Qué</b> fue &amp; ya"), "Qué fue & ya\n")

if __name__ == "__main__":
    unittest.main()
