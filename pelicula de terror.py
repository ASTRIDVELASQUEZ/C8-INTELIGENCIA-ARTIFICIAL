#HACER UN PROGRAMA PARA INGRESAR A UNA PELICULA DE TERROR
#NO PUEDE TENER MAS DE 100 AÑOS

print("bienvenido a CINEMAX")
nombre=(input("digite su Nombre: "))
edad_usuario=int(input(nombre + "Digite su edad por favor: "))
if edad_usuario<100:
    print("no puede ver la pelicula puede ser perjudicial para su salud")
    edad_usuario=int(print('puede ver la pelicula'))
else:
    print("usuario entra: ")
