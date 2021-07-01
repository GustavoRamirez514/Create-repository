import math


def simulador_prestamo_baniscutp(datos_prestamo: dict) -> dict:

 
 MESES = int(datos_prestamo["cuotas"])

 TMV = (math.pow((1+(datos_prestamo["interes anual"]/100)),(1/12))-1)*100 

 saldo_financiar = round(datos_prestamo["prestamo"] + datos_prestamo["gastos documentacion"],0)

 TMV /= 100

 cuota = round(( saldo_financiar * TMV ) / (1 - math.pow((1 + TMV),-MESES)),0)

 nuevo_saldo = saldo_financiar

 diccionario1 = { 
    "saldo financiar": saldo_financiar, 
    "cuota": cuota,
    "amortizacion": []
  }


 for n in range(MESES):

  valor_interes = round(nuevo_saldo * TMV,2)

  capital_abonado = round(cuota - valor_interes,2)


  if n == MESES-1:

      excedente = round(nuevo_saldo - capital_abonado,2)

      capital_abonado = nuevo_saldo

      cuota = cuota + excedente
          
          
  nuevo_saldo = round(nuevo_saldo - capital_abonado,2)

  diccionario1["amortizacion"] +=  [
    (n+1,
    capital_abonado,
    valor_interes,
    cuota,
    nuevo_saldo)]  
  

 return TMV
"""
print(simulador_prestamo_baniscutp (datos_prestamo= {
"prestamo": 2000000.0, 
"gastos documentacion": 0.0, 
"cuotas": 6, 
"interes anual": 28.99
}))
"""
print(simulador_prestamo_baniscutp (datos_prestamo= {
"prestamo": 1200000, 
"gastos documentacion": 100000, 
"cuotas": 12, 
"interes anual": 25.13
}))
