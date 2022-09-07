import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculadora()

    # def setUp(self):
    #     self.calc = Calculadora()
    
    # def tearDown(self):
    #     pass

    def test_sumar_dos_mas_dos(self):
        resultado = self.calc.sumar(2, 2)
        self.assertEqual(4, resultado, "El resultado no fue lo esperado")


    def test_sumar_cinco_mas_veinte(self):
        resultado = self.calc.sumar(5, 20)
        self.assertEqual(25, resultado, "El resultado no fue lo esperado")


    def test_solo_numeros_positivos(self):
        resultado = self.calc.sumar(4, -1)
        self.assertEqual('Sólo números positivos', resultado, "El resultado no fue lo esperado")


if __name__ == '__main__':
    unittest.main(verbosity=2)