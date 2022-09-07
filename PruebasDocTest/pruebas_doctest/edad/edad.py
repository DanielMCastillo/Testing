def edad(numero):
    if numero <0:
        return 'No existes'
    if numero < 13:
        return 'Eres niño'
    elif numero > 13 and numero < 18:
        return 'Eres adolescente'
    elif numero >  18 and numero < 65:
        return 'Eres adulto'
    elif numero >  65 and numero < 120:
        return 'Eres adulto mayor'

    else:
        return 'Eres Mumm-Ra'
    

