from datetime import datetime
import validaciones as val
import Utilities as util
from ClasePersonas import Administrador, Usuarios
from ClaseAlquileres import Alquiler
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos

''' se importan:
- validaciones: para validar los datos ingresados por teclado y pasados por parametro
utilities: para escribir los csv con la informacion actuaizada de los diccionarios
clases: se trabajara con sus diccionarios para asi poder acceder a los objetos y sus metodos'''

seguir_operando = "SI"
'''se verifica que los archivos existan en el directorio correcto. Sino, se informe a la persona'''

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


        '''Ingreso a las opciones de Usuario'''
        if opcion_elegida == '1':                                 
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

            '''Registro del Usuario (Persona)'''
            if opcion_elegida == "1":                              
                                                    
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
                while val.validarFechaNac(fecnac) == False:
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
                    
            

                '''Ingreso del Usuario (Persona)'''
            elif opcion_elegida == "2":                             
                
                dni_ingresado = input("Ingrese su dni ")
                contraseña_ingresada = input("Ingrese su contraseña ")

                while val.validarexistenciaPersona(dni_ingresado, contraseña_ingresada, Usuarios.setdnis) == False:
                    print("Alguno de los datos ingresados es incorrecto, intente nuevamente")
                    dni_ingresado = input("Ingrese su dni ")
                    contraseña_ingresada = input("Ingrese su contraseña ")

                print('')
                print("Ha ingresado:")
                print(Usuarios.diccUsuarios [dni_ingresado])
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

                    while operacion not in ['1','2','3','4','5','6']: 
                        opoperacion = input("Ingrese nuevamente la opcion: ")


                    '''Realizar una reserva'''
                    if operacion == "1":                        
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
                            Usuarios.diccUsuarios[dni_ingresado].agregarReserva(auto, fechainicio, fechafin)
                            print("Infromación detallada del vehículo: ", Vehiculos.diccVehiculos[auto])
                        
                                
                        '''Cambiar una fecha de reserva'''        
                    elif operacion == "2":                     

                        print('Operaciones que puede realizar:')
                        print('')
                        print('1. Cambiar el inicio de su alquiler')
                        print('2. Cambiar la fecha de fin de su alquiler')
                        print('')
                        cambio = input("Ingrese el número de operación que desea realizar")

                        while cambio not in ['1','2']: 
                            cambio = input("ingrese nuevamente la opcion: ")
                        print('Las reservas a su nombre son las siguientes')
                        print(Usuarios.diccUsuarios[dni_ingresado].mostrarMisReservas())

                        idres = input("Ingrese el id de su reserva ")
                        while val.validarexistenciaclave(idres, Reserva.setReservas) == False:
                            idres = input("Ingrese el id de su reserva ")
                        

                        '''Cambiar el incicio de la reserva'''
                        if cambio == '1':                
                            fechanueva = input('ingrese fecha de Inicio de alquiler de la forma D-M-YYYY')
                            while val.validarModifFechaInicio(fechanueva,Reserva.diccReservas[idres].fechaFin) == False:
                                fechanueva = input('Ingrese fecha de inicio del alquiler de la forma D-M-YYYY ')
                            
                            Usuarios.diccUsuarios[dni_ingresado].modifFecInicioReserva(idres,fechanueva)

                            
                            '''Cambiar el fin de la reserva'''
                        elif cambio == '2':               
                            fechanueva = input('ingrese fecha de expiración de alquiler de la forma D-M-YYYY')
                            while val.validarFechaFin(Reserva.diccReservas[idres].fechaInicio,fechanueva) == False:                    
                                fechanueva = input('Ingrese fecha fin del alquiler de la forma D-M-YYYY ')

                            Usuarios.diccUsuarios[dni_ingresado].modifFecFinReserva(idres,fechanueva)

                        

                        '''Cancelar una reserva'''
                    elif operacion == "3":                     
                        validado = False
                        idres = input("ingrese el id de su reserva ")
                        while val.validarexistenciaclave(idres,Reserva.setReservas) == False:
                            idres = input("ingrese el id de su reserva ")
                            
                        Usuarios.diccUsuarios[dni_ingresado].cancelarReserva(idres)

                            

                        '''Cambiar un dato del usuario'''
                    elif operacion == "4":                      
                        
                        atributo = input('Ingrese el atributo a cambiar (dni, nombre, apellido, fecnac, email, contraseña) ')
                        while val.validaratributoPersona(atributo)==False:
                            print('Escriba correctamente el atributo a modificar')
                            atributo = input('Ingrese el atributo a cambiar(dni, nombre, apellido, fecnac, email, constraseña) ')

                        valor = input('Ingrese el nuevo valor para el atributo a cambiar ')
                        while val.validarCambiarDatosPersona(atributo,valor) == False:
                            valor = input('Ingrese el nuevo valor para el atributo a cambiar')
                                
                        Usuarios.diccUsuarios[dni_ingresado].cambiar_dato(dni_ingresado,atributo,valor)



                        '''Eliminar un usuario (eliminarse a si mismo como usuario)'''
                    elif operacion == "5":                       
                        Usuarios.diccUsuarios[dni_ingresado].darDeBajaUsuario()



                        '''Salir'''
                    elif operacion == "6":                      
                        pass
                
                    
                    '''Valido que el usuario no se haya eliminado a si mismo para poder permitirle seguir realizando operaciones'''
                    if val.validarexistenciaclave(dni_ingresado,Usuarios.diccUsuarios) == True:
                        seguir_operando = input("Desea seguir operando como usuario (SI o NO)? ").strip().upper()
                        while seguir_operando not in ['SI','NO']: 
                            seguir_operando = input("No ha ingresado una opción válida. Desea seguir operando (SI o NO)? ").strip().upper()
                    
                    else: seguir_operando = "NO"



                '''Salir'''
            elif opcion_elegida == '3':                      
                pass

                    
        

        
        elif opcion_elegida == '2':                               
            print('')
            print("Ingrese sus datos como empleado")
            print('')
            
            validado = False
            volver_a_ingresar = "SI"

            while not validado and volver_a_ingresar == "SI":

                legajo = input("Ingrese su legajo ")
                contraseña_ingresada = input("Ingrese su contraseña ")
                
                '''Valido que el usuario como administrador ya se encuentre registrado'''
                validado = val.validarexistenciaPersona(legajo, contraseña_ingresada, Administrador.setlegajos)
                
                legajo=int(legajo)

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
                        print('8. Dar de baja a otro empleado')
                        print('9. Ejecutar tareas de gestión económica de la Empresa')
                        print('')
                        print('10. Salir')
                        print('')

                        opcion_elegida = input('Ingrese el número de operación que desea realizar ')

                        while opcion_elegida not in ['1','2','3','4','5','6','7','8','9','10']: 
                            opcion_elegida = input("Ingrese nuevamente la opcion ")
                        
                        
                        '''Registrar un empleado nuevo'''
                        if opcion_elegida == '1':                      

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
                            while val.validarFechaNac(fecnac) == False:
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


                        '''Agregar un vehículo'''
                        if opcion_elegida == "2":                       
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
                            

                        '''Modificar un vehículo'''
                        if opcion_elegida == "3":                       
                            patente = input('Ingrese la patente del vehículo al que le desea realizar modificaciones ')
                            while  val.validarexistenciaclave(patente,Vehiculos.setVehiculos) == False:
                                patente = input('Ingrese patente existente ')  

                            atributo = input('Ingrese atributo a cambiar (patente, modelo, marca, año, tipo, gama) ')
                            while  val.validaratributo(atributo) == False:
                                atributo = input('Ingrese un atributo válido para cambiar ')

                            valor_nuevo = input('Ingrese el valor del atributo a cambiar')
                            while val.validarCambiarDatosVehiculo(atributo, valor_nuevo) == False:
                                valor_nuevo = input('Ingrese el valor del atributo a cambiar nuevamente')
                                    
                            Administrador.diccEmpleados[legajo].modificarVehiculo(patente,atributo,valor_nuevo) 
                        
                        
                        '''Eliminar un vehículo'''
                        if opcion_elegida == "4":                       
                            patente = input('Ingrese patente')
                            while  val.validarexistenciaclave(patente,Vehiculos.setVehiculos) == False:
                                patente = input('Ingrese patente existente')
                                
                            Administrador.diccEmpleados[legajo].eliminarVehiculo(patente)                 


                        '''Finalizar un alquiler (reportar auto devuelto)'''
                        if opcion_elegida == "5":                        
                            idalquiler = input('Ingrese id del alquiler a finalizar ')
                            while  val.validarexistenciaId(idalquiler,Alquiler.diccAlquileres) == False:
                                idalquiler=input('Ingrese id del alquiler ')
                                
                            Administrador.diccEmpleados[legajo].finalizarAlquiler(idalquiler) 


                        '''Cambiar un dato del administrador'''
                        if opcion_elegida == "6":                       
                            atributo = input('Ingrese el atributo a cambiar (dni,nombre,apellido,fecnac,email,contraseña) ')
                            while val.validaratributoPersona(atributo)==False:
                                print('Escriba correctamente el atributo a modificar')
                                atributo = input('Ingrese el atributo a cambiar(dni,nombre,apellido,fecnac,email,constraseña)')
                            
                            valor_nuevo = input('Ingrese el nuevo valor para el atributo a cambiar')
                        
                            while val.validarCambiarDatosPersona(atributo,valor_nuevo)==False:
                                valor_nuevo=input('Ingrese el nuevo valor para el atributo a cambiar')

                            Administrador.diccEmpleados[legajo].cambiar_dato(legajo, atributo, valor_nuevo)


                        '''Modificar precio por dia de un vehiculo '''  
                        if opcion_elegida == "7":                               
                            tipo = input('Ingrese el tipo de auto ')
                            while  val.validartipo(tipo) == False:
                                tipo = input('Ingrese tipo de auto correcto ')
                            
                            gama = input('Ingrese la gama del auto ')
                            while val.validargama(gama) == False:
                                gama = input('Ingrese gama de auto correcta')
                                
                            precio_nuevo = input('Ingrese nuevo precio por dia para este tipo y gama de autos ')
                            while  val.validarprecio(precio_nuevo) == False:
                                precio_nuevo = input('Ingrese nuevo precio por dia para este tipo y gama de autos ') 

                            Administrador.diccEmpleados[legajo].modifPreciosAutos(tipo,gama,precio_nuevo)


                        '''Eliminar otro empleado/administrador. El set que se pasa por parametro contiene
                        unicamente los legajos de los empleados, donde cada legajo diferente es un elemento.'''
                        if opcion_elegida == '8':
                            legajoEliminar = input('Ingrese legajo del empleado que quiere eliminar ')
                            while  val.validarexistenciaclave(legajoEliminar,{tupla[0] for tupla in Administrador.setlegajos}) == False:
                                legajoEliminar = input('Ingrese legajo existente ') 
                            legajoEliminar=int(legajoEliminar)
                            Administrador.diccEmpleados[legajoEliminar].darDeBajaEmpleado()


                        '''Ejecutar tareas de gestión económica de la Empresa'''
                        if opcion_elegida == "9":                       
                            print('Operaciones que puede realizar:')
                            print('')
                            print('1. Consultar ventas en un dia de su interes')
                            print('2. Consultar ventas en un mes de su interes')
                            print('')
                            operacion = input("Ingrese el número de operación que desea realizar")

                            while operacion not in ['1','2']: 
                                operacion = input("ingrese nuevamente la opcion: ")
                            
                            '''Consultar ventas de un día en particular'''
                            if operacion == '1':
                                dia = input('Ingrese fecha a consultar ')
                                while val.validarFechaAConsultar(dia) == False:
                                    print('Ingrese una fecha válida')
                                    dia = input('Ingrese fecha a consultar')
                                Administrador.diccEmpleados[legajo].consultarVentasXDia(dia)

                                '''Consultar ventas de un mes en particular'''
                            elif operacion == '2':
                                mes = input('Ingrese mes a consultar ')
                                while val.validarMesAConsultar(mes) == False:
                                    print('Ingrese un mes válido')
                                    mes = input('Ingrese mes consultar')
                                Administrador.diccEmpleados[legajo].consultarVentasXMes(mes)

                                
                        '''Salir'''
                        if opcion_elegida == "10":                       
                            pass


                        seguir_operando = input("Desea seguir operando como administrador (SI o NO)? ").strip().upper()
                        while seguir_operando not in ['SI','NO']: 
                            seguir_operando = input("No ha ingresado una opción válida. Desea seguir operando (SI o NO)? ").strip().upper()
        




        
        elif opcion_elegida == "3":                          
            pass




        
        print('')
        seguir_operando = input("Desea seguir operando (SI o NO)? ").strip().upper()
        while seguir_operando not in ['SI','NO']: 
            seguir_operando = input("No ha ingresado una opción válida. Desea seguir operando (SI o NO)? ").strip().upper()
    
        
        '''Actualizo los archivos de: Empleados, Usuarios, Alquileres, Reservas y Vehiculos. Se cargan los 
        csv con la información actualizada de los diccionarios'''
        util.escribirCsv('Empleados.csv', Administrador.diccEmpleados)                     
        util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
        util.escribirCsv('Alquileres.csv', Alquiler.diccAlquileres)
        util.escribirCsv('Reservas.csv', Reserva.diccReservas)
        util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)

