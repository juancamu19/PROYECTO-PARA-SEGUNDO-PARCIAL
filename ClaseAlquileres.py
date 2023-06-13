from datetime import datetime
from ClaseVehiculos import Vehiculos
import funcionescsv as funcsv
from ClaseReservas import diccReservas
from ClaseVehiculos import diccVehiculos

class Alquiler():
    cantAlquileres = 0
    # diccionario=dict()
    ################################################################obs: en todas las clases estoy poniendo valores por default en el consructor asi cuando leo el csv me pasa todos los parametros, si no va a haber paraetros de mas o de menos. EN ESTE CLASE EN PARTICULAR, EL ID LO TENGO QUE PASAR POR DEFAULT
    def __init__(self,id=cantAlquileres+1,idReserva=None,dni=None,patente_auto=None,fechaInicioAlq=None,fechaExpiracionAlq=None,fechadev=None,monto=None):
        self.id = id 
        self.idReserva = idReserva  
        self.dni = dni         
        self.patente_auto = patente_auto 
        self.fechaInicioAlq = fechaInicioAlq 
        self.fechaExpiracionAlq = fechaExpiracionAlq 
        self.fechadev = fechadev  
        self.monto=monto     

        Alquiler.cantAlquileres += 1

    def objeto_a_lista(self):
        obj_list = []
        for attr, value in self.__dict__.items():
            obj_list.append(value)
        return obj_list
    
    def finalizar(self):
        self.fechadev=datetime.now()
    

    def __str__(self):
        return ('{}-{}-{}-{}-{}'.format(self.id, self.fecha, self.dni, self.auto))
   
diccAlquileres = funcsv.leerCsv('Alquileres.csv', Alquiler)

for k in diccReservas.keys():
    if datetime.strptime(diccReservas[k].fechaInicio,"%d-%m-%Y").date()==datetime.now():
        fechafin=datetime.strptime(diccReservas[k].fechaFin)
        cantdias=(fechafin-datetime.now().date()).days          
        diccAlquileres[Alquiler.cantAlquileres+1]=Alquiler(k,diccReservas[k].dni,diccReservas[k].patente_auto,diccReservas[k].fechaInicio,diccReservas[k].fechaFin,None,cantdias*diccReservas[k].patente_auto.precioxdia)
        diccVehiculos[diccAlquileres[Alquiler.cantAlquileres].patente_auto].disponible=False
# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass