#metodo de resolucion de orden con varias clases para definir que metodo tomaria de referencia

class A:
    def hablar(self):#seria el  ultimo en ejecutarse ya que es el padre
        print("Hola desde A")
        
class B(A):#como b es el segundo en gerarquia se ejecutari desúes
    def hablar(self):
        print("Hola desde B")
        
class C(A):#se ejecutaria por tercero
    def hablar(self):
        print("Hola desde c")

#ejemplo pasando esta clase ya que por jerarqui se seguiria ejecuando        
class D(B,C):
    pass
    #def hablar(self):
    #    print("Hola desde D")        
        
#cual es el orden de ejecucion si creo un objeto

d = D()

d.hablar()

#con este tema lo que se debe hacer es probar las clases y herencias ,
# se puede hacer un diagrama de flujo

#tambien puede usar mro(), para ver el arbol de herencias
print(D.mro())

#si quiero llamar una clase mas especifica ,primero coloco la clase
#luego llamo a el objeto

B.hablar(d)
