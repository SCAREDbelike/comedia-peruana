"""Validación de metadatos: NO valida que los chistes hagan reír."""
import json
import unittest
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parents[1]

class TestCatalogo(unittest.TestCase):
    def test_catalogo_valido(self):
        catalogo = json.loads((ROOT / "videos" / "catalogo.json").read_text(encoding="utf-8"))
        videos = catalogo["videos"]
        self.assertGreaterEqual(len(videos), 2)
        ids = [v["id"] for v in videos]
        self.assertEqual(len(ids), len(set(ids)))
        for video in videos:
            with self.subTest(id=video["id"]):
                self.assertTrue(video["titulo"].strip())
                self.assertTrue(video["fuente"].startswith("https://"))
                parts = urlparse(video["url"])
                self.assertEqual(parts.netloc, "www.youtube.com")
                self.assertTrue(parse_qs(parts.query).get("v"))
                self.assertEqual(video["estado_observacion"], "pendiente_de_visionado_directo")
                self.assertFalse(video["transcripcion_incluida"])

    def test_ejemplos_originales(self):
        ruta = ROOT / "datasets" / "ejemplos-originales.jsonl"
        filas = [json.loads(s) for s in ruta.read_text(encoding="utf-8").splitlines() if s.strip()]
        self.assertGreaterEqual(len(filas), 8)
        self.assertEqual(len({f["id"] for f in filas}), len(filas))
        self.assertGreaterEqual(len({f["formato"] for f in filas}), 4)
        for fila in filas:
            self.assertEqual(fila["origen"], "original")
            self.assertTrue(fila["texto"].strip())
            self.assertEqual(fila["evaluacion"], "pendiente_humana")

if __name__ == "__main__":
    unittest.main()
