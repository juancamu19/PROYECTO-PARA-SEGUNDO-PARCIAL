from datetime import datetime
import pandas as pd
import random
import Utilities as util
from ClaseReservas import Reserva


'''Se crea la clase Vehiculos'''
class Vehiculos():
    diccVehiculos=dict()
    cantVehiculos = 0
    setVehiculos=set()
    

    def __init__(self, patente, modelo, marca, anio, tipo, gama, precioxdia = None ,disponible = True):
        """Iniciador de la clase Vehículos. Cada objeto se agrega al diccionario al crearse, con su patente unica como
        identificador. Vale aclarar que la elecion de sets facilita el uso de validaciones para este campo, a pesar
        de no hacer una gran diferncia con respecto a otras estructuras de datos, como si lo hace en usuario, reservas.
        El precioxdia de cada auto se asigna automaticamente a partir de su tipo y gama

        Args:
            patente (str): patente del vehículo
            modelo (str): modelo del vehículo
            marca (str): marca del vehículo
            anio (str): año de fabricación del vehículo
            tipo (str): tipo de vehículo (sedane, suv, ...)
            gama (str): gama del vehículo (alta, media, ...)
            precioxdia (str): costo de alquiler por día. Defaults to None.
            disponible (bool): estado de disponibilidad para ser alquilado. Defaults to True.
        """
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.tipo = tipo
        self.gama = gama
        self.disponible = True
        self.precioxdia = self.asignarPrecio()
        Vehiculos.cantVehiculos+=1
        Vehiculos.setVehiculos.add(self.patente)
        Vehiculos.diccVehiculos[self.patente]=self
    
    
    '''Funcion para cambiar estado de disponibilidad de auto al devolverlo'''
    def devolver(self):
        self.disponible = True
    

    
    def modificar(self, atributo, valor_nuevo):
        """Funcion para modificar un atributo de un auto. Se ingresa por parametro el atributo a cambiar y el
        nuevo valor a darle'''

        Args:
            atributo (str): atributo del objeto a ser modificado
            valor_nuevo (str): atributo nuevo para reemplazar el anterior
        """
        match atributo:
            
            case 'patente':
                self.patente = valor_nuevo 
            
            case 'modelo' :
                self.modelo = valor_nuevo 
            
            case 'marca' :
                self.marca = valor_nuevo
            
            case 'año':
                self.anio = valor_nuevo
            
            case 'tipo' :
                self.tipo = valor_nuevo
            
            case 'gama':
                self.gama = valor_nuevo 


    '''Funcion para asignar el precio estipulado en el archivo PreciosVehiculos a cada vehiculo creado. Se utiliza
    el dataframe de pandas ya que facilita el manejo de tablas con
    doble entrada '''    
    def asignarPrecio(self):
        df = pd.read_csv('PreciosVehiculos.csv', index_col=0)
        if self.tipo in df.columns and self.gama in df.index:
            precio = df.loc[self.gama, self.tipo]
        return precio



    def asignarauto(fecinicio, fecfin, tipo_elegido, gama_elegida):
        """Funcion para designar el auto elegido por el usuario al realizar una reserva. Este auto es elegido 
        aleatoriamente, siempre y cuando sea del tipo y gama pedido, y este disponible para esa fecha segun
        las reservas existentes

        Args:
            fecinicio (datetime): fecha de inicio de alquiler
            fecfin (datetime): decha de fin de alquiler
            tipo_elegido (str): tipo de vehículo a alquilar
            gama_elegida (str): gama del vehículo a alquilar

        Returns:
            Auto asignado a la reserva
        """
        fecinicio = datetime.strptime(fecinicio,"%d-%m-%Y").date()
        fecfin = datetime.strptime(fecfin,"%d-%m-%Y").date()
        setvehiculosdisponibles=set()
        for k,v in Vehiculos.diccVehiculos.items():
            if v.tipo == tipo_elegido and v.gama==gama_elegida:
                setvehiculosdisponibles.add(k)        
        
        for k in Reserva.diccReservas.keys():
            fechaInicioReservak = datetime.strptime(Reserva.diccReservas[k].fechaInicio,"%d-%m-%Y").date()
            fechaFinReservak = datetime.strptime(Reserva.diccReservas[k].fechaFin,"%d-%m-%Y").date()
            if Vehiculos.diccVehiculos[Reserva.diccReservas[k].patente_auto].tipo == tipo_elegido and Vehiculos.diccVehiculos[Reserva.diccReservas[k].patente_auto].gama == gama_elegida:
                if ((fecinicio >= fechaInicioReservak and fecinicio <= fechaFinReservak) or ( fecfin <= fechaFinReservak and fecfin >= fechaInicioReservak) or (fecinicio<=fechaInicioReservak and fecfin >= fechaFinReservak)) and (Reserva.diccReservas[k].fechaCancel in ['',None]):
                
                    setvehiculosdisponibles.remove(Reserva.diccReservas[k].patente_auto)  

        if len(setvehiculosdisponibles) == 0:
            return None
        else:
            return random.choice(list(setvehiculosdisponibles))
    

    '''Función para eliminar un vehículo'''
    def eliminar(self):
        for k,v in Vehiculos.diccVehiculos.items():
            if k==self.patente:
                Vehiculos.setVehiculos.discard(self.patente)                
        del(Vehiculos.diccVehiculos[self.patente])


    '''Método str para clase vehiculos'''
    def __str__(self):    
        return(f"El vehículo {self.marca} {self.modelo} de patente {self.patente}, año {self.anio}, tiene un precio de alquiler por día de {self.precioxdia}, es de tipo {self.tipo} y gama {self.gama}")
    

'''Función que ejecuta las instancias de la clase. Estas instancias se crean con la informacion del archivo csv
correspondiente, y son cargados al diccionario desde su constructor'''
util.leerCsv('Vehiculos.csv', Vehiculos)



if __name__ == "__main__":
   pass

