import csv
import random
from ClaseAlquileres import Alquiler
from ClaseVehiculos import Vehiculos
from ClaseReservas import Reserva
from ClasePersonas import Personas
from datetime import datetime

def escribirCsv(archivo, dicc):
    with open(archivo, "w", newline="") as fileEscAlq:  
        escritorAlquiler = csv.writer(fileEscAlq)

        for idPersona in dicc.keys():
            escritorAlquiler.writerow(dicc[idPersona].objeto_a_lista())

def leerCsv(archivo, clase):
    dic1 = dict()
    with open(archivo) as file:
        lector = csv.reader(file)
        for row in lector:
            clave = row[0]
            dic1[clave] = clase(*row[:])
    return dic1
   

def asignarauto(fecinicio, fecfin, tipo, gama, diccreservas, diccVehiculos):
    
    setvehiculosdisponibles=Vehiculos.setVehiculos
    for k in diccreservas.keys():
        if diccVehiculos[diccreservas[k].patente_auto].tipo==tipo and diccVehiculos[diccreservas[k].patente_auto].gama==gama:
            if (fecinicio >= diccreservas[k].fechaInicio and fecinicio <= diccreservas[k].fechaFin) or ( fecfin <= diccreservas[k].fechaFin and fecfin >= diccreservas[k].fechaIncio) or (fecinicio<=diccreservas[k].fechaInicio and fecfin >= diccreservas[k].fechaFin):
                
                setvehiculosdisponibles.remove(diccreservas[k].patente_auto)  ##NO ME UPDATEA EL SET

    if len(setvehiculosdisponibles)==0:
        return None
    else:
        return random.choice(list(setvehiculosdisponibles))


# Pruebas de Funcionamiento
if __name__ == "__main__":
    diccr=leerCsv('Reservas.csv',Reserva)
    diccv=leerCsv('Vehiculos.csv',Vehiculos)
    for key in diccr.keys():
        diccr[key].fechaInicio = datetime.strptime(diccr[key].fechaInicio,"%d-%m-%Y").date()
        diccr[key].fechaFin = datetime.strptime(diccr[key].fechaFin,"%d-%m-%Y").date()
    fecinicio=datetime.strptime('10-7-2023',"%d-%m-%Y").date()
    fecfin=fecfin=datetime.strptime('25-7-2023',"%d-%m-%Y").date()
    auto=asignarauto(fecinicio,fecfin,'urbano','baja',diccr,diccv)
    print(auto)
    # Reserva.cambiarfechaInicioAlquiler('2',diccr)
    # escribirCsv('Reservas.csv',diccr)

    