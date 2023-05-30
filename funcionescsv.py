import csv
import random
from ClaseAlquileres import Alquiler
from ClaseVehiculos import Vehiculos
from ClaseReservas import Reserva
from ClasePersonas import Personas


### FUNCION PARA ESRIBIR SOBRE LOS CSV ###
def escribirCsv(archivo, dicc):
    with open(archivo, "w", newline="") as fileEscAlq:  ##escribo sobre el archivo csv el nuevo registro de alquiler
        escritorAlquiler = csv.writer(fileEscAlq)

        for idPersona in dicc.keys():
            vars(dicc[idPersona])
            escritorAlquiler.writerow(list(vars(dicc[idPersona])))

### FUNCION PARA LEER CSV ###
def leerCsv(archivo, clase):
    dic1 = dict()
    with open(archivo) as file:
        lector = csv.reader(file)
        for row in lector:
            clave = row[0]
            dic1[clave] = clase(*row[1:])
    return dic1


### FUNCION PARA VALIDAR CONTRASEÑA ###

def validarexistenciaPersona(dni, contraseñaing,dicc):
    for k in dicc.keys():
        if k == dni:  ##busco la persona
            if dicc[k].contraseña == contraseñaing:  ##veo que la contraseña es la correcta
                return True
    else:
        return False

### FUNCION PARA VER SI LA PERSONA  YA ESTA REGISTRADA ###

def validarexistenciaDNI(dni):

    if dni in Personas.setdnis:  ##busco si ya existe la persona
        return True          ##ya existe
    else:
        return False

### VERIFICO QUE EL CODIGO DE RESERVA EXISTE ###

def validarReserva(id):
    if id in Reserva.setReservas:  ##busco si ya existe la persona
        return True          ##ya existe
    else:
        return False
   

### FUNCION PARA ASIGNAR UN AUTO AUTOMÁTICAMENTE ###

def asignarauto(fecinicio, fecfin,diccreservas):
    ### OBS: aca se pasa como parametro los diccionarios sobre los cuales se va a buscar, los mismos son "rellenado" al inicializar el programa"
    ### Asumo que la compañia tiene al menos un auto
    ### METODOLOGIA DE BUSQUEDA: tomo aquellas reservas con las cuales se le superponen las fechas, y le asigno el primer auto que encuentre que no este ocupado por las mismas. Si no se superpone fechas con ninguna reserva, se le asigna el primer auto que encuentre.  
    setvehiculosdisponibles=Vehiculos.setVehiculos
    for k in diccreservas.keys():
        if (fecinicio >= diccreservas[k].fechaInicio and fecinicio <= diccreservas[k].fechaFin) or ( fecfin <= diccreservas[k].fechaFin and fecfin >= diccreservas[k].fechaIncio) or (fecinicio<=diccreservas[k].fechaInicio and fecfin >= diccreservas[k].fechaFin):  ##selecciono aquellas reservas donde se superpongan las fechas
            
            setvehiculosdisponibles.difference_update(diccreservas[k].patente)  ## voy actualizando el set de vehiculos disponibles con aquellos que no estan dentro de estas fechas
            if len(setvehiculosdisponibles)==0:
                return None
            else:
                return random.choice(list(setvehiculosdisponibles))
        else: 
            
            return random.choice(list(Vehiculos.setVehiculos)) ##no hay ninguna reserva que superponga su fecha con la del cliente, entonces se toma al azar cualquier auto

# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass