#es una clase que no se puede instanciar pero se puede usar para otras clases
#es como herencia pero mas complejo,es como una plantilla
#implementar un metodo es definir como funciona

#abc es un modulo de python ,ABC esto es una clase,abstrasmethod es una metaclase
#metaclase o metodoclase, es un metodo que no tiene implementacion

#abstractclassmethod is deprecated usar abstractmethod

from abc import ABC,abstractmethod

class Persona(ABC):#el metodo abstracto es ABC ojo
    @abstractmethod #decorador para un metodo abstracto
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad #la he creado despues para la herencia en estudiante
        
    @abstractmethod #decorador para un metodo abstracto
    def hacer_actividad(self):
        pass
    def presentarse(self):
        print(f"Hola me llamo : {self.nombre} , y tengo : {self.edad} años")
 
#todo lo de arriba es una plantilla que nos permite crear personas  
        
#juank = Persona("Juan",33,"masculino","Finanzas")

#no se ejecuta ya que el metodo abstracto actividad no esta definido , si quito el ABC
#funcionaria ya que los classmethod, pierden el chiste        

#ahora creare una nueva clase que herede de personas
class Estudiante(Persona):
        def __init__(self,nombre,edad,sexo,actividad):
            super().__init__(nombre,edad,sexo,actividad)
            
        def hacer_actividad(self):
            print(f"Estoy estudiando : {self.actividad}")
            
class Trabajador(Persona):
        def __init__(self,nombre,edad,sexo,actividad):
            super().__init__(nombre,edad,sexo,actividad)
            
        def hacer_actividad(self):
            print(f"Estoy trabajando como : {self.actividad}")
        
juank = Estudiante("Juan",33,"masculino","Finanzas")
Lic_Romero = Trabajador("Romero",15,"masculino","Master")
    

juank.presentarse()
juank.hacer_actividad()
Lic_Romero.presentarse()
Lic_Romero.hacer_actividad()

#usar clases abstractas son como contratos es decir formatos 
#fomentan el polimorfismo
