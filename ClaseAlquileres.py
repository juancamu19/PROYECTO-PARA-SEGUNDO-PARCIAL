from datetime import datetime
from ClaseVehiculos import Vehiculos
import Utilities as util
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos

'''Se crea la clase Alquiler'''
class Alquiler():
    cantAlquileres = 0 
    diccAlquileres=dict() 
    setAlquileres = set() 
    
    
    def __init__(self, id = None, idReserva = None, dni = None, patente_auto = None, fechaInicioAlq = None, fechaExpiracionAlq = None, fechadev = None, monto = None):
        """Iniciador de la clase Alquiler, en el mismo se agrega desde el constructor el objeto al diccionario
        de la clase. A su vez se carga el set de la clase para facilitar las validaciones

        Args:
            id (int): número de identificación del alquiler
            idReserva (int): número de identificación de la reserva
            dni (str): número de identificación de la persona
            patente_auto (str): patente del auto alquilado
            fechaInicioAlq (datetime): fecha de inicio del alquiler
            fechaExpiracionAlq (datetime): fecha de expiración del alquier.
            fechadev (datetime): fecha de devolución del vehículo
            monto (int): monto a pagar total del alquiler
        """
        self.id = id 
        self.idReserva = idReserva  
        self.dni = dni         
        self.patente_auto = patente_auto 
        self.fechaInicioAlq = fechaInicioAlq 
        self.fechaExpiracionAlq = fechaExpiracionAlq 
        self.fechadev = fechadev  
        self.monto = monto     
        Alquiler.cantAlquileres += 1
        Alquiler.setAlquileres.add(self.id)
        Alquiler.diccAlquileres[self.id]=self
    

    '''Funcion para dar por finalizado el alquiler. 
    Nota: Este método es necesario ya que no basta con establecer una fecha fin del alquiler. 
    Eventualmente, los usuarios pueden no respetar estos límites, con lo cual la disponibilidad del vehiculo usado
    no debe ser True una vez llegada esta fin'''
    def finalizar(self):
        self.fechadev = datetime.now()
        
    
    
    '''Método str para la clase'''
    def __str__(self):
        return ('{}-{}-{}-{}-{}'.format(self.id, self.fecha, self.dni, self.auto))
   

'''Función que ejecuta las instancias de la clase. Estas instancias se crean con la informacion del archivo csv
correspondiente, y son cargados al diccionario desde su constructor'''
util.leerCsv('Alquileres.csv', Alquiler)


'''Generacion automatica de un alquiler una vez llegada su fecha. Esta función se ejecuta independientemente. 
Vale la pena notar que al no dar la posibilidad de cancelar una reserva con menos de 5 dias de anticipacion con su 
fecha de inicio, el alquiler se ejecutara de todas maneras. Se crea la instancia con la información traída desde 
la reserva que se va a concretar en alquiler. Se actualiza tambien el estado de disponibildad del auto en uso. '''
for k in Reserva.diccReservas.keys():
    if datetime.strptime(Reserva.diccReservas[k].fechaInicio,"%d-%m-%Y").date()==datetime.now().date():
        fechafin=datetime.strptime(Reserva.diccReservas[k].fechaFin,"%d-%m-%Y").date()
        fechaactual=datetime.now()
        cantdias=(fechafin-fechaactual.date()).days
        for clave,v in Alquiler.diccAlquileres.items():
            if k!=v.idReserva:
                Alquiler(Alquiler.cantAlquileres+1,k,Reserva.diccReservas[k].dni,Reserva.diccReservas[k].patente_auto,Reserva.diccReservas[k].fechaInicio,Reserva.diccReservas[k].fechaFin,None,cantdias*(Vehiculos.diccVehiculos[Reserva.diccReservas[k].patente_auto].precioxdia))
                Vehiculos.diccVehiculos[Alquiler.diccAlquileres[Alquiler.cantAlquileres].patente_auto].disponible=False
        



# Pruebas de Funcionamiento
if __name__ == "__main__":
    pass