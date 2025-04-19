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
    
juank = Persona("Jc",33)

#print(juank)

repre = repr(juank)
resultado = eval(repre)
print(resultado)

#como resultado es un objeto tambien puedo hacer esto
print(resultado.nombre)
