from datetime import datetime
from ClaseVehiculos import Vehiculos

class Alquiler():
    cantAlquileres = 0
    registroAlquileres = {} 
    
    def __init__(self, idReserva):
        self.id = self.cantAlquileres+1  #agrego el 1 porque cuando cree, a cant le sumo 1 una vez creado el objeto
        self.idReserva = idReserva #numero de reserva
        #antes de asignar un auto debo hacer la verificacion de si esta disponible, pero antes de eso debo preguntar que tipo de auto quiere
        self.auto = None #pongo none ya que se completa automaticamente de reserva, estamos suponiendo que todos los alquileres tiene reserva, si no suponemos eso, esto se cambia
        self.fechainicioalquiler = None ##pongo None porque este campo se completa automaticamente a partir del numero de reserva
        self.fechaExpiracionAlquiler = None ##pongo None porque este campo se completa automaticamente a partir del numero de reserva
        self.fechadev = None ##pongo None porque este campo se completa automaticamente una vez devuelto el auto
        # self.penali=None ##acá se puede poner si averio el auto o si lo entrego tarde etc
        self.dni = None ##obtengo de reserva
        # self.monto = monto ## podria verse de autocompletar este dato con la cant de dias y auto que saques

        Alquiler.cantAlquileres += 1

    def __str__(self):
        return ('{}-{}-{}-{}-{}'.format(self.id, self.fecha, self.dni, self.auto))
   
