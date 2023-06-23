from datetime import datetime
from datetime import date
import hashlib

'''Valido que el precio ingresado sea positivo'''
def validarprecio(precio_vehiculo): 
           
    try:
        if int(precio_vehiculo)<0:
            print('El precio debe ser mayor que cero')
            return False
    
    except ValueError:
        print('Ingrese un precio válido')
        return False 


'''Valido que el tipo de auto sea uno de los que tenemos en nuestro sistema'''
def validartipo(tipo_vehiculo): 
            
    if tipo_vehiculo.strip().lower() not in ['sedan','pick-up','suv','deportivo']:
        return False
    else:
        return True


'''Valido que la gama del auto sea una de los que tenemos en nuestro sistema'''
def validargama(gama_vehiculo):  
         
    if gama_vehiculo.strip().lower() not in ['baja','media','alta']:
        return False
    else:
        return True


'''Valido que no se ingrese un nombre de marca con números'''
def validarmarca(marca_vehiculo):  
          
    try:
        marca_vehiculo = marca_vehiculo.replace(' ','')
        if not marca_vehiculo.isalpha():
            print('Nombre inválido')
            return False
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True


'''Valido que el modelo sólo contenga caracteres alfanuméricos o espacios'''
def validarmodelo(modelo_vehiculo):      
    try:
        modelo_vehiculo = modelo_vehiculo.replace(' ','')
        if not modelo_vehiculo.isalnum():
            print('Nombre inválido')
            return False
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True



def validaranio(anio_ingresado): 
    '''Valido que el año ingresado no sea del futuro. devuelve bool'''        
    try:
        if int(anio_ingresado) <= date.today().year:
            return True
        else:
            print('No hemos alcanzado ese año aún, registra el auto cuando llegue su momento')
            return False
    
    except ValueError:
        print('Ingrese un año numérico')
        return False 



def validaratributoVehiculo(atributo_vehiculo): 
    """ Se ingresa por parametro el atributo a cambiar, y se valida que sea uno de los attr de vehiculos"""   
    if atributo_vehiculo.strip().lower() not in ['patente','modelo','marca','año','tipo','gama']:
        return False
    else:
        return True
def validaratributoPersona(atributo_persona):  
    """ Se ingresa por parametro el atributo a cambiar, y se valida que sea uno de los attr de personas"""  
    if atributo_persona.strip().lower() not in ['dni','nombre','apellido','fecnac','email','contraseña']:
        return False
    else:
        return True


'''Valido que la clave de un diccionario exista en el set de claves asociado al mismo. devuelve bool'''
def validarexistenciaclave(clave, set): 
                 
    if clave in set:
        return True
    else:
        return False         
     

'''Valido que la persona se encuentre registrada. El set pasado por parametro es o bien setdnis de usuarios, o setlegajos de
administrador. Ambos son conjuntos de tuplas, conteniendo el identificador(dni o legajo) y la contraseña hasheada en cada una de ellas. '''
def validarexistenciaPersona(identificador, contraseña_ingresada, set):
        
    contraseña_ingresada = contraseña_ingresada.encode('utf-8')
    objetoHash = hashlib.sha256(contraseña_ingresada)
    contraHasheada = objetoHash.hexdigest()
    if (identificador, contraHasheada) in set:  
        return True
    else:
        return False
    

def validarFechaNac(fecha): 
    """Valido que la fecha de nacmiento de una persona sea previa a la del presente

        Returns:
            bool: True si la fecha intresada es menor que la actual, False caso contrario
        """            
    try:
        
        fecha_ingresada = datetime.strptime(fecha, "%d-%m-%Y").date()
        fecha_actual = date.today()
        if fecha_ingresada < fecha_actual:
             return True
        else:
             print('La fecha ingresada no es valida')
             return False
        
    except ValueError:
        print('El formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False



def validarFechaAConsultar(fecha):
    """Valido que la fecha a consultar para gestion economica se encuentre en el formato correcto

    Args:
        fecha (str): fecha ingresada por el usuario

    Returns:
        bool: True si el formato de la fecha es "D-M-Y", Flase caso contrario
    """
    try:
        fecha_ing = datetime.strptime(fecha, "%d-%m-%Y").date()
        return True
        
    except ValueError:
        print('El formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False



def validarMesAConsultar(mes):
    """Valido que el mes a consultar para gestion economica sea uno de los 12 del año'''

    Args:
        mes (str): mes ingresado por el administrador

    Returns:
        bool: True si el mes es uno de los 12 del año, Flase caso contrario
    """
    try:
        if int(mes)<=12 and int(mes)>=1:
            return True
        
    except ValueError:
        print('El mes es incorrecto')
        return False


'''Valido que la fecha de inicio de la reserva sea posterior a 5 días desde el presente'''
def validarAgregarFechaInicio(fechainicio): 
    """ se ingresa fecinicio y se valida que difiere en al menos 5 dias con la fecha actual. devuelve bool"""    
    try:
        fecha_ingresada = datetime.strptime(fechainicio,"%d-%m-%Y").date()
        fecha_actual = datetime.now().date()
        if (fecha_ingresada - fecha_actual).days >= 0:
             return True
        else:
             print('La fecha ingresada debe tener como mínimo una anticipación de 5 días')
             return False
    
    except ValueError:
        print('El formato de fecha ingresada es incorrecto, debe ser D-M-Y')
        return False


'''Valido que la modificación de la fecha de inicio del alquiler pertenezca al futuro y sea previa a la fecha de fin del mismo'''
def validarModifFechaInicio(fechainicio, fechafin):
    """ Se valida modificar fecinicio, se pasa por paramettro esta y fecfin. Se valida que la fecinicio difiere en 
    mas de 5 dias con la actual y que sea anterior a la fecfin. Devuelve bool"""    
    try:
        fecha_ingresada = datetime.strptime(fechainicio,"%d-%m-%Y").date()
        fecha_fin = datetime.strptime(fechafin,"%d-%m-%Y").date()
        fecha_actual = datetime.now().date()
        if (fecha_ingresada - fecha_actual).days >= 5 and fecha_ingresada <= fecha_fin:  
             return True
        else:
             print('la fecha ingresada no cumple con los 5 dias de anticipación o es posterior a la fecha pactada de fin de alquiler')
             return False
        
    except ValueError:
        print('el formato de fecha ingresa es incorrecto, debe ser D-M-Y')
        return False


'''Valido que la fecha de fin de alquiler sea posterior a la fecha de inicio de alquiler'''
def validarFechaFin(fechainicio, fechafin): 
    """ Se ingresa por parametro una fechainicio y fechafin. Se valida que la fechafin sea posterior a la de ininico"""       
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


'''Valido que el largo del nombre de usuario sea mayor o igual que 5 caracteres, pero menor o igual que 20'''
def validarusuario(usuario): 
    """ impone reestricciones minimas para el nombre de usuario y devuelve True si lo cumple"""        
    usuario = str(usuario).strip()
    try:
        if len(usuario) < 5 or len(usuario) > 20:
            print('El nombre de usuario no cumple con las condiciones de cantidad de caracteres')
            return False 
        
    except TypeError as error:
        print(f"Error: {error}")
        return False
    
    return True


'''Valido que el dni tenga entre 7 y 8 dígitos'''
def validardni(dni):
    """ se verifica que el dni este formado por digitos y extension adecuada. Devuelve True si asi lo es."""        
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


'''Valido que el nombre de la persona sólo contenga caracteres alfabéticos o espacios'''
def validarnombre(nombre): 
    """ Se verifia que el nombre este formado por letras"""    
    try:
        nombre = nombre.replace(' ','')
        if not nombre.isalpha():
            print('Nombre inválido')
            return False
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True


'''Valido que el mail no sea nulo y que contenga el "@"'''
def validaremail(mail):
    """ Verifica que el mail no sea nulo o no contenga @. Se devuelve True si pasa la validacion."""       
    try:
         if len(mail) == 0 or mail.count("@") == 0:
            print("El mail ingresado es incorrecto, intente de nuevo")
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True 


'''Valido que el largo de la contraseña sea mayor o igual que 5 caracteres, pero menor o igual que 20'''
def validarcontraseña(contraseña_ingresada):  
    """ se ingresa la contraseña y se verifica que cumpla con las conidicones minimas y maximas de extension.
    Devuelve True si contraseña tiene la extension adecuada."""         
    contraseña_ingresada = str(contraseña_ingresada)
    
    try:
         if len(contraseña_ingresada) < 5 or len(contraseña_ingresada) > 20:
            raise ValueError("La contraseña ingresada es incorrecta, intente de nuevo")
         
    except ValueError as error:
            print(f"Error: {error}")
            return False
    
    return True   
                   

'''Valido que la patente pueda ser una de las permitidas en Argentina'''
def validarpatente(patente): 
    """_summary_

    Args:
        patente (str): patente del auto a ingresar

    Returns:
        bool: True si patente esta validada
    """
        
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


'''Valido que el atributo que el usuario quiera cambiar de su perfil, cumpla los requerimientos propio de dicho atributo'''
def validarCambiarDatosPersona(atributo, valor_ingresado):
    """_summary_

    Args:
        atributo (string): atributo a cambiar
        valor_ingresado (string): nuevo valor para el attr

    Returns:
        bool: True si el valor esta validado
    """
    match atributo:

        case 'dni':
            return validardni(valor_ingresado)

        case 'nombre':
            return validarnombre(valor_ingresado)

        case 'apellido':
            return validarnombre(valor_ingresado)

        case 'fecnac':
            return validarFechaNac(valor_ingresado)

        case 'email':
            return validaremail(valor_ingresado)
        
        case 'contraseña':
            return validarcontraseña(valor_ingresado)  


'''Valido que el atributo que un administador quiera cambiar de un vehículo, cumpla los requerimientos propio de dicho atributo'''
def validarCambiarDatosVehiculo(atributo,valor_ingresado):
    """_summary_

    Args:
        atributo (string): atributo a cambiar
        valor_ingresado (string): nuevo valor para el attr

    Returns:
        bool: True si el valor esta validado
    """
    match atributo:
            
        case 'patente':
            return validarpatente(valor_ingresado) 
        
        case 'modelo' :
            return validarmodelo(valor_ingresado) 
        
        case 'marca' :
            return validarmarca(valor_ingresado)
        
        case 'año':
            return validaranio(valor_ingresado)
        
        case 'tipo' :
            return validartipo(valor_ingresado)
        
        case 'gama':
            return validargama(valor_ingresado)




if __name__=="__main__":
    pass







