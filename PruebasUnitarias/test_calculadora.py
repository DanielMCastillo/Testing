import unittest

from calculadora import Calculadora

class TestSmoke(unittest.TestCase):

    def test_prueba_de_humo(self):
        self.assertEqual(2+2, 4, '2 mas 2 no es igual a 5')

    def setUp(self):
        #print('Configura el entorno')
        self.cal = Calculadora()

    def tearDown(self):
        #print('Limpia el entorno')
        return

    ## PRUEBAS SUMA
    def test_dos_mas_dos(self):
        resultado = self.cal.sumar(2, 2)
        self.assertEqual(4, resultado)
    
    def test_siete_mas_dos(self):
        resultado = self.cal.sumar(7, 2)
        self.assertEqual(9, resultado)

    def test_sumar_cadena(self):
        resultado = self.cal.sumar('X', 2)
        self.assertEqual('Solo se aceptan numeros', resultado)
    
    def test_sumar_millon(self):
        resultado = self.cal.sumar(1000000, 2)
        self.assertEqual('Solo se pueden sumar numeros por debajo de 1 millon', resultado)

    def test_sumar_negativos(self):
        resultado = self.cal.sumar(-3, 2)
        self.assertEqual('Solo se pueden sumar numeros positivos', resultado)

    def test_sumar_flotantes(self):
        resultado = self.cal.sumar(3.3, 2)
        self.assertEqual('Solo se pueden sumar numeros enteros', resultado)

    ##PRUEBAS RESTA
    def test_dos_menos_dos(self):
        resultado = self.cal.restar(2, 2)
        self.assertEqual(0, resultado)
    
    def test_siete_menos_dos(self):
        resultado = self.cal.restar(7, 2)
        self.assertEqual(5, resultado)

    def test_restar_cadena(self):
        resultado = self.cal.restar('X', 2)
        self.assertEqual('Solo se aceptan numeros', resultado)
    
    def test_restar_millon(self):
        resultado = self.cal.restar(1000002, 2)
        self.assertEqual('Solo se pueden restar numeros por debajo de 1 millon', resultado)

    def test_restar_negativos(self):
        resultado = self.cal.restar(-3, 2)
        self.assertEqual('Solo puedes ingresar numeros positivos', resultado)

    def test_restar_flotantes(self):
        resultado = self.cal.restar(3.3, 2)
        self.assertEqual('Solo se pueden restar numeros enteros', resultado)

    ## PRUEBAS MULTIPLICACIÓN
    def test_dos_por_dos(self):
        resultado = self.cal.multiplicar(2, 2)
        self.assertEqual(4, resultado)
    
    def test_siete_por_dos(self):
        resultado = self.cal.multiplicar(7, 2)
        self.assertEqual(14, resultado)

    def test_multiplicar_cadena(self):
        resultado = self.cal.multiplicar('X', 2)
        self.assertEqual('Solo se aceptan numeros', resultado)
    
    def test_multiplicar_millon(self):
        resultado = self.cal.multiplicar(1000000, 2)
        self.assertEqual('Solo se pueden multiplicar numeros por debajo de 1 millon', resultado)

    def test_multiplicar_negativos(self):
        resultado = self.cal.multiplicar(-3, 2)
        self.assertEqual('Solo se pueden multiplicar numeros positivos', resultado)

    def test_multiplicar_flotantes(self):
        resultado = self.cal.multiplicar(3.3, 2)
        self.assertEqual('Solo se pueden multiplicar numeros enteros', resultado)

    ## PRUEBAS DIVISIÓN
    def test_dos_entre_dos(self):
        resultado = self.cal.dividir(2, 2)
        self.assertEqual(1, resultado)
    
    def test_siete_entre_dos(self):
        resultado = self.cal.dividir(7, 2)
        self.assertEqual(3, resultado) ##Redondea hacia abajo.

    def test_dividir_cadena(self):
        resultado = self.cal.dividir('X', 2)
        self.assertEqual('Solo se aceptan numeros', resultado)
    
    def test_dividir_millon(self):
        resultado = self.cal.dividir(1000000, 1)
        self.assertEqual('Solo se pueden dividir numeros por debajo de 1 millon', resultado)

    def test_dividir_negativos(self):
        resultado = self.cal.dividir(-3, 2)
        self.assertEqual('Solo se pueden dividir numeros positivos', resultado)

    def test_dividir_flotantes(self):
        resultado = self.cal.dividir(3.3, 2)
        self.assertEqual(1, resultado)

    def test_dividir_entre_cero(self):
        resultado = self.cal.dividir(5, 0)
        self.assertEqual('No es posible dividir entre 0', resultado)

    ##PRUEBAS POTENCIA
    def test_dos_elevado_dos(self):
        resultado = self.cal.potencia(2, 2)
        self.assertEqual(4, resultado)
    
    def test_siete_elevado_dos(self):
        resultado = self.cal.potencia(7, 2)
        self.assertEqual(49, resultado)

    def test_potencia_cadena(self):
        resultado = self.cal.potencia('X', 2)
        self.assertEqual('Solo se aceptan numeros', resultado)
    
    def test_potencia_millon(self):
        resultado = self.cal.potencia(1000000, 2)
        self.assertEqual('Solo se pueden elevar numeros por debajo de 1 millon', resultado)

    def test_potencia_negativos(self):
        resultado = self.cal.potencia(-3, 2)
        self.assertEqual('Solo se pueden elevar numeros positivos', resultado)

    def test_potencia_flotantes(self):
        resultado = self.cal.potencia(3.3, 2)
        self.assertEqual('Solo se pueden elevar numeros enteros', resultado)

if __name__ == '__main__':
    unittest.main()