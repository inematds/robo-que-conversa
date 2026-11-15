import unittest

import escolher

P = escolher.carregar()


def ids(lista):
    return [p["id"] for p in lista]


class TestEscolher(unittest.TestCase):
    def test_body_sozinho_nunca_aparece(self):
        # o corpo do StackChan não fala sozinho
        self.assertNotIn("stackchan-body", ids(escolher.filtrar(P)))

    def test_rodas_e_camera(self):
        self.assertEqual(ids(escolher.filtrar(P, rodas=True, camera=True)), ["picarx", "miniauto", "turbopi"])

    def test_orcamento(self):
        self.assertEqual(ids(escolher.filtrar(P, rodas=True, ate=200)), ["picarx", "miniauto"])

    def test_pronto_com_rodas(self):
        self.assertNotIn("picarx", ids(escolher.filtrar(P, rodas=True, pronto=True)))

    def test_mesa_que_mexe_com_camera(self):
        r = ids(escolher.filtrar(P, camera=True, mexe=True, ate=120))
        self.assertEqual(r, ["picarx", "stackchan-kit"])

    def test_ordem_por_preco(self):
        precos = [p["usd"] for p in escolher.filtrar(P)]
        self.assertEqual(precos, sorted(precos))

    def test_nada(self):
        self.assertEqual(escolher.filtrar(P, rodas=True, ate=50), [])

    def test_todos_tem_link_e_wifi(self):
        for p in P:
            self.assertTrue(p["link"].startswith("https://"), p["id"])
            self.assertTrue(p["wifi"], p["id"])


if __name__ == "__main__":
    unittest.main()
