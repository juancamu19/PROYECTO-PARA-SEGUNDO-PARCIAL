import validaciones as val
from datetime import datetime
import funcionescsv as funcsv
class Reserva():
    cantReservas = 0  
    setReservas = set()
    # diccionario=dict()

    def __init__(self, id = None, dni = None, patente_auto = None, fechaInicio = None, fechaFin = None, fechaCancel = None):
        self.id = id
        self.dni = dni
        self.patente_auto = patente_auto
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.fechaCancel = fechaCancel

        Reserva.cantReservas += 1
        Reserva.setReservas.add(self.id)
    
    def objeto_a_lista(self):
        obj_list = []
        for attr, value in self.__dict__.items():
            obj_list.append(value)
        return obj_list
    
    
    def cancelarreserva(self):
        fechainicio=datetime.strptime(self.fechaInicio,"%d-%m-%Y").date()
        fechaactual=datetime.now()
        if  (fechainicio-fechaactual.date()).days<5:
            print('faltan menos de 5 dias para que comience su alquiler, no puede cancelar la reserva')
        else:
            self.fechaCancel=datetime.now()                
        
    
    def cambiarfechaExpiracionAlquiler(self):
        fechanueva = input('ingrese fecha de expiración de alquiler de la forma D-M-YYYY')
        while val.validarFechaFin(self.fechaInicio,fechanueva) == False:
                    
            fechanueva = input('Ingrese fecha fin del alquiler de la forma D-M-YYYY ')
        
        self.fechaFin = fechanueva 

    
    def cambiarfechaInicioAlquiler(self):
        fechanueva = input('ingrese fecha de Inicio de alquiler de la forma D-M-YYYY')
        while val.validarModifFechaInicio(fechanueva,self.fechaFin) == False:
            fechanueva = input('Ingrese fecha de inicio del alquiler de la forma D-M-YYYY ')      
        self.fechaInicio = fechanueva 

    
    def validarReserva(id):
        if id in Reserva.setReservas:  
            return True          
        else:
            return False

    
    def __str__(self):
        return f"La reserva de id {self.id}, hecha por el usuario de dni {self.dni} para el vehículo de patente {self.patente_auto}, inicia el {self.fechaInicio} y finaliza el {self.fechaFin}"

diccReservas = funcsv.leerCsv('Reservas.csv', Reserva)

# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass
