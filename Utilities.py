import csv

def escribirCsv(archivo, dicc):
    with open(archivo, "w", newline="",encoding='utf-8') as fileEscAlq:  
        escritorAlquiler = csv.writer(fileEscAlq)

        for idPersona in dicc.keys():
            escritorAlquiler.writerow(objeto_a_lista(dicc[idPersona]))

def leerCsv(archivo, clase):
    dic1 = dict()
    with open(archivo) as file:
        lector = csv.reader(file)
        for row in lector:
            if archivo=='Empleados.csv':
                clave = row[6]
                dic1[clave] = clase(*row[:])
            else:
                clave = row[0]
                dic1[clave] = clase(*row[:])
    return dic1
def objeto_a_lista(objeto):
        obj_list = []
        for attr, value in objeto.__dict__.items():
            obj_list.append(value)
        return obj_list

    