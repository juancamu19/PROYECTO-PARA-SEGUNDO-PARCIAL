import csv
from ClaseAlquileres import Alquiler
from ClaseVehiculos import Vehiculos
from ClaseReservas import Reserva
from ClasePersonas import Personas
from datetime import datetime
import funcionescsv as funcsv
import validaciones as val

class Empresa():
    def __init__(self):
        self.cuenta = 0
        self.fecinicio = None 
    
    
    # def aggVehiculo(patente, modelo, marca, anio, precio):
    #      nuevoauto = Vehiculos(patente, modelo, marca, anio, precio)
    #      Vehiculos.cantVehiculos+=1
         
    #      with open('Vehiculos.csv','a',newline='') as fileEscAut: ##aca agrego al csv el registro nuevo de auto
    #        EscritorAutos = csv.writer(fileEscAut)
    #        EscritorAutos.writerow(fn.list_to_str(nuevoauto.listaVehiculo))
    
    
    # def aggReserva(dni, patente_auto, fechaInicio, fechaFin):
    #      Reserva.cantReservas+=1
    #      nuevareserva = Reserva(dni, patente_auto, fechaInicio, fechaFin)  
    #      print('su id de reserva es {}'.format(nuevareserva.id))
    #      with open('Reservas.csv','a',newline='') as fileEscRes: ##aca agrego al csv el registro nuevo de reserva
    #        EscritorReservas=csv.writer(fileEscRes)
    #        EscritorReservas.writerow(fn.list_to_str(nuevareserva.listareserva))
         
    
    
    # def cancelarreserva(idreserva):
    #     Vehiculos.registroVehiculos = []
    #     fn.BajarVehiculos(Vehiculos.registroVehiculos)
        
    #     Reserva.registroReservas = []
    #     fn.BajarReserva(Reserva.registroReservas)
        
    #     for reserva in Reserva.registroReservas:
    #             if idreserva == reserva[0]:  ##encuentro la reserva que quiero cancelar
    #                 autoreserva = reserva[2]  ##guardo en autoreserva el auto que le correspondia a esa reserva
    #                 reserva[5] = datetime.now() ##agrego fecha de cancelacion en reserva
        
    #     for vehiculo in Vehiculos.registroVehiculos:
    #          if vehiculo[0] == autoreserva:     
    #               vehiculo[5] = True   ##cambio la disponibilidad del auto que antes queria reservar
        
    #     fn.AgregarReservaCSV(Reserva.registroReservas)  #escribo los archivos en el csv
    #     fn.AgregarVehiculosCSV(Vehiculos.registroVehiculos)                     
    
    
    # def cambiarfechaExpiracionAlquiler(idreserva):
    #     Reserva.registroReservas = []
    #     fn.BajarReserva(Reserva.registroReservas)
    #     for reserva in Reserva.registroReservas:
    #             if idreserva == reserva[0]:  ##encuentro la reserva que quiero cambiar
    #                 fechainicio=reserva[3]
    #     fechanueva = input('ingrese fecha de expiración de alquiler de la forma D-M-YYYY')
    #     while val.validarFechaFin(fechainicio,fechanueva) == False:
                    
    #                 fechanueva = input('Ingrese fecha fin del alquiler de la forma D-M-YYYY ')
        
    #     for reserva in Reserva.registroReservas:
    #             if idreserva == reserva[0]:  ##encuentro la reserva que quiero cambiar
    #                 reserva[4] = fechanueva
    #     fn.AgregarReservaCSV(Reserva.registroReservas)        
    
    
    # def cambiarfechaInicioAlquiler(idreserva):
    #     Reserva.registroReservas = []
    #     fn.BajarReserva(Reserva.registroReservas)
    #     fechafin=''
    #     for reserva in Reserva.registroReservas:
    #             if idreserva == reserva[0]:  ##encuentro la reserva que quiero cambiar
    #                 reserva[4] = fechafin
    #     fechanueva = input('ingrese fecha de Inicio de alquiler de la forma D-M-YYYY')
    #     while val.validarModifFechaInicio(fechanueva,fechafin) == False:
    #                 fechanueva = input('Ingrese fecha de inicio del alquiler de la forma D-M-YYYY ')
                             
                    
    #     for reserva in Reserva.registroReservas:
    #             if idreserva == reserva[0]:  ##encuentro la reserva que quiero cambiar
    #                 reserva[3] = fechanueva
        
    #     fn.AgregarReservaCSV(Reserva.registroReservas)            
    
    
    # def aggAlquiler(idReserva):
    #       Vehiculos.registroVehiculos = []
    #       fn.BajarVehiculos(Vehiculos.registroVehiculos)
          
    #       Reserva.registroReservas = []
    #       fn.BajarReserva(Reserva.registroReservas)
          
    #       nuevoalquiler=Alquiler(idReserva)
          
    #       for reserva in Reserva.registroReservas:
    #             if nuevoalquiler.idReserva == reserva[0]:  ##encuentro la reserva que se encuentra en el alquiler
    #                 nuevoalquiler.fechainicioalquiler = reserva[3]  ##en esta linea y en la de abajo, genero automaticamente los campos de inicio y fin de alquiler a partir de la reserva 
    #                 nuevoalquiler.fechaExpiracionAlquiler = reserva[4]
    #                 nuevoalquiler.dni = reserva[1]
    #                 nuevoalquiler.auto = reserva[2]
          
    #       nuevoalquiler.listaAlquiler = [nuevoalquiler.id,nuevoalquiler.idReserva,nuevoalquiler.auto,nuevoalquiler.fechainicioalquiler,nuevoalquiler.fechaExpiracionAlquiler,nuevoalquiler.fechadev,nuevoalquiler.dni]
          
    #       for auto in Vehiculos.registroVehiculos:
    #           if auto[0] == nuevoalquiler.auto:
    #               auto[5] = False
          
    #       fn.AgregarReservaCSV(Reserva.registroReservas)
    #       fn.AgregarVehiculosCSV(Vehiculos.registroVehiculos)
    #     #   with open('Finanzas.csv','w',newline='') as fileEscFin: ##aca agrego al csv el registro nuevo de monto
    #     #    EscritorFinanzas=csv.writer(fileEscFin)
    #     #    EscritorFinanzas.writerow(list(str(nuevoalquiler.monto)))
          
    #       with open('Alquileres.csv','a',newline='') as fileEscAlq:  ##escribo sobre el archivo csv el nuevo registro de alquiler
    #        EscritorAlquiler = csv.writer(fileEscAlq)
    #        EscritorAlquiler.writerow(nuevoalquiler.listaAlquiler)    
    
    
    # def devolverauto(idalquiler):
    #     Alquiler.registroAlquileres = []
    #     fn.BajarAlquileres(Alquiler.registroAlquileres)
    #     Vehiculos.registroVehiculos = []
    #     fn.BajarVehiculos(Vehiculos.registroVehiculos)
        
    #     for alquiler in Alquiler.registroAlquileres:
    #             if alquiler[0] == idalquiler:  ##encuentro el alquiler, y agrego el valor de fecha devolucion 
    #                 alquiler[5] = datetime.now()
    #                 auto = alquiler[2]
       
    #     for vehiculo in Vehiculos.registroVehiculos:
    #           if vehiculo[0] == auto: ##modifico la disponibilidad en el auto devuelto(lo pongo disponible)
    #                vehiculo[5] = True
        
    #     fn.AgregarAlquilerCSV(Alquiler.registroAlquileres)
    #     fn.AgregarVehiculosCSV(Vehiculos.registroVehiculos)
    
    
    def aggCliente(dni, nombre, apellido, fecnac, email, contraseña):
         #Personas.registroPersonas = []
         #fn.BajarPersonas(Personas.registroPersonas)
         
         nuevocliente = Personas(dni, nombre, apellido, fecnac, email, contraseña)
         with open('Personas.csv','a',newline='') as fileEscPer:  ##escribo sobre el archivo csv el nuevo registro de persona
           EscritorPersona = csv.writer(fileEscPer)
           EscritorPersona.writerow(nuevocliente.listapersona)
    


