import validaciones as val
from datetime import datetime
class Reserva():
    cantReservas = 0  
    setReservas=set()

    def __init__(self, id = None,dni=None, patente_auto=None, fechaInicio=None, fechaFin=None,fechaCancel=None):
        self.id =id
        self.dni = dni
        self.patente_auto = patente_auto
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.fechaCancel = fechaCancel

        Reserva.cantReservas += 1
        Reserva.setReservas.add(self.id)
    
    def aggReserva(dni, patente_auto, fechaInicio, fechaFin,diccres):
        diccres[Reserva.cantReservas+1] = Reserva(Reserva.cantReservas+1,dni, patente_auto, fechaInicio, fechaFin)  
        print('su id de reserva es {}'.format(Reserva.cantReservas))

    def objeto_a_lista(self):
        obj_list = []
        for attr, value in self.__dict__.items():
            obj_list.append(value)
        return obj_list
    
    def cancelarreserva(idreserva,diccres):
        fechainicio=datetime.strptime(diccres[idreserva].fechaInicio,"%d-%m-%Y").date()
        fechaactual=datetime.now()
        if  (fechainicio-fechaactual.date()).days<5:
            print('faltan menos de 5 dias para que comience su alquiler, no puede cancelar la reserva')
        else:
            diccres[idreserva].fechaCancel=datetime.now()                
        
    def cambiarfechaExpiracionAlquiler(idreserva,diccres):
        fechanueva = input('ingrese fecha de expiración de alquiler de la forma D-M-YYYY')
        while val.validarFechaFin(diccres[idreserva].fechaInicio,fechanueva) == False:
                    
            fechanueva = input('Ingrese fecha fin del alquiler de la forma D-M-YYYY ')
        
        diccres[idreserva].fechaFin = fechanueva 

    def cambiarfechaInicioAlquiler(idreserva,diccres):
        fechanueva = input('ingrese fecha de Inicio de alquiler de la forma D-M-YYYY')
        while val.validarModifFechaInicio(fechanueva,diccres[idreserva].fechaFin) == False:
            fechanueva = input('Ingrese fecha de inicio del alquiler de la forma D-M-YYYY ')      
        diccres[idreserva].fechaInicio = fechanueva 

    def validarReserva(id):
        if id in Reserva.setReservas:  
            return True          
        else:
            return False

    
    def __str__(self):
        pass

# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass
