





if tipo_operacion == "2": #aqui se realiza la resta 
    print("usted ha eligido resta de dos numeros: ")
    primernumero=float(input("digite el primer numero a operar:  "))
    segundonumero=float(input("digite el segundo numero a operar:  "))
    resta=primernumero-segundonumero
    print("el resultado de la resta es : " ,resta)

elif tipo_operacion == "3": #aqui se realiza la multiplicacion 
    print("usted a elegido multiplicar dos numeros: ")
    primernumero=float(input("digite el primer numero a operar: "))
    segundonumero=float(input("digite el segundo numero a operar: "))
    multiplicacion=primernumero*segundonumero
    print("el resultado de la multiplicacion es: ",multiplicacion)

elif tipo_operacion == "4":
    print("usted ha elegido dividir dos numeros: ")
    primernumero=float(input("digite el primer numero a operar: "))
    segundonumero=float(input("digite el segundo numero a operar: "))
    division=primernumero/segundonumero
    print("el resultado de la divicion es: ",division)
elif tipo_operacion == "5":  #aqui se realiza la potencia
    print("usted ha elegido potencia dos numeros: ")
    primernumero=float(input("digite el primer numero a operar: "))
    segundonumero=float(input("digite el segundo numero a operar: "))
    potencia=primernumero**segundonumero
    print("el resultado de la potencia del primer numero y el segundo numero es:  ",potencia)

elif tipo_operacion == " ":
     print("ha elejido una pocion n valida, intente de nuevo porfavor")

else:
     print("Atencion debe elegir una opcion rntre  1 y 5 unicamente gracias")