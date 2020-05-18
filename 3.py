# Haz una clase llamada Persona que siga las siguientes condiciones:
# Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No
# queremos que se accedan directamente a ellos. Piensa que modificador de acceso
# es el más adecuado, también su tipo. Si quieres añadir algún atributo puedes
# hacerlo.
# Por defecto, todos los atributos menos el DNI serán valores por defecto según su
# tipo (0 números, cadena vacía para String, etc.).
# Sexo sera hombre por defecto, usa una “constante” para ello.

# Se implantaran varios constructores:
# • Un constructor por defecto.
# • Un constructor con el nombre, edad y sexo, el resto por defecto.
# • Un constructor con todos los atributos como parámetro.

# Los métodos que se implementaran son:

# • calcularIMC(): calculara si la persona esta en su peso ideal (peso en
# kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la
# función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos),
# significa que esta por debajo de su peso ideal la función devuelve un 0 y si
# devuelve un valor mayor que 25 significa que tiene sobrepeso, la función
# devuelve un 1. Te recomiendo que uses “constantes” para devolver estos
# valores.
# • esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
# • comprobarSexo(char sexo): comprueba que el sexo introducido es correcto.
# Si no es correcto, sera H. No sera visible al exterior.
# • toString(): devuelve toda la información del objeto como String en un
# formato elegido por usted.
# • generaDNI(): genera un número aleatorio de 8 cifras. Este método sera
# invocado cuando se construya el objeto. Puedes dividir el método para que
# te sea más fácil. No será visible al exterior.

# • Métodos set de cada parámetro, excepto de DNI.


from random import randint
class Persona:
    SEXO = 'H'
    
    def __init__(self):
        self.__nombre = ''
        self.__edad = 0
        self.__dni = __generaDNI()
        self.__sexo = 'H'
        self.__peso = 0
        self.__altura = 0


    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__dni = __generaDNI()
        self.__peso = 0
        self.__altura = 0


    def __init__(self, nombre='', edad=0, sexo=SEXO, peso=0, altura=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = __generaDNI()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura


    def setnombre(self, nombre):
        self.__nombre = nombre

    def setedad(self, edad):
        self.__edad = edad
    
    def setsexo(self, sexo):
        self.__sexo= sexo

    def setpeso(self, peso):
        self.__peso = peso
    
    def setaltura(self, altura):
        self.__altura = altura


    def calcularIMC(self, peso, altura):
        resultado = peso/(altura^2)

        if resultado<20:
            return -1
        elif 20<=resultado<=25:
            return 0
        elif resultado<25:
            return 1
        

    def esMayorDeEdad(self,edad):
        if edad<18:
            return "Es menor de edad"
        else:
            return "Es mayor de edad"


    def comprobarSexo(self, sexo):
        if sexo==self.__sexo:
            return "Es correcto"
        else:
            return self.setsexo('H')


    def __str__(self):
        return """\
    Nombre: {}
    Edad: {}
    Sexo: {}
    DNI:{}
    Peso: {}
    Altura:{} """.format(self.__nombre, self.__edad, self.__sexo,self.__dni,self.__peso,self.__altura)

    def __generaDNI(self):
        dni = randint(9999999, 1000000000)