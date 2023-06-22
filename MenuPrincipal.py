from datetime import datetime
import validaciones as val
import Utilities as util
from ClasePersonas import Administrador, Usuarios
from ClaseAlquileres import Alquiler
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos
seguir_operando = "SI"

# any(not dicc for dicc in[diccAlquileres,diccReservas,diccVehiculos,diccUsuarios,diccEmpleados])
if Alquiler.diccAlquileres==False or Reserva.diccReservas==False or Vehiculos.diccVehiculos==False or Usuarios.diccUsuarios==False or Administrador.diccEmpleados==False:
    print('Corrobore con el administrador que se encuentren todos los archivos necesarios en el directorio que corresponde')
    
else:    
    while seguir_operando == "SI":
        

        print('Bienvenido/a a NoVoyEnTren.com')
        print('')
        print('Elija el método de ingreso')
        print('')
        print('1. Ingresar/Registrarse como usuario')
        print('2. Ingresar como empleado')
        print('3. Salir')
        print('')

        opcion_elegida = input('Ingrese el número de operación que desea realizar ')
        while opcion_elegida not in ['1','2',"3"]: 
            opcion_elegida = input("Ingrese nuevamente la opcion: ")


        
        if opcion_elegida == '1':                                 #Ingreso a las opciones de Usuario
            print('')
            print('Operaciones que puede realizar:')
            print('')
            print('1. Registrarse')
            print('2. Ingresar')
            print('3. Salir')
            print('')
            
            opcion_elegida = input('Ingrese el número de operación que desea realizar ')
            while opcion_elegida not in ['1','2','3']: 
                opcion_elegida = input("Ingrese nuevamente la opcion: ")
            
            print('')

            if opcion_elegida == "1":                               #Registro del Usuario (Persona)
                                                    
                dni = input("Ingrese su dni (sólo números) ")
                while val.validardni(dni) == False:              
                    dni = input("Ingrese su dni (sólo números) ")
                while val.validarexistenciaclave(dni,Usuarios.setdnis) ==True:
                    print('El usuario ya esta registrado')
                    dni = input("Ingrese su dni (sólo números) ")
                
                nombre = input("Ingrese su nombre (el apellido se lo solicitaremos a continuación) ")
                while val.validarnombre(nombre) == False:
                    nombre = input("Ingrese su nombre ")

                apellido = input("Ingrese su apellido ")
                while val.validarnombre(apellido) == False:
                    apellido = input("Ingrese su apellido ")

                fecnac = input('Ingrese su fecha de nacimiento de la forma D-M-YYYY ')
                while val.validarFecha(fecnac) == False:
                    fecnac = input('Ingrese su fecha de nacimiento de la forma D-M-YYYY ')
                fecnac = datetime.strptime(fecnac,"%d-%m-%Y").date()
                        
                usuario = input("Ingrese su nombre de usuario (mínimo 5 caracteres, máximo 20) ")
                while val.validarusuario(usuario) == False:
                    usuario = input('Ingrese un nombre de usuario ')

                email = input("Ingrese su email ")
                while val.validaremail(email) == False:
                    email = input("Ingrese su email ")

                contraseña = input('Ingrese su contraseña (mínimo 5 caracteres, máximo 20) ')
                confirmar_contraseña = input('Confirmar contraseña ingresada ')
                while (val.validarcontraseña(contraseña) == False) or (contraseña != confirmar_contraseña):
                    contraseña = input("Ingrese su contraseña nuevamente")
                    confirmar_contraseña = input('Confirmar contraseña ingresada ')

                Usuarios.agregarUsuario(dni, usuario, nombre, apellido, fecnac, email, contraseña)    

                print('')
                print("Se ha registrado la siguiente información:")
                print(Usuarios.diccUsuarios [dni])    
                    
            

            elif opcion_elegida == "2":                             #Ingreso del Usuario (Persona)
                
                dnix = input("Ingrese su dni ")
                contraseñax = input("Ingrese su contraseña ")

                while val.validarexistenciaPersona(dnix, contraseñax, Usuarios.setdnis) == False:
                    print("Alguno de los datos ingresados es incorrecto, intente nuevamente")
                    dnix = input("Ingrese su dni ")
                    contraseñax = input("Ingrese su contraseña ")

                print('')
                print("Ha ingresado:")
                print(Usuarios.diccUsuarios [dnix])
                print('')
                
                seguir_operando = "SI"
                while seguir_operando == "SI":

                    print('Operaciones que puede realizar:')
                    print('')
                    print('1. Realizar una reserva')
                    print('2. Cambiar una fecha de reserva')
                    print('3. Cancelar una reserva')
                    print('4. Cambiar un dato de su usuario')
                    print('5. Darse de baja (eliminar usuario)')
                    print('')
                    print('6. Salir')
                    print('')

                    operacion = input("Ingrese el número de operación que desea realizar ")

                    while opcion_elegida not in ['1','2','3','4','5','6']: 
                        opcion_elegida = input("ingrese nuevamente la opcion: ")


                    if operacion == "1":                        #Realizar una reserva
                        fechainicio = input('Ingrese fecha inicio del alquiler de la forma D-M-YYYY (debe haber una anticipación mínima de 5 días) ')
                        while val.validarAgregarFechaInicio(fechainicio) == False:
                            print('Ingrese una fecha válida')
                            fechainicio = input('Ingrese fecha de inicio de alquiler de la forma D-M-YYYY ')

                        fechafin = input('ingrese fecha fin del alquiler de la forma D-M-YYYY ')
                        while val.validarFechaFin(fechainicio, fechafin) == False: 
                            print('Ingrese una fecha válida')
                            fechafin = input('Ingrese fecha fin del alquiler de la forma D-M-YYYY ')

                        tipo = input('Ingrese el tipo de auto que desea alquilar (sedan,pick-up,suv,deportivo) ')
                        while val.validartipo(tipo) == False: 
                            print('Ingrese un tipo válido (sedan,pick-up,suv,deportivo)')
                            tipo = input('Ingrese el tipo de auto que desea alquilar (sedan,pick-up,suv,deportivo) ')
                            
                        gama = input('Ingrese gama de auto(baja,media,alta) ')
                        while val.validargama(gama) == False: 
                            print('Ingrese una gama válida(baja,media,alta)')
                            gama = input('Ingrese gama de auto(baja,media,alta) ')
                        
                        auto = Vehiculos.asignarauto(fechainicio, fechafin, tipo, gama)
                        
                        if auto == None:
                            print('No hay auto disponible')
                        else: 
                            Usuarios.diccUsuarios[dnix].agregarReserva(auto, fechainicio, fechafin)
                            print("Infromación detallada del vehículo: ", Vehiculos.diccVehiculos[auto])
                        
                                
                                
                    elif operacion == "2":                     #Cambiar una fecha de reserva

                        print('Operaciones que puede realizar:')
                        print('')
                        print('1. Cambiar el inicio de su alquiler')
                        print('2. Cambiar la fecha de fin de su alquiler')
                        print('')
                        cambio = input("Ingrese el número de operación que desea realizar")

                        while cambio not in ['1','2']: 
                            opcion_elegida = input("ingrese nuevamente la opcion: ")
                        
                        
                        idres = input("Ingrese el id de su reserva ")
                        while val.validarexistenciaclave(idres, Reserva.setReservas) == False:
                            idres = input("Ingrese el id de su reserva ")
                    

                        if cambio == '1':                 #Cambiar el incicio de la reserva
                            fechanueva = input('ingrese fecha de Inicio de alquiler de la forma D-M-YYYY')
                            while val.validarModifFechaInicio(fechanueva,Reserva.diccReservas[idres].fechaFin) == False:
                                fechanueva = input('Ingrese fecha de inicio del alquiler de la forma D-M-YYYY ')
                            Usuarios.diccUsuarios[dnix].modifFecInicioReserva(idres,fechanueva)

                            
                        elif cambio == '2':               #Cambiar el fin de la reserva
                            fechanueva = input('ingrese fecha de expiración de alquiler de la forma D-M-YYYY')
                            while val.validarFechaFin(Reserva.diccReservas[idres].fechaInicio,fechanueva) == False:                    
                                fechanueva = input('Ingrese fecha fin del alquiler de la forma D-M-YYYY ')

                            Usuarios.diccUsuarios[dnix].modifFecFinReserva(idres,fechanueva)

                        
                                    
                    elif operacion == "3":                     #Cancelar una reserva
                        validado = False
                        idres = input("ingrese el id de su reserva ")
                        while val.validarexistenciaclave(idres,Reserva.setReservas) == False:
                            idres = input("ingrese el id de su reserva ")
                            
                        Usuarios.diccUsuarios[dnix].cancelarReserva(idres)

                            
                        
                    elif operacion == "4":                      #Cambiar un dato del usuario
                        
                        atributo = input('Ingrese el atributo a cambiar (dni, nombre, apellido, fecnac, email, contraseña) ')
                        while atributo.strip().lower() not in ['dni','nombre','apellido','fecnac','email','contraseña']:
                            print('Escriba correctamente el atributo a modificar')
                            atributo = input('Ingrese el atributo a cambiar(dni, nombre, apellido, fecnac, email, constraseña) ')

                        valor = input('Ingrese el nuevo valor para el atributo a cambiar ')
                        while val.validarCambiarDatosPersona(atributo,valor) == False:
                            valor = input('Ingrese el nuevo valor para el atributo a cambiar')
                                
                        Usuarios.diccUsuarios[dnix].cambiar_dato(dnix,atributo,valor)



                    elif operacion == "5":                       #Darse de baja
                        Usuarios.diccUsuarios[dnix].darDeBaja(dnix,Usuarios.diccUsuarios)



                    elif operacion == "6":                      #Salir
                        pass
                
                    
                    if val.validarexistenciaclave(dnix,Usuarios.diccUsuarios) == True:
                        seguir_operando = input("Desea seguir operando como usuario (SI o NO)? ").strip().upper()
                        while seguir_operando not in ['SI','NO']: 
                            seguir_operando = input("No ha ingresado una opción válida. Desea seguir operando (SI o NO)? ").strip().upper()
                    
                    else: seguir_operando = "NO"



            elif opcion_elegida == '3':                      #Salir
                pass

                    
        

        
        elif opcion_elegida == '2':                               #Ingreso a las opciones de Empleado
            print("Ingrese sus datos como empleado")
            print('')
            
            validado = False
            volver_a_ingresar = "SI"

            while not validado and volver_a_ingresar == "SI":

                legajo = input("Ingrese su legajo ")
                contraseñax = input("Ingrese su contraseña ")
                validado = val.validarexistenciaPersona(legajo, contraseñax, Administrador.setlegajos)
                
                if not validado:
                    print("Su legajo o contraseña son incorrectos")
                    volver_a_ingresar = input("Desea volver a ingresar sus datos (SI o NO)? ").strip().upper()
                
                else:
                    
                    seguir_operando = "SI"
                    while seguir_operando == "SI":

                        print('')
                        print('Empleado verificado correctamente')
                        print('')
                        print('Operaciones que puede realizar:')
                        print('')
                        print('1. Registrar un empleado nuevo')
                        print('2. Agregar un vehiculo')
                        print('3. Modificar un vehiculo')
                        print('4. Eliminar un vehiculo')
                        print('5. Finalizar un alquiler (reportar auto devuelto)')
                        print('6. Cambiar un dato suyo')
                        print('7. Modificar precio por dia de un vehiculo')
                        print('')
                        print('8. Salir')
                        print('')

                        opcion_elegida = input('Ingrese el número de operación que desea realizar ')

                        while opcion_elegida not in ['1','2','3','4','5','6','7','8']: 
                            opcion_elegida = input("Ingrese nuevamente la opcion ")
                        
                        
                        if opcion_elegida == '1':                      #Registrar un empleado nuevo

                            dni = input("Ingrese el dni del nuevo empleado(sólo números) ")
                            while val.validardni(dni) == False:              
                                dni = input("Ingrese el dni del nuevo empleado(sólo números) ")
                            while val.validarexistenciaclave(dni,Administrador.setdnis) == True:
                                print('el empleado ya esta registrado')
                                dni = input("Ingrese el dni del nuevo empleado(sólo números) ")            
                                    
                            nombre = input("Ingrese el nombre del nuevo empleado (el apellido se lo solicitaremos a continuación) ")
                            while val.validarnombre(nombre) == False:
                                nombre = input("Ingrese el nombre del nuevo empleado")

                            apellido = input("Ingrese el apellido del nuevo empleado")
                            while val.validarnombre(apellido) == False:
                                apellido = input("Ingrese el apellido del nuevo empleado")

                            fecnac = input('Ingrese la fecha de nacimiento de la forma D-M-YYYY ')
                            while val.validarFecha(fecnac) == False:
                                fecnac = input('Ingrese fecha de nacimiento de la forma D-M-YYYY ')
                            fecnac = datetime.strptime(fecnac,"%d-%m-%Y").date()

                            email = input("Ingrese el email ")
                            while val.validaremail(email) == False:
                                email = input("Ingrese el email ")

                            contraseña = input('Ingrese la contraseña (mínimo 5 caracteres, máximo 20) ')
                            confirmar_contraseña = input('Confirmar contraseña ingresada ')
                            while (val.validarcontraseña(contraseña) == False) or (contraseña != confirmar_contraseña):
                                contraseña = input("Ingrese la contraseña ")
                                confirmar_contraseña = input('Confirmar contraseña ingresada ')

                            Administrador.diccEmpleados[legajo].agregarEmpleado(dni, nombre, apellido, fecnac, email, contraseña)  


                        if opcion_elegida == "2":                       #Agregar un vehículo
                            patente = input('Ingrese la patente ')
                            while (val.validarpatente(patente) == False) or (val.validarexistenciaclave(patente,Vehiculos.setVehiculos) == True):
                                print('La patente ingresada se encuentra en un formato incorrecto, o ya se encuentra asociada a un vehículo')
                                patente = input('Ingrese la patente nuevamente ')
                                
                            modelo = input('Ingrese modelo ')
                            while val.validarmodelo(modelo) == False:
                                modelo = input('Ingrese el modelo nuevamente ')
                                
                            marca = input('Ingrese marca ')
                            while val.validarmarca(marca) == False:
                                marca = input('Ingrese la marca nuevamente ')
                                
                            anio = input('Ingrese anio ')
                            while  val.validaranio(anio) == False:
                                anio = input('Ingrese el anio nuevamente ')
                                
                            tipo = input('Ingrese tipo de auto (sedan, pick-up, suv, deportivo) ')
                            while  val.validartipo(tipo) == False:
                                tipo = input('Ingrese un tipo de auto válido ')
                                
                            gama = input('Ingrese gama de auto (alta, media o baja)')
                            while  val.validargama(gama) == False:
                                gama = input('Ingrese una gama válida de auto ')
                                
                            Administrador.diccEmpleados[legajo].agregarVehiculo(patente, modelo, marca, anio,tipo,gama)
                            print()
                            

                        if opcion_elegida == "3":                       #Modificar un vehículo
                            patente=input('Ingrese patente')
                            while  val.validarexistenciaclave(patente,Vehiculos.setVehiculos) == False:
                                patente=input('Ingrese patente existente')
                                    

                            atributo=input('Ingrese atributo a cambiar')

                            while  val.validaratributo(atributo) == False:
                                atributo=input('Ingrese atributo a cambiar')

                            valor=input('Ingrese el valor del atributo a cambiar')

                            while val.validarCambiarDatosVehiculo(atributo,valor)==False:
                                valor=input('Ingrese el valor del atributo a cambiar')
                                    
                            Administrador.diccEmpleados[legajo].modificarVehiculo(patente,atributo,valor) 
                        
                        
                        if opcion_elegida == "4":                       #Eliminar un vehículo
                            patente=input('Ingrese patente')
                            while  val.validarexistenciaclave(patente,Vehiculos.setVehiculos) == False:
                                patente=input('Ingrese patente existente')
                                
                            Administrador.diccEmpleados[legajo].eliminarVehiculo(patente)                 


                        if opcion_elegida == "5":                        #Finalizar un alquiler (reportar auto devuelto)
                            idalquiler = input('Ingrese id del alquiler ')
                            while  val.validarexistenciaId(idalquiler,Alquiler.diccAlquileres) == False:
                                idalquiler=input('Ingrese id del alquiler ')
                                
                            Administrador.diccEmpleados[legajo].finalizarAlquiler(idalquiler) 


                        if opcion_elegida == "6":                        #Cambiar un dato suyo
                            atributo = input('Ingrese el atributo a cambiar (dni,nombre,apellido,fecnac,email,contraseña)')
                            while atributo.strip().lower() not in ['dni','nombre','apellido','fecnac','email','contraseña']:
                                print('Escriba correctamente el atributo a modificar')
                                atributo = input('Ingrese el atributo a cambiar(dni,nombre,apellido,fecnac,email,constraseña)')
                            
                            valor=input('Ingrese el nuevo valor para el atributo a cambiar')
                        
                            while val.validarCambiarDatosPersona(atributo,valor)==False:
                                valor=input('Ingrese el nuevo valor para el atributo a cambiar')

                            Administrador.diccEmpleados[legajo].cambiar_dato(legajo,atributo,valor)


                        if opcion_elegida == "7":                        #Modificar precio por dia de un vehiculo       
                            tipo = input('Ingrese el tipo de auto ')
                            while  val.validartipo(tipo) == False:
                                tipo = input('Ingrese tipo de auto correcto ')
                            
                            gama = input('Ingrese la gama del auto ')
                            while val.validargama(gama) == False:
                                gama = input('Ingrese gama de auto correcta')
                                
                            precio = input('Ingrese nuevo precio por dia para este tipo y gama de autos ')
                            while  val.validarprecio(precio) == False:
                                precio = input('Ingrese nuevo precio por dia para este tipo y gama de autos ') 

                            Administrador.diccEmpleados[legajo].modifPreciosAutos(tipo,gama,precio)    


                        if opcion_elegida == "8":                        #Salir
                            pass


                        seguir_operando = input("Desea seguir operando como administrador (SI o NO)? ").strip().upper()
                        while seguir_operando not in ['SI','NO']: 
                            seguir_operando = input("No ha ingresado una opción válida. Desea seguir operando (SI o NO)? ").strip().upper()
        




        elif opcion_elegida == "3":                                #Salir
            pass

        
        print('')
        seguir_operando = input("Desea seguir operando (SI o NO)? ").strip().upper()
        while seguir_operando not in ['SI','NO']: 
            seguir_operando = input("No ha ingresado una opción válida. Desea seguir operando (SI o NO)? ").strip().upper()
    
        
        util.escribirCsv('Empleados.csv', Administrador.diccEmpleados)                     #Actualizo los csv
        util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
        util.escribirCsv('Alquileres.csv', Alquiler.diccAlquileres)
        util.escribirCsv('Reservas.csv', Reserva.diccReservas)
        util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)

