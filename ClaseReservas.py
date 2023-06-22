from datetime import datetime
import Utilities as util

#se crea la clase reserva
class Reserva():
    cantReservas = 0  
    setReservas = set()
    diccReservas=dict()

    def __init__(self, id = None, dni = None, patente_auto = None, fechaInicio = None, fechaFin = None, fechaCancel = None):
        self.id = id
        self.dni = dni
        self.patente_auto = patente_auto
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.fechaCancel = fechaCancel
        Reserva.cantReservas += 1
        Reserva.setReservas.add(self.id)
        Reserva.diccReservas[self.id] = self
    
    def cancelarreserva(self):
        fechainicio=datetime.strptime(self.fechaInicio,"%d-%m-%Y").date()
        fechaactual=datetime.now()
        if  (fechainicio-fechaactual.date()).days<5:
            print('faltan menos de 5 dias para que comience su alquiler, no puede cancelar la reserva')
        else:
            self.fechaCancel=datetime.now()                
        
    #no habria que cambiar ALQUILER ahi? o el nombre de la funcion o el lugar
    def cambiarfechaExpiracionAlquiler(self,fechanueva):     
        self.fechaFin = fechanueva 
    
    def cambiarfechaInicioAlquiler(self,fechanueva):
        self.fechaInicio = fechanueva 

    #método str para clase reserva
    def __str__(self):
        return f"La reserva de id {self.id}, hecha por el usuario de dni {self.dni} para el vehículo de patente {self.patente_auto}, inicia el {self.fechaInicio} y finaliza el {self.fechaFin}"


#diccionario que contiene los registros nuevos de reservas
util.leerCsv('Reservas.csv', Reserva)

# Pruebas de Funcionamiento
if __name__ == "__main__":
    r1=Reserva(2,'44998438')
    a=r1.__str__()
    print(a)
