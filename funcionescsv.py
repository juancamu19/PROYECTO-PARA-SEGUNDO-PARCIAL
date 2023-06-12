import csv

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

# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass

    