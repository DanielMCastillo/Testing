
class Calculadora:

	def sumar(self, num1, num2):
		if (isinstance(num1, str) == True) or (isinstance(num2, str) == True):
			return 'Solo se aceptan numeros'
		
		if ((num1 + num2) > 999999):
			return 'Solo se pueden sumar numeros por debajo de 1 millon'

		if (isinstance(num1, int) == False) or (isinstance(num2, int) == False):
			return 'Solo se pueden sumar numeros enteros'

		if(num1 < 0) or (num2 < 0):
			return 'Solo se pueden sumar numeros positivos'

		return num1 + num2

	def restar(self, num1, num2):
		if (isinstance(num1, str) == True) or (isinstance(num2, str) == True):
			return 'Solo se aceptan numeros'
		
		if ((num1 - num2) > 999999):
			return 'Solo se pueden restar numeros por debajo de 1 millon'

		if (isinstance(num1, int) == False) or (isinstance(num2, int) == False):
			return 'Solo se pueden restar numeros enteros'

		if(num1 < 0) or (num2 < 0):
			return 'Solo puedes ingresar numeros positivos'

		
		
		return num1 - num2

	def multiplicar(self, num1, num2):
		if (isinstance(num1, str) == True) or (isinstance(num2, str) == True):
			return 'Solo se aceptan numeros'
		
		if ((num1 * num2) > 999999):
			return 'Solo se pueden multiplicar numeros por debajo de 1 millon'

		if (isinstance(num1, int) == False) or (isinstance(num2, int) == False):
			return 'Solo se pueden multiplicar numeros enteros'

		if(num1 < 0) or (num2 < 0):
			return 'Solo se pueden multiplicar numeros positivos'

		
		return num1 * num2

	def dividir(self, num1, num2):
		if (isinstance(num1, str) == True) or (isinstance(num2, str) == True):
			return 'Solo se aceptan numeros'

		if(num2 == 0):
			return 'No es posible dividir entre 0'

		if(num1 < 0) or (num2 < 0):
			return 'Solo se pueden dividir numeros positivos'
		
		if ((num1 / num2) > 999999):
			return 'Solo se pueden dividir numeros por debajo de 1 millon'
		
		return int (num1 / num2)
	
	def potencia(self, num1, num2):
		if (isinstance(num1, str) == True) or (isinstance(num2, str) == True):
			return 'Solo se aceptan numeros'
		
		if ((num1 ** num2) > 999999):
			return 'Solo se pueden elevar numeros por debajo de 1 millon'

		if (isinstance(num1, int) == False) or (isinstance(num2, int) == False):
			return 'Solo se pueden elevar numeros enteros'

		if(num1 < 0) or (num2 < 0):
			return 'Solo se pueden elevar numeros positivos'

		if (num1 > 999999) or (num2 > 999999):
			return 'Solo se pueden elevar numeros por debajo de 1 millon'
		
		return num1 ** num2

	
