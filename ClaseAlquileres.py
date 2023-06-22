from datetime import datetime
from ClaseVehiculos import Vehiculos
import Utilities as util
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos

'''Se crea la clase Alquiler'''
class Alquiler():
    cantAlquileres = 0 
    diccAlquileres=dict() 
    setAlquileres = set() 
    
    '''Iniciador de la clase Alquiler'''
    def __init__(self, id = None, idReserva = None, dni = None, patente_auto = None, fechaInicioAlq = None, fechaExpiracionAlq = None, fechadev = None, monto = None):
        self.id = id 
        self.idReserva = idReserva  
        self.dni = dni         
        self.patente_auto = patente_auto 
        self.fechaInicioAlq = fechaInicioAlq 
        self.fechaExpiracionAlq = fechaExpiracionAlq 
        self.fechadev = fechadev  
        self.monto = monto     
        Alquiler.cantAlquileres += 1
        Alquiler.setAlquileres.add(self.id)
        Alquiler.diccAlquileres[self.id]=self
    

    '''Funcion para establecer fecha de devolucion'''
    def finalizar(self):
        self.fechadev = datetime.now()
    
    
    '''Método str para la clase'''
    def __str__(self):
        return ('{}-{}-{}-{}-{}'.format(self.id, self.fecha, self.dni, self.auto))
   

'''Diccionario que contiene los registros del archivo csv de alquiler'''
util.leerCsv('Alquileres.csv', Alquiler)


'''Actualización de diccionarios al iniciar un alquiler'''
for k in Reserva.diccReservas.keys():
    if datetime.strptime(Reserva.diccReservas[k].fechaInicio,"%d-%m-%Y").date()==datetime.now().date():
        fechafin=datetime.strptime(Reserva.diccReservas[k].fechaFin,"%d-%m-%Y").date()
        fechaactual=datetime.now()
        cantdias=(fechafin-fechaactual.date()).days
        for clave,v in Alquiler.diccAlquileres.items():
            if k!=v.idReserva:
                Alquiler(Alquiler.cantAlquileres+1,k,Reserva.diccReservas[k].dni,Reserva.diccReservas[k].patente_auto,Reserva.diccReservas[k].fechaInicio,Reserva.diccReservas[k].fechaFin,None,cantdias*(Vehiculos.diccVehiculos[Reserva.diccReservas[k].patente_auto].precioxdia))
                Vehiculos.diccVehiculos[Alquiler.diccAlquileres[Alquiler.cantAlquileres].patente_auto].disponible=False
        



# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass