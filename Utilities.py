import csv

def escribirCsv(archivo, dicc):                    #Escribo un archivo csv para almacenar la información en el tiempo
    with open(archivo, "w", newline="",encoding='utf-8') as fileEscAlq:  
        escritor = csv.writer(fileEscAlq)

        for clave_de_clase in dicc.keys():
            escritor.writerow(objeto_a_lista(dicc[clave_de_clase]))


def leerCsv(archivo, clase):                        #Leo el archivo csv e instancio su contenido en un diccionario para facilitar el manejo de la información
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

    