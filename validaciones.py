#ACA SE GENERAN TODAS LAS FUNCIONES DE VALIDACION
from datetime import datetime
from datetime import date
import string
import hashlib

def validarprecio(precio):
    try:
        if int(precio)<0:
            print('Precio debe ser positivo')
            return False
    
    except ValueError:
        print('ingrese un precio numérico')
        return False 

def validartipo(tipo):
    if tipo.strip().lower() not in ['sedan','pick-up','suv','deportivo']:
        return False
    else:
        return True

def validargama(gama):
    if gama.strip().lower() not in ['baja','media','alta']:
        return False
    else:
        return True
def validarmarca(marca):
     letrasYNumeros = set(string.ascii_letters + string.digits)
     if marca not in letrasYNumeros:
          return False
     else:
          return True
def validaranio(anio):
    try:
        if int(anio)<date.today().year:
            return True
        else:
            print('no hemos alcanzado ese año aún, registra el auto cuando llegue su momento')
            return False
    
    except ValueError:
        print('ingrese un año numérico')
        return False 
def validarmodelo(modelo):
    if modelo in string.ascii_letters:
        return True
    else:
        return False
def validaratributo(modelo):
    if modelo.strip().lower() not in ['patente','modelo','marca','año','tipo','gama']:
        return False
    else:
        return True
def validarexistenciaclave(clave,dicc):
     if clave in dicc.keys():
          return True
     else:
          return False         
     

def validarexistenciaPersona(identificador, contraseña_ingresada, dicc):
        for k in dicc.keys():
            if k == identificador: 
                contraseña_ingresada = contraseña_ingresada.encode('utf-8')
                hash_object = hashlib.sha256(contraseña_ingresada)
                hashed_password = hash_object.hexdigest()
                if dicc[k].contraseña == hashed_password:  
                    return True
       
            else:
                return False

def validarFecha(fecha): ##dar nombre mas significativo
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
             print('La fecha ingresada no es valida')
             return False
        
    except ValueError:
        print('El formato de fecha ingresa es incorrecto, debe ser D-M-Y')
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
        fechafin = datetime.strptime(fechafin,"%d-%m-%Y").date()
        if fechafin >= fechainicio:
            return True
        else:
            print('la fecha ingresada es menor que la de inicio de alquiler')
            return False
        
    except ValueError:
        print('el formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False


def validato(tipodato, validando):  ##este lo usamos??
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
    try:
        if nombre not in string.ascii_letters():
            print('Nombre inválido')
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True


def validaremail(mail):
    
    try:
         if len(mail) == 0 or mail.count("@") == 0:
            print("El mail ingresado es incorrecto, intente de nuevo")
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True 


def validarcontraseña(contraseña):
    contraseña = str(contraseña)
    
    try:
         if len(contraseña) < 5 or len(contraseña) > 20:
              raise ValueError("La contraseña ingresada es incorrecta, intente de nuevo")
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True 


#fechas en datetime ojo
def validiffechas(fecha1,fecha2): ## este lo usamos?
    try:  
        if fecha2>fecha1:
            raise ValueError("La fecha ingresada es incorrecta, intente de nuevo")
    
    except ValueError as error:
            print(f"Error: {error}")
            return False 

    return True   
                   

def validarpatente(patente):
    patente = str(patente)
    
    try:
        if len(patente)==6:
            letras=patente[0:3]
            numeros=patente[3:]
            if (not letras.isalpha()) or (not numeros.isdigit()):
                    raise ValueError("La patente ingresada es incorrecta, intente de nuevo")  
        
        elif len(patente)==7:
            letras1 = patente[0:2]
            letras2 = patente[5:]
            numeros1 = patente[2:5]
            if (not letras1.isalpha()) or (not letras2.isalpha()) or (not numeros1.isdigit()):
                    raise ValueError("La patente ingresada es incorrecta, intente de nuevo")
        
        else:
            raise ValueError("La patente ingresada es incorrecta, intente de nuevo")
    
    except ValueError as error:
        print(f"Error: {error}")
        return False 
    
    return True









