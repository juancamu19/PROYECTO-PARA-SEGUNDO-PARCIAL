import hashlib
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos
from ClaseAlquileres import Alquiler
import pandas as pd
import Utilities as util
from claseEmpresa import Empresa

'''Se crea la clase Personas'''
class Personas:
    
    
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña):
        """Iniciador de la clase Personas

        Args:
            dni (str): documento nacional de identidad de la persona (identificación)
            nombre (str): nombre de la perdona
            apellido (str): apellido de la persona
            fecnac (datetime): fecha de nacimiento de la persona
            email (str): email de la persona
            contraseñia (str): contraseña del perfil creado por la  persona
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


    
    def cambiar_dato(self, identificador, atributo, valor_nuevo):
        """Funcion para cambiar un atributo de la Persona. Se ingresa por parámetro que atributo se va a modificar(validado)
        y que valor se le dara a este atributo. A su vez, se pasaa por parámetro el identificador ya que mientras que
        en persona se trabaja con dni como clave, en empleados con legajos. De esta manera permite la herencia y eficientización
        de código. Aclaraciones extras: 1- Al cambiar el dni, se debe reemplazar el valor anterior por el nuevo en el set
        2- Al cambiar la contraseña se debe hacer lo mismo, solo que en este caso la que se reemplaza es la tupla dni:contraseña

        Args:
            identificador (str): identificado de la persona que quiere cambiar un dato suyo (dni)
            atributo (str): atributo que la persona quiera modificar
            valor_nuevo (str): valor nuevo que la persona quiera darle al atributo
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

    
    def __init__(self,dni, nombre, apellido, fecnac, email, contraseña,username, cantreservas=0):
        """Iniciador de la clase Usuarios, en el mismo se agrega desde el constructor el objeto al diccionario
        de la clase. A su vez se carga el set de la clase para facilitar las validaciones. 
        Notar que setdnis contiene un conjunto de tuplas, donde cada tupla almacena un par dni,contraseña. Se utiliza
        esta estructura de datos al ser las mismas hasheables e irrepetibles por el dni. Notar también que su mayor implementacion
        será en validaciones de login, con lo cual no es lo frecuente ir modificando el valor de las tuplas, adecuandose
        al caso. 
        Por otra parte, la eleccion de sets se adecua a la funcion de validacion por su rapidez y bajo costo de computo.

        Args:
            dni (str): documento nacional de identidad de la persona (identificación)
            nombre (str): nombre de la perdona
            apellido (str): apellido de la persona
            fecnac (datetime): fecha de nacimiento de la persona
            email (str): email de la persona
            contraseñia (str): contraseña del perfil creado por la  persona
            username (str): nombre de usuario elegido por la persona
            cantreservas (int): cantidad total de reservas realizadas por el usuario
        """
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.username = username
        self.cantreservas = int(cantreservas)
        Usuarios.setdnis.add((self.dni,self.contraseña)) 
        Usuarios.diccUsuarios[self.dni]=self
    

    
    def agregarUsuario(dni, username, nombre, apellido, fecnac, email, contraseña):
        """Funcion para crear un usuario. Se pasa por parámetro la contraseña hasheada. Como el usuario interactua con la
        interfaz por su cuenta, el mismo puede agregarse como usuario.  

        Args:
            dni (str): documento nacional de identidad de la persona (identificación)
            username (str): nombre de usuario elegido por la persona
            nombre (str): nombre de la perdona
            apellido (str): apellido de la persona
            fecnac (datetime): fecha de nacimiento de la persona
            email (str): email de la persona
            contraseñia (str): contraseña del perfil creado por la  persona
        """
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()  
        Usuarios(dni, nombre, apellido, fecnac, email, contraHasheada, username)
    

    
    def agregarReserva(self, patente_auto, fechaInicio, fechaFin):
        """Funcion para agregar una reserva al diccionario de reservas. Al instanciar el objeto reservas, ella sola se agrega
        al dicionario correspondiente

        Args:
            patente_auto (str): patente del auto asociada a la reserva
            fechaInicio (datetime): fecha de inicio de la reserva
            fechaFin (datetime): fecha de finalización de la reserva
        """
        Reserva(Reserva.cantReservas+1, self.dni, patente_auto, fechaInicio, fechaFin)
        self.cantreservas+=1  
        print(f'La reserva de id {Reserva.cantReservas}, hecha por el usuario de dni {self.dni} para el vehículo de patente {patente_auto}, inicia el {fechaInicio} y finaliza el {fechaFin}')


        
    def cancelarReserva(self,idreserva):
        """Funcion para eliminar una reserva del diccionario

        Args:
            idreserva (int): número de identificacion de la reserva
        """
        Reserva.diccReservas[idreserva].cancelarreserva()


    '''Funciones para modificar las fechas de la reserva. Las fechas se pasan ya validadas'''
    def modifFecInicioReserva(self,idreserva,fechanueva):
        """Funcion para modificar la fecha de inicio de una reserva

        Args:
            idreserva (int): número de identificacion de la reserva
            fechanueva (datetime): nueva fecha de inicio de alquiler
        """
        Reserva.diccReservas[idreserva].cambiarfechaInicioAlquiler(fechanueva)

    def modifFecFinReserva(self,idreserva,fechanueva):
        """Funcion para modificar la fecha de fin de una reserva

        Args:
            idreserva (int): número de identificacion de la reserva
            fechanueva (datetime): nueva fecha de fin de alquiler
        """
        Reserva.diccReservas[idreserva].cambiarfechaExpiracionAlquiler(fechanueva)


    
    def mostrarMisReservas(self):
        """Funcion para mostrar las reservas a nombre de un usuario

        Returns:
            Reservas a nombre de un usuario
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
    
    
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña, legajo = None):
        """Iniciador de la clase Administrador. La explicacion para las estructuras elegidas para los sets son análogas
        a las de la clase usuarios. Se trabaja con legajo como clave identificatoria al ser más representativa y tambien unica. 

        Args:
            dni (str): número de documento 
            nombre (str): nombre de la persona
            apellido (str): apellido de la persona
            fecnac (datetime): fecha de nacimiento de la persona
            email (str): email de la persona
            contraseña (str): contraseña del usuario
            legajo (int): número de empleado (identifiación)
        """
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.legajo= Administrador.cantempleadosAcumulativo
        Administrador.cantempleadosAcumulativo+=1       
        Administrador.setlegajos.add((str(self.legajo),self.contraseña))
        Administrador.setdnis.add(self.dni)
        Administrador.diccEmpleados[self.legajo]=self


    
    def agregarEmpleado(self, dni, nombre, apellido, fecnac, email, contraseña):
        """Funcion para agregar empleado a diccionario para su carga a csv de empleados. Un empleado ya existente
        se encarga de agregar a otro nuevo. Esto presupone la existencia de al menos un empleado, lo cual se
        considero como base 

        Args:
            dni (str): número de documento 
            nombre (str): nombre de la persona
            apellido (str): apellido de la persona
            fecnac (datetime): fecha de nacimiento de la persona
            email (str): email de la persona
            contraseña (str): contraseña del usuario
        """
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()
        Administrador(dni, nombre, apellido, fecnac, email, contraHasheada)
    

    
    def agregarVehiculo(self, patente, modelo, marca, anio, tipo, gama):   
        """Funcion para agregar un vehiculo a diccionario para su carga al archivo Vehiculos. Al instanciar el objeto,
        el mismo se agrega en el diccionario

        Args:
            patente (str): patente del vehículo
            modelo (str): modelo del vehículo
            marca (str): marca del vehículo
            anio (str): año de fabricación del vehículo
            tipo (str): tipo de vehículo
            gama (str): gama del vehículo
        """   
        Vehiculos(patente, modelo, marca, anio, tipo, gama)
        print(f"Se ha agregado correctamente el vehículo de patente {patente}, modelo {modelo}, marca {marca}, anio {anio}, tipo {tipo}")



    def modificarVehiculo(self, patente, atributo, valor_nuevo):
        """Funcion para modificar un atributo de un vehiculo

        Args:
            patente (str): patente del vehículo al cual se le quiere hacer una modificación
            atributo (str): atributo del vehículo que se desea modificar
            valor_nuevo (str): valor nuevo para el atributo
        """
        Vehiculos.diccVehiculos[patente].modificar(atributo,valor_nuevo)


  
    def finalizarAlquiler(self, idalquiler):
        """Funcion para dar por finalizado un alquiler. Se modifica la disponibilidad en vehiculos

        Args:
            idalquiler (str): número de identificación del alquiler
        """
        Alquiler.diccAlquileres[idalquiler].finalizar()
        Vehiculos.diccVehiculos[Alquiler.diccAlquileres[idalquiler].patente_auto].devolver()


    '''Funcion para eliminar un vehículo'''
    def eliminarVehiculo(self, patente): 
                             
        Vehiculos.diccVehiculos[patente].eliminar()


    
    def modifPreciosAutos(self, tipo, gama, precionuevo):
        """Funcion para cambiar el precio de un auto segun gama y tipo. La modificacion se hace directamente en el csv
        con los precios por categoria y tipo. Se utiliza el dataframe de pandas ya que facilita el manejo de tablas con
        doble entrada

        Args:
            tipo (str): tipo de vehículo
            gama (str): gama del vehículo
            precionuevo (int): precio nuevo a aplicar la gama y tipo de vehículo indicados
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


    '''FUNCIONES DE GESTIÓN'''

    def consultarVentasXDia(self, dia):
        """Funcion para consultar las ventas por día

        Args:
            dia (datetime): día a consultar
        """
        Empresa.gestionVentasxdia(dia)
    

    
    def consultarVentasXMes(self, mes):
        """Funcion para consultar las ventas por mes

        Args:
            mes (str): mes a consultar
        """
        Empresa.gestionVentasxmes(mes)


'''Se instancian objetos de administrador, estos se cargan al diccionario de su clase por su cuenta'''
util.leerCsv('Empleados.csv', Administrador)
    


'''Pruebas de Funcionamiento'''
if __name__ == "__main__":
    pass

    
    

