#programa que compara los salarios de los empleados de una empresa 
salario_presidente=int(input("digite el salario deln presisdente d ela empresa: "))
salario_director=int(input("digite el saalrio deñ director: "))
salario_jefe_de_area=int(input("deigite el salrio del jefe de area"))
salario_administrativo=int(input("digite el salario del administrador: "))
#aqui comparamos los salarios en orden de cargos a mayor cargo mas salario
if salario_presidente>salario_director>salario_jefe_de_area > salario_administrativo:
    print("los salario estan asignados de manera correcta, deacuerdo al cargo")

else:
    print("la escala salarial se debe ajustar o replantear, deacuerdo al orden de los cargos")
    