class Edad:
    def edad(self, numero):
        if numero < 0:
            return 'No existes'
        if numero < 13:
            return 'Eres niño'
        if numero < 18:
            return 'Eres adolescente'
        if numero < 65:
            return 'Eres adulto'
        if numero < 120:
            return 'Eres adulto mayor'
        return 'Eres Mumm-Ra'