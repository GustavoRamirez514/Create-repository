#Clase 4, Jueves 6 de mayo, 10 retos

#RETO 1
"""
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
"""
def llamado(nombre):

    print("Hola", nombre,"\n")

llamado("Gus")


#RETO 2
"""
Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""
def calcular_factorial(numero):
 import math

 print(math.factorial(numero),"\n")

calcular_factorial(0)


#RETO 3
"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir
la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.
"""
def calcular_factura(cantidad_sin_iva, porcentaje_iva=19):
    total = cantidad_sin_iva+(cantidad_sin_iva*porcentaje_iva/100)

    print(total)
    

calcular_factura(430, 20)
calcular_factura(430)
print()


#RETO 4
"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro 
usando la primera función.
"""
def area_circulo(radio):
    pi = 3.1415

    return pi*radio**2

def volumen_cilindro(radio, altura):
    
    return area_circulo(radio)*altura

print(volumen_cilindro(3,5),"\n")


#RETO 5
"""
Escribir un programa que lea un entero positivo n, introducido por el usuario 
y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
"""
n = int(input("Digite un numero entero: "))

suma = n*(n+1)/2

print("La suma de todos los enteros desde 1 hasta ", n," es ", suma, "\n")


#RETO 6
"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal
 y lo almacene en una variable, y muestre por pantalla la frase Tu índice de
masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
peso = float(input("Digite su peso en KG: "))
estatura = float(input("Digite su altura en M: "))

imc = round(peso/estatura**2,2)

print("Su índice de masa corporal es ", imc,"\n")


#RETO 7 
"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo 
y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos 
y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa
que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete
que será enviado.
"""
peso_payaso = 112
peso_muñeca = 75

payasos = int(input("Digite el numero de payasos vendidos en el ultimo pedido: "))
muñecas = int(input("Digite el numero de muñecas vendidos en el ultimo pedido: "))

peso_paquete = peso_payaso*payasos+peso_muñeca*muñecas

print("El peso total del paquete es",peso_paquete,"gramos\n")


#RETO 8
"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total.
"""
precio = 3.49 
descuento = 60

barras = int(input("Digite las barras de pan vendidas que no son del dia: "))

total = barras*precio*(descuento/100)

print("El precio habitual de una barra de pan es:",precio,"€")
print("El descuento por una barra no fresca es:",descuento,"%")
print("El coste final total es:",total,"€\n")


#RETO 9
"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta
de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros 
tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
interes = 4/100

dinero_depositado = int(input("Digite la cantidad de dinero depositada en la cuenta de ahorros: "))

ahorro_1año = dinero_depositado*(interes+1)
ahorro_2año = ahorro_1año*(interes+1)
ahorro_3año = ahorro_2año*(interes+1)

print("los ahorros del primer año son de: $",(round(ahorro_1año,2)))
print("Los ahorros del segundo año son de: $",(round(ahorro_2año,2)))
print("Los ahorros del tercer año son de: $",(round(ahorro_3año,2)),"\n")


#RETO 10
"""
Crea un programa que dado un número entero que designa un periodo de tiempo expresado en segundos,
imprima el equivalente en días, horas, minutos y segundos.
"""
segundos=int(input("Digite la cantidad de segundos a transformar: "))

seg_a_minutos = int(segundos/60)
seg_a_horas = int(segundos/3600)
seg_a_dias = int(segundos/86400)

print("Son",segundos,"segundos,",seg_a_minutos,"minutos,",seg_a_horas,"horas,",seg_a_dias,"dias")

