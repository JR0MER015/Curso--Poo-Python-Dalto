#creando clases , ya puede ser en snakecase,camelcase o pascalcase(esta es como camel case pero inicia con mayuscula)
#por general las clases se hacen es pascalcase.

#creando la clase
class Celular():
    marca = "samsung"#estos son atributos fijos
    modelo = "S23"     
    camara = "48MP"
    
#creando el objeto
celular1 = Celular()

#tambien podria crear diferentes objetos o modelos de celulales
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()

#tambien podria cambiar la camara por ejemplo
celular3.camara ="43MP"#aunque esto no es optimo

#accediendo por ejemplo a la marca
print(celular3.camara)



