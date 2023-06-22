from datetime import datetime
import pandas as pd
import random
import Utilities as util
from ClaseReservas import Reserva


'''Se crea la clase Vehiculos'''
class Vehiculos():
    diccVehiculos=dict()
    cantVehiculos = 0
    setVehiculos=set()
    
    '''Iniciador de la clase Vehículos'''
    def __init__(self, patente, modelo, marca, anio, tipo, gama, precioxdia = None ,disponible = True):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.tipo = tipo
        self.gama = gama
        self.disponible = True
        self.precioxdia = self.asignarPrecio()
        Vehiculos.cantVehiculos+=1
        Vehiculos.setVehiculos.add(self.patente)
        Vehiculos.diccVehiculos[self.patente]=self
    
    
    '''Funcion para cambiar estado de dispponibilidad de auto al devolverlo'''
    def devolver(self):
        self.disponible = True
    

    '''Funcion para modificar un atributo de un auto'''
    def modificar(self, atributo, valor_nuevo):
        match atributo:
            
            case 'patente':
                self.patente = valor_nuevo 
            
            case 'modelo' :
                self.modelo = valor_nuevo 
            
            case 'marca' :
                self.marca = valor_nuevo
            
            case 'año':
                self.anio = valor_nuevo
            
            case 'tipo' :
                self.tipo = valor_nuevo
            
            case 'gama':
                self.gama = valor_nuevo 


    '''Funcion para asignar el precio estipulado en el archivo PreciosVehiculos a un nuevo vehiculo'''    
    def asignarPrecio(self):
        df = pd.read_csv('PreciosVehiculos.csv', index_col=0)
        if self.tipo in df.columns and self.gama in df.index:
            precio = df.loc[self.gama, self.tipo]
        return precio


    '''Funcion para designar el auto elegido por el usuario al realizar una reserva'''
    def asignarauto(fecinicio, fecfin, tipo_elegido, gama_elegida):
        fecinicio = datetime.strptime(fecinicio,"%d-%m-%Y").date()
        fecfin = datetime.strptime(fecfin,"%d-%m-%Y").date()
        setvehiculosdisponibles=set()
        for k,v in Vehiculos.diccVehiculos.items():
            if v.tipo == tipo and v.gama==gama:
                setvehiculosdisponibles.add(k)        
        
        for k in Reserva.diccReservas.keys():
            fechaInicioReservak = datetime.strptime(Reserva.diccReservas[k].fechaInicio,"%d-%m-%Y").date()
            fechaFinReservak = datetime.strptime(Reserva.diccReservas[k].fechaFin,"%d-%m-%Y").date()
            if Vehiculos.diccVehiculos[Reserva.diccReservas[k].patente_auto].tipo == tipo_elegido and Vehiculos.diccVehiculos[Reserva.diccReservas[k].patente_auto].gama == gama_elegida:
                if ((fecinicio >= fechaInicioReservak and fecinicio <= fechaFinReservak) or ( fecfin <= fechaFinReservak and fecfin >= fechaInicioReservak) or (fecinicio<=fechaInicioReservak and fecfin >= fechaFinReservak)) and (Reserva.diccReservas[k].fechaCancel in ['',None]):
                
                    setvehiculosdisponibles.remove(Reserva.diccReservas[k].patente_auto)  

        if len(setvehiculosdisponibles) == 0:
            return None
        else:
            return random.choice(list(setvehiculosdisponibles))
    

    '''Función para eliminar un vehículo'''
    def eliminar(self):
        for elem in Vehiculos.setVehiculos:
            if elem==self.patente:
                Vehiculos.setVehiculos.discard(elem)
        del(Vehiculos.diccVehiculos[self.patente])


    '''Método str para clase vehiculos'''
    def __str__(self):    
        return(f"El vehículo {self.marca} {self.modelo} de patente {self.patente}, año {self.anio}, tiene un precio de alquiler por día de {self.precioxdia}, es de tipo {self.tipo} y gama {self.gama}")
    

'''Diccionario que contiene los registros de vehículos'''
util.leerCsv('Vehiculos.csv', Vehiculos)



if __name__ == "__main__":
   pass

