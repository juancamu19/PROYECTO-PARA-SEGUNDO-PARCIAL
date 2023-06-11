import hashlib
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos

class Personas:
    diccionario=dict()
    setdnis=set()
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecnac = fecnac
        self.email = email
        self.contraseña = contraseña     

    def __str__(self):
        return f"{self.nombre} {self.apellido} de dni {self.dni}, nació en la fecha {self.fecnac}, su email es {self.email}, y realizó {self.cantreservas} reservas hasta el momento"

    def objeto_a_lista(self):
        obj_list = []
        for attr, value in self.__dict__.items():
            obj_list.append(value)
        return obj_list  

    def validarexistenciaDNI(dni):
        if dni in Personas.setdnis:  
            return True          
        else:
            return False
   
    def cambiar_dato(self):
        print("1.DNI, 2.Nombre, 3.Apellido, 4.Fecha de Nacimiento, 5.Email, 6.Contraseña")
        opcion = input("Elija el número que se encuentra junto al dato que desea modificar: ")
        dato_nuevo = input("Ingrese su nuevo dato: ")
        dato_viejo = None

        if opcion == "1":
            dato_viejo = self.dni
            self.dni = dato_nuevo
            print("Su DNI ha sido modificado exitosamente de: ", dato_viejo," a: ", dato_nuevo)

        elif opcion == "2":
            dato_viejo = self.nombre
            self.nombre = dato_nuevo
            print("Su Nombre ha sido modificado exitosamente de: ", dato_viejo," a: ", dato_nuevo)

        elif opcion == "3":
            dato_viejo = self.apellido
            self.apellido = dato_nuevo
            print("Su Apellido ha sido modificado exitosamente de: ", dato_viejo," a: ", dato_nuevo)

        elif opcion == "4":
            dato_viejo = self.fecnac
            self.fecnac = dato_nuevo
            print("Su fecha de nacimiento ha sido modificado exitosamente de: ", dato_viejo," a: ", dato_nuevo)

        elif opcion == "5":
            dato_viejo = self.email
            self.email = dato_nuevo
            print("Su email ha sido modificado exitosamente de: ", dato_viejo," a: ", dato_nuevo)

        elif opcion == "6":
            dato_viejo = self.dni
            self.contraseña = dato_nuevo
            print("Su contraseña ha sido modificada exitosamente de: ", dato_viejo," a: ", dato_nuevo)


class Usuarios(Personas):
    def __init__(self,dni,username, nombre, apellido, fecnac, email, contraseña, cantreservas=0):
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        username = username
        cantreservas = cantreservas
        Usuarios.setdnis.add(self.dni) 
    def agregarCliente(dni,username, nombre, apellido, fecnac, email, contraseña):  
        contraseña = contraseña.encode('utf-8')
        hash_object = hashlib.sha256(contraseña)
        hashed_password = hash_object.hexdigest()
        Usuarios.diccionario[dni]= Personas(dni,username, nombre, apellido, fecnac, email, hashed_password)
    def agregarReserva(self,patente_auto, fechaInicio, fechaFin, diccres):
        diccres[Reserva.cantReservas + 1] = Reserva( Reserva.cantReservas + 1, self.dni, patente_auto, fechaInicio, fechaFin)  
        return f'La reserva de id {Reserva.cantReservas} , hecha por el usuario de dni {self.dni} para el vehículo de patente {patente_auto}, inicia el {fechaInicio} y finaliza el {fechaFin}'
        
    def cancelarReserva(self,idreserva,diccres):
        diccres[idreserva].cancelarreserva()

    def modifFecInicioReserva(self,idreserva,diccres):
        diccres[idreserva].cambiarfechaInicioAlquiler()

    def modifFecFinReserva(self,idreserva,diccres):
        diccres[idreserva].cambiarfechaExpiracionAlquiler()


class Administrador(Personas):
    def __init__(self,dni,legajo, nombre, apellido, fecnac, email, contraseña):
        super().__init__(dni, nombre, apellido, fecnac, email, contraseña)
        legajo=legajo        
        Administrador.setdnis.add(self.dni)
    def agregarVehiculo(self,patente, modelo, marca, anio,tipo,gama,dicc):        
        dicc[patente]= Vehiculos(patente, modelo, marca, anio, tipo,gama)

    def modificarVehiculo(self,patente,atributo,diccVehi):
        diccVehi[patente].modificar(atributo)

    def finalizarAlquiler(self,idalquiler,diccalq,diccVehi):
        diccalq[idalquiler].finalizar()
        diccVehi[diccalq[idalquiler].patente_auto].devolver()

    def eliminarVehiculo(self,patente,diccVehi):
        diccVehi[patente].eliminar(diccVehi)

    
    
# Pruebas de Funcionamiento
if __name__ == "__main__":
    Per1 = Usuarios(44788302,"user1", "Juan Cruz", "Varela", "28-04-2023", "jvarela@itba.eduar", "juancin",2)
    print(Per1.__dict__.items())
    
    

