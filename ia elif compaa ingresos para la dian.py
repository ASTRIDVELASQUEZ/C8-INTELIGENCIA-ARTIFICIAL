# este programa es para realizar la comparacion de los ingresos de una persona para declarar 
ingresos=float(input("cual es su ingreso anual:  "))
#condicional para determinar el porcentaje a pagar de impuesto
if ingresos < 10000:
    porcentaje = 5
elif ingresos <20000:
    porcentaje=15
elif ingresos <35000:
    porcentaje=20
elif ingresos<60000:
    porcentaje=30
else:
    porcentaje=45   
print("TIENE QUE PAGAR $",ingresos*porcentaje/100)

