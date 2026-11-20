import copy
import importlib.util
import json
import unittest
from pathlib import Path
R = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("conferir", R / "scripts/conferir.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
class Conferir(unittest.TestCase):
    def setUp(self):
        self.f = json.loads((R / "kit/exemplos/ficha.json").read_text())
        self.f["modelo"] = "modelo-real-do-teste"
        self.f["evidencias"] = {k: True for k in m.EVIDENCIAS}
    def test_local_com_provas(self):
        self.assertEqual(m.conferir(self.f)["estado"], "ficha-conferida")
    def test_nao_aceita_texto_true(self):
        self.f["evidencias"]["resultado_conferido"] = "true"
        self.assertEqual(m.conferir(self.f)["estado"], "invalida")
    def test_nuvem_nao_e_offline(self):
        self.f["execucao"] = "provedor"
        self.assertEqual(m.conferir(self.f)["estado"], "revisar")
    def test_sem_revisao_nao_fecha(self):
        self.f["revisao"] = "nenhuma"
        self.assertEqual(m.conferir(self.f)["estado"], "revisar")
    def test_segundo_modelo_avisa(self):
        self.f["revisao"] = "segundo-modelo"
        self.assertTrue(m.conferir(self.f)["avisos"])
    def test_dado_sensivel_nuvem_avisa(self):
        self.f.update(dados="confidenciais", execucao="provedor", offline_necessario=False)
        self.assertTrue(m.conferir(self.f)["avisos"])
    def test_sem_objeto(self):
        self.assertEqual(m.conferir([])["estado"], "invalida")
    def test_evidencia_faltando(self):
        del self.f["evidencias"]["sem_rede"]
        self.assertEqual(m.conferir(self.f)["estado"], "invalida")
    def test_modelo_placeholder(self):
        self.f["modelo"] = "preencher-modelo"
        self.assertEqual(m.conferir(self.f)["estado"], "invalida")
if __name__ == "__main__": unittest.main()
