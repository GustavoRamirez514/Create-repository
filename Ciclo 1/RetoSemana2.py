#Reto de la semana 2, miercoles 19 de mayo
"""
Para los clientes nacionales, si las compras acumuladas anuales son iguales o superan los $200.000.000
le asigna un recargo del 10% a todas las compras. Si no llega a este monto total, se verifica que por lo
menos en el tipo de producto "Agujas" haya comprado más de $70.000.000, en "Escolares" una
compra superior a $30.000.000 y en "Hogar" compras superiores a $40.000.000 entonces se le
asignará un recargo del 7% a todas sus compras. Pero en solo superó los topes anteriores para algunos
de los productos, se cobrará un 5% al tipo de producto que haya superado el umbral.
Para los clientes internacionales, los precios están en dólares, se aplican reglas equivalentes a la de los
clientes nacionales, pero con los siguientes umbrales y porcentaje de descuentos a aplicar:
Para compras totales de US$100.000 o superiores, un 8% de descuento. 5% si compra mas de
US$25.000 en Agujas, mas de US$10.000 en Escolares y US$15.000 en Hogar. Si superan el umbral
individual un 3% por cada tipo que lo supere.
"""

def calculo_recargos(cliente: dict) -> dict:
     
    if cliente["nacional"] == True :
        
        compras_acumuladas = cliente["agujas"] + cliente["escolares"] + cliente["hogar"]
        del cliente["nacional"]

        if compras_acumuladas >= 200000000 : 
                
            cliente["agujas"] = 10.0
            cliente["escolares"] = 10.0
            cliente["hogar"] = 10.0

            return cliente
    
    
        elif cliente["agujas"] > 70000000 and cliente["escolares"] > 30000000 and cliente["hogar"] > 40000000 :
               
                cliente["agujas"] = 7.0
                cliente["escolares"] = 7.0
                cliente["hogar"] = 7.0
                
                return cliente


        if cliente ["agujas"] > 70000000 and cliente["escolares"] > 30000000 :

                cliente["agujas"] = 5.0
                cliente["escolares"] = 5.0
                cliente["hogar"] = 0.0

                return cliente

        if cliente["agujas"] > 70000000 and cliente["hogar"] > 40000000 :

                cliente["agujas"] = 5.0
                cliente["escolares"] = 0.0
                cliente["hogar"] = 5.0

                return cliente

        if cliente["escolares"] > 30000000 and cliente["hogar"] > 40000000 :

                cliente["agujas"] = 0.0
                cliente["escolares"] = 5.0
                cliente["hogar"] = 5.0

                return cliente


        if cliente["agujas"] > 70000000 :
                cliente["agujas"] = 5.0

        if cliente["escolares"] > 30000000 :
                cliente["escolares"] = 5.0
        
        if cliente["hogar"] > 40000000 :
                cliente["hogar"] = 5.0


        else:
            cliente["agujas"] = 0.0
            cliente["escolares"] = 0.0
            cliente["hogar"] = 0.0

        return cliente



    elif cliente["nacional"] == False :

        compras_acumuladas = cliente["agujas"] + cliente["escolares"] + cliente["hogar"]
        del cliente["nacional"]

        if compras_acumuladas >= 100000 : 

                cliente["agujas"] = 8.0
                cliente["escolares"] = 8.0
                cliente["hogar"] = 8.0
                
                return cliente

    
        if cliente["agujas"] > 25000 and cliente["escolares"] > 10000  and cliente["hogar"] > 15000  :
               
                cliente["agujas"] = 5.0
                cliente["escolares"] = 5.0
                cliente["hogar"] = 5.0
                
                return cliente

        
        if cliente ["agujas"] > 25000 and cliente["escolares"] > 10000 :

                cliente["agujas"] = 3.0
                cliente["escolares"] = 3.0
                cliente["hogar"] = 0.0

                return cliente

        if cliente["agujas"] > 25000 and cliente["hogar"] > 15000 :

                cliente["agujas"] = 3.0
                cliente["escolares"] = 0.0
                cliente["hogar"] = 3.0

                return cliente

        if cliente["escolares"] > 10000 and cliente["hogar"] > 15000 :

                cliente["agujas"] = 0.0
                cliente["escolares"] = 3.0
                cliente["hogar"] = 3.0

                return cliente


        if cliente["agujas"] > 25000 :
                cliente["agujas"] = 3.0
            
        if cliente["escolares"] > 10000 :
                cliente["escolares"] = 3.0
        
        if cliente["hogar"] > 15000 :
                cliente["hogar"] = 3.0
        
        else: 
            cliente["agujas"] = 0.0
            cliente["escolares"] = 0.0
            cliente["hogar"] = 0.0      
            
        return cliente


print(calculo_recargos( cliente ={
"nombre": "César Díaz",
 "nacional": False,
 "agujas": 0.0,
 "escolares": 0.0,
 "hogar": 0.0
}))

print(calculo_recargos( cliente ={
 "nombre": "César Díaz",
 "nacional": False,
 "agujas": 150000000.0,
 "escolares": 30000000.0,
 "hogar": 20000000.0
}))

print(calculo_recargos( cliente ={
 "nombre": "César Díaz",
 "nacional": False,
 "agujas": 100000001.0,
 "escolares": 32000000.0,
 "hogar": 41325120.0
}))

print(calculo_recargos( cliente ={
 "nombre": "César Díaz",
 "nacional": False,
 "agujas": 70000100.0,
 "escolares": 20000000.0,
 "hogar": 40000001.0
}))

print(calculo_recargos( cliente ={
 "nombre": "César Díaz",
 "nacional": False,
 "agujas": 25000,
 "escolares": 10000,
 "hogar": 15000
}))