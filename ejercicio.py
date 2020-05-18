import operator

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return  "Color {} , {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada= cilindrada
    def __str__(self):
        return "Color {} , {} KM/H, {} ruedas, {} cc".format(self.color, self.ruedas,  self.velocidad, self.cilindrada)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo

    def __str__(self):
        return "Color {} , {} ruedas, tipo {} ".format(self.color, self.ruedas, self.tipo)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada= cilindrada
        self.carga = carga
    def __str__(self):
        return "Color {} , {} KM/H, {} ruedas, {} cc, carga {}".format(self.color, self.velocidad, self.ruedas, self.cilindrada, self.carga)


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Color {} , {} ruedas, tipo {},  {} KM/H, {} cc ".format(self.color, self.ruedas, self.tipo, self.velocidad, self.cilindrada)


coche = Coche('azul', 4, 150, 1200)
bicicleta = Bicicleta("Amarillo", 2, "urbana")
camioneta = Camioneta("Gris", 4 , 200, 6000, 50)
motocicleta = Motocicleta ("Blanco", 2, "Deportiva", 50, 200)

vehiculos = [coche, bicicleta, camioneta, motocicleta]


def catalogar(vehiculos, ruedas = 4):
    cont = 0
    for vehiculo in vehiculos:
        if ruedas == vehiculo.ruedas:
            print(vehiculo.__dict__)
            cont = cont + 1

    print ("Se han encontrado {} vehículos con {} ruedas:".format(cont,ruedas))

resultado = catalogar(vehiculos, 3)




