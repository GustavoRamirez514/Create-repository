#Clase 9, miercoles 19 de mayo

#RETO 1
"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas.
"""
numero = int(input("Digite un numero: "))

while numero >= 0 :
    print (numero, end=",")
    numero = numero - 1
print ()


#RETO 2
"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
triángulo rectángulo como el de más abajo, de altura el número introducido.
"""
numero = int(input("Digite un numero: "))

for contador in range(numero+1) :
    print ("*" * contador)
print()


#RETO 3 
"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
triángulo rectángulo como el de más abajo, de altura el número introducido.
"""
numero = int(input("Digite un numero: "))
for contador in range(1, numero+1, 2):
    for contador2 in range(contador, 0, -2):
        print(contador2, end=" ")
    print(" ")
print (" ")    


#RETO 4
"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba
“salir” que terminará.
"""
while True :
 eco = input("Digite lo que se hara: ")
 
 if eco == "salir" :
   import sys
   sys.exit("Has salido del sistema")
 print (eco)
