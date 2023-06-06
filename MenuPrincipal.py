from datetime import datetime
from claseEmpresa import Empresa
import validaciones as val
import funcionescsv as funcsv
import string
from ClasePersonas import Personas
from ClaseAlquileres import Alquiler
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos

diccPersonas=funcsv.leerCsv('Personas.csv',Personas)
diccAlquileres=funcsv.leerCsv('Alquileres.csv',Alquiler)
diccReservas=funcsv.leerCsv('Reservas.csv',Reserva)
diccVehiculos=funcsv.leerCsv('Vehiculos.csv',Vehiculos)

for k in diccReservas.keys():
    if datetime.strptime(diccReservas[k].fechaInicio,"%d-%m-%Y").date()==datetime.now():
        Alquiler.aggAlquiler(k,diccReservas,diccAlquileres)


letras = string.ascii_letters


seguir_operando = "SI"


while seguir_operando == "SI":
    print('Operaciones que puede realizar:')
    print('')
    print('1. Registrarse')
    print('2. Ingresar')
    print('')
    print('3. Salir')
    print('')
    opcion_elegida = input('Ingrese el número de operación que desea realizar ')

    while opcion_elegida not in ['1','2','3']: 
        opcion_elegida = input("ingrese nuevamente la opcion: ")
        

    if opcion_elegida == "1":
        dni = input("Ingrese su dni (sólo números) ")

        while val.validardni(dni) == False:              
            print('Ingrese un dni válido')
            dni = input("Ingrese su dni (sólo números) ")

        while Personas.validarexistenciaDNI(dni)==True:
            print('el usuario ya esta registrado')
            dni = input("Ingrese su dni (sólo números) ")
                
        nombre = input("Ingrese su nombre ")

        while val.validarnombre(nombre) == False:
            print('Ingrese un nombre válido')
            nombre = input("Ingrese su nombre ")

        apellido = input("Ingrese su apellido ")

        while val.validarnombre(apellido) == False:
            print('Ingrese un apellido válido')
            apellido = input("Ingrese su apellido ")

        fecnac = input('Ingrese fecha de nacimiento de la forma D-M-YYYY ')

        while val.validarFechaNac(fecnac) == False:
            print('Ingrese una fecha válida')
            fecnac = input('Ingrese fecha de nacimiento de la forma D-M-YYYY ')
        fecnac = datetime.strptime(fecnac,"%d-%m-%Y").date()
                
        usuario= input("Ingrese su nombre de usuario (mínimo 5 caracteres, máximo 20) ")

        while val.validarusuario(usuario) == False:
            print('Ingrese un usuario válido')
            usuario= input('Ingrese un nombre de usuario')

        email = input("Ingrese su email ")

        while val.validaremail(email) == False:
            print('Ingrese un email válido')
            email = input("Ingrese su email ")

        contraseña = input('Ingrese su contraseña ')
        confirmar_contraseña = input('Confirmar contraseña ingresada ')

        while (val.validarcontraseña(contraseña) == False) or (contraseña != confirmar_contraseña):
            print('Ingrese una contraseña válida')
            contraseña = input("Ingrese su contraseña ")
            confirmar_contraseña = input('Confirmar contraseña ingresada ')


        Personas.aggCliente(dni, nombre, apellido, fecnac, email, contraseña, diccPersonas)       
            
    
    elif opcion_elegida == "2":
        validado = False
        volver_a_ingresar = "SI"

        while not validado and volver_a_ingresar == "SI":

            dnix = input("Ingrese su dni ")
            contraseñax = input("Ingrese su contraseña ")
            validado = Personas.validarexistenciaPersona(dnix,contraseñax,diccPersonas)
            
            if not validado:
                print("Su dni o contraseña son incorrectos")
                volver_a_ingresar = input("Desea volver a ingresar sus datos (SI o NO)? ").strip().upper()
                
            else:
                
                print("Si desea realizar una reserva ingrese 1")
                print("Si desea cambiar una fecha de reserva ingrese 2")
                print("Si desea cancelar una reserva ingrese 3")
                print("Si desea cambiar alguno de sus datos ingrese 5")
                print("Si desea salir ingrese 6")

                operacion = int(input("ingrese opcion"))

                while operacion not in [1,2,3,4,5]:
                    print('ingrese opcion valida')
                    operacion = int(input("ingrese opcion"))


                if operacion == 1:
                        
                    fechainicio = input('ingrese fecha inicio del alquiler de la forma D-M-YYYY')
                    

                    while val.validarAgregarFechaInicio(fechainicio) == False:
                        print('Ingrese una fecha válida')
                        fechainicio = input('Ingrese fecha de inicio de alquiler de la forma D-M-YYYY ')
                    fechainicio = datetime.strptime(fechainicio,"%d-%m-%Y").date()

                    fechafin = input('ingrese fecha fin del alquiler de la forma D-M-YYYY')
                    while val.validarFecha(fechafin) == False:
                        print('Ingrese una fecha válida')
                        fechafin = input('Ingrese fecha de la forma D-M-YYYY ')
                    fechafin = datetime.strptime(fechafin,"%d-%m-%Y").date()

                    while val.validarFechaFin(fechainicio,fechafin) == False: 
                        print('Ingrese una fecha válida')
                        fechafin = input('Ingrese fecha fin del alquiler de la forma D-M-YYYY ')
                    
                    auto = funcsv.asignarauto()
                    
                    if auto == None:
                        print('no hay auto disponible')
                    else: 
                            Reserva.aggReserva(dnix, auto, fechainicio, fechafin, diccReservas) ##funciona 
                            
                            

                elif operacion == 2:
                    print("si desea cambiar el inicio de su alquiler ingrese 1")
                    print("si desea cambiar la fecha de fin de su alquiler ingrese 2")
                    print("si desea cambiar ambos ingrese 3")

                    cambio = int(input("ingrese su operacion a realizar ").strip()) 
                        
                    while cambio not in [1,2,3]: #Valido que elija una operacion permitida
                        print('ingrese opcion valida')
                        cambio = int(input("ingrese su operacion a realizar "))
                    
                    validado = False
                            
                    while validado == False:
                        idres = input("ingrese el id de su reserva ")
                        validado= funcsv.validarReserva(idres)


                    if cambio == 1:
                                
                        Reserva.cambiarfechaInicioAlquiler(idres,diccReservas)


                    elif cambio == 2:

                        Reserva.cambiarfechaExpiracionAlquiler(idres,diccReservas)


                    elif cambio == 3:
                                                    
                        Reserva.cambiarfechaInicioAlquiler(idres,diccReservas)
                        Reserva.cambiarfechaExpiracionAlquiler(idres,diccReservas)

                            
                elif operacion == 3:
                    validado = False
                    while validado == False:
                        idres = input("ingrese el id de su reserva")
                        validado = funcsv.validarReserva(idres)
                    Reserva.cancelarreserva(idres,diccReservas)

                elif operacion == 4:
                    validado = False
                            
                    while validado == False:
                        idres = input("ingrese el id de su reserva ")
                        validado = funcsv.validarReserva(idres)
                    Empresa.aggAlquiler(idres)

                elif operacion == 5:
                    per.cambiar_dato()
                    
                elif operacion==6:
                    pass


    elif opcion_elegida == 3:
        print("Ingrese sus datos de DNI e Email")
        dni = input("Ingrese su dni (sólo números) ")
            
        while val.validardni(dni) == False:                
            print('Ingrese un dni válido')
            dni = input("Ingrese su dni (sólo números) ")

        while funcsv.validarexistenciaDNI(dni)==False:
            print('el usuario ya esta registrado')
            dni = input("Ingrese su dni (sólo números) ")
                

        email = input("Ingrese su email ")

        while val.validaremail(email) == False:
            print('Ingrese un email válido')
            email = input("Ingrese su email ")

        if funcsv.validarexistenciaDNI(dni)==True and funcsv.validarexistenciaemail(email)==True:    
            print("Usted ya se ha registrado, puede ingresar")
            
            Empresa.contaringresos(dni)

            print("Si desea cambiar sus datos, ingrese 1")
            print("Si desea realizar una reserva ingrese 2")

            operacion=input("ingrese su numero de operación deseada")

            if operacion==1:
                nombre=input("ingrese nombre")
                apellido=input("ingrese apellido")
                Empresa.cambiarDatosInv(dni,email,nombre,apellido)

            elif operacion==2:
                pass
            

        else:
            print("ingrese su nombre y apellido")
            nombre = input("Ingrese su nombre ")

            while val.validarnombre(nombre) == False:
                print('Ingrese un nombre válido')
                nombre = input("Ingrese su nombre ")

            apellido = input("Ingrese su apellido ")

            while val.validarnombre(apellido) == False:
                print('Ingrese un válido')
                apellido = input("Ingrese su apellido ")
        
            Empresa.aggInvitado(dni, nombre, apellido, email)


    elif opcion_elegida==4:
        break
        
    seguir_operando = input("Desea seguir operando (SI o NO)? ").strip().upper()
    if seguir_operando=='NO':
        funcsv.escribirCsv('Personas.csv',diccPersonas)
        funcsv.escribirCsv('Alquileres.csv',diccAlquileres)
        funcsv.escribirCsv('Reservas.csv',diccReservas)
        funcsv.escribirCsv('Vehiculos.csv',diccVehiculos)
