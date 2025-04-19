#no existe como tal en python pero hay que entenderlo
#esto se hace  para proteger clases , claves y que no se puedan acceder a ellos

#creacion de un atributo privado
class MiClase:
    def __init__(self):
        self._atributo_privado = "valor" #la forma que sea privado es mediante _ despues de self.

#nota siempre se puede imprimir aunque sea privado
objeto = MiClase()
#print(objeto._atributo_privado)

#ahota creacion de un atributo muy privado
#esto se hace con 2 guillones bajos

#a esto muy privado no se deveria de acceder
class MiClase2:
    def __init__(self):
        self.__atributo_muy_privado = "contraseña"
        
#el encapsulamiento protege algunos atributos, mejora en mantenimiento
#para acceder acceder a atributos privados se hace con setters y getters

