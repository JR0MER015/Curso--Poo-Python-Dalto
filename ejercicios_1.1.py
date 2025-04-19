#crear una clase llamada estudiantes, atibutos nombre, edad,grado
#metodos estudiar "el estudiante (nombre)esta estudiando"
#crear un objeto Estudiante y usar el metodo estudiar()
#se debe interactuar con el usuario y este debe brindar los atributos

class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
 
pedro = Estudiante("Pedro","23",3) 

print(pedro.grado)       
