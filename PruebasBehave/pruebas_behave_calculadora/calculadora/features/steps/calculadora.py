class Calculadora:

    def sumar(self, num1, num2):
        if (isinstance(num1,str) == True) or (isinstance(num2,str) == True):
            return 'Solo aceptan numeros'
        if(num1<0) or (num2<0):
            return 'Solo se pueden sumar numeros positivos'
        if ((num1+num2)>1000000):
            return 'Solo se pueden sumar numeros por debajo de 1 millon'
        if(isinstance(num1,int)and isinstance(num2,int)):
            return num1+num2  
        if(isinstance(num1,float)and isinstance(num2,float)):
            return 'Solo se pueden sumar numeros enteros'    
        if (isinstance(num1,int)!= True) or (isinstance(num2,int)!= True):
            return 'Solo se pueden sumar numeros enteros'
        

#Tarea implementar casos de pruebas para restar, multiplicar, dividir, potencia.
    def restar(self, num1, num2):
        if (isinstance(num1,str) == True) or (isinstance(num2,str) == True):
            return 'Solo aceptan numeros'
        if(num1<0) or (num2<0):
            return 'Solo se pueden restar numeros positivos'
        if ((num1-num2)>1000000):
            return 'Solo se pueden restar numeros por debajo de 1 millon'
        if (isinstance(num1,int)!= True) or (isinstance(num2,int)!= True):
            return 'Solo se pueden restar numeros enteros'
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        if (isinstance(num1,str) == True) or (isinstance(num2,str) == True):
            return 'Solo aceptan numeros'
        if(num1<0) or (num2<0):
            return 'Solo se pueden multiplicar numeros positivos'
        if ((num1-num2)>1000000):
            return 'Solo se pueden multiplicar numeros por debajo de 1 millon'
        if (isinstance(num1,int)!= True) or (isinstance(num2,int)!= True):
            return 'Solo se pueden multiplicar numeros enteros'
        return num1 * num2

    def dividir(self, num1, num2):
        if (isinstance(num1,str) == True) or (isinstance(num2,str) == True):
            return 'Solo aceptan numeros'
        if(num1==0) or (num2==0):
            return 'No se puede dividir entre cero'
        if(num1<0) or (num2<0):
            return 'Solo se pueden dividir numeros positivos'
        if ((num1-num2)>1000000):
            return 'Solo se pueden dividir numeros por debajo de 1 millon'
        if (isinstance(num1,int)!= True) or (isinstance(num2,int)!= True):
            return 'Solo se pueden dividir numeros enteros'
        return round(num1/num2,1)
    
    def potencia(self, num1, num2):
        if (isinstance(num1,str) == True) or (isinstance(num2,str) == True):
            return 'Solo aceptan numeros'
        if(num1==0) or (num2==0):
            return 'No se puede tener potencia a cero'
        if(num1<0) or (num2<0):
            return 'Solo se pueden potenciar numeros positivos'
        if ((num1-num2)>1000000):
            return 'Solo se pueden potenciar numeros por debajo de 1 millon'
        if (isinstance(num1,int)!= True) or (isinstance(num2,int)!= True):
            return 'Solo se pueden potenciar numeros enteros'
        return pow(num1,num2)  