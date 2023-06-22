from datetime import datetime
import pandas as pd
import random
import Utilities as util
from ClaseReservas import Reserva


#se crea la clase vehiculos
class Vehiculos():
    diccVehiculos=dict()
    cantVehiculos = 0
    setVehiculos=set()
    
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
    
    
    #funcion para cambiar estado de dispponibilidad de auto al devolverlo
    def devolver(self):
        self.disponible = True
    

    #funcion para modificar un atributo de un auto
    def modificar(self, atributo, valor):
        match atributo:
            
            case 'patente':
                self.patente = valor 
            
            case 'modelo' :
                self.modelo = valor 
            
            case 'marca' :
                self.marca = valor
            
            case 'año':
                self.anio = valor
            
            case 'tipo' :
                self.tipo = valor
            
            case 'gama':
                self.gama = valor 


    #funcion para asignar el precio estipulado en csv a un nuevo vehiculo    
    def asignarPrecio(self):
        df = pd.read_csv('PreciosVehiculos.csv', index_col=0)
        if self.tipo in df.columns and self.gama in df.index:
            precio = df.loc[self.gama, self.tipo]
        return precio


    #funcion para designar el auto elegido por el usuario al realizar una reserva
    def asignarauto(fecinicio, fecfin, tipo, gama):
        fecinicio = datetime.strptime(fecinicio,"%d-%m-%Y").date()
        fecfin = datetime.strptime(fecfin,"%d-%m-%Y").date()    
        setvehiculosdisponibles=Vehiculos.setVehiculos
        
        for k in Reserva.diccReservas.keys():
            fechaInicioReservak = datetime.strptime(Reserva.diccReservas[k].fechaInicio,"%d-%m-%Y").date()
            fechaFinReservak = datetime.strptime(Reserva.diccReservas[k].fechaFin,"%d-%m-%Y").date()
            if Vehiculos.diccVehiculos[Reserva.diccReservas[k].patente_auto].tipo == tipo and Vehiculos.diccVehiculos[Reserva.diccReservas[k].patente_auto].gama == gama:
                if ((fecinicio >= fechaInicioReservak and fecinicio <= fechaFinReservak) or ( fecfin <= fechaFinReservak and fecfin >= fechaInicioReservak) or (fecinicio<=fechaInicioReservak and fecfin >= fechaFinReservak)) and Reserva.diccReservas[k].fechaCancel==None:
                
                    setvehiculosdisponibles.remove(Reserva.diccReservas[k].patente_auto)  

        if len(setvehiculosdisponibles) == 0:
            return None
        else:
            return random.choice(list(setvehiculosdisponibles))

    #método str para clase vehiculos
    def __str__(self):    
        return(f"El vehículo {self.marca} {self.modelo} de patente {self.patente}, año {self.anio}, tiene un precio de alquiler por día de {self.precioxdia}, es de tipo {self.tipo} y gama {self.gama}")
    
#diccionario que contiene los registros nuevos de vehiculos
util.leerCsv('Vehiculos.csv', Vehiculos)



# Pruebas de Funcionamiento
#creo un falcon de pruebas
# TESTER=Vehiculos('abc500','Falcon','Ford',2023,'deportivo','alta')



# if __name__ == "__main__":
#    print(Vehiculos.asignarPrecio(TESTER))
#    print(Vehiculos.objeto_a_lista(TESTER))
#    print(Vehiculos.modificar(TESTER,'patente'))

