from datetime import datetime
import pandas as pd
import random
import Utilities as util
import validaciones as val
from ClaseReservas import diccReservas


#se crea la clase vehiculos
class Vehiculos():
    # diccionario=dict()
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
    
    #funcion para cambiar estado de dispponibilidad de auto al devolverlo
    def devolver(self):
        self.disponible = True
    
    #funcion para modificar un atributo de un auto
    def modificar(self, atributo, valor):
        match atributo:
            
            case 'patente':
                self.patente = valor 
            
            case 'modelo' :
                modelonuevo = input('Ingrese el modelo nuevo ')
                while validado == False:
                    modelonuevo=input('Ingrese el modelo nuevo ')
                    validado = val.validarmodelo(modelonuevo)
                self.modelo = modelonuevo 
            
            case 'marca' :
                marcanueva = input('Ingrese la marca nueva ')
                while validado == False:
                    marcanueva = input('Ingrese la marca nueva ')
                    validado = val.validarmodelo(marcanueva)
                self.marca = marcanueva
            
            case 'año':
                anionuevo = input('Ingrese el año nuevo ')
                while validado == False:
                    anionuevo=input('Ingrese el año nuevo ')
                    validado = val.validarmodelo(anionuevo)
                self.anio = anionuevo
            
            case 'tipo' :
                tiponuevo = input('Ingrese el nuevo tipo ')
                while validado == False:
                    tiponuevo = input('Ingrese el nuevo tipo ')
                    validado = val.validarmodelo(tiponuevo)
                self.tipo = tiponuevo
            
            case 'gama':
                gamanueva = input('Ingrese la nueva gama ')
                while validado == False:
                    gamanueva=input('Ingrese la nueva gama ')
                    validado = val.validarmodelo(gamanueva)
                self.gama = gamanueva 


    #funcion para asignar el precio estipulado en csv a un nuevo vehiculo    
    def asignarPrecio(self):
        df = pd.read_csv('PreciosVehiculos.csv', index_col=0)
        if self.tipo in df.columns and self.gama in df.index:
            precio = df.loc[self.gama, self.tipo]
        return precio
    
    # def objeto_a_lista(self):
    #     obj_list = []
    #     for attr, value in self.__dict__.items():
    #         obj_list.append(value)
    #     return obj_list
        
    #funcion para designar el auto elegido por el usuario al realizar una reserva
    def asignarauto(fecinicio, fecfin, tipo, gama):
        fecinicio = datetime.strptime(fecinicio,"%d-%m-%Y").date()
        fecfin = datetime.strptime(fecfin,"%d-%m-%Y").date()    
        setvehiculosdisponibles=Vehiculos.setVehiculos
        
        for k in diccReservas.keys():
            fechaInicioReservak = datetime.strptime(diccReservas[k].fechaInicio,"%d-%m-%Y").date()
            fechaFinReservak = datetime.strptime(diccReservas[k].fechaFin,"%d-%m-%Y").date()
            if diccVehiculos[diccReservas[k].patente_auto].tipo==tipo and diccVehiculos[diccReservas[k].patente_auto].gama==gama:
                if ((fecinicio >= fechaInicioReservak and fecinicio <= fechaFinReservak) or ( fecfin <= fechaFinReservak and fecfin >= fechaInicioReservak) or (fecinicio<=fechaInicioReservak and fecfin >= fechaFinReservak)) and diccReservas[k].fechaCancel==None:
                
                    setvehiculosdisponibles.remove(diccReservas[k].patente_auto)  

        if len(setvehiculosdisponibles) == 0:
            return None
        else:
            return random.choice(list(setvehiculosdisponibles))

    #método str para clase vehiculos
    def __str__(self):    
        return(f"El vehículo {self.marca} {self.modelo} de patente {self.patente}, año {self.anio}, tiene un precio de alquiler por día de {self.precioxdia}, es de tipo {self.tipo} y gama {self.gama}")
    
#diccionario que contiene los registros nuevos de vehiculos
diccVehiculos = util.leerCsv('Vehiculos.csv', Vehiculos)

# Pruebas de Funcionamiento
#creo un falcon de pruebas
TESTER=Vehiculos('abc500','Falcon','Ford',2023,'deportivo','alta')

if __name__ == "__main__":
   print(Vehiculos.asignarPrecio(TESTER))
   print(Vehiculos.objeto_a_lista(TESTER))
   print(Vehiculos.modificar(TESTER,'patente'))

