# Daniel Alejandro Morales Castillo
# Clase Domino
class Domino():
    def fichas(self, tupla1, tupla2):
        (ar, ai) = tupla1
        (br, b1) = tupla2

        if (isinstance(tupla1, str)) or (isinstance(tupla2, str)):
            return 'Solo se aceptan numeros en las fichas'

    # Pruebas de comparación solo con las fichas iguales en ambos lados
    def comparar_ficha(self, tupla1, tupla2):
        (p1, p2) = tupla1
        (p3, p4) = tupla2
        if (tupla1 == tupla2):
            return True

    # Pruebas de comparación con un lado de la ficha
    def comparar_solo_un_lado_de_ficha(self, tupla1, tupla2):
        (p1, p2) = tupla1
        (p3, p4) = tupla2

        if (p1 == p3 or p1 == p4):
            return True

        if (p2 == p3 or p2 == p4):
            return True

        return tupla1, tupla2
