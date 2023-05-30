import csv
import random
from ClaseAlquileres import Alquiler
from ClaseVehiculos import Vehiculos
from ClaseReservas import Reserva
from ClasePersonas import Personas

def escribirCsv(archivo, dicc):
    with open(archivo, "w", newline="") as fileEscAlq:  
        escritorAlquiler = csv.writer(fileEscAlq)

        for idPersona in dicc.keys():
            escritorAlquiler.writerow(list(vars(dicc[idPersona])))

def leerCsv(archivo, clase):
    dic1 = dict()
    with open(archivo) as file:
        lector = csv.reader(file)
        for row in lector:
            clave = row[0]
            dic1[clave] = clase(*row[1:])
    return dic1
   

def asignarauto(fecinicio, fecfin,tipo,gama,diccreservas,diccVehiculos):
    
    setvehiculosdisponibles=Vehiculos.setVehiculos
    for k in diccreservas.keys():
        if diccVehiculos[diccreservas[k].patente_auto].tipo==tipo and diccVehiculos[diccreservas[k].patente_auto].gama==gama:
            if (fecinicio >= diccreservas[k].fechaInicio and fecinicio <= diccreservas[k].fechaFin) or ( fecfin <= diccreservas[k].fechaFin and fecfin >= diccreservas[k].fechaIncio) or (fecinicio<=diccreservas[k].fechaInicio and fecfin >= diccreservas[k].fechaFin):
            
                setvehiculosdisponibles.difference_update(diccreservas[k].patente_auto)  
                if len(setvehiculosdisponibles)==0:
                    return None
                else:
                    return random.choice(list(setvehiculosdisponibles))
            else: 
            
                return random.choice(list(Vehiculos.setVehiculos)) 


# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass