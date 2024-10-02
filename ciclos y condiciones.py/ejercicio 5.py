# programa que valide la contraseña digita, y la compara con una ya establecida 
key="contraseña123"
password=input("digite una contraseña a validar:  ")
#aqui compara la contraseña digitada con la contraseña guardada en la variable key
if key == password.lower():
    print("las contraseña son iguales : ☺️, felicidades ") 
else:
    print("atencion ¡ las contraseñas no coinciden o no son iguales, inteente denuevo" )

