class Vehiculos():
    cantVehiculos = 0
    
    def __init__(self, patente, modelo, marca, anio, precio):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.precio = precio             #Por día de alquiler
        self.disponible = True

    def __str__(self):     #Sería como una consulta general sobre el estado de un vehículo
        return(f"""El vehículo {self.marca} {self.modelo} de patente {self.patente}, año {self.anio}, tiene un precio de alquiler por día de {self.precio}, ...""") 
    

    # def aggVehiculo(patente, modelo, marca, anio, precio):
    #      nuevoauto = Vehiculos(patente, modelo, marca, anio, precio)
    #      Vehiculos.cantVehiculos+=1
         
    #     with open('Vehiculos.csv','a',newline='') as fileEscAut: ##aca agrego al csv el registro nuevo de auto
    #        EscritorAutos = csv.writer(fileEscAut)
    #        EscritorAutos.writerow(fn.list_to_str(nuevoauto.listaVehiculo))