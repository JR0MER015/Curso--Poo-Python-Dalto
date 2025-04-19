#hay diferentes tipos de polimorfismo
#es hace que un metodo se conforme diferente por sus propiedades

class Gato():
    def sonido(self):
        return "Miau"

class Perro():
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



