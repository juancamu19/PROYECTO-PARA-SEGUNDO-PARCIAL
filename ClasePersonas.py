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
        """_summary_

        Args:
            dni (_type_): _description_
            nombre (_type_): _description_
            apellido (_type_): _description_
            fecnac (_type_): _description_
            email (_type_): _description_
            contrase (_type_): _description_
        """
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecnac = fecnac
        self.email = email
        self.contraseña=contraseña


    '''Metodo str para la clase'''
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, DNI: {self.dni}, Fecha de nacimiento: {self.fecnac}, Email: {self.email}, Cantidad de reservas realizadas hasta el momento: {self.cantreservas}"


    '''Funcion para cambiar un atributo de la Persona. Se ingresa por parámetro que atributo se va a modificar(validado)
    y que valor se le dara a este atributo. A su vez, se pasaa por parámetro el identificador ya que mientras que
    en persona se trabaja con dni como clave, en empleados con legajos. De esta manera permite la herencia y eficientización
    de código'''
    ''' Aclaraciones extras: 1- Al cambiar el dni, se debe reemplazar el valor anterior por el nuevo en el set
    2- Al cambiar la contraseña se debe hacer lo mismo, solo que en este caso la que se reemplaza es la tupla dni:contraseña'''
    def cambiar_dato(self, identificador, atributo, valor_nuevo):
        """_summary_

        Args:
            identificador (_type_): _description_
            atributo (_type_): _description_
            valor_nuevo (_type_): _description_
        """
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

                

