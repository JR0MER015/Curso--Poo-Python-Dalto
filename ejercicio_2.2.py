class Animal:
    def comer(self):
        print("El animal esta comiendo")
        
class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando") 
        
class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.volar()
murcielago.amamantar()    

#igual lo puedo hacer con el metod ave solo que no tiene la opcion amamantar

print(Murcielago.mro())
   