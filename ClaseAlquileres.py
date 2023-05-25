from datetime import datetime
from ClaseVehiculos import Vehiculos

class Alquiler():
    cantAlquileres = 0
    registroAlquileres = {} 
    
    def __init__(self, idReserva,dni,patente_auto,fechaInicioAlq,fechaExpiracionAlq):
        self.id = self.cantAlquileres+1  #agrego el 1 porque cuando cree, a cant le sumo 1 una vez creado el objeto
        self.idReserva = idReserva 
        #antes de asignar un auto debo hacer la verificacion de si esta disponible, pero antes de eso debo preguntar que tipo de auto quiere
        self.patente_auto = patente_auto 
        self.fechaInicioAlq = fechaInicioAlq 
        self.fechaExpiracionAlq = fechaExpiracionAlq 
        self.fechadev = None ##pongo None porque este campo se completa automaticamente una vez devuelto el auto
        # self.penali=None ##acá se puede poner si averio el auto o si lo entrego tarde etc
        self.dni = dni 
        # self.monto = monto podria verse de autocompletar este dato con la cant de dias y auto que saques

        Alquiler.cantAlquileres += 1

    def aggAlquiler(idReserva,diccres,diccalq,diccVehi):
          ##aca cuando instancio el objeto estoy suponiendo que todos los alquileres tienen reserva, se podría cambiar
          diccalq[Alquiler.cantAlquileres+1]=Alquiler(idReserva,diccres[idReserva].dni,diccres[idReserva].patente_auto,diccres[idReserva].fechaInicio,diccres[idReserva].fechaFin)
                    
          for k in diccVehi.keys():
              diccVehi[diccalq[Alquiler.cantAlquileres].patente_auto].disponible=False
    

    def __str__(self):
        return ('{}-{}-{}-{}-{}'.format(self.id, self.fecha, self.dni, self.auto))
   
# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass