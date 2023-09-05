from models.car import Car
from models.motorcycle import Motorcycle
from models.pista import Pista
from models.carrera import race


if __name__ == '__main__':
    carro1 = Car(400,1255,1050,"Ferrari")
    carro2 = Car(150,800,100,"Twingo")
    moto1 = Motorcycle(130, 44, 26, "duke 200")
    longitud = int(input("Ingrese la longitud de la pista: "))
    pista1 = Pista(longitud)
    carrera = race([],pista1)
    carrera.insertCompetitor(moto1)
    carrera.insertCompetitor(carro1)
    carrera.insertCompetitor(carro2)
    carrera.realizarCarrera()


