from .vehicle import Vehicle    

class Motorcycle(Vehicle):

    def __init__(self, vMax, peso, potencia, tipo):
        super().__init__(vMax, peso, potencia)
        self.tipo = tipo

    def getTipo(self):
        return self.tipo