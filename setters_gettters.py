#se usan para acceder o madificar una class privada
#class privada,funciona igual con una clase muy privada
class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        
#asi no deberiamos acceder ya que hay un guion bajo y la clase es privada       
#jc = Persona("Juan",33)
#print(jc._edad)

    def get_nombre(self):#obtenemos el valor predefinido
        return self._nombre
    
    def set_nombre(self,new_nombre):#obtenemos el valor privado y modificamos el valor privado
        self._nombre = new_nombre
    
jc = Persona("Juan",33)

nombre = jc.get_nombre()
print(nombre)

jc.set_nombre("Juankita corazón del Nazareno")#aqui cambio el nombe son set

nombre = jc.get_nombre() #y llamo el nombre con get ya que esta cambiado
print(nombre)
        