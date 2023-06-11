from datetime import datetime
import pandas as pd
import funcionescsv as funcsv
class Vehiculos():
    diccionario=dict()
    cantVehiculos = 0
    setVehiculos=set()
    def __init__(self, patente, modelo, marca, anio,tipo,gama,precioxdia=None,disponible=True):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.tipo = tipo
        self.gama = gama
        self.precioxdia = self.asignarPrecio()
        self.disponible = True   
        Vehiculos.cantVehiculos+=1
        Vehiculos.setVehiculos.add(self.patente)
    
    def devolver(self):
        self.disponible=True
    
    def modificar(self,atributo):
        match atributo:
            case 'patente':
                patentenueva=input('ingrese patente nueva')
                self.patente=patentenueva
                #####Y ASI CON EL RESTO DE ATRIBUTOS #################################  
    def eliminar(self,diccVehi):
        del diccVehi[self.patente]
        
    def asignarPrecio(self):
        df = pd.read_csv('PreciosVehiculos.csv', index_col=0)
        if self.tipo in df.columns and self.gama in df.index:
            precio = df.loc[self.gama, self.tipo]
        return precio
    
    def objeto_a_lista(self):
        obj_list = []
        for attr, value in self.__dict__.items():
            obj_list.append(value)
        return obj_list
        
         

    def __str__(self):     #Sería como una consulta general sobre el estado de un vehículo
        return(f"""El vehículo {self.marca} {self.modelo} de patente {self.patente}, año {self.anio}, tiene un precio de alquiler por día de {self.precio}, ...""") 
    
# Pruebas de Funcionamiento
if __name__ == "__main__":
   print(Vehiculos.asignar_precio('deportivo','alta'))
    

