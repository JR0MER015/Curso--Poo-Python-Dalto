#crear una clase llamada estudiantes, atibutos nombre, edad,grado
#metodos estudiar "el estudiante (nombre)esta estudiando"
#crear un objeto Estudiante y usar el metodo estudiar()
#se debe interactuar con el usuario y este debe brindar los atributos

class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("Estudiando...")
    
nombre = input("Digame su nombre:  ") 
edad = input("Digame su edad:  ") 
grado = input("Digame su grado:  ") 
 
estudiante = Estudiante(nombre,edad,grado) 

print(f"""Datos del estudiante: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      """)       

while True:
    estudiar =input()
    if (estudiar.lower() == "estudiar"):#los metodos se colocan con ()
        estudiante.estudiar()