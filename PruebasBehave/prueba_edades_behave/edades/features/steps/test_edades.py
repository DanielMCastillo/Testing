from behave import given, when, then
from edades import Edad


@given(u'que ingreso el numero "{numero}"')
def step_impl(context, numero):
    context.ed=Edad()
    context.numero=int(numero)


@when(u'realizo la validacion de la edad')
def step_impl(context):
    context.resultado=context.ed.edad(context.numero)


@then(u'obtengo el mensaje "{esperado}"')
def step_impl(context, esperado):
    assert esperado == context.resultado, \
        "Esperado {esperado} obtenido {context.resultado}"
