class Persona:
    def __init__(self,nombre,edad,):
        self.nombre = nombre
        self.edad = edad 
        
    def mostrar_datos(self):
        print(f"Nombre:{self.nombre}")
        print(f"Edad:{self.edad}")
        
#creamos una clase estudiante eque herede de personas

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)#con super no se usa self
        self.grado = grado
        
    #ahora creo un metodo para mostrar el grado
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")
        
estudiante = Estudiante("Juan",33,"Master")
estudiante.mostrar_datos()
estudiante.mostrar_grado()