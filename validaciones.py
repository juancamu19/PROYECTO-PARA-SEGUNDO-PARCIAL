from datetime import datetime
from datetime import date
import hashlib

def validarprecio(precio):        #Valido que el precio ingresado sea positivo
    try:
        if int(precio)<0:
            print('El precio debe ser positivo')
            return False
    
    except ValueError:
        print('Ingrese un precio válido')
        return False 


def validartipo(tipo):         #Valido que el tipo de auto sea uno de los que tenemos en nuestro sistema
    if tipo.strip().lower() not in ['sedan','pick-up','suv','deportivo']:
        return False
    else:
        return True


def validargama(gama):          #Valido que la gama del auto sea una de los que tenemos en nuestro sistema
    if gama.strip().lower() not in ['baja','media','alta']:
        return False
    else:
        return True


def validarmarca(marca):        #Valido que no se ingrese un nombre de marca con números
    try:
        marca = marca.replace(' ','')
        if not marca.isalpha():
            print('Nombre inválido')
            return False
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True


def validarmodelo(modelo):      #Valido que el modelo sólo contenga caracteres alfanuméricos o espacios
    try:
        modelo = modelo.replace(' ','')
        if not modelo.isalnum():
            print('Nombre inválido')
            return False
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True


def validaranio(anio):         #Valido que el año ingresado no sea del futuro
    try:
        if int(anio) <= date.today().year:
            return True
        else:
            print('No hemos alcanzado ese año aún, registra el auto cuando llegue su momento')
            return False
    
    except ValueError:
        print('Ingrese un año numérico')
        return False 


def validaratributo(atributo_vehiculo):     #Valido que el atributo que se quiera modificar sea uno de los definidos
    if atributo_vehiculo.strip().lower() not in ['patente','modelo','marca','año','tipo','gama']:
        return False
    else:
        return True


def validarexistenciaclave(clave, set):        #Valido que la clave de un diccionario exista en el mismo
     if clave in set:
          return True
     else:
          return False         
     

def validarexistenciaPersona(identificador, contraseña_ingresada, set):     #Valido que la persona se encuentre registrada 
    contraseña_ingresada = contraseña_ingresada.encode('utf-8')
    objetoHash = hashlib.sha256(contraseña_ingresada)
    contraHasheada = objetoHash.hexdigest()
    if (identificador, contraHasheada) in set:  
        return True
    else:
        return False
    



def validarFecha(fecha):              #Valido que la fecha de nacmiento de una persona sea previa a la del presente
    try:
        fecha_ing = datetime.strptime(fecha, "%d-%m-%Y").date()
        fecha_actual = date.today()
        if fecha_ing < fecha_actual:
             return True
        else:
             print('La fecha ingresada no es valida')
             return False
        
    except ValueError:
        print('El formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False


def validarAgregarFechaInicio(fechainicio):      #Valido que la fecha de inicio de la reserva sea posterior a 5 días desde el presente
    try:
        fecha_ing = datetime.strptime(fechainicio,"%d-%m-%Y").date()
        fechaactual = datetime.now()
        if (fecha_ing - fechaactual.date()).days >= 5:
             return True
        else:
             print('la fecha ingresada debe tener como mínimo una anticipación de 5 días')
             return False
    
    except ValueError:
        print('el formato de fecha ingresada es incorrecto, debe ser D-M-Y')
        return False


def validarModifFechaInicio(fechainicio, fechafin):     #Valido que la modificación de la fecha de inicio del alquiler pertenezca al futuro y sea previa a la fecha de fin del mismo
    try:
        fecha_ing = datetime.strptime(fechainicio,"%d-%m-%Y").date()
        fecha_fin = datetime.strptime(fechafin,"%d-%m-%Y").date()
        if fecha_ing >= date.today() and fecha_ing <= fecha_fin:  
             return True
        else:
             print('la fecha ingresada ya paso o es posterior a la fecha pactada de fin de alquiler')
             return False
        
    except ValueError:
        print('el formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False


def validarFechaFin(fechainicio, fechafin):         #Valido que la fecha de fin de alquiler sea posterior a la fecha de inicio de alquiler
    try:
        fechainicio = datetime.strptime(fechainicio,"%d-%m-%Y").date()
        fechafin = datetime.strptime(fechafin,"%d-%m-%Y").date()
        if fechafin >= fechainicio:
            return True
        else:
            print('La fecha ingresada es menor que la de inicio de alquiler')
            return False
        
    except ValueError:
        print('El formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False


def validarusuario(usuario):         #Valido que el largo del nombre de usuario sea mayor o igual que 5 caracteres, pero menor o igual que 20
    usuario = str(usuario).strip()
    try:
        if len(usuario) < 5 or len(usuario) > 20:
            print('El nombre de usuario no cumple con las condiciones de cantidad de caracteres')
            return False 
        
    except TypeError as error:
        print(f"Error: {error}")
        return False
    
    return True


def validardni(dni):         #Valido que el dni tenga entre 7 y 8 dígitos
    dni = str(dni).strip()
    try:
        if len(dni) < 7 or len(dni) > 8 or dni.isdigit() == False:
            raise ValueError("El dni ingresado es incorrecto, intente de nuevo")
            
         
    except ValueError as error:
        print(f"Error: {error}")
        return False
    
    except:
         print(f"Error")
    
    return True


def validarnombre(nombre):      #Valido que el nombre de la persona sólo contenga caracteres alfabéticos o espacios
    try:
        nombre = nombre.replace(' ','')
        if not nombre.isalpha():
            print('Nombre inválido')
            return False
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True


def validaremail(mail):       #Valido que el mail no sea nulo y que contenga el "@"
    try:
         if len(mail) == 0 or mail.count("@") == 0:
            print("El mail ingresado es incorrecto, intente de nuevo")
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True 


def validarcontraseña(contraseña):        #Valido que el largo de la contraseña sea mayor o igual que 5 caracteres, pero menor o igual que 20
    contraseña = str(contraseña)
    
    try:
         if len(contraseña) < 5 or len(contraseña) > 20:
              raise ValueError("La contraseña ingresada es incorrecta, intente de nuevo")
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True   
                   

def validarpatente(patente):      #Valido que la patente pueda ser una de las permitidas en Argentina
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

def validarCambiarDatosPersona(atributo,valor):
     match atributo:

        case 'dni':
            return validardni(valor)

        case 'nombre':
            return validarnombre(valor)

        case 'apellido':
            return validarnombre(valor)

        case 'fecnac':
            return validarFecha(valor)

        case 'email':
            return validaremail(valor)
        
        case 'contraseña':
            return validarcontraseña(valor)  
         
def validarCambiarDatosVehiculo(atributo,valor):
    match atributo:
            
        case 'patente':
            return validarpatente(valor) 
        
        case 'modelo' :
            return validarmodelo(valor) 
        
        case 'marca' :
            return validarmarca(valor)
        
        case 'año':
            return validaranio(valor)
        
        case 'tipo' :
            return validartipo(valor)
        
        case 'gama':
            return validargama(valor)
        
if __name__=="__main__":
    pass







