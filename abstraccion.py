#es ocultar lo completo y mostrar lo simple
#es decir no importa como se se obtiene , si no como se usa
#el auto es electronico

class Auto():
    def __init__(self,):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_auto = Auto()
mi_auto.conducir()
#aqui hay abstraccion ya que el usuario lo que ve es que se conduce pero no ve lo
#lo que hay detras , la accion de ensenderlo si esta apagado 


