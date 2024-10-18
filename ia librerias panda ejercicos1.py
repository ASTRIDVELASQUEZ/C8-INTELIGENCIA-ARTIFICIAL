#creamos un objeto de tipo series con los datos de una lista
import pandas as pd 
materias=pd.series(["ciencias", "historia", "economia", "programacion", "ingles", "emprendimiento"])
materias2=pd.Series(["ciencias", "historia", "economia", "programacion", "ingles", "emprendimiento"], dtype= "string")
print(materias)
print("\n")
print(materias2)
