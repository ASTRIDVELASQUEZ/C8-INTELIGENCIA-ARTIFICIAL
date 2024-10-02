#programa jovenes en accion se deben cumplir 3 condiciones para poder aspirar al aculio 
#1 que el estudiante viva a mas de 40 km del colegio 
#2 que tenga mas hermanos en el mismo colegio
#3 que el salrio mensual familiar sea <= de 200.000
#4 que el sisben sea menor a 5
print("programa para postularse al auxilio de jovenes en accion, cumpliendo los 4 condiciones")
distancia_colegio=int(input("digite la distancia desde su casa al colegui en km: "))
numero_hermanos=int(input("digite el numero de hermanos que estudian en su IE:  " ))
salario_familiar=int(input("digite el valor del salario o ingreso en su familia:  " ))
sisben_menor=int(input("digite el nivel del sisben:"  ))
#aqui utilizamos un if para compara las variables digitadas por el ususario 
if distancia_colegio>40 and numero_hermanos>2 and salario_familiar <=200000 and sisben_menor<5:
    print("usted es apto para recibir el auxilio de jovenes en accion ya que cumple con las condiciones")
    print("la distancia de su casa al cooegio a su casa mayor de 40km", distancia_colegio)
    print("usted tiene mas de 2 hermanos estudiando en el mism colegio")
    print("el ingreso familiar en su hogar es menor de 200000", salario_familiar)
    print("el ingreso del nivel del sisben es menor de 5", sisben_menor)
else:
    print("lo siento, usted no cumple con las condiciones basicas para recibir el auxilio")