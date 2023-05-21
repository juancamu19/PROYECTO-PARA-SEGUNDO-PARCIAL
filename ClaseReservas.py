class Reserva():
    cantReservas = 0  
    registroReservas = {}

    def __init__(self, dni, patente_auto, fechaInicio, fechaFin):
        self.id = Reserva.cantReservas+1
        self.dni = dni
        self.patente_auto = patente_auto
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.fechaCancel = 'no hay fecha de cancelacion'

        Reserva.cantReservas += 1

    def __str__(self):
        p