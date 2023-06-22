import hashlib
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos
from ClaseAlquileres import Alquiler
import pandas as pd
import Utilities as util
from claseEmpresa import Empresa

'''Se crea la clase Personas'''
class Personas:
    
    '''Iniciador de la clase Personas'''
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecnac = fecnac
        self.email = email
        self.contraseña=contraseña


    '''Metodo str para la clase'''
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, DNI: {self.dni}, Fecha de nacimiento: {self.fecnac}, Email: {self.email}, Cantidad de reservas realizadas hasta el momento: {self.cantreservas}"


    '''Funcion para cambiar un atributo de la Persona'''
    def cambiar_dato(self, identificador, atributo, valor_nuevo):
        match atributo:

            case 'dni':
                dniviejo  = self.dni
                self.dni = valor_nuevo
                for elem in type(self).setdnis:
                    if elem[0]==dniviejo:
                        type(self).setdnis.discard(elem)
                        type(self).setdnis.add((self.dni,self.contraseña))

            case 'nombre':
                self.nombre = valor_nuevo

            case 'apellido':
                self.apellido = valor_nuevo

            case 'fecnac':
                self.fecnac = valor_nuevo

            case 'email':
                self.email = valor_nuevo
              
            case 'contraseña':
                contraseñanuevo = valor_nuevo
                contraseñanuevo = contraseñanuevo.encode('utf-8')
                objetoHash = hashlib.sha256(contraseñanuevo)
                contraHasheada = objetoHash.hexdigest()
                self.contraseña = contraHasheada
                for elem in type(self).setdnis:
                    if elem[0]==str(identificador):
                        type(self).setdnis.discard(elem)
                        type(self).setdnis.add((elem[0],self.contraseña))
        
        print(f"Su {atributo} se ha modficado correctamente a {valor_nuevo}")

                

'''Se crea un hijo de la clase personas: Usuarios'''
class Usuarios(Personas):
    diccUsuarios=dict()
    setdnis = set()

    '''Iniciador de la clase Usuarios'''
    def __init__(self,dni, nombre, apellido, fecnac, email, contraseña,username, cantreservas=0):
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.username = username
        self.cantreservas = int(cantreservas)
        Usuarios.setdnis.add((self.dni,self.contraseña)) 
        Usuarios.diccUsuarios[self.dni]=self
    

    '''Funcion para crear un usuario '''
    def agregarUsuario(dni, username, nombre, apellido, fecnac, email, contraseña):
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()  
        Usuarios(dni, nombre, apellido, fecnac, email, contraHasheada, username)
    

    '''Funcion para agregar una reserva al diccionario de reservas'''
    def agregarReserva(self, patente_auto, fechaInicio, fechaFin):
        Reserva(Reserva.cantReservas+1, self.dni, patente_auto, fechaInicio, fechaFin)
        self.cantreservas+=1  
        print(f'La reserva de id {Reserva.cantReservas}, hecha por el usuario de dni {self.dni} para el vehículo de patente {patente_auto}, inicia el {fechaInicio} y finaliza el {fechaFin}')


    '''Funcion para eliminar una reserva del diccionario'''    
    def cancelarReserva(self,idreserva):
        Reserva.diccReservas[idreserva].cancelarreserva()


    '''Funciones para modificar las fechas de la reserva'''
    def modifFecInicioReserva(self,idreserva,fechanueva):
        Reserva.diccReservas[idreserva].cambiarfechaInicioAlquiler(fechanueva)

    def modifFecFinReserva(self,idreserva,fechanueva):
        Reserva.diccReservas[idreserva].cambiarfechaExpiracionAlquiler(fechanueva)


    '''Funcion para mostrar las reservas a nombre de un usuario'''
    def mostrarMisReservas(self):
        Mensaje=''
        for k,v in Reserva.diccReservas.items():            
            if v.dni==self.dni:
                Mensaje+=v.__str__()+'\n'
        return Mensaje
    

    '''Funcion para eliminar un usuario'''
    def darDeBajaUsuario(self):
        for k,v in Usuarios.diccUsuarios.items():
            if k==self.dni:
                Usuarios.setdnis.discard((self.dni,self.contraseña))
        del(Usuarios.diccUsuarios[self.dni])
        print("Su usuario de ha eliminado correctamente")


