#PROGRAMA QUE REALIZA LA GESTION ACADEMICA DEL COLEGIO SAGRADA FAMILIA.
listaestudiantes=[]
class Estudiantes():
    def __init__(self, cedula, nombre, apellido, edad, nota1=0, nota2=0, nota3=0):
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
        self.promedio = (float(nota1) + float(nota2) + float(nota3)) / 3
        self.historial=[]

    def entregadatos(self):
        
        print("Cedula: ", self.cedula, "Nombre: ", self.nombre, self.apellido, "Edad", self.edad, "Notas: ", self.nota1, self.nota2, self.nota3, "Promedio: ", self.promedio)

    def editarnotas(self, nota1, nota2, nota3):

        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
        self.notafinal=(nota1+nota2+nota3)/3
        print("Registro exitoso")

    def incluirevento(self, nota1, nota2, nota3):
        return(nota1, nota2, nota3)
    
def registrarestudiante():
    print("registro de estudiantes ")
    cedula=int(input("ingrese el numero de cedula del estudiante: "))
    nombre=input("ingrese el nombre del estudiante: ")
    apellido=input("ingrese el apellido del estudiante: ")
    edad=input("ingrese el edad del estudiante: ")
    nota1=input("ingrese el nota1 del estudiante: ")
    nota2=input("ingrese el nota2 del estudiante: ")
    nota3=input("ingrese el nota3 del estudiante: ")
    objAlumno=Estudiantes(cedula, nombre, apellido, edad, nota1, nota2, nota3)
    listaestudiantes.append(objAlumno)

def listadoestudiantes():
    print("Listado de estudiantes ")
    for i in listaestudiantes:
        i.entregadatos()

def buscarestudiantes():
    cedula=int(input("Ingresa el numero de cedula a buscar "))
    for i in listaestudiantes:
        if cedula==i.cedula:
            i.entregadatos()
        
        else:
            print("No hay estudiante registrado con la cedula ", cedula)

def modificarnota():
    print(" Modificar Nota")
    cedula=int(input("Ingrese el numero de cedula a buscar: "))
    for objAlumno in listaestudiantes:
        if cedula== objAlumno.cedula:
            n1=float(input("Ingrese la nota 1: "))
            n2=float(input("Ingrese la nota 2: "))
            n3=float(input("Ingrese la nota 3: "))
            objAlumno.editarnotas(n1, n2, n3)
            objAlumno.entregadatos()
            #recepcionmensaje=objAlumno.incluirevento(n1, n2, n3)
            #objAlumno.historial.append(recepcionmensaje)
        else:
            print("No existe estudiante con este numero de cedula")

def eliminar():
    #print("Historial ")
    cedula=int(input("Ingrese el numero de cedula a eliminar: "))
    for i in listaestudiantes:
        if cedula==i.cedula:
            listaestudiantes.remove(i)
            print("Eliminado")
        else:
            print("No hay estudiante registrado con la cedula: ", cedula)

def salir():
    print("Gracias por utilizarme")
    exit()

def menu():
    while True:
        print("\n")
        print("|********************************************************************************|")
        print("|***************************COLEGIO SAGRADA FAMILIA******************************|")
        print("|*******************************SISTEMA DE NOTAS*********************************|")
        print("                     Seleccione la opcion                                         ")
        print("                         1.-Registrar estuduante")
        print("                         2.-Mostrar estuduante")
        print("                         3.-Buscar estuduante")
        print("                         4.-Modificar estuduante")
        print("                         5.-Eliminar")
        print("                         6.-Salir \n")

        opcion=int(input("Digite la opcion: "))
        print("")
        if opcion==1:
            registrarestudiante()
        elif opcion==2:
            listadoestudiantes()
        elif opcion==3:
            buscarestudiantes()
        elif opcion==4:
            modificarnota()
        elif opcion==5:
            eliminar()
        elif opcion==6:
            salir()

menu()


            
