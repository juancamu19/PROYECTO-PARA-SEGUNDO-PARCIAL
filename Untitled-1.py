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
dni1 = "44788302"
dni2 = 447883
print(validardni(dni1))
print(validardni(dni2))