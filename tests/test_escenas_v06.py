"""Pruebas estructurales para tarjetas de escenas; no valoran si una escena causa risa."""
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class TestEscenas(unittest.TestCase):
    def test_escenas_bien_estructuradas(self):
        lines = (ROOT / "datasets" / "escenas-v06.jsonl").read_text(encoding="utf-8").splitlines()
        scenes = [json.loads(line) for line in lines if line.strip()]
        self.assertGreaterEqual(len(scenes), 3)
        self.assertEqual(len({s["id"] for s in scenes}), len(scenes))
        self.assertEqual(len({s["lugar"] for s in scenes}), len(scenes))
        for scene in scenes:
            with self.subTest(id=scene["id"]):
                for field in ("regla_del_lugar","disparador","pago_final"):
                    self.assertTrue(scene[field].strip())
                self.assertGreaterEqual(len(scene["personajes"]), 2)
                self.assertEqual(len(scene["golpes"]), 3)
                self.assertEqual(scene["estado"],"prototipo_no_evaluado")
                for personaje in scene["personajes"]:
                    self.assertTrue(personaje["objetivo"])
                    self.assertTrue(personaje["defecto"])
                    self.assertTrue(personaje["secreto"])
if __name__ == "__main__":
    unittest.main()
