from datetime import datetime
from claseEmpresa import Empresa
import validaciones as val
import Utilities as util
from ClasePersonas import Administrador, Usuarios, Personas,diccEmpleados,diccUsuarios
from ClaseAlquileres import Alquiler,diccAlquileres
from ClaseReservas import Reserva,diccReservas
from ClaseVehiculos import Vehiculos,diccVehiculos

seguir_operando = "SI"


while seguir_operando == "SI":
    
    print('Elija como quiere ingresar')
    print('')
    print('1. Ingresar como usuario')
    print('')
    print('2. Ingresar como empleado')
    opcion_elegida = input('Ingrese el número de operación que desea realizar ')
    while opcion_elegida not in ['1','2']: 
        opcion_elegida = input("ingrese nuevamente la opcion: ")

    if opcion_elegida=='1':    
        print('Operaciones que puede realizar:')
        print('')
        print('1. Registrarse')
        print('')
        print('2. Ingresar')
        print('')
        print('3. Salir')
        print('')
        

        opcion_elegida = input('Ingrese el número de operación que desea realizar ')

        while opcion_elegida not in ['1','2','3']: 
            opcion_elegida = input("ingrese nuevamente la opcion: ")
            

        if opcion_elegida == "1":                               #REGISTRO del Usuario (Persona)
            
            dni = input("Ingrese su dni (sólo números) ")
            while val.validardni(dni) == False:              
                dni = input("Ingrese su dni (sólo números) ")
            while Personas.validarexistenciaDNI(dni)==True:
                print('el usuario ya esta registrado')
                dni = input("Ingrese su dni (sólo números) ")
            
                    
            nombre = input("Ingrese su nombre (el apellido se lo solicitaremos a continuación) ")
            while val.validarnombre(nombre) == False:
                nombre = input("Ingrese su nombre ")

            apellido = input("Ingrese su apellido ")
            while val.validarnombre(apellido) == False:
                apellido = input("Ingrese su apellido ")

            fecnac = input('Ingrese fecha de nacimiento de la forma D-M-YYYY ')
            while val.validarFechaNac(fecnac) == False:
                fecnac = input('Ingrese fecha de nacimiento de la forma D-M-YYYY ')
            fecnac = datetime.strptime(fecnac,"%d-%m-%Y").date()
                    
            usuario= input("Ingrese su nombre de usuario (mínimo 5 caracteres, máximo 20) ")
            while val.validarusuario(usuario) == False:
                usuario= input('Ingrese un nombre de usuario ')

            email = input("Ingrese su email ")
            while val.validaremail(email) == False:
                email = input("Ingrese su email ")

            contraseña = input('Ingrese su contraseña (mínimo 5 caracteres, máximo 20) ')
            confirmar_contraseña = input('Confirmar contraseña ingresada ')
            while (val.validarcontraseña(contraseña) == False) or (contraseña != confirmar_contraseña):
                contraseña = input("Ingrese su contraseña ")
                confirmar_contraseña = input('Confirmar contraseña ingresada ')

            Usuarios.agregarUsuario(dni,usuario, nombre, apellido, fecnac, email, contraseña)    

            print("Se ha registrado la siguiente información:")
            print(diccUsuarios [dni])    
                
        

        elif opcion_elegida == "2":                             #INGRESO del Usuario (Persona)
            
            dnix = input("Ingrese su dni ")
            contraseñax = input("Ingrese su contraseña ")

            while val.validarexistenciaPersona(dnix, contraseñax, diccUsuarios)==False:

                dnix = input("Ingrese su dni ")
                contraseñax = input("Ingrese su contraseña ")
                
            print('Operaciones que puede realizar:')
            print('')
            print('1. Realizar una reserva')
            print('2. Cambiar una fecha de reserva')
            print('3. Cancelar una reserva')
            print('4. Cambiar un dato de su usuario')
            print('')
            print('5. Salir')

            operacion = input("Ingrese el número de operación que desea realizar")

            while opcion_elegida not in ['1','2','3','4','5']: 
                opcion_elegida = input("ingrese nuevamente la opcion: ")

            if operacion == "1":                        #Realizar una reserva
                    
                fechainicio = input('ingrese fecha inicio del alquiler de la forma D-M-YYYY (debe haber una anticipación mínima de 5 días)')
                while val.validarAgregarFechaInicio(fechainicio) == False:
                    print('Ingrese una fecha válida')
                    fechainicio = input('Ingrese fecha de inicio de alquiler de la forma D-M-YYYY ')

                fechafin = input('ingrese fecha fin del alquiler de la forma D-M-YYYY')

                while val.validarFechaFin(fechainicio,fechafin) == False: 
                    print('Ingrese una fecha válida')
                    fechafin = input('Ingrese fecha fin del alquiler de la forma D-M-YYYY ')

                tipo=input('Ingrese tipo de auto(sedan,pick-up,suv,deportivo)')
                while val.validartipo(tipo) == False: 
                    print('Ingrese un tipo válido(sedan,pick-up,suv,deportivo)')
                    
                gama=input('Ingrese gama de auto(baja,media,alta)')
                while val.validargama(gama) == False: 
                    print('Ingrese una gama válida(baja,media,alta)')
                
                auto = Vehiculos.asignarauto(fechainicio,fechafin,tipo,gama)
                
                if auto == None:
                    print('no hay auto disponible')
                else: 
                    diccUsuarios[dnix].agregarReserva(auto,fechainicio,fechafin) 
                
                
                        
                        
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
                while val.validarexistenciaId(idres,diccReservas) == False:
                    idres = input("Ingrese el id de su reserva ")
            

                
            
                if cambio == '1':
                            
                    diccUsuarios[dnix].modifFecInicioReserva(idres)

                    


                elif cambio == '2':

                    diccUsuarios[dnix].modifFecFinReserva(idres)

                    

                            
            elif operacion == "3":
                validado = False
                idres = input("ingrese el id de su reserva")
                while val.validarReserva(idres) == False:
                    idres = input("ingrese el id de su reserva")
                    
                diccUsuarios[dnix].cancelarReserva(idres)

                    

                
            elif operacion == "4":
                atributo=input('Ingrese el atributo a cambiar(dni,nombre,apellido,fecnac,email,constraseña)')
                while atributo.strip().lower() not in ['dni','nombre','apellido','fecnac','email','constraseña']:
                    print('escriba denuevo el atributo')
                    atributo=input('Ingrese el atributo a cambiar(dni,nombre,apellido,fecnac,email,constraseña)')
                diccUsuarios[dnix].cambiar_dato(atributo)

                    
            elif operacion == "5":
                pass

        elif opcion_elegida=='3':
            pass
            
        seguir_operando = input("Desea seguir operando (SI o NO)? ").strip().upper()
        
    
    elif opcion_elegida =='2':
        print('Operaciones que puede realizar:')
        print('')
        print('1. Registrar un empleado nuevo')
        print('')
        print('2. Ingresar como empleado')
        print('')
        print('3. Salir')
        print('')

        opcion_elegida = input('Ingrese el número de operación que desea realizar ')

        while opcion_elegida not in ['1','2','3']: 
            opcion_elegida = input("ingrese nuevamente la opcion: ")
            

        if opcion_elegida == "1":   

            legajo=input('Ingrese su legajo')
            contraseña=input('Ingrese su contraseña')
            while val.validarexistenciaPersona(legajo,contraseña,diccEmpleados) == False: 
                print('contraseña o legajo no válidos')             
                legajo = input("Ingrese su legajo ")
                contraseña=input('Ingrese una contraseña válida')

            print('Empleado verificado, a continuación ingrese los datos del nuevo empleado')
            
            dni = input("Ingrese el dni del nuevo empleado(sólo números) ")
            while val.validardni(dni) == False:              
                dni = input("Ingrese el dni del nuevo empleado(sólo números) ")
            while Personas.validarexistenciaDNI(dni)==True:
                print('el empleado ya esta registrado')
                dni = input("Ingrese el dni del nuevo empleado(sólo números) ")            
                    
            nombre = input("Ingrese el nombre del nuevo empleado(el apellido se lo solicitaremos a continuación) ")
            while val.validarnombre(nombre) == False:
                nombre = input("Ingrese el nombre del nuevo empleado")

            apellido = input("Ingrese el apellido del nuevo empleado")
            while val.validarnombre(apellido) == False:
                apellido = input("Ingrese el apellido del nuevo empleado")

            fecnac = input('Ingrese fecha de nacimiento de la forma D-M-YYYY ')
            while val.validarFechaNac(fecnac) == False:
                fecnac = input('Ingrese fecha de nacimiento de la forma D-M-YYYY ')
            fecnac = datetime.strptime(fecnac,"%d-%m-%Y").date()

            email = input("Ingrese su email ")
            while val.validaremail(email) == False:
                email = input("Ingrese su email ")

            contraseña = input('Ingrese su contraseña (mínimo 5 caracteres, máximo 20) ')
            confirmar_contraseña = input('Confirmar contraseña ingresada ')
            while (val.validarcontraseña(contraseña) == False) or (contraseña != confirmar_contraseña):
                contraseña = input("Ingrese su contraseña ")
                confirmar_contraseña = input('Confirmar contraseña ingresada ')

            diccEmpleados[legajo].agregarEmpleado(dni, nombre, apellido, fecnac, email, contraseña)      
                
        elif opcion_elegida == "2":                        
            
            validado = False
            volver_a_ingresar = "SI"

            while not validado and volver_a_ingresar == "SI":

                legajo = input("Ingrese su legajo ")
                contraseñax = input("Ingrese su contraseña ")
                validado = val.validarexistenciaPersona(legajo, contraseñax, diccEmpleados)
                
                if not validado:
                    print("Su legajo o contraseña son incorrectos")
                    volver_a_ingresar = input("Desea volver a ingresar sus datos (SI o NO)? ").strip().upper()
                    
                else:
                    
                    print('Operaciones que puede realizar:')
                    print('')
                    print('1. Agregar un vehiculo')
                    print('2. Modificar un vehiculo')
                    print('3. Eliminar un vehiculo')
                    print('4. Finalizar un alquiler(reportar auto devuelto)')
                    print('5. Cambiar un dato suyo')
                    print('6. Modificar precio por dia de un vehiculo')
                    print('')
                    print('7. Salir')

                    operacion = input("Ingrese el número de operación que desea realizar")

                    while opcion_elegida not in ['1','2','3','4','5']: 
                        opcion_elegida = input("ingrese nuevamente la opcion: ")

                    if operacion == "1":                        
                        
                        patente=input('Ingrese patente')
                        while val.validarpatente(patente) == False:
                            patente=input('Ingrese patente')
                            
                        modelo=input('Ingrese modelo')
                        while val.validarmodelo(modelo) == False:
                            modelo=input('Ingrese modelo')
                            
                        marca=input('Ingrese marca')
                        while val.validarmarca(marca) == False:
                            marca=input('Ingrese marca')
                            
                        anio=input('Ingrese anio')
                        while  val.validaranio(anio) == False:
                            anio=input('Ingrese anio')
                            
                        tipo=input('Ingrese tipo de auto')
                        while  val.validartipo(tipo) == False:
                            tipo=input('Ingrese tipo de auto')
                            
                        gama=input('Ingrese gama de auto')
                        while  val.validargama(gama) == False:
                            gama=input('Ingrese gama de auto')
                           
                        diccEmpleados[legajo].agregarVehiculo(patente, modelo, marca, anio,tipo,gama)

                         
                                
                                
                    elif operacion == "2": 
                        patente=input('Ingrese patente')
                        while  val.validarpatente(patente) == False:
                            patente=input('Ingrese patente')
                               

                        atributo=input('Ingrese atributo a cambiar')
                        while  val.validaratributo(atributo) == False:
                            atributo=input('Ingrese atributo a cambiar')
                              
                        diccEmpleados[legajo].modificarVehiculo(patente,atributo) 
    
                    elif operacion == "3":
                        patente=input('Ingrese patente')
                        while  val.valipatente(patente) == False:
                            patente=input('Ingrese patente')
                            
                        diccEmpleados[legajo].eliminarVehiculo(patente)

                    
                    elif operacion == "4":
                        idalquiler=input('Ingrese id del alquiler')
                        while  val.validarexistenciaId(idalquiler,diccAlquileres) == False:
                            idalquiler=input('Ingrese id del alquiler')
                            
                        diccEmpleados[legajo].finalizarAlquiler(idalquiler)

                    elif operacion == "5":
                        atributo=input('Ingrese el atributo a cambiar(dni,nombre,apellido,fecnac,email,constraseña)')
                        while atributo.strip().lower() not in ['dni','nombre','apellido','fecnac','email','constraseña']:
                            print('escriba denuevo el atributo')
                            atributo=input('Ingrese el atributo a cambiar(dni,nombre,apellido,fecnac,email,constraseña)')
                        diccEmpleados[legajo].cambiar_dato(atributo)
                        

                    elif operacion == "6":
                        tipo=input('Ingrese tipo de auto')
                        while  val.validartipo(tipo) == False:
                            tipo=input('Ingrese tipo de auto')
                            validado = val.validartipo(tipo)
                        gama=input('Ingrese gama de auto')
                        while val.validargama(gama) == False:
                            gama=input('Ingrese gama de auto')
                            
                        precio=input('Ingrese nuevo precio por dia para este tipo y gama de autos')
                        while  val.validarprecio(precio) == False:
                            precio=input('Ingrese nuevo precio por dia para este tipo y gama de autos')
                            


                    elif operacion == "7":
                        pass

        elif opcion_elegida=='3':
            pass
            
        seguir_operando = input("Desea seguir operando (SI o NO)? ").strip().upper()
        while seguir_operando not in ['SI','NO']: 
            seguir_operando = input("Desea seguir operando (SI o NO)? ")
 
if seguir_operando=='NO':
    util.escribirCsv('Empleados.csv',diccEmpleados)
    util.escribirCsv('Usuarios.csv',diccUsuarios)
    util.escribirCsv('Empleados.csv',diccEmpleados)
    util.escribirCsv('Alquileres.csv',diccAlquileres)
    util.escribirCsv('Reservas.csv',diccReservas)
    util.escribirCsv('Vehiculos.csv',diccVehiculos)

