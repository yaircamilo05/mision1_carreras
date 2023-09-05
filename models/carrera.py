from .pista import Pista
from .vehicle import Vehicle

class race:
    def __init__(self,competidores,pista):
        self.competidores: list[Vehicle] = competidores
        self.pista: Pista = pista

    def insertCompetitor(self,competidor):
        self.competidores.append(competidor)

    def mostrarPodio(self):
        for i in range(3):
            print("Puesto " + str(i+1) + ": " + self.competidores[i].getTipo() + " " + str( self.competidores[i].getTiempo()))

    def realizarCarrera(self):
        for vehiculo in self.competidores:
            vehiculo.correrCarrera(self.pista.getLongitud())
        self.competidores.sort(key=lambda x: x.tiempo, reverse=False)
        self.mostrarPodio()




        