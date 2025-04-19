#plimorfismo con herencias en este caso todo viene de animal

class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
#aplicando polimorfismo
#creando objetos
gato = Gato()
perro = Perro()

hacer_sonido(gato)

#print(gato.sonido())
#print(perro.sonido())



