from datetime import datetime
from ClaseVehiculos import Vehiculos
import Utilities as util
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos
#se crea la clase alquiler
class Alquiler():
    cantAlquileres = 0 
    diccAlquileres=dict() 
    setAlquileres = set() 
    def __init__(self, id = cantAlquileres+1, idReserva = None, dni = None, patente_auto = None, fechaInicioAlq = None, fechaExpiracionAlq = None, fechadev = None, monto = None):
        self.id = id 
        self.idReserva = idReserva  
        self.dni = dni         
        self.patente_auto = patente_auto 
        self.fechaInicioAlq = fechaInicioAlq 
        self.fechaExpiracionAlq = fechaExpiracionAlq 
        self.fechadev = fechadev  
        self.monto=monto     
        Alquiler.cantAlquileres += 1
        Alquiler.setAlquileres.add(self.id)
        Alquiler.diccAlquileres[self.id]=self



    # def objeto_a_lista(self):
    #     obj_list = []
    #     for attr, value in self.__dict__.items():
    #         obj_list.append(value)
    #     return obj_list
    
#funcion para establecer fecha de devolucion
    def finalizar(self):
        self.fechadev=datetime.now()
    
#método str para la clase
    def __str__(self):
        return ('{}-{}-{}-{}-{}'.format(self.id, self.fecha, self.dni, self.auto))
   
#diccionario que contiene los registros del archivo csv de alquiler
util.leerCsv('Alquileres.csv', Alquiler)

#actualización de diccionarios al iniciar un alquiler
for k in Reserva.diccReservas.keys():
    if datetime.strptime(Reserva.diccReservas[k].fechaInicio,"%d-%m-%Y").date()==datetime.now():
        fechafin=datetime.strptime(Reserva.diccReservas[k].fechaFin)
        cantdias=(fechafin-datetime.now().date()).days          
        Alquiler.diccAlquileres[Alquiler.cantAlquileres+1]=Alquiler(k,Reserva.diccReservas[k].dni,Reserva.diccReservas[k].patente_auto,Reserva.diccReservas[k].fechaInicio,Reserva.diccReservas[k].fechaFin,None,cantdias*(Reserva.diccReservas[k].patente_auto.precioxdia))
        Vehiculos.diccVehiculos[Alquiler.diccAlquileres[Alquiler.cantAlquileres].patente_auto].disponible=False



# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass