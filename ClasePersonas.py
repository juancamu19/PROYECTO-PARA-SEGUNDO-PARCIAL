import hashlib
from ClaseReservas import Reserva,diccReservas
from ClaseVehiculos import Vehiculos,diccVehiculos 
from ClaseAlquileres import diccAlquileres
import pandas as pd
import Utilities as util

#se crea la clase personas
class Personas:
    setdnis = set()
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecnac = fecnac
        self.email = email
        self.contraseña=contraseña

#metodo str para la clase
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, DNI: {self.dni}, Fecha de nacimiento: {self.fecnac}, Email: {self.email}, Cantidad de reservas realizadas hasta el momento: {self.cantreservas}"

        
    # def objeto_a_lista(self):
    #     obj_list = []
    #     for attr, value in self.__dict__.items():
    #         obj_list.append(value)
    #     return obj_list
   
   #MODIFICO CAMBIAR DATO PARA INGRESAR UN PARAMETRO
    def cambiar_dato(self, identificador,atributo, valor):
        match atributo:

            case 'dni':
                dniviejo=self.dni
                self.dni = valor
                for elem in type(self).setdnis:
                    if elem[0]==dniviejo:
                        type(self).setdnis.discard(elem)
                        type(self).setdnis.add((self.dni,self.contraseña))

            case 'nombre':
                self.nombre = valor

            case 'apellido':
                self.apellido = valor

            case 'fecnac':
                self.fecnac = valor

            case 'email':
                self.email = valor
              
            case 'contraseña':
                contraseñanuevo = valor
                contraseñanuevo = contraseñanuevo.encode('utf-8')
                objetoHash = hashlib.sha256(contraseñanuevo)
                contraHasheada = objetoHash.hexdigest()
                self.contraseña = contraHasheada
                for elem in type(self).setdnis:
                    if elem[0]==identificador:
                        type(self).setdnis.discard(elem)
                        type(self).setdnis.add((elem[0],self.contraseña))
        
        print(f"Su {atributo} se ha modficado correctamente a {valor}")
   
   
    def darDeBaja(self,indentificador,dicc):
        del(dicc[indentificador])

        contraseñax = self.contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseñax)
        contraHasheada = objetoHash.hexdigest()
        Usuarios.setdnis.remove((self.dni,contraHasheada))

        print("Su usuario de ha eliminado correctamente")

                


#se crea un hijo de la clase personas: usuarios
class Usuarios(Personas):
    setdnis = set()
    def __init__(self,dni, nombre, apellido, fecnac, email, contraseña,username, cantreservas=0):
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.username = username
        self.cantreservas = int(cantreservas)
        Usuarios.setdnis.add((self.dni,self.contraseña)) 
    
    #funcion para agregar usuario a diccionario para cargar a csv
    def agregarUsuario(dni, username, nombre, apellido, fecnac, email, contraseña):
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()  
        diccUsuarios[dni]= Usuarios(dni, nombre, apellido, fecnac, email, contraHasheada, username)
    
    #funcion para agregar reserva a diccionario
    def agregarReserva(self, patente_auto, fechaInicio, fechaFin):
        diccReservas[Reserva.cantReservas + 1] = Reserva( Reserva.cantReservas+1, self.dni, patente_auto, fechaInicio, fechaFin)
        self.cantreservas+=1  
        print(f'La reserva de id {Reserva.cantReservas}, hecha por el usuario de dni {self.dni} para el vehículo de patente {patente_auto}, inicia el {fechaInicio} y finaliza el {fechaFin}')

    #funcion para quitar reserva del diccionario    
    def cancelarReserva(self,idreserva):
        diccReservas[idreserva].cancelarreserva()

    #funciones para modificar las fechas de la reserva
    def modifFecInicioReserva(self,idreserva,fechanueva):
        diccReservas[idreserva].cambiarfechaInicioAlquiler(fechanueva)

    def modifFecFinReserva(self,idreserva,fechanueva):
        diccReservas[idreserva].cambiarfechaExpiracionAlquiler(fechanueva)



#diccionario que contiene los registros de usuarios del csv
diccUsuarios = util.leerCsv('Usuarios.csv', Usuarios)



#se crea otro hijo de la clase persona: Administrador
class Administrador(Personas):
    cantempleados = 0
    setlegajos = set()
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña, legajo = None):
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.legajo= Administrador.cantempleados
        Administrador.cantempleados+=1       
        Administrador.setlegajos.add((str(self.legajo),self.contraseña))
        Administrador.setdnis.add(self.dni)

    #funcion para agregar empleado a diccionario para su carga a csv de empleados
    def agregarEmpleado(self,dni, nombre, apellido, fecnac, email, contraseña):
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()
        diccEmpleados [Administrador.cantempleados] = Administrador(dni, nombre, apellido, fecnac, email, contraHasheada)
    
    #funcion para agregar un vehiculo a diccionario para su carga a csv de vehiculos
    def agregarVehiculo(self, patente, modelo, marca, anio, tipo, gama):        
        diccVehiculos[patente]= Vehiculos(patente, modelo, marca, anio, tipo, gama)
        print(f"Se ha agregado correctamente el vehículo de patente {patente}, modelo {modelo}, marca {marca}, anio {anio}, tipo {tipo}")

    #funcion para modificar un atributo de un vehiculo
    def modificarVehiculo(self, patente, atributo,valor):
        diccVehiculos[patente].modificar(atributo,valor)

    #funcion para dar por finalizado un alquiler
    def finalizarAlquiler(self, idalquiler):
        diccAlquileres[idalquiler].finalizar()
        diccVehiculos[diccAlquileres[idalquiler].patente_auto].devolver()

    #funcion para quitar un vehiculo de diccionario
    def eliminarVehiculo(self, patente):         
        diccVehiculos[patente].eliminar(diccVehiculos)

    #funcion para cambiar precios de un auto segun gama y tipo
    def modifPreciosAutos(self,tipo,gama,precionuevo):
        df = pd.read_csv('PreciosVehiculos.csv', index_col=0)
        df.at[gama, tipo] = precionuevo
        df.to_csv('PreciosVehiculos.csv')

#diccionario que contiene los registros nuevos de empleados
diccEmpleados = util.leerCsv('Empleados.csv', Administrador)
    
# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass

    
    

