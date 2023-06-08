import hashlib
class Personas:
    setdnis = set()
    
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña, cantreservas = 0):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecnac = fecnac
        self.email = email
        self.contraseña = contraseña
        self.cantreservas = cantreservas
        Personas.setdnis.add(self.dni)  

    
    def __str__(self):
        return f"{self.nombre} {self.apellido} de dni {self.dni}, nació en la fecha {self.fecnac}, su email es {self.email}, y realizó {self.cantreservas} reservas hasta el momento"

    
    def contador_reservas(self):
        self.cantreservas += 1
    
    
    def objeto_a_lista(self):
        obj_list = []
        for attr, value in self.__dict__.items():
            obj_list.append(value)
        return obj_list
    
    
    def aggCliente(dni, nombre, apellido, fecnac, email, contraseña, diccPersonas):  
        contraseña = contraseña.encode('utf-8')
        hash_object = hashlib.sha256(contraseña)
        hashed_password = hash_object.hexdigest()

        diccPersonas[dni] = Personas(dni, nombre, apellido, fecnac, email, hashed_password)

    
    def validarexistenciaDNI(dni):
        if dni in Personas.setdnis:  
            return True          
        else:
            return False
        
    
    def validarexistenciaPersona(dni, contraseña_ingresada, dicc):
        for k in dicc.keys():
            if k == dni: 
                contraseña_ingresada = contraseña_ingresada.encode('utf-8')
                hash_object = hashlib.sha256(contraseña_ingresada)
                hashed_password = hash_object.hexdigest()
                if dicc[k].contraseña == hashed_password:  
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


# Pruebas de Funcionamiento
if __name__ == "__main__":
    Per1 = Personas(44788302, "Juan Cruz", "Varela", "28-04-2023", "jvarela@itba.eduar", "juancin",2)
    print(Per1.objeto_a_lista())
    

