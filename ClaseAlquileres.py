from datetime import datetime
from ClaseVehiculos import Vehiculos

class Alquiler():
    cantAlquileres = 0
    registroAlquileres = {} 
    
    def __init__(self, idReserva,dni,patente_auto,fechaInicioAlq,fechaExpiracionAlq):
        self.id = self.cantAlquileres+1  
        self.idReserva = idReserva 
        
        self.patente_auto = patente_auto 
        self.fechaInicioAlq = fechaInicioAlq 
        self.fechaExpiracionAlq = fechaExpiracionAlq 
        self.fechadev = None 
       
        self.dni = dni 
        

        Alquiler.cantAlquileres += 1

    def aggAlquiler(idReserva,diccres,diccalq,diccVehi):
          
          diccalq[Alquiler.cantAlquileres+1]=Alquiler(idReserva,diccres[idReserva].dni,diccres[idReserva].patente_auto,diccres[idReserva].fechaInicio,diccres[idReserva].fechaFin)
                    
          for k in diccVehi.keys():
              diccVehi[diccalq[Alquiler.cantAlquileres].patente_auto].disponible=False
    

    def __str__(self):
        return ('{}-{}-{}-{}-{}'.format(self.id, self.fecha, self.dni, self.auto))
   
# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass