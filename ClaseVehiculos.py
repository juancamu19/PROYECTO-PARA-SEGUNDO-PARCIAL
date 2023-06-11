from datetime import datetime
#import pandas as pd
class Vehiculos():
    cantVehiculos = 0
    setVehiculos=set()
    def __init__(self, patente, modelo, marca, anio,tipo,gama,precioxdia,disponible=True):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.tipo = tipo
        self.gama = gama
        self.precioxdia = precioxdia
        self.disponible = True   
        Vehiculos.cantVehiculos+=1
        Vehiculos.setVehiculos.add(self.patente)
    
    def aggVehiculo(patente, modelo, marca, anio,tipo,gama,dicc):  
        precioxdia=Vehiculos.asignar_precio(tipo,gama)

        
        dicc[patente]= Vehiculos(patente, modelo, marca, anio, tipo,gama,precioxdia) #precioxdia debe ir automatico

    def asignar_precio(tipo,gama):
        df = pd.read_csv('PreciosVehiculos.csv', index_col=0)
        if tipo in df.columns and gama in df.index:
            precio = df.loc[gama, tipo]
        return precio
    def objeto_a_lista(self):
        obj_list = []
        for attr, value in self.__dict__.items():
            obj_list.append(value)
        return obj_list
        
    def devolverVehiculo(idalquiler,diccalq,diccVehi):
        diccalq[idalquiler].fechadev=datetime.now()
        diccVehi[diccalq[idalquiler].patente_auto].disponible=True
        
         

    def __str__(self):     #Sería como una consulta general sobre el estado de un vehículo
        return(f"""El vehículo {self.marca} {self.modelo} de patente {self.patente}, año {self.anio}, tiene un precio de alquiler por día de {self.precio}, ...""") 
    
# Pruebas de Funcionamiento
if __name__ == "__main__":
   print(Vehiculos.asignar_precio('deportivo','alta'))
    

