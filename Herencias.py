#que una clase tenga las caracteristicas de la clase padres
#esto es una herencia simple
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):#este metodo es lo que hace
        print("Hola, estoy hablando un poco")

#pass se usa para que las clase no tengan nada
class Empleado(Persona):#aqui la clase empleado heredo a personas
    #pass
    def __init__(self,nombre,edad,nacionalidad, trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)#lo que va a heredar
        self.trabajo = trabajo
        self.salario = salario

#creando una nueva clase estudiante heredando de personas 
#herencia jerarquica, padre:personas, hijos :empleados y estudiantes        
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)#lo que va a heredar
        self.notas = notas
        self.universidad = universidad

roberto = Empleado("Roberto",43,"Hondureña","Profesor",3000)#y funcionaria igual si la clase fuera persona y que es la clase padre

#print(roberto.nombre)
roberto.hablar()
