#metodos especiales
#son funciones que tienen un nombre especial reservado inician con 2
#con 2 guiones bajos , como __init__

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):#devuelve como lo vere en pantalla
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    
    def __repr__(self):#es una representacion del objeto.
        return f"""Persona("{self.nombre}",{self.edad})"""
    #eran comillas sencillas,pero yo use comillas triples que es lo mismo
    #investigar como sacar una comilla sensilla
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre,nuevo_valor)
    #recordar siempre retornar para ver que se muestra
    
juank = Persona("Jc",33)
burzum = Persona("Alex",31)
sanson = Persona("Roberto",32)
poter = Persona("Ariel",32)

resultado = juank + burzum + sanson + poter
print(resultado)
print(resultado.edad)