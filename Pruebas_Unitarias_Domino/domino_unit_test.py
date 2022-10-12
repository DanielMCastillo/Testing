import unittest
from domino import Domino


class TestSmoke(unittest.TestCase):
    def setUp(self):
        #print('Configura el entorno')
        self.dom = Domino()

    # PRUEBAS DE FICHAS IGUALES
    def test_ficha(self):
        resultado = self.dom.comparar_ficha((5, 5), (5, 5))
        self.assertEqual(True, resultado)

    # PRUEBAS DE FICHAS IGUALES

    def test_ficha2(self):
        resultado = self.dom.comparar_ficha((2, 2), (2, 2))
        self.assertEqual(True, resultado)

    # PRUEBAS DE FICHAS SOLO UN LADO
    def test_ficha_por_un_lado(self):
        resultado = self.dom.comparar_solo_un_lado_de_ficha((2, 1), (1, 2))
        self.assertEqual(True, resultado)

    # PRUEBAS DE FICHAS SOLO UN LADO
    def test_ficha_por_un_lado2(self):
        resultado = self.dom.comparar_solo_un_lado_de_ficha((5, 1), (5, 5))
        self.assertEqual(True, resultado)


if __name__ == '__main__':
    unittest.main()
