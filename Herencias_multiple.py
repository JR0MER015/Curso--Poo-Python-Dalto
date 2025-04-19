#que una clase tenga las caracteristicas de la clase padres
#esto es una herencia multiple
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):#este metodo es lo que hace
        print("Hola, estoy hablando un poco")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrat_habilidad(self):#esto es un metodo
        return f"Mi habilidad es :{self.habilidad}"
        
#creando una clase que tenga informacion de varias clases
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,empresa,salario):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    #def mostrar_habilidad(self):
    #    print("no tengo :(")
    
    #con self yo acceso a presentar accion de esta calse actual
    #con super acceso a la accion de la clase padre
    def presentarse(self):
        #return f"{self.mostrat_habilidad()}"#llamo a la clase actual
        #return f"{super().mostrat_habilidad()}" #llamo clase padre
        print(f"Hola,soy : {self.nombre},{self.mostrat_habilidad()} y trabajo en {self.empresa}")
        
roberto = EmpleadoArtista("Roberto",43,"Hondureña","Profesor","Escuela CuSu",30000)#y funcionaria igual si la clase fuera persona y que es la clase padre

#print(roberto.nombre)
roberto.presentarse()

print(roberto.salario)

#como saber si uns clase herencia o es padre
herencia = issubclass(EmpleadoArtista,Artista)

#print(herencia)#si regresa True es que es verdad

#ahora como saber si es una instancia u objeto,de una clase
instancia = isinstance(roberto,EmpleadoArtista)

print(instancia)



