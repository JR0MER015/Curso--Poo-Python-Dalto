#los atributos son variables que pertenecen a una clase
#con este codigo he creado una maquina de celulares

class Celular:
    def __init__(self,marca,modelo,camara):#esto es un metodo contructor 
        self.marca = marca #decir self.marca es como decir celular.marca
        self.modelo = modelo#esto define las propiedades del objeto
        self.camara = camara
    
celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15 Pro","96MP")

print(celular2.marca)

