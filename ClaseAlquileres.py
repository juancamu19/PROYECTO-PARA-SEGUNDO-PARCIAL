from datetime import datetime
from ClaseVehiculos import Vehiculos

# import funcionescsv as funcsv

class Alquiler():
    cantAlquileres = 0
    diccionario=dict()
    ################################################################obs: en todas las clases estoy poniendo valores por default en el consructor asi cuando leo el csv me pasa todos los parametros, si no va a haber paraetros de mas o de menos. EN ESTE CLASE EN PARTICULAR, EL ID LO TENGO QUE PASAR POR DEFAULT
    def __init__(self,id=cantAlquileres+1,idReserva=None,dni=None,patente_auto=None,fechaInicioAlq=None,fechaExpiracionAlq=None,fechadev=None):
        self.id = id 
        self.idReserva = idReserva  
        self.dni = dni         
        self.patente_auto = patente_auto 
        self.fechaInicioAlq = fechaInicioAlq 
        self.fechaExpiracionAlq = fechaExpiracionAlq 
        self.fechadev = fechadev       

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
   
# diccAlquileres = funcsv.leerCsv('Alquileres.csv', Alquiler)
# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass