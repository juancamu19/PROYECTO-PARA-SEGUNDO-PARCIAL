import csv
from ClaseAlquileres import Alquiler
from ClaseVehiculos import Vehiculos
from ClaseReservas import Reserva
from ClasePersonas import Personas

###


# def list_to_str(lista):
#     return [str(elem) if elem is not None else "" for elem in lista]


def escribirCsv(archivo, dicc):
    with open(archivo, "w", newline="") as fileEscAlq:  ##escribo sobre el archivo csv el nuevo registro de alquiler
        escritorAlquiler = csv.writer(fileEscAlq)

        for idPersona in dicc.keys():
            vars(dicc[idPersona])
            escritorAlquiler.writerow(list(vars(dicc[idPersona])))


def leerCsv(archivo, clase):
    dic1 = dict()
    with open(archivo) as file:
        lector = csv.reader(file)
        for row in lector:
            clave = row[0]
            dic1[clave] = clase(*row[1:])
    return dic1



def validarexistenciaPersona(dni, contraseña):
    lista = []
    BajarPersonas(lista)

    for elem in lista:
        if elem[0] == dni:  ##busco la persona
            if elem[5] == contraseña:  ##veo que la contraseña es la correcta
                return True
    else:
        return False


def validarexistenciaDNI(dni):
    lista = []
    BajarPersonas(lista)

    for elem in lista:
        if elem[0] == dni:  ##busco si ya existe la persona
            return False  ##ya existe
    else:
        return True


def validarReserva(id):
    lista = []
    BajarReserva(lista)

    for elem in lista:
        if elem[0] == id:
            return True
    else:
        return False


##FORMA VIEJA DE ASIGNAR UN AUTO
# def asignarauto():
#      lista = []
#      BajarVehiculos(lista)

#      for elem in lista:
#           if elem[5]=='True':
#                return elem[0]


def asignarauto(fecinicio, fecfin):
    listaRes = []
    listaAut = []
    AutosOcupados = []
    BajarVehiculos(listaAut)
    BajarReserva(listaRes)
    for elem in listaRes:
        if (fecinicio <= elem[3] and fecfin >= elem[4]) or (
            fecinicio >= elem[3] and fecfin < elem[4]
        ):  ##veo que no se superpongan las fechas
            AutosOcupados.append(elem[2])
    for elem in listaAut:
        if elem[0] not in AutosOcupados:
            return elem[0]
