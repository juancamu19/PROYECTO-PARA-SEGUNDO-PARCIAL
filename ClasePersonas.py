import hashlib
from ClaseReservas import Reserva,diccReservas
from ClaseVehiculos import Vehiculos,diccVehiculos 
from ClaseAlquileres import diccAlquileres
import validaciones as val
import pandas as pd
import Utilities as util

class Personas:
    setdnis = set()

    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecnac = fecnac
        self.email = email
        self.contraseña=contraseña   

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, DNI: {self.dni}, Fecha de nacimiento: {self.fecnac}, Email: {self.email}, Cantidad de reservas realizadas hasta el momento: {self.cantreservas}"
    
    def validarexistenciaDNI(dni):
        if dni in Personas.setdnis:  
            return True          
        else:
            return False
        
    # def objeto_a_lista(self):
    #     obj_list = []
    #     for attr, value in self.__dict__.items():
    #         obj_list.append(value)
    #     return obj_list
   
    def cambiar_dato(self, atributo):
        match atributo:

            case 'dni':
                dniviejo = self.dni
                dninuevo = input('Ingrese su nuevo dni ')
                while validado == False:
                    dninuevo = input('Ingrese su nuevo dni ')
                    validado = val.validardni(dninuevo)
                self.dni = dninuevo
                print("Su DNI ha sido modificado exitosamente de: ", dniviejo," a: ", dninuevo)

            case 'nombre':
                nombreviejo = self.nombre
                nombrenuevo = input('Ingrese su nombre nuevo ')
                while validado == False:
                    nombrenuevo = input('Ingrese su nombre nuevo ')
                    validado = val.validarnombre(nombrenuevo)
                self.nombre = nombrenuevo
                print("Su Nombre ha sido modificado exitosamente de: ", nombreviejo," a: ", nombrenuevo)

            case 'apellido':
                apellidoviejo = self.apellido
                apellidonuevo = input('Ingrese su apellido nuevo ')
                while validado == False:
                    apellidonuevo=input('Ingrese su apellido nuevo ')
                    validado = val.validarnombre(apellidonuevo)
                self.apellido=apellidonuevo
                print("Su Apellido ha sido modificado exitosamente de: ", apellidoviejo," a: ", apellidonuevo)

            case 'fecnac':
                fecnacviejo = self.fecnac
                fecnacnuevo = input('Ingrese su nueva fecha de nacimiento ')
                while validado == False:
                    fecnacnuevo = input('Ingrese su nueva fecha de nacimiento ')
                    validado = val.validarFecha(fecnacnuevo)
                self.fecnac = fecnacnuevo
                print("Su fecha de nacimiento ha sido modificado exitosamente de: ", fecnacviejo," a: ", fecnacnuevo)

            case 'email':
                emailviejo=self.email
                emailnuevo=input('Ingrese su email nuevo ')
                while validado == False:
                    emailnuevo=input('Ingrese su email nuevo ')
                    validado = val.validaremail(emailnuevo)
                self.email = emailnuevo
                print("Su email ha sido modificado exitosamente de: ", emailviejo," a: ", emailnuevo)

            case 'contraseña':
                contraseñanuevo = input('Ingrese su contraseña nueva ')
                while validado == False:
                    contraseñanuevo = input('Ingrese su contraseña nueva ')
                    validado = val.validarcontraseña(contraseñanuevo)
                contraseñanuevo = contraseñanuevo.encode('utf-8')
                objetoHash = hashlib.sha256(contraseñanuevo)
                contraHasheada = objetoHash.hexdigest()
                self.contraseña = contraHasheada
                



class Usuarios(Personas):
    def __init__(self,dni, nombre, apellido, fecnac, email, contraseña,username, cantreservas=0):
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.username = username
        self.cantreservas = int(cantreservas)
        Usuarios.setdnis.add(self.dni) 
    
    def agregarUsuario(dni, username, nombre, apellido, fecnac, email, contraseña):
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()  
        diccUsuarios[dni]= Usuarios(dni, nombre, apellido, fecnac, email, contraHasheada, username)
    
    def agregarReserva(self,patente_auto, fechaInicio, fechaFin):
        diccReservas[Reserva.cantReservas + 1] = Reserva( Reserva.cantReservas+1, self.dni, patente_auto, fechaInicio, fechaFin)
        self.cantreservas+=1  
        return f'La reserva de id {Reserva.cantReservas} , hecha por el usuario de dni {self.dni} para el vehículo de patente {patente_auto}, inicia el {fechaInicio} y finaliza el {fechaFin}'
        
    def cancelarReserva(self,idreserva):
        diccReservas[idreserva].cancelarreserva()

    def modifFecInicioReserva(self,idreserva):
        diccReservas[idreserva].cambiarfechaInicioAlquiler()

    def modifFecFinReserva(self,idreserva):
        diccReservas[idreserva].cambiarfechaExpiracionAlquiler()




diccUsuarios = util.leerCsv('Usuarios.csv', Usuarios)




class Administrador(Personas):
    cantempleados = 0
    
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña, legajo = None):
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        self.legajo= Administrador.cantempleados
        Administrador.cantempleados+=1       
        Administrador.setdnis.add(self.dni)

    def agregarEmpleado(self,dni, nombre, apellido, fecnac, email, contraseña):
        contraseña = contraseña.encode('utf-8')
        objetoHash = hashlib.sha256(contraseña)
        contraHasheada = objetoHash.hexdigest()
        diccEmpleados [Administrador.cantempleados] = Administrador(dni, nombre, apellido, fecnac, email, contraHasheada)
    
    def agregarVehiculo(self, patente, modelo, marca, anio, tipo, gama):        
        diccVehiculos[patente]= Vehiculos(patente, modelo, marca, anio, tipo, gama)

    def modificarVehiculo(self, patente, atributo):
        diccVehiculos[patente].modificar(atributo)

    def finalizarAlquiler(self, idalquiler):
        diccAlquileres[idalquiler].finalizar()
        diccVehiculos[diccAlquileres[idalquiler].patente_auto].devolver()

    def eliminarVehiculo(self, patente):         
        diccVehiculos[patente].eliminar(diccVehiculos)

    def modifPreciosAutos(self,tipo,gama,precionuevo):
        df = pd.read_csv('PreciosVehiculos.csv', index_col=0)
        df.at[gama, tipo] = precionuevo
        df.to_csv('PreciosVehiculos.csv')


diccEmpleados = util.leerCsv('Empleados.csv', Administrador)
    
# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass

    
    

