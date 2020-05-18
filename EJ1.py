class Contador:

    def __init__(self, contador=0):
        self.contador = contador

    def constructor_dos(self, contador=0):
        self.contador = contador

    def __str__(self):
        return self.contador

    def getcontador(self):
        return self.contador

    def setcontador(self, contador):
        self.contador = contador

    def aumentar(self, n_aumento):
        total1 = self.getcontador()
        total2 = total1 + n_aumento
        self.setcontador(total2)
        print(total2)

    def disminuir(self, n_disminuir):
        total = self.getcontador()
        totalr = total - n_disminuir
        self.setcontador(totalr)
        print(totalr)

contador = Contador(5).aumentar(8)
