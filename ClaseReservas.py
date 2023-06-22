from datetime import datetime
import Utilities as util

'''Se crea la clase Reserva. Set Reservas contiene los id de reservas, y es utilizado para las validaciones, 
haciendo diferencia con otras estructuras de datos al trabajar con una gran cantidad de datos y frecuentemente.'''
class Reserva():
    cantReservas = 0  
    setReservas = set()
    diccReservas=dict()

    
    def __init__(self, id = None, dni = None, patente_auto = None, fechaInicio = None, fechaFin = None, fechaCancel = None):
        """Iniciador de la clase Reserva. Se lleva el contador de reservas para generar automaticamente el id de cada
        reserva

        Args:
            id (int): número de id designado para la reserva (identificación)
            dni (str): dni del usuario que realizó la reserva
            patente_auto (str): patente del auto reservado
            fechaInicio (datetime): fecha de inicio del alquiler
            fechaFin (datetime): fecha de fin del alquiler
            fechaCancel (datetime): fecha de cancelación del alquiler (opcional)
        """
        self.id = id
        self.dni = dni
        self.patente_auto = patente_auto
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.fechaCancel = fechaCancel
        Reserva.cantReservas += 1
        Reserva.setReservas.add(self.id)
        Reserva.diccReservas[self.id] = self
    

    '''Funcion para calcelar una reserva. No se permite cancelar una reserva faltando menos de 5 dias para el alquiler'''
    def cancelarreserva(self):
        fechainicio = datetime.strptime(self.fechaInicio,"%d-%m-%Y").date()
        fechaactual = datetime.now()
        if  (fechainicio - fechaactual.date()).days<5:
            print('Faltan menos de 5 dias para que comience su alquiler, no puede cancelar la reserva')
        else:
            self.fechaCancel=datetime.now()                
        

    
    def cambiarfechaExpiracionAlquiler(self,fechanueva):
        """Funcion para cambiar la fecha de finalización de una reserva(posible alquiler, de ahi el nombre)'''

        Args:
            fechanueva (datetime): nueva fecha de finalización del alquiler
        """     
        self.fechaFin = fechanueva 
    

    
    def cambiarfechaInicioAlquiler(self,fechanueva):
        """Funcion para cambiar la fecha de inicio de una reserva(posible alquiler, de ahi el nombre)

        Args:
            fechanueva (datetime): nueva fecha de inicio del alquiler
        """
        self.fechaInicio = fechanueva 


    '''Método str para clase reserva'''
    def __str__(self):
        return f"La reserva de id {self.id}, hecha por el usuario de dni {self.dni} para el vehículo de patente {self.patente_auto}, inicia el {self.fechaInicio} y finaliza el {self.fechaFin}"


'''Se instancian objetos de reservas ya cargadas, estos se cargan al diccionario de su clase por su cuenta'''
util.leerCsv('Reservas.csv', Reserva)



'''Pruebas de Funcionamiento'''
if __name__ == "__main__":
    r1=Reserva(2,'44998438')
    a=r1.__str__()
    print(a)
