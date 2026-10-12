"""Verifica estructura y procedencia, no cuánto hace reír una broma."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestHumorPicaro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contenido = (ROOT / "datasets" / "humor-picaro-v05.jsonl").read_text(encoding="utf-8")
        cls.ejemplos = [json.loads(line) for line in contenido.splitlines() if line.strip()]

    def test_ids_unicos(self):
        ids = [x["id"] for x in self.ejemplos]
        self.assertEqual(len(ids), len(set(ids)))

    def test_variedad_formato(self):
        self.assertGreaterEqual(len(self.ejemplos), 7)
        self.assertGreaterEqual(len(set(x["formato"] for x in self.ejemplos)), 4)

    def test_sin_falso_entrenamiento(self):
        for dato in self.ejemplos:
            with self.subTest(id=dato["id"]):
                self.assertEqual(dato["origen"], "original")
                self.assertEqual(dato["estado"], "no_probado_con_publico")
                self.assertIn(dato["nivel"], [1, 2, 3, 4])
                self.assertGreater(len(dato["texto"]), 25)

if __name__ == "__main__":
    unittest.main()
