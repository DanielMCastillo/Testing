from behave import given, when, then
from calculadora import Calculadora

@given(u'que ingreso los numeros "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.cal=Calculadora()
    context.num1= int(num1)
    context.num2=int(num2)

@when(u'realizo el calculo')
def step_impl(context):
    context.resultado=context.cal.sumar(context.num1, context.num2)

@then(u'obtengo el resultado "{esperado}"')
def step_impl(context,esperado):
    assert int(esperado) == context.resultado, \
        "Esperado {esperado} obtenido {context.resultado}"

#CARACTER ESCENARIO
@given(u'que ingreso el caracter "{caracter}" y el numero "{num2}"')
def step_impl(context, caracter, num2):
    context.cal=Calculadora()
    context.num1= caracter
    context.num2=int(num2)


@then(u'obtengo el mensaje "{esperado}"')
def step_impl(context, esperado):
    assert esperado == context.resultado, \
        "Esperado {esperado} obtenido {context.resultado}"
        
        

@given(u'que resto los numeros "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.cal=Calculadora()
    context.num1= int(num1)
    context.num2=int(num2)
    
@when(u'realizo la resta')
def step_impl(context):
    context.resultado=context.cal.restar(context.num1, context.num2)

@then(u'obtengo el resultado de la resta "{esperado}"')
def step_impl(context,esperado):
    assert int(esperado) == context.resultado, \
        "Esperado {esperado} obtenido {context.resultado}"
        


@given(u'que multiplico los numeros "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.cal=Calculadora()
    context.num1= int(num1)
    context.num2=int(num2)
    
@when(u'realizo la multiplicacion')
def step_impl(context):
    context.resultado=context.cal.multiplicar(context.num1, context.num2)

@then(u'obtengo el resultado de la multiplicacion "{esperado}"')
def step_impl(context,esperado):
    assert int(esperado) == context.resultado, \
        "Esperado {esperado} obtenido {context.resultado}"


@given(u'que divido los numeros "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.cal=Calculadora()
    context.num1= int(num1)
    context.num2=int(num2)
    
@when(u'realizo la division')
def step_impl(context):
    context.resultado=context.cal.dividir(context.num1, context.num2)

@then(u'obtengo el resultado de la division "{esperado}"')
def step_impl(context,esperado):
    assert int(esperado) == context.resultado, \
        "Esperado {esperado} obtenido {context.resultado}"
        


@given(u'que elevo los numeros "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.cal=Calculadora()
    context.num1= int(num1)
    context.num2=int(num2)
    
@when(u'realizo la elevacion')
def step_impl(context):
    context.resultado=context.cal.potencia(context.num1, context.num2)

@then(u'obtengo el resultado de la elevacion "{esperado}"')
def step_impl(context,esperado):
    assert int(esperado) == context.resultado, \
        "Esperado {esperado} obtenido {context.resultado}"
        