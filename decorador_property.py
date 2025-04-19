#son como getters , setters y ademas deletters
#funciona igual como con datos privados y muy privados
class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad

    @property#este es un decorados que le dice al codigo mira esto que viene es un getter
    def nombre(self):#obtenemos el valor predefinido
        return self._nombre
    
    @nombre.setter #este es un decorador para setter
    def nombre(self,new_nombre):#obtenemos el valor privado y modificamos el valor privado
        self._nombre = new_nombre
        
    @nombre.deleter #este es un decorador para deleler
    def nombre(self):#obtenemos el valor privado a eliminar el valor privado
       del self._nombre
    
    
jc = Persona("Juan",33)

nombre = jc.nombre #como tengo un decorador @property no uso ()
print(nombre)

jc.nombre ="Juankita corazón del Nazareno"#aqui cambio el nombe son set

nombre = jc.nombre #y llamo el nombre con get ya que esta cambiado
print(nombre)

#aqui estoy eliminando 
#del jc.nombre # si lo comento se corre bien
nombre = jc.nombre #y llamo el nombre con get ya que esta cambiado
print(nombre)#da un error ya que que con del se elimino todo