'''Se crea un hijo de la clase personas: Usuarios. 
ATENCION: setdnis hace referencia a un set de tuplas dni,contraseña usado para login. No son unicamente dnis'''
class Usuarios(Personas):
    diccUsuarios=dict()
    setdnis = set()

    '''Iniciador de la clase Usuarios, en el mismo se agrega desde el constructor el objeto al diccionario
    de la clase. A su vez se carga el set de la clase para facilitar las validaciones. 
    Notar que setdnis contiene un conjunto de tuplas, donde cada tupla almacena un par dni,contraseña. Se utiliza
    esta estructura de datos al ser las mismas hasheables e irrepetibles por el dni. Notar también que su mayor implementacion
    será en validaciones de login, con lo cual no es lo frecuente ir modificando el valor de las tuplas, adecuandose
    al caso. 
    Por otra parte, la eleccion de sets se adecua a la funcion de validacion por su rapidez y bajo costo de computo.'''
    def __init__(self,dni, nombre, apellido, fecnac, email, contraseña,username, cantreservas=0):
        """_summary_

        Args:
            dni (_type_): _description_
            nombre (_type_): _description_
            apellido (_type_): _description_
            fecnac (_type_): _description_
            email (_type_): _description_
            contrase (_type_): _description_
            username (_type_): _description_
            cantreservas (int, optional): _description_. Defaults to 0.
        """
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.username = username
        self.cantreservas = int(cantreservas)
        Usuarios.setdnis.add((self.dni,self.contraseña)) 
        Usuarios.diccUsuarios[self.dni]=self
    

    '''Funcion para crear un usuario. Se pasa por parámetro la contraseña hasheada. Como el usuario interactua con la
     interfaz por su cuenta, el mismo puede agregarse como usuario.  '''
    def agregarUsuario(dni, username, nombre, apellido, fecnac, email, contraseña):
        """_summary_

        Args:
            dni (_type_): _description_
            username (_type_): _description_
            nombre (_type_): _description_
            apellido (_type_): _description_
            fecnac (_type_): _description_
            email (_type_): _description_
            contrase (_type_): _description_
        """
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()  
        Usuarios(dni, nombre, apellido, fecnac, email, contraHasheada, username)
    

    '''Funcion para agregar una reserva al diccionario de reservas. Al instanciar el objeto reservas, ella sola se agrega
    al dicionario correspondiente'''
    def agregarReserva(self, patente_auto, fechaInicio, fechaFin):
        """_summary_

        Args:
            patente_auto (_type_): _description_
            fechaInicio (_type_): _description_
            fechaFin (_type_): _description_
        """
        Reserva(Reserva.cantReservas+1, self.dni, patente_auto, fechaInicio, fechaFin)
        self.cantreservas+=1  
        print(f'La reserva de id {Reserva.cantReservas}, hecha por el usuario de dni {self.dni} para el vehículo de patente {patente_auto}, inicia el {fechaInicio} y finaliza el {fechaFin}')


    '''Funcion para eliminar una reserva del diccionario'''    
    def cancelarReserva(self,idreserva):
        """_summary_

        Args:
            idreserva (_type_): _description_
        """
        Reserva.diccReservas[idreserva].cancelarreserva()


    '''Funciones para modificar las fechas de la reserva. Las fechas se pasan ya validadas'''
    def modifFecInicioReserva(self,idreserva,fechanueva):
        """_summary_

        Args:
            idreserva (_type_): _description_
            fechanueva (_type_): _description_
        """
        Reserva.diccReservas[idreserva].cambiarfechaInicioAlquiler(fechanueva)

    def modifFecFinReserva(self,idreserva,fechanueva):
        """_summary_

        Args:
            idreserva (_type_): _description_
            fechanueva (_type_): _description_
        """
        Reserva.diccReservas[idreserva].cambiarfechaExpiracionAlquiler(fechanueva)


    '''Funcion para mostrar las reservas a nombre de un usuario'''
    def mostrarMisReservas(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        Mensaje=''
        for k,v in Reserva.diccReservas.items():            
            if v.dni==self.dni:
                Mensaje+=v.__str__()+'\n'
        return Mensaje
    

    '''Funcion para eliminar un usuario. No basta con eliminarlo como objeto, tambien se debe eliminarlo de los sets.'''
    def darDeBajaUsuario(self):
        for k,v in Usuarios.diccUsuarios.items():
            if k==self.dni:
                Usuarios.setdnis.discard((self.dni,self.contraseña))
        del(Usuarios.diccUsuarios[self.dni])
        print("Su usuario de ha eliminado correctamente")


'''Funcion que instancia los usuarios con la informacion del csv'''
util.leerCsv('Usuarios.csv', Usuarios)



'''Se crea otro hijo de la clase personas: Administrador
ATENCION: setdnis en administrador es un set que contiene unicamente los dnis de empleados, a diferencia de usuarios.
setlegajos, en cambio, es un set de tuplas legajo,contraseña que se usan para validar el login.
Esta diferencia radica en que para usuarios la clave identificatoria es dni, pero en administrador no.'''
class Administrador(Personas):
    cantempleadosAcumulativo = 0
    setlegajos = set()
    diccEmpleados = dict()
    setdnis = set()
    
    '''Iniciador de la clase Administrador. La explicacion para las estructuras elegidas para los sets son análogas
    a las de la clase usuarios. Se trabaja con legajo como clave identificatoria al ser más representativa y tambien 
     unica. '''
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña, legajo = None):
        """_summary_

        Args:
            dni (_type_): _description_
            nombre (_type_): _description_
            apellido (_type_): _description_
            fecnac (_type_): _description_
            email (_type_): _description_
            contrase (_type_): _description_
            legajo (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.legajo= Administrador.cantempleadosAcumulativo
        Administrador.cantempleadosAcumulativo+=1       
        Administrador.setlegajos.add((str(self.legajo),self.contraseña))
        Administrador.setdnis.add(self.dni)
        Administrador.diccEmpleados[self.legajo]=self


    '''Funcion para agregar empleado a diccionario para su carga a csv de empleados. Un empleado ya existente
    se encarga de agregar a otro nuevo. Esto presupone la existencia de al menos un empleado, lo cual se
     considero como base '''
    def agregarEmpleado(self, dni, nombre, apellido, fecnac, email, contraseña):
        """_summary_

        Args:
            dni (_type_): _description_
            nombre (_type_): _description_
            apellido (_type_): _description_
            fecnac (_type_): _description_
            email (_type_): _description_
            contrase (_type_): _description_
        """
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()
        Administrador(dni, nombre, apellido, fecnac, email, contraHasheada)
    

    '''Funcion para agregar un vehiculo a diccionario para su carga al archivo Vehiculos. Al instanciar el objeto,
    el mismo se agrega en el diccionario'''
    def agregarVehiculo(self, patente, modelo, marca, anio, tipo, gama):   
        """_summary_

        Args:
            patente (_type_): _description_
            modelo (_type_): _description_
            marca (_type_): _description_
            anio (_type_): _description_
            tipo (_type_): _description_
            gama (_type_): _description_
        """   
        Vehiculos(patente, modelo, marca, anio, tipo, gama)
        print(f"Se ha agregado correctamente el vehículo de patente {patente}, modelo {modelo}, marca {marca}, anio {anio}, tipo {tipo}")


    '''Funcion para modificar un atributo de un vehiculo'''
    def modificarVehiculo(self, patente, atributo, valor_nuevo):
        """_summary_

        Args:
            patente (_type_): _description_
            atributo (_type_): _description_
            valor_nuevo (_type_): _description_
        """
        Vehiculos.diccVehiculos[patente].modificar(atributo,valor_nuevo)


    '''Funcion para dar por finalizado un alquiler. Se modifica la disponibilidad en vehiculos'''
    def finalizarAlquiler(self, idalquiler):
        """_summary_

        Args:
            idalquiler (_type_): _description_
        """
        Alquiler.diccAlquileres[idalquiler].finalizar()
        Vehiculos.diccVehiculos[Alquiler.diccAlquileres[idalquiler].patente_auto].devolver()


    '''Funcion para eliminar un vehículo'''
    def eliminarVehiculo(self, patente): 
                             
        Vehiculos.diccVehiculos[patente].eliminar()


    '''Funcion para cambiar el precio de un auto segun gama y tipo. La modificacion se hace directamente en el csv
    con los precios por categoria y tipo. Se utiliza el dataframe de pandas ya que facilita el manejo de tablas con
    doble entrada'''
    
    def modifPreciosAutos(self, tipo, gama, precionuevo):
        """_summary_

        Args:
            tipo (_type_): _description_
            gama (_type_): _description_
            precionuevo (_type_): _description_
        """
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


    '''FUNCIONES SON DE GESTIÓN'''

    '''Funcion para consultar las ventas por día'''
    def consultarVentasXDia(self, dia):
        """_summary_

        Args:
            dia (_type_): _description_
        """
        Empresa.gestionVentasxdia(dia)
    

    '''Funcion para consultar las ventas por mes'''
    def consultarVentasXMes(self, mes):
        """_summary_

        Args:
            mes (_type_): _description_
        """
        Empresa.gestionVentasxmes(mes)


'''Se instancian objetos de administrador, estos se cargan al diccionario de su clase por su cuenta'''
util.leerCsv('Empleados.csv', Administrador)
    


'''Pruebas de Funcionamiento'''
if __name__ == "__main__":
    pass

    
    

