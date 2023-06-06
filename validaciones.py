#ACA SE GENERAN TODAS LAS FUNCIONES DE VALIDACION
from datetime import datetime
from datetime import date
import string

def validarFecha(fecha):
    try:
        fecha = datetime.strptime(fecha,"%d-%m-%Y").date()
        if fecha.year > datetime.today().year:
            raise ValueError("El año ingresado es inválido, no hemos alcanzado ese año aún!")
        if fecha.year == datetime.today().year and fecha.month > datetime.today().month:
             raise ValueError("El mes ingresado es inválido, no hemos alcanzado esa fecha!")
        if fecha.year == datetime.today().year and fecha.month == datetime.today().month and fecha.day > datetime.today().day:
             raise ValueError("El día ingresado es inválido, no hemos alcanzado esa fecha!")
        
    except ValueError as error:
        print(f"Error: {error}")
        return False

    return True

def validarFechaNac(fecha):
    try:
        fecha_ing = datetime.strptime(fecha,"%d-%m-%Y").date()
        fecha_actual = date.today()
        if fecha_ing < fecha_actual:
             return True
        else:
             print('la fecha ingresada no es valida')
             return False
        
    except ValueError:
        print('el formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False


def validarAgregarFechaInicio(fechainicio):
    try:
        fecha_ing = datetime.strptime(fechainicio,"%d-%m-%Y").date()
        fechaactual=datetime.now()
        if (fecha_ing - fechaactual.date()).days >= 5:
             return True
        else:
             print('la fecha ingresada debe tener como mínimo una anticipación de 5 días')
             return False
    
    except ValueError:
        print('el formato de fecha ingresada es incorrecto, debe ser D-M-Y')
        return False


def validarModifFechaInicio(fechainicio, fechafin):
    try:
        fecha_ing = datetime.strptime(fechainicio,"%d-%m-%Y").date()
        fecha_fin = datetime.strptime(fechafin,"%d-%m-%Y").date()
        if fecha_ing >= date.today() and fecha_ing <= fecha_fin:  ##aca verifico ademas que la fecha de inicio sea menor que la de fin
             return True
        else:
             print('la fecha ingresada ya paso o es posterior a la fecha pactada de fin de alquiler')
             return False
        
    except ValueError:
        print('el formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False


def validarFechaFin(fechainicio, fechafin):
    try:
        if fechafin >= fechainicio:
            return True
        else:
            print('la fecha ingresada es menor que la de inicio de alquiler')
            return False
        
    except ValueError:
        print('el formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False


def validato(tipodato, validando):
    try:
        if type(validando)!= tipodato:
           raise TypeError("El tipo de dato es incorrecto")
    
    except TypeError as error:
        print(f"Error: {error}")
        return False

    return True


def validarusuario(usuario):
    usuario = str(usuario)
    try:
        if len(usuario) < 5 or len(usuario) > 20:
            print('el usuario no cumple con las condiciones de cantidad de caracteres')
            return False 
        
    except TypeError as error:
        print(f"Error: {error}")
        return False
    
    return True


def validardni(dni):
    dni = str(dni)

    try:
        if len(dni) < 7 or len(dni) > 8 or dni.isdigit() == False:
            raise ValueError("El dni ingresado es incorrecto, intente de nuevo")
         
    except ValueError as error:
        print(f"Error: {error}")
        return False
    
    except:
         print(f"Error")
    
    return True


def validarnombre(nombre):
    nombre = str(nombre)
    
    try:
         if (len(nombre) == 0 or (nombre.isalpha() or nombre.count(' ')>=0)) == False:
              raise ValueError("El nombre propio es incorrecto, intente de nuevo")
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True


def validaremail(mail):
    mail = str(mail)
    
    try:
         if len(mail) == 0 or mail.count("@") == 0:
              raise ValueError("El mail ingresado es incorrecto, intente de nuevo")
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True 


def validarcontraseña(contraseña):
    contraseña = str(contraseña)
    
    try:
         if len(contraseña) == 0:
              raise ValueError("La contraseña ingresada es incorrecta, intente de nuevo")
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True 


def valinumerospositivos(monto):
    monto = int(monto)
    
    try:
        if monto <= 0:
            raise ValueError("El monto ingresado es incorrecto, intente de nuevo")
    
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True


#fechas en datetime ojo
def validiffechas(fecha1,fecha2):
    try:  
        if fecha2>fecha1:
            raise ValueError("La fecha ingresada es incorrecta, intente de nuevo")
    
    except ValueError as error:
            print(f"Error: {error}")
            return False 

    return True   
                   

def valipatente(patente):
    patente = str(patente)
    
    try:
        if len(patente)==6:
            letras=patente[0:3]
            numeros=patente[3:]
            if letras in string.ascii_letters:  
                if numeros in string.digits:
                    pass
                else:
                    raise ValueError("La patente ingresada es incorrecta, intente de nuevo")
            else:
                    raise ValueError("La patente ingresada es incorrecta, intente de nuevo")    
        
        elif len(patente)==7:
            letras1 = patente[0:2]
            letras2 = patente[5:]
            numeros1 = patente[2:5]
            if letras1 and letras2 in string.ascii_letters:
                if numeros1 in string.digits:
                    pass
                else:
                    raise ValueError("La patente ingresada es incorrecta, intente de nuevo")
            else:
                    raise ValueError("La patente ingresada es incorrecta, intente de nuevo") 
        
        else:
            raise ValueError("La patente ingresada es incorrecta, intente de nuevo")
    
    except ValueError as error:
        print(f"Error: {error}")
        return False 
    
    return True









