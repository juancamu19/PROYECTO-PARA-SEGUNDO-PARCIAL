class Personas():
    registroPersonas = {}

    def __init__(self, dni, nombre, apellido, fecnac, email,contraseña):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecnac = fecnac
        self.email = email
        self.contraseña = contraseña
        self.cantreservas = 0 ##aca llevo registro de cuantas compras lleva e cliente. Es relevante tener este dato?
        
    def __str__(self):
        return(f"""{self.nombre} {self.apellido} de dni {self.dni}, nació en la fecha {self.fecnac}, 
        su email es {self.email} y realizó {self.cantreservas} reservas""")

