#RETO 1
"""
Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
"""
numero = input("Digite un numero de dos digitos: ")

if int(numero)<9 or int(numero)>99:
    import sys
    sys.exit("El numero digitado no tiene dos digitos")

if int(numero[0]) % 2 == 0:
    print("El primer digito es par")
else: 
    print("El primer digito NO es par")

if int(numero[1]) % 2 == 0:
        print("El segundo digito es par")
else:
    print("El segundo digito NO es par")


#RETO 2
"""
A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. 
Si la cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las horas extras. 
Calcular el salario del trabajador dadas las horas trabajadas y la tarifa ingresadas por el usuario.
"""
incremento=50/100

tarifaXhora = int(input("Digite la tarifa por hora: "))
horas_trabajadas = int(input("Digite las horas trabajadas: "))

if int(horas_trabajadas) > 40:
    salario = horas_trabajadas * ((tarifaXhora * incremento) + tarifaXhora)

    print("Su salario es de $", salario)
else :
    salario = horas_trabajadas * tarifaXhora

    print("Su salario es de: $", salario)


#RETO 3
"""
Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o más 
se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%
"""
def camisas (num_camisas, precio_camisas):
    if num_camisas < 1 or precio_camisas < 10000:
        import sys
        sys.exit("Datos ingresados invalidos")
    
    if num_camisas > 0 and num_camisas < 3:
        total=  num_camisas * ((precio_camisas * 0.1) + precio_camisas)
        print("Su total a pagar es de", total ,"con descuento del 10%")
    
    if num_camisas >= 3 :
        total=  num_camisas * ((precio_camisas * 0.2) + precio_camisas)
        print("Su total a pagar es de", total, "con descuento del 20%")

camisas(2, 20000)
camisas(3, 20000)
camisas(0,20000)
camisas(1,10)

#RETO 4
"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
nombre = input("Digite su nombre: ")
numero = input("Digite un numero entero: ")

print((nombre+"\n")*int(numero))


