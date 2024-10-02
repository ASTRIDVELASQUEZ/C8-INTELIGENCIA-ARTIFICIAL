# programa que valida si un correo tiene el @ incluido
email=False
miemail=input("digite por favor rl email completo: ")
for i in miemail: 
    if i == "@":
        email=True
if email==True:
         print("el correo es valido por que tiene el sombolo @")
else:
      print("el correo no es valido por que no tiene el @")
