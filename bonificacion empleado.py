#programa que mide el desepeño de un empleado para el pago de una comicion anual
#a mejor desempeño ganas mas comision los valores estan entre 0 .04 y 0.6 punto
bonificacion_diciembre=2400 # este es el pago de la comicion por buen trabajador
#escala de calificacion de rendimiento de empleado 
inaceptable=0
aceptable=0.04
sobresaliente=0.6
print("programa que  mide el desempeño de un empleado: inaceptable / aceptable / sobresaliente")
puntos=float(input("digite su puntuacion con valores validos entre: 0 , 0.4 y 0.6 unicamente : "))
#clasificamos por nibeles de emprendimiento
if puntos == inaceptable:
    nivel="inaceptable"
elif puntos== aceptable: 
    nivel= "aceptable" 
elif puntos >= 0.6:
    nivel="sobresaliente"
else:
    nivel=""

if nivel=="":
    print("esta no es una opcion valida")
else:
    print("su nivvel de rendimiento es %s" % nivel)
    print ("le corresponde cobrar %.2f$" %(puntos*bonificacion_diciembre))