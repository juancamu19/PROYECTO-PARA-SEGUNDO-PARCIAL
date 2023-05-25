class Personas:
    setdnis=set()
    def __init__(self, dni, nombre, apellido, fecnac, email, contraseña):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecnac = fecnac
        self.email = email
        self.contraseña = contraseña
        self.cantreservas = 0
        Personas.setdnis.add(self.dni)  ### cuando se lea el csv, y se instancien los objetos en el diccionario, al instanciarlos se agregan los dnis al set

    def __str__(self):
        return f"""{self.nombre} {self.apellido} de dni {self.dni}, nació en la fecha {self.fecnac}, su email es {self.email}, su contraseña es {self.contraseña}, y realizó {self.cantreservas} reservas"""

    def contador_reservas(self):
        self.cantreservas += 1
    
    def aggCliente(dni, nombre, apellido, fecnac, email, contraseña,diccPersonas):  ##no lleva atributo self
         diccPersonas[dni]= Personas(dni, nombre, apellido, fecnac, email, contraseña)

    def cambiar_dato(self):
        print("1.DNI, 2.Nombre, 3.Apellido, 4.Fecha de Nacimiento, 5.Email, 6.Contraseña")
        opcion = input("Elija el número que se encuentra junto al dato que desea modificar: ")
        dato_nuevo = input("Ingrese su nuevo dato: ")
        dato_viejo = None

        if opcion == "1":
            dato_viejo = self.dni
            self.dni = dato_nuevo
            print("Su DNI ha sido modificado exitosamente de: ",dato_viejo," a: ",dato_nuevo)

        elif opcion == "2":
            dato_viejo = self.nombre
            self.nombre = dato_nuevo
            print("Su Nombre ha sido modificado exitosamente de: ",dato_viejo," a: ",dato_nuevo)

        elif opcion == "3":
            dato_viejo = self.apellido
            self.apellido = dato_nuevo
            print("Su Apellido ha sido modificado exitosamente de: ",dato_viejo," a: ",dato_nuevo)

        elif opcion == "4":
            dato_viejo = self.fecnac
            self.fecnac = dato_nuevo
            print("Su fecha de nacimiento ha sido modificado exitosamente de: ",dato_viejo," a: ",dato_nuevo)

        elif opcion == "5":
            dato_viejo = self.email
            self.email = dato_nuevo
            print("Su email ha sido modificado exitosamente de: ",dato_viejo," a: ",dato_nuevo)

        elif opcion == "6":
            dato_viejo = self.dni
            self.contraseña = dato_nuevo
            print("Su contraseña ha sido modificada exitosamente de: ",dato_viejo," a: ",dato_nuevo)


# Pruebas de Funcionamiento
if __name__ == "__main__":
    Per1 = Personas(44788302, "Juan Cruz", "Varela", "28-04-2023", "jvarela@itba.eduar", "juancin")
    dic = list(vars(Per1).values())
    print(dic)
