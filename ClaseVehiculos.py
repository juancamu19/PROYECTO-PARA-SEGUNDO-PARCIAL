from datetime import datetime
class Vehiculos():
    cantVehiculos = 0
    setVehiculos=set()
    def __init__(self, patente, modelo, marca, anio, precio):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.precio = precio             #Por día de alquiler
        self.disponible = True   ##se podría sacar, creo que no lo usamos mas
        Vehiculos.cantVehiculos+=1
        Vehiculos.setVehiculos.add(self.patente)
    
    def aggVehiculo(patente, modelo, marca, anio, precio,dicc):  ##este atributo no tiene self
        dicc[patente]= Vehiculos(patente, modelo, marca, anio, precio)
        
    def devolverVehiculo(idalquiler,diccalq,diccVehi):
        diccalq[idalquiler].fechadev=datetime.now()
        diccVehi[diccalq[idalquiler].patente_auto].disponible=True
        
         

    def __str__(self):     #Sería como una consulta general sobre el estado de un vehículo
        return(f"""El vehículo {self.marca} {self.modelo} de patente {self.patente}, año {self.anio}, tiene un precio de alquiler por día de {self.precio}, ...""") 
    
# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass
