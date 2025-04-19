#crear personajes en un juego que se puedan fusionar

class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza 
        self.velocidad = velocidad
        
    #ahora creo una representacion para ver crear al personaje
    def __repr__(self):
        return f"""{self.nombre} (fuerza: {self.fuerza}, velocidad :{self.velocidad})"""
     
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**2)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**2)
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
    
burrito = Personaje("Burrito",100,100)
culo_sucio = Personaje("Culo Sucio",666,666)

El_culo_sucio_de_Burrito = burrito + culo_sucio
print(El_culo_sucio_de_Burrito)