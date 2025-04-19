#es un funcion que decora a otra
def decorador (funcion):
    def funcion_modificada():
        print("Antes de llamar la funcion")
        funcion()
        print("Despues de llamar la funcion")
    return funcion_modificada #no la devolvemos ejecutada

# def saludo():
#     print("Hola Jc")

# #para llamar al decorador se hace asi,primero creo una variable

# saludo_modificado = decorador(saludo)
# saludo_modificado()

# #ctrl,k,c comento todo el codigo
# # #lo que se hizo arriba no es optimo, lo mejoramos asi

@decorador#el decorador se llama con @ y despues creo la definición
def saludo():
     print("Hola Junankita")
     
saludo()
 
#esto sirve para hacer validaciones     
