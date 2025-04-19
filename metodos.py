#los metos son acciones que pueden hacer los objetos , como correr, jugar etc
#las funciones se programan como metodos
#todas las funciones que creemos en una clase son metodos

class Celular:
    def __init__(self,marca,modelo,camara):#esto es un metodo contructor 
        self.marca = marca #decir self.marca es como decir celular.marca
        self.modelo = modelo#esto define las propiedades del objeto
        self.camara = camara
        
    def llamar(self):#siempre que el metodo este dentro de una clase se le agrega self
        print(f"Estas haciendo un llamado desde un {self.modelo}")
        
    def cortar(self):
        print(f"Cortaste la llamada desde tu modelo {self.modelo}")
        
            
celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15 Pro","96MP")

print(celular1.llamar())



