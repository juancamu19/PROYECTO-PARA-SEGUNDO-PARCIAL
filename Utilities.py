import csv
def escribirCsv(archivo, dicc):
    try:                    #Escribo un archivo csv para almacenar la información en el tiempo
        with open(archivo, "w", newline="",encoding='utf-8') as fileEscAlq:  
            escritor = csv.writer(fileEscAlq)

            for clave_de_clase in dicc.keys():
                escritor.writerow(objeto_a_lista(dicc[clave_de_clase]))
    except FileNotFoundError:
        print('Archivo no encontrado')
        return False


# def leerCsv(archivo, clase):                        #Leo el archivo csv e instancio su contenido en un diccionario para facilitar el manejo de la información
#     dic1 = dict()
#     try:
#         with open(archivo) as file:
#             lector = csv.reader(file)
#             for row in lector:
#                 if archivo=='Empleados.csv':
#                     if len(row)<6:
#                         pass
#                     else:
#                         clave = row[6]
#                         dic1[clave] = clase(*row[:])
#                 else:
#                     if len(row)==0:
#                         pass
#                     else:
#                         clave = row[0]
#                         dic1[clave] = clase(*row[:])
#         return dic1
#     except FileNotFoundError:
#         print('Archivo no encontrado')
#         return False

def leerCsv(archivo, clase):                        
    try:
        with open(archivo) as file:
            lector = csv.reader(file)
            for row in lector:
                    if len(row)!=0:
                        clase(*row[:])
                    else:
                        pass
    except FileNotFoundError:
        print('Archivo no encontrado')
        return False

def objeto_a_lista(objeto):
        obj_list = []
        for attr, value in objeto.__dict__.items():
            obj_list.append(value)
        return obj_list

if __name__=='__main__':
    pass

    