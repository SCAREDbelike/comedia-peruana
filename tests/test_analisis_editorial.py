"""Verifica integridad editorial, sin atribuir visionado a análisis textuales."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CASOS={
    "eh-marisol-christian":"analisis/fichas/eh-marisol-christian.md",
    "eh-jaime-cristian":"analisis/fichas/eh-jaime-cristian.md",
}

class TestAnalisisEditorial(unittest.TestCase):
    def test_fichas_catalogo_estado(self):
        catalogo=json.loads((ROOT/"videos/catalogo.json").read_text(encoding="utf-8"))
        estado=json.loads((ROOT/"analisis/estado.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(catalogo["videos"]),19)
        self.assertEqual(len(catalogo["videos"]),len(estado["videos"]))
        index={v["id"]:v for v in catalogo["videos"]}
        seguimiento={v["id"]:v for v in estado["videos"]}
        self.assertEqual(set(index),set(seguimiento))
        for video_id,ficha in CASOS.items():
            with self.subTest(video=video_id):
                video=index[video_id]
                self.assertEqual(video["estado_observacion"],"pendiente_de_visionado_directo")
                self.assertEqual(video["estado_analisis"],"transcripcion_analizada_sin_visionado")
                self.assertFalse(video["transcripcion_incluida"])
                self.assertFalse(video["material_descargado"])
                self.assertEqual(video["ficha_analisis"],ficha)
                self.assertTrue((ROOT/ficha).exists())
                self.assertEqual(seguimiento[video_id]["segmentos_validados"],0)
                data=json.loads((ROOT/"analisis/observaciones"/(video_id+".json")).read_text(encoding="utf-8"))
                self.assertEqual(data["estado"],"transcripcion_analizada_sin_visionado")
                self.assertEqual(data["url"],video["url"])
                self.assertEqual(len(data["segmentos"]),8)
                self.assertEqual(len(data["segmentos"]),seguimiento[video_id]["segmentos_textuales_anotados"])
                self.assertTrue(all(x["inicio"]<x["fin"] for x in data["segmentos"]))
                self.assertEqual(len({x["id"] for x in data["segmentos"]}),8)

    def test_muestra_segundo_srt(self):
        data=json.loads((ROOT/"analisis/observaciones/eh-jaime-cristian.json").read_text(encoding="utf-8"))
        meta=data["datos_archivo"]
        self.assertEqual(meta["bloques_subtitulos"],86)
        self.assertEqual(meta["duracion_hasta"],"00:12:27")
        self.assertEqual(meta["intervalos_con_huecos_positivos"],0)
        self.assertEqual(meta["etiquetas_textuales"],{"Aplausos":1,"Música":3,"Risas":1})


if __name__=="__main__":
    unittest.main()