# with open('Vehiculos.csv','w',newline='') as fileEscAut: ##aca agrego al csv el registro nuevo de auto
#            EscritorAutos=csv.writer(fileEscAut)
# with open('Reservas.csv','w',newline='') as fileEscAut: ##aca agrego al csv el registro nuevo de auto
#            EscritorAutos=csv.writer(fileEscAut)
# with open('Alquileres.csv','w',newline='') as fileEscAut: ##aca agrego al csv el registro nuevo de auto
#            EscritorAutos=csv.writer(fileEscAut)
# with open('Personas.csv','w',newline='') as fileEscAut: ##aca agrego al csv el registro nuevo de auto
#            EscritorAutos=csv.writer(fileEscAut)
# if __name__=='__main__':
#     Empresa.aggVehiculo('abc123','ka','ford',2000,5000000)
#     Empresa.aggVehiculo('bcd123','ka','ford',2000,5000000)

# Empresa.aggReserva('0','44998438','abc123','19/05/2003','19/06/2003')
# Empresa.aggReserva('1','44998438','bcd123','19/05/2003','19/06/2003')
# empresaprueba.aggAlquiler('0')
# empresaprueba.devolverauto('1')




# Empresa.aggCliente('44998438','juan','cams','19/05/2003','mail')
# fn.BajarVehiculos(Vehiculos.registroVehiculos)
# print(Vehiculos.registroVehiculos)
# fn.AgregarVehiculosCSV(Vehiculos.registroVehiculos)
########OBS: AGG VEHICULO FUNCA BIEN, HAY PROBLEMA PARA BAJAR VEHICULO(AL EJECUTAR AGGRESERVA), Y EN RESERVA NO SE PORQUE PERO NO SE ESCRIBE NADA