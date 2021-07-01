#Reto de la semana1, Jueves 6 de mayo
"""
Para poder estimar la cantidad de camas que hay que mover de los municipios cercanos, se te ha pedido
que crees una función que permita calcular cuantas camas son necesarias mover para un municipio si se
entrega: el número de camas que actualmente tiene el municipio, el porcentaje de ocupación actual y el
porcentaje objetivo a alcanzar que por defecto será el 70%. Como resultado, se espera que se devuelva
el número de camas que deben ser movidas de los municipios aledaños. Este resultado debe ser
entregado en un valor entero
"""

import math

def camas_a_mover(camas_actual, ocupacion_actual, ocupacion_esperada =  70):
#creo la funcion camas a mover que va a recibir como paremetros 3 variables, la ocupacion esperada por defecto es 70
#por si el usuario no ingresa este dato.

    math.ceil(ocupacion_actual)
    math.ceil(ocupacion_esperada)
 
    total_camas_ocupadas = ocupacion_actual/100 
    #convierto el porcentaje de ocupacion actual al numero de camas de la ocupacion actual segun el numero de camas actuales
 
    total_camas_ocupadas_esperadas = ocupacion_esperada/100
    #convierto el porcentaje de la ocupacion esperada al numero de camas de la ocupacion esperada segun 
    #el numero de camas actuales

    mover_camas = math.ceil((math.ceil(camas_actual*total_camas_ocupadas)/total_camas_ocupadas_esperadas)-camas_actual)
    #resto el numero de camas ocupadas con el numero de camas ocupadas esperadas

    return mover_camas
    #retorno el numero de camas a mover

print(camas_a_mover(100,90))
print(camas_a_mover(257, 80.25, 68.5))
print(camas_a_mover(350, 100, 1))