Característica: Verificar edades
    Como usuario del programa
    quiero poder validar las edades
    para obtener un mensaje que diga a que grupo pertenezco.

    Escenario: Menor a 0
        Dado que ingreso el numero "-1"
        Cuando realizo la validacion de la edad
        Entonces obtengo el mensaje "No existes"
    
    Escenario: Menor a 13
        Dado que ingreso el numero "6"
        Cuando realizo la validacion de la edad
        Entonces obtengo el mensaje "Eres niño"
    
    Escenario: Menor a 18
        Dado que ingreso el numero "12"
        Cuando realizo la validacion de la edad
        Entonces obtengo el mensaje "Eres adolescente"
    
    Escenario: Menor a 65
        Dado que ingreso el numero "45"
        Cuando realizo la validacion de la edad
        Entonces obtengo el mensaje "Eres adulto"

    Escenario: Menor a 120
        Dado que ingreso el numero "119"
        Cuando realizo la validacion de la edad
        Entonces obtengo el mensaje "Eres adulto mayor"

    Escenario: Mayor a 120
        Dado que ingreso el numero "200"
        Cuando realizo la validacion de la edad
        Entonces obtengo el mensaje "Eres Mumm-Ra"