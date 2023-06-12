from datetime import datetime
import pandas as pd
import random
# import funcionescsv as funcsv
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
            case 'modelo' :
                modelonuevo=input('ingrese modelo nuevo')
                self.modelo=modelonuevo 
            case 'marca' :
                marcanueva=input('ingrese marca nueva')
                self.marca=marcanueva
            case 'anio':
                anionuevo=input('ingrese año nuevo')
                self.anio=anionuevo
                #validamos que el año sea menor que el año actual? 
            case 'tipo' :
                tiponuevo=input ('ingrese nuevo tipo')
                self.tipo=tiponuevo
            case 'gama':
                gamanueva=input('ingrese nueva gama')
                self.gama=gamanueva
            ##No se como se haria esto con el tema del precio xq esta el asignar precio, faltaria eso 
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
        
    def asignarauto(fecinicio, fecfin, tipo, gama, diccreservas, diccVehiculos):
    
        setvehiculosdisponibles=Vehiculos.setVehiculos
        for k in diccreservas.keys():
            if diccVehiculos[diccreservas[k].patente_auto].tipo==tipo and diccVehiculos[diccreservas[k].patente_auto].gama==gama:
                if (fecinicio >= diccreservas[k].fechaInicio and fecinicio <= diccreservas[k].fechaFin) or ( fecfin <= diccreservas[k].fechaFin and fecfin >= diccreservas[k].fechaIncio) or (fecinicio<=diccreservas[k].fechaInicio and fecfin >= diccreservas[k].fechaFin):
                
                    setvehiculosdisponibles.remove(diccreservas[k].patente_auto)  

        if len(setvehiculosdisponibles)==0:
            return None
        else:
            return random.choice(list(setvehiculosdisponibles))



    def __str__(self):     #Sería como una consulta general sobre el estado de un vehículo
        return(f"""El vehículo {self.marca} {self.modelo} de patente {self.patente}, año {self.anio}, tiene un precio de alquiler por día de {self.precio}, ...""") 
    

# diccVehiculos = funcsv.leerCsv('Vehiculos.csv', Vehiculos)

# Pruebas de Funcionamiento
#creo un falcon de pruebas
TESTER=Vehiculos('abc500','Falcon','Ford',2023,'deportivo','alta')

if __name__ == "__main__":
   print(Vehiculos.asignarPrecio(TESTER))
   print(Vehiculos.objeto_a_lista(TESTER))
   print(Vehiculos.modificar(TESTER,'patente'))

