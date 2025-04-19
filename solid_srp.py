#S- srp,principio de responsabilidad único
#una clase debe tener una sola razon para cambiar
#la clase se debe dedicar a una cosa 
#evitar que las clases esten sobre cargadas y asi no dependan de otras

#ejemplo
#class Auto():
#    def __init__(self):
#        self.position = 0
#        self.combustible = 100
        
#    def mover (self,distancia):
#        if self.combustible >= distancia / 2:
#            self.position += distancia
#            self.combustible -= distancia / 2 
#        else:
#            print("No hay combustible")
            
#    def agregar_combustible(self,cantidad):
#        self.combustible += cantidad
        
#    def obtener_combustible(self):
#        return self.combustible
    
# el codigo esta bien pero esta incumpliendo el principio ya que esta tomando el movimiento y combudtible
#ra cumplir el principio lo que hago es divivir la clase
#ejemplo correcto

class TanqueDeCombustible():
    def __init__(self):
        self.combustible = 100#propiedad estatica que tendra 100
    
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible
        
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad


class Auto():
    def __init__(self,tanque):#aqui agrego tanque para crear el objeto
        self.position = 0 #estatico
        self.tanque = tanque #varianza ya que esta definido
        
    def mover (self,distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.position += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente")
        else:
            print("No hay combustible")
     
    def obtener_posicion_auto(self):
         return self.position
            
       
#creando los objetos
tanque = TanqueDeCombustible()
auto = Auto(tanque)

#
print(auto.obtener_posicion_auto())
print(auto.mover(10))
print(auto.obtener_posicion_auto())
print(auto.mover(20))                       
print(auto.obtener_posicion_auto())
print(auto.mover(60))
print(auto.obtener_posicion_auto())
print(auto.mover(100))       
print(auto.obtener_posicion_auto())
print(auto.mover(100))    




