import time as t

class Vehicle:
    def __init__(self, vMax, peso, potencia):
        self.vMax = vMax
        self.velocidadActual = 0
        self.tiempo = 0
        self.peso = peso
        self.potencia = potencia


    def getTiempo(self):
        return self.tiempo
    
    def getVMax(self):
        return self.vMax


    def setVMax(self, vMax):
        self.vMax = vMax

    def turbo(func):
        def wrapper(self, distancia):
            valorRetorno = func(self, distancia)
            if self.tiempo > 10:
                self.vMax = self.vMax * 1.1
                print("Se activo el turbo" + self.getTipo() + " " + str(self.vMax))
            return valorRetorno
        
        return wrapper

    def calcularAceleracion(self):
        aceleracion = self.potencia / self.peso
        return aceleracion


    @turbo
    def correrCarrera(self,distancia):
        aceleracion = self.calcularAceleracion()
        velocidad_final = (0 ** 2 + 2 * aceleracion * distancia) ** 0.5
        if (velocidad_final > self.vMax):
            velocidad_final = self.vMax
        self.tiempo =(velocidad_final - 0) / aceleracion
        if self.tiempo>10:
            distanciaFaltante = distancia - (0.5 * aceleracion * 10 ** 2)
            velocidadFinal = self.vMax
            print("velocidad final: ", velocidadFinal)
            self.tiempo += 10 + ( distanciaFaltante / velocidadFinal)



    

    