import csv

'''Escribo un archivo csv con los elementos del diccionario indicado para almacenar la información en el tiempo'''
def escribirCsv(archivo, dicc):
    try:                    
        with open(archivo, "w", newline="",encoding='utf-8') as fileEscAlq:  
            escritor = csv.writer(fileEscAlq)

            for clave_de_clase in dicc.keys():
                escritor.writerow(objeto_a_lista(dicc[clave_de_clase]))
    
    except FileNotFoundError:
        print('Archivo no encontrado')
        return False


'''Leo el archivo csv, e instancio los objetos de la clase indicada por parametro, donde los valores para los
atributos de cada objeto se obtienen del csv. La creacion de cada objeto basta para que el mismo se cargue
al diccionario de su clase '''
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


'''Almaceno en una lista la información un objeto. Esta funcion se utiliza en escribircsv. La finalidad es que con
un objeto pasado por parametro, se almacene su informacion en una lista, y esa lista sea escrita en cada linea del csv.'''
def objeto_a_lista(objeto):
        obj_list = []
        for attr, value in objeto.__dict__.items():
            obj_list.append(value)
        return obj_list



if __name__=='__main__':
    pass

    