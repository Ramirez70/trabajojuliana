class Cuenta:

    cantidad = 0.0

    def __init__(self, cedula, nombre, fecha, cantidad=None):
        self.cedula = cedula
        self.nombre = nombre
        self.fecha = fecha
        if not (cantidad is None):
          self.cantidad = cantidad

    #getter
    def get_cedula(self):
        return self._cedula
    def get_nombre(self):
        return self._nombre
    def get_fecha(self):
        return self._fecha
    def get_cantidad(self):
        return self._cantidad

    #setter
    def set_cedula(self , cedula):
        self.cedula = cedula
    def set_nombre(self , nombre):
        self.nombre = nombre
    def set_fecha(self, fecha):
        self.fecha = fecha
    def set_fecha(self, cantidad):
        self.cantidad = cantidad

    def __repr__(self):
        return str(self.__dict__)

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad

    def retirar(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad = self.cantidad - cantidad
        else:
          self.cantidad = 0.0
          print("Se pudo retirar ", self.cantidad)


cuenta = Cuenta(1000532011, "Evelin Kalil", "21/03/2020", 5000)
print(cuenta)