'''Diccionario que contiene los registros de Usuarios'''
util.leerCsv('Usuarios.csv', Usuarios)



'''Se crea otro hijo de la clase personas: Administrador'''
class Administrador(Personas):
    cantempleadosAcumulativo = 0
    setlegajos = set()
    diccEmpleados = dict()
    setdnis = set()
    
    '''Iniciador de la clase Administrador'''
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña, legajo = None):
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.legajo= Administrador.cantempleadosAcumulativo
        Administrador.cantempleadosAcumulativo+=1       
        Administrador.setlegajos.add((str(self.legajo),self.contraseña))
        Administrador.setdnis.add(self.dni)
        Administrador.diccEmpleados[self.legajo]=self


    '''Funcion para agregar empleado a diccionario para su carga a csv de empleados'''
    def agregarEmpleado(self, dni, nombre, apellido, fecnac, email, contraseña):
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()
        Administrador(dni, nombre, apellido, fecnac, email, contraHasheada)
    

    '''Funcion para agregar un vehiculo a diccionario para su carga al archivo Vehiculos'''
    def agregarVehiculo(self, patente, modelo, marca, anio, tipo, gama):        
        Vehiculos(patente, modelo, marca, anio, tipo, gama)
        print(f"Se ha agregado correctamente el vehículo de patente {patente}, modelo {modelo}, marca {marca}, anio {anio}, tipo {tipo}")


    '''Funcion para modificar un atributo de un vehiculo'''
    def modificarVehiculo(self, patente, atributo, valor_nuevo):
        Vehiculos.diccVehiculos[patente].modificar(atributo,valor_nuevo)


    '''Funcion para dar por finalizado un alquiler'''
    def finalizarAlquiler(self, idalquiler):
        Alquiler.diccAlquileres[idalquiler].finalizar()
        Vehiculos.diccVehiculos[Alquiler.diccAlquileres[idalquiler].patente_auto].devolver()


    '''Funcion para eliminar un vehículo'''
    def eliminarVehiculo(self, patente):         
        Vehiculos.diccVehiculos[patente].eliminar()


    '''Funcion para cambiar el precio de un auto segun gama y tipo'''
    def modifPreciosAutos(self, tipo, gama, precionuevo):
        df = pd.read_csv('PreciosVehiculos.csv', index_col=0)
        df.at[gama, tipo] = precionuevo
        df.to_csv('PreciosVehiculos.csv')


    '''Funcion para eliminar un empleado'''
    def darDeBajaEmpleado(self):
        for k,v in Administrador.diccEmpleados.items():
            if k==self.legajo:
                Administrador.setlegajos.discard((self.legajo,self.contraseña))
                Administrador.setdnis.discard(self.dni)
        del(Administrador.diccEmpleados[self.legajo])
        print("El empleado se ha eliminado correctamente")


    '''Funcion para consultar las ventas por día'''
    def consultarVentasXDia(self, dia):
        Empresa.gestionVentasxdia(dia)
    

    '''Funcion para consultar las ventas por mes'''
    def consultarVentasXMes(self, mes):
        Empresa.gestionVentasxmes(mes)


'''Diccionario que contiene los registros nuevos de empleados'''
util.leerCsv('Empleados.csv', Administrador)
    


'''Pruebas de Funcionamiento'''
if __name__ == "__main__":
    dicc1={1:'a',2:'b'}
    dicc2={1:'a',2:'b'}
    print(type(dicc1))
    del(dicc1[1])
   
    print(dicc1)

    
    

