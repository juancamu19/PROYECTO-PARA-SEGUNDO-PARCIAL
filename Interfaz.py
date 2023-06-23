import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QCalendarWidget, QComboBox, QDesktopWidget
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QColor
from PyQt5 import QtCore
from PyQt5.QtCore import Qt 

from datetime import datetime
from claseEmpresa import Empresa
import validaciones as val
import Utilities as util
from ClasePersonas import Administrador, Usuarios
from ClaseAlquileres import Alquiler
from ClaseReservas import Reserva
from ClaseVehiculos import Vehiculos


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inicio de Sesión')
        self.setMinimumSize(600, 600)
        self.center()

        # Create a central widget and a layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        # Create a welcome label
        welcome_label = QLabel('Bienvenido/a', self)
        welcome_label.setAlignment(Qt.AlignCenter)

        # Create labels
        label_dni = QLabel('DNI del usuario:', self)
        label_user = QLabel('Nombre de Usuario:', self)
        label_password = QLabel('Contraseña:', self)

        # Create input boxes
        input_dni = QLineEdit(self)
        self.input_dni = input_dni
        input_user = QLineEdit(self)
        self.input_user = input_user
        input_password = QLineEdit(self)
        self.input_password = input_password
        input_password.setEchoMode(QLineEdit.Password)

        # Create login button
        self.button_login = QPushButton('Ingresar', self)
        self.button_registro = QPushButton('No tenes cuenta? Registrate', self)
        self.button_admin = QPushButton('Ingresar como Administrador',self)

        # Create the error label (hidden by default)
        self.error_label = QLabel("El usuario, DNI o contraseña es incorrecto.", central_widget)
        self.error_label.setStyleSheet("color: red")
        self.error_label.hide()

        self.button_login.clicked.connect(self.openMainWindow)

        self.button_admin.clicked.connect(self.openLoginAdminWindow)

        self.button_registro.clicked.connect(self.openRegistroWindow)

        # Add widgets to the layout
        layout.addWidget(logo_label)
        layout.addWidget(welcome_label)
        layout.addWidget(label_dni)
        layout.addWidget(input_dni)
        layout.addWidget(label_user)
        layout.addWidget(input_user)
        layout.addWidget(label_password)
        layout.addWidget(input_password)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_registro)
        layout.addWidget(self.button_admin)
        layout.addWidget(self.error_label)

        # Set the central widget and apply the style sheet
        self.setCentralWidget(central_widget)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)

    def center(self):
        # Get the screen's geometry
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        # Calculate the center point
        center_point = screen_geometry.center()

        # Adjust the window position
        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def resizeEvent(self, event):
        # Center the objects when the window is resized
        super().resizeEvent(event)
        self.centerObjects()

    def centerObjects(self):
        # Center the objects in the window
        central_widget = self.centralWidget()
        layout = central_widget.layout()
        layout.setAlignment(Qt.AlignCenter)

    def show_error(self):
        self.error_label.show()
    
    def clear_inputs(self):
        self.input_dni.clear()
        self.input_user.clear()
        self.input_password.clear()
    
    def openMainWindow(self):
        dni=self.input_dni.text()
        usuario = self.input_user.text() 
        contrasena = self.input_password.text()
        validado = val.validarexistenciaPersona(dni, contrasena, Usuarios.setdnis)

        if not validado:
            self.show_error()
            self.clear_inputs()
                   
        else:
            self.close()
            self.window = MainWindow(dni, usuario, contrasena) 
            self.window.show()

    def openLoginAdminWindow(self):
            self.close()
            self.window = LoginAdministradorWindow()
            self.window.show()

    def openRegistroWindow(self):
        self.close()
        self.window = RegistroWindow()
        self.window.show()

class LoginAdministradorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inicio de Sesión de Administradores')
        self.setMinimumSize(600, 600)
        self.center()

        # Create a central widget and a layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        # Create a welcome label
        welcome_label = QLabel('Bienvenido/a', self)
        welcome_label.setAlignment(Qt.AlignCenter)

        # Create labels
        label_legajo = QLabel('Legajo del empleado:', self)
        label_password = QLabel('Contraseña:', self)

        # Create input boxes
        input_legajo = QLineEdit(self)
        self.input_legajo = input_legajo
        input_user = QLineEdit(self)
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)

        # Create login button
        self.button_login = QPushButton('Ingresar', self)
    
        # Create the error label (hidden by default)
        self.error_label = QLabel("El legajo o contraseña es incorrecto.", central_widget)
        self.error_label.setStyleSheet("color: red")
        self.error_label.hide()

        self.button_login.clicked.connect(self.openAdminWindow)

        # Add widgets to the layout
        layout.addWidget(logo_label)
        layout.addWidget(welcome_label)
        layout.addWidget(label_legajo)
        layout.addWidget(input_legajo)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)
        layout.addWidget(self.error_label)

        # Set the central widget and apply the style sheet
        self.setCentralWidget(central_widget)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def resizeEvent(self, event):
        # Center the objects when the window is resized
        super().resizeEvent(event)
        self.centerObjects()

    def centerObjects(self):
        # Center the objects in the window
        central_widget = self.centralWidget()
        layout = central_widget.layout()
        layout.setAlignment(Qt.AlignCenter)

    def show_error(self):
        self.error_label.show()
    
    def clear_inputs(self):
        self.input_legajo.clear()
        self.input_password.clear()

    def openAdminWindow(self):
        legajo = self.input_legajo.text()
        contraseña = self.input_password.text()
        validado=True
        
        if val.validarexistenciaPersona(legajo, contraseña, Administrador.setlegajos)==False:
            self.show_error()
            self.input_legajo.clear()
            self.input_password.clear()

        if validado==True:
            self.close()
            self.window = AdminWindow(legajo,contraseña)
            self.window.show()

class AdminWindow(QMainWindow):
    def __init__(self, legajo, contraseña):
        super().__init__()
        self.setWindowTitle('Gestión de Administrador')
        self.setMinimumSize(600, 600)
        self.center()

        """Traigo los valores de legajo y contraseña desde Login window"""
        self.legajo=int(legajo)
        self.contraseña=contraseña

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        # Create a central widget and a layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)

        # Create buttons
        self.button1 = QPushButton('Agregar un auto', central_widget)
        self.button1.clicked.connect(self.openAgregarAuto)

        self.button2 = QPushButton('Modificar un auto existente', central_widget)
        self.button2.clicked.connect(self.openModificarAuto)

        self.button3 = QPushButton('Modificar el precio de un tipo y gama de auto', central_widget)
        self.button3.clicked.connect(self.openModificarPrecioAuto)

        self.button4 = QPushButton('Eliminar un auto', central_widget)
        self.button4.clicked.connect(self.openEliminarAuto)  

        self.button5 = QPushButton('Agregar un empleado nuevo', central_widget)
        self.button5.clicked.connect(self.openAgregarEmpleado)

        self.button6 = QPushButton('Eliminar un empleado', central_widget)
        self.button6.clicked.connect(self.openEliminarEmpleado)

        self.button7 = QPushButton('Finalizar un alquiler', central_widget)
        self.button7.clicked.connect(self.openFinalizarAlquiler)

        self.button8 = QPushButton('Realizar tareas de gestión económica', central_widget)
        self.button8.clicked.connect(self.openGestionEconomica)

        # Add buttons to the layout
        layout.addWidget(logo_label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.addWidget(self.button7)
        layout.addWidget(self.button8)

        # Set the central widget and apply the style sheet
        self.setCentralWidget(central_widget)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def openAgregarAuto(self):
        self.close()
        self.window1 = AgregarAuto(self.legajo, self.contraseña)
        self.window1.show()

    def openModificarAuto(self):
        self.close()
        self.window2 = ModificarAuto(self.legajo, self.contraseña)
        self.window2.show()

    def openEliminarAuto(self):
        self.close()
        self.window3 = EliminarAuto(self.legajo, self.contraseña)
        self.window3.show()
    
    def openAgregarEmpleado(self):
        self.close()
        self.window4 = AgregarEmpleado(self.legajo, self.contraseña)
        self.window4.show()

    def openEliminarEmpleado(self):
        self.close()
        self.window5 = EliminarEmpleado(self.legajo, self.contraseña)
        self.window5.show()

    def openModificarPrecioAuto(self):
        self.close()
        self.window6 = ModificarPrecioAuto(self.legajo, self.contraseña)
        self.window6.show()
    
    def openFinalizarAlquiler(self):
        self.close()
        self.window7 = FinalizarAlquiler(self.legajo, self.contraseña)
        self.window7.show()

    def openGestionEconomica(self):
        self.close()
        self.window8 = GestionEconomica(self.legajo, self.contraseña)
        self.window8.show()

class OperacionRealizadaAdmin(QWidget):
    def __init__(self, legajo, contraseña):
        super().__init__()
        self.setWindowTitle("Operación realizada")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo desde la ventana en que esté trabajando el valor de legajo y contraseña"""
        self.legajo=legajo
        self.contraseña=contraseña

    def initUI(self):
        layout = QVBoxLayout()

        # Label
        label_aviso = QLabel("Su operación fue realizada exitosamente!")
        label_aviso.setStyleSheet("color: green")
        layout.addWidget(label_aviso)

        self.button2 = QPushButton("Volver al Inicio")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)
    
    def Volver(self):
        self.close()
        self.window = AdminWindow(self.legajo, self.contraseña)
        self.window.show()

"""Se crea ventana para agregar autos nuevos"""
class AgregarAuto(QMainWindow):
    def __init__(self, legajo, contraseña):
        super().__init__()
        self.setWindowTitle('Agregar un auto')
        self.setMinimumSize(700, 700)
        self.center()

        self.legajo=int(legajo)
        self.contraseña = contraseña

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter) 

        # Create a central widget and a layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Create labels and input boxes
        label_patente = QLabel("Patente:", central_widget)
        self.input_patente = QLineEdit(central_widget)

        label_marca = QLabel("Marca:", central_widget)
        self.input_marca = QLineEdit(central_widget)

        label_modelo = QLabel("Modelo:", central_widget)
        self.input_modelo = QLineEdit(central_widget)

        label_año = QLabel("Año:", central_widget)
        self.input_año = QLineEdit(central_widget)

        label_tipo = QLabel("Tipo:", central_widget)   
        self.input_tipo = QLineEdit(central_widget)

        label_gama = QLabel("Gama:", central_widget)
        self.input_gama = QLineEdit(central_widget)


        #Creo un label que informa cuando se agregó un auto exitosamente. Está escondido por defecto, se muestra al pasar la validación de los datos
        self.confirmado_label = QLabel("El auto fue agregado exitosamente!.", central_widget)
        self.confirmado_label.setStyleSheet("color: green")
        self.confirmado_label.hide()

        layout.addWidget(logo_label)
        layout.addWidget(label_patente)
        layout.addWidget(self.input_patente)
        layout.addWidget(label_marca)
        layout.addWidget(self.input_marca)
        layout.addWidget(label_modelo)
        layout.addWidget(self.input_modelo)
        layout.addWidget(label_año)
        layout.addWidget(self.input_año)
        layout.addWidget(label_tipo)
        layout.addWidget(self.input_tipo)
        layout.addWidget(label_gama)
        layout.addWidget(self.input_gama)
        layout.addWidget(self.confirmado_label)

        # Create the register button
        register_button = QPushButton('Register', central_widget)
        register_button.clicked.connect(self.validate_data)
        layout.addWidget(register_button)

        button2= QPushButton('Volver', central_widget)
        button2.clicked.connect(self.Volver)
        layout.addWidget(button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def Volver(self):
        self.close()
        window = AdminWindow(self.legajo, self.contraseña)
        window.open()

    def show_confirmado(self):
        self.confirmado_label.show()
    
    def PlaceholderText(self, input, text):
        input.clear()
        input.setPlaceholderText(text)
        palette = input.palette()
        placeholder_color = QColor(255, 0, 0)  # Red color
        palette.setColor(QPalette.PlaceholderText, placeholder_color)
        input.setPalette(palette)
    
    def openOperacionRealizada(self, legajo, contraseña):
        self.window1 = OperacionRealizadaAdmin(legajo, contraseña)
        self.window1.show()        

    def validate_data(self):    
        patente = self.input_patente.text()
        marca = self.input_marca.text()
        modelo = self.input_modelo.text()
        año = self.input_año.text()
        tipo = self.input_tipo.text()
        gama = self.input_gama.text()

        valid_data = True

        if val.validarpatente(patente) == False:
            valid_data = False
            self.PlaceholderText(self.input_patente, "Ingrese una patente con formato válido")

        if val.validarmodelo(modelo) == False:
            valid_data = False
            self.PlaceholderText(self.input_modelo, "Ingrese un modelo de vehículo válido")

        if val.validarmarca(marca) == False:
            valid_data = False
            self.PlaceholderText(self.input_marca, "Ingrese una marca de vehículo válido")

        if val.validaranio(año) == False:
            valid_data = False
            self.PlaceholderText(self.input_año, "Ingrese un año válido (anterior o igual al año actual)")

        if val.validartipo(tipo) == False:
            valid_data = False
            self.PlaceholderText(self.input_tipo, "Ingrese un tipo de vehículo válido")

        if val.validargama(gama) == False:
            valid_data = False
            self.PlaceholderText(self.input_gama, "Ingrese una gama de vehículo válida")

        if valid_data== True:
            self.show_confirmado()
            self.close()
            self.openOperacionRealizada(self.legajo, self.contraseña)
            Administrador.diccEmpleados[self.legajo].agregarVehiculo(patente, modelo, marca, año, tipo ,gama)  
            util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)
            
"""Se crea ventana para modificar datos de autos existentes"""
class ModificarAuto(QWidget):   
    def __init__(self, legajo, contraseña):
        super().__init__()
        self.setWindowTitle("Modificar un auto")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo el valor de legajo y contraseña desde AdminWindow"""
        self.legajo= int(legajo)
        self.contraseña=contraseña

    def initUI(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        # Label
        label_patente = QLabel("Ingrese la patente del auto:")
        label_atributo= QLabel("Ingrese el atributo a cambiar:")
        label_valor = QLabel("Ingrese el valor por el que desea modificar")
        self.label_confirmado = QLabel("El dato ha sido cambiado satisfactoriamente", central_widget)
        self.label_confirmado.setStyleSheet("color: green")
        self.label_confirmado.hide()
        
        # Input Box
        self.input_patente = QLineEdit(central_widget)
        self.combo_atributo = QComboBox(central_widget)
        self.input_valor = QLineEdit(central_widget)

        self.combo_atributo.addItem("Patente")
        self.combo_atributo.addItem("Marca")
        self.combo_atributo.addItem("Modelo")
        self.combo_atributo.addItem("Tipo")
        self.combo_atributo.addItem("Gama")       

        layout.addWidget(logo_label)
        layout.addWidget(label_patente)
        layout.addWidget(self.input_patente)
        layout.addWidget(label_atributo)
        layout.addWidget(self.combo_atributo)
        layout.addWidget(label_valor)
        layout.addWidget(self.input_valor)
        layout.addWidget(self.label_confirmado)

        # Button
        self.button = QPushButton("Continuar")
        self.button.clicked.connect(self.ClickContinuar)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Volver")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def show_confirmado(self):
        self.label_confirmado.show()

    def PlaceholderText(self, input, text):
        input.clear()
        input.setPlaceholderText(text)
        palette = input.palette()
        placeholder_color = QColor(255, 0, 0)  # Red color
        palette.setColor(QPalette.PlaceholderText, placeholder_color)
        input.setPalette(palette)
    
    def openOperacionRealizada(self, legajo, contraseña):
        self.window1 = OperacionRealizadaAdmin(legajo, contraseña)
        self.window1.show()  

    def ClickContinuar(self):
        patente = self.input_patente.text()
        atributo= self.combo_atributo.currentText().lower()
        valor = self.input_valor.text()

        validado = True
        if val.validarpatente(patente) == False:
            validado= False
            self.PlaceholderText(self.input_patente, "La patente ingresada no existe")
        
        if val.validaratributoVehiculo(atributo)==False:
            validado= False
        else:
            match atributo:

                case 'patente':
                    if val.validarpatente(valor)==False:
                        self.PlaceholderText(self.input_valor, "Reingrese una patente válida")
                    else:
                        Administrador.diccEmpleados[self.legajo].modificarVehiculo(patente,atributo,valor)
                        util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)
                        self.show_confirmado()
                        self.openOperacionRealizada(self.legajo, self.contraseña)

                case 'modelo':
                    if val.validarmodelo(valor)==False:
                        self.PlaceholderText(self.input_valor, "Reingrese un modelo de vehículo válido")
                    else:
                        Administrador.diccEmpleados[self.legajo].modificarVehiculo(patente,atributo,valor)
                        util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)
                        self.show_confirmado()
                        self.openOperacionRealizada(self.legajo, self.contraseña)

                case 'marca':
                    if val.validarmarca(valor)==False:
                        self.PlaceholderText(self.input_valor, "Reingrese una marca de auto válida")
                    else:
                        Administrador.diccEmpleados[self.legajo].modificarVehiculo(patente,atributo,valor) 
                        util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)
                        self.show_confirmado()
                        self.close()
                        self.openOperacionRealizada(self.legajo, self.contraseña)

                case 'año':  
                    if val.validaranio(valor)==False:
                        self.PlaceholderText(self.input_valor, "Reingrese una año válido (anterior al año actual)")
                    else:
                        Administrador.diccEmpleados[self.legajo].modificarVehiculo(patente,atributo,valor)
                        util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)
                        self.show_confirmado() 
                        self.close()
                        self.openOperacionRealizada(self.legajo, self.contraseña)

                case 'tipo':
                    if val.validartipo(valor)==False:
                        self.PlaceholderText(self.input_valor, "Reingrese una tipo de vehículo válido")
                    else:
                        Administrador.diccEmpleados[self.legajo].modificarVehiculo(patente,atributo,valor) 
                        util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)
                        self.show_confirmado()
                        self.close()
                        self.openOperacionRealizada(self.legajo, self.contraseña)
              
                case 'gama':
                    if val.validargama(valor)==False:
                        self.PlaceholderText(self.input_valor, "Reingrese una gama e vehículo válido")
                    else:
                        Administrador.diccEmpleados[self.legajo].modificarVehiculo(patente,atributo,valor)
                        util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)
                        self.show_confirmado()
                        self.close()
                        self.openOperacionRealizada(self.legajo, self.contraseña)
                
    def Volver(self):
        self.close()
        self.window = AdminWindow(self.legajo, self.contraseña)
        self.window.show() 

"""Se crea ventana para eliminar autos existentes"""
class EliminarAuto(QWidget):
    def __init__(self, legajo, contraseña):
        super().__init__()
        self.setWindowTitle("Eliminar auto")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo desde AdminWindow el valor de legajo y contraeña"""
        self.legajo=int(legajo)
        self.contraseña=contraseña

    def initUI(self):
        layout = QVBoxLayout()

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        # Label
        label_patente = QLabel("Ingresa la patente del auto a eliminar:")
        layout.addWidget(label_patente)

        # Input Box
        self.input_patente = QLineEdit()
        layout.addWidget(self.input_patente)

        """Se crea label reutilizable de confirmación y de error, oculto por defecto."""
        self.error_label=QLabel()
        self.error_label.hide()
        layout.addWidget(self.error_label)

        # Button
        self.button = QPushButton("Continuar")
        self.button.clicked.connect(self.confirmButtonClicked)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Volver")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()
    
    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def showError(self, text, color):
        self.error_label.clear()
        self.error_label.setText(text)
        coloraplicado= "color: " + color
        self.error_label.setStyleSheet(coloraplicado)
        self.error_label.show()
    
    def openOperacionRealizada(self, legajo, contraseña):
        self.window1 = OperacionRealizadaAdmin(legajo, contraseña)
        self.window1.show()  

    def confirmButtonClicked(self):
        patente = self.input_patente.text().strip()
        validado=True

        if val.validarpatente(patente)==False:
            validado=False
            self.showError("Ingrese una patente de formato válido", "red")
        else:
            if val.validarexistenciaclave(patente,Vehiculos.setVehiculos) == False:
                self.showError("Ingrese una patente existente", "red")
            else:
                self.close()
                self.openOperacionRealizada(self.legajo, self.contraseña)
                Administrador.diccEmpleados[self.legajo].eliminarVehiculo(patente) 
                util.escribirCsv('Vehiculos.csv', Vehiculos.diccVehiculos)
    
    def Volver(self):
        self.close()
        self.window = AdminWindow(self.legajo, self.contraseña)
        self.window.show()    

"""Se crea ventana para agregar empleados nuevos"""
class AgregarEmpleado(QWidget):
    def __init__(self, legajo, contraseña):
        super().__init__()
        self.setWindowTitle('Registro de Empleado')
        self.setMinimumSize(600,600)
        self.center()

        """Traigo desde MainWindow el valor de DNI, usuario y contraseña"""
        self.legajo= int(legajo)
        self.contraseña=contraseña

        # Create a central widget and a layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        # Create a welcome label
        welcome_label = QLabel('Registre un nuevo empleado', self)
        welcome_label.setAlignment(Qt.AlignCenter)

        # Create labels and input boxes
        label_dni = QLabel("DNI:", central_widget)
        self.input_dni = QLineEdit(central_widget)

        label_nombre = QLabel("Nombre:", central_widget)
        self.input_nombre = QLineEdit(central_widget)

        label_apellido = QLabel("Apellido:", central_widget)
        self.input_apellido = QLineEdit(central_widget)

        label_fecnac = QLabel("Fecha de nacimiento: (DD-MM-YYYY)", central_widget)   #PONER UN CALENDARIO
        self.input_fecnac = QLineEdit(central_widget)

        label_email = QLabel("Email:", central_widget)   
        self.input_email = QLineEdit(central_widget)

        label_contraseña = QLabel("Contraseña:", central_widget)
        self.input_contraseña = QLineEdit(central_widget)

        label_confirmarcontraseña = QLabel("Confirmar contraseña:", central_widget)
        self.input_confirmarcontraseña = QLineEdit(central_widget)

        #Creo un label que informa cuando se agregó un auto exitosamente. Está escondido por defecto, se muestra al pasar la validación de los datos
        self.confirmado_label = QLabel("El empleado ha sido registrado exitosamente!.", central_widget)
        self.confirmado_label.setStyleSheet("color: green")
        self.confirmado_label.hide()

        """Se agregan al layout todos los widgets"""
        layout.addWidget(logo_label)
        layout.addWidget(welcome_label)
        layout.addWidget(label_dni)
        layout.addWidget(self.input_dni)
        layout.addWidget(label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(label_apellido)
        layout.addWidget(self.input_apellido)
        layout.addWidget(label_fecnac)
        layout.addWidget(self.input_fecnac)
        layout.addWidget(label_email)
        layout.addWidget(self.input_email)
        layout.addWidget(label_contraseña)
        layout.addWidget(self.input_contraseña)
        layout.addWidget(label_confirmarcontraseña)
        layout.addWidget(self.input_confirmarcontraseña)
        layout.addWidget(self.confirmado_label)

        # Create the register button
        button1 = QPushButton('Registrar', central_widget)
        button1.clicked.connect(self.validacionRegistro)
        layout.addWidget(button1)

        button2 = QPushButton('Volver', central_widget)
        button2.clicked.connect(self.Volver)
        layout.addWidget(button2)
        
        # Set the central widget and apply the style sheet
        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def show_Confirmado(self):
        self.confirmado_label.show()
    
    def openOperacionRealizada(self, legajo, contraseña):
        self.window1 = OperacionRealizadaAdmin(legajo, contraseña)
        self.window1.show() 
    
    def PlaceholderText(self, input, text):
        input.clear()
        input.setPlaceholderText(text)
        palette = input.palette()
        placeholder_color = QColor(255, 0, 0)  # Red color
        palette.setColor(QPalette.PlaceholderText, placeholder_color)
        input.setPalette(palette)

    def Volver(self):
        self.close()
        self.window = AdminWindow(self.legajo, self.contraseña)
        self.window.show()     
    
    def validacionRegistro(self):
        dni= self.input_dni.text()
        nombre= self.input_nombre.text()
        apellido= self.input_apellido.text()
        fecnac= self.input_fecnac.text()
        email=self.input_email.text()
        contraseña= self.input_contraseña.text()
        confcontraseña=self.input_confirmarcontraseña.text()

        validado=True

        if val.validardni(dni)==False:
            validado=False
            self.PlaceholderText(self.input_dni, "Ingrese un DNI válido")
        
        if val.validarnombre(nombre)==False:
            validado=False
            self.PlaceholderText(self.input_nombre, "Reingrese el nombre de forma correcta")
        
        if val.validarnombre(apellido)==False:
            validado=False
            self.PlaceholderText(self.input_apellido, "Reingrese el apellido de forma correcta")
       
        if val.validarFechaNac(fecnac)==False:
            validado=False
            self.PlaceholderText(self.input_fecnac, "Reingrese una fecha de nacimiento válida (Mayor 18 años)")
        
        if val.validarcontraseña(contraseña)==False:
            validado=False
            self.PlaceholderText(self.input_contraseña, "Reingrese una contraseña entre 6 y 20 caracteres")
        
        if contraseña != confcontraseña:
            validado=False
            self.PlaceholderText(self.input_confirmarcontraseña, "Las contraseñas deben coincidir")       
        
        if validado==True:
            self.show_Confirmado() 
            self.close()
            self.openOperacionRealizada(self.legajo, self.contraseña)
            Administrador.diccEmpleados[self.legajo].agregarEmpleado(dni, nombre, apellido, fecnac, email, contraseña)
            util.escribirCsv('Empleados.csv', Administrador.diccEmpleados) 

"""Se crea ventana para eliminar empleados"""
class EliminarEmpleado(QWidget):
    def __init__(self, legajo, contraseña):
        super().__init__()
        self.setWindowTitle("Eliminar empleado")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo desde MainWindow el valor de DNI"""
        self.legajo=int(legajo)
        self.contraseña=contraseña

    def initUI(self):
        layout = QVBoxLayout()

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        # Label
        label_legajo = QLabel("Ingresa tu Legajo:")
        layout.addWidget(label_legajo)

        # Input Box
        self.input_legajo = QLineEdit()
        layout.addWidget(self.input_legajo)

        """Se crea label reutilizable de confirmación y de error, oculto por defecto."""
        self.error_label=QLabel()
        self.error_label.hide()
        layout.addWidget(self.error_label)

        # Button
        self.button = QPushButton("Continuar")
        self.button.clicked.connect(self.confirmButtonClicked)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Volver")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()
    
    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def openOperacionRealizada(self, legajo, contraseña):
        self.window1 = OperacionRealizadaAdmin(legajo, contraseña)
        self.window1.show() 
    
    def showError(self, text, color):
        self.error_label.clear()
        self.error_label.setText(text)
        coloraplicado= "color: " + color
        self.error_label.setStyleSheet(coloraplicado)
        self.error_label.show()

    def confirmButtonClicked(self):
        legajo= self.input_legajo.text().strip()

        if val.validarexistenciaclave(str(legajo), {tupla[0] for tupla in Administrador.setlegajos})==False:
            self.showError("Ingrese un legajo válido", "red")
            self.input_legajo.clear()
        else:
            self.showError("La cuenta fue eliminada exitosamente", "green")
            self.close()
            Administrador.diccEmpleados[int(legajo)].darDeBajaEmpleado()
            util.escribirCsv('Empleados.csv', Administrador.diccEmpleados)
            self.openOperacionRealizada(self.legajo, self.contraseña)
    
    def Volver(self):
        self.close()
        self.window = AdminWindow(self.legajo, self.contraseña)
        self.window.show() 

"""Se crea ventana para modificar precios de autos"""
class ModificarPrecioAuto(QWidget):
    def __init__(self,legajo, contraseña):
        super().__init__()
        self.setWindowTitle("Elegi tus fechas de alquiler")
        self.setMinimumSize(600, 600)
        self.center()
        self.initUI()

        """Traigo desde AdminWindow el valor de DNI, usuario y contraseña"""
        self.legajo= int(legajo)
        self.contraseña=contraseña

    def initUI(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        """Labels y combo boxes de tipo y gama de auto cuyo precio se desea cambiar"""
        label_comboTipo = QLabel("Seleccione el tipo de vehículo cuyo precio desea cambiar")
        label_comboGama = QLabel("Seleccione la gama de vehículo cuyo precio desea cambiar")
        self.comboTipo = QComboBox(self)
        self.comboGama = QComboBox(self)

        # Add options to combo boxes
        self.comboTipo.addItem("Sedan")
        self.comboTipo.addItem("Pick-up")
        self.comboTipo.addItem("SUV")
        self.comboTipo.addItem("Deportivo")

        self.comboGama.addItem("Baja")
        self.comboGama.addItem("Media")
        self.comboGama.addItem("Alta")

        label_precio= QLabel("Ingrese el precio por día a cambiar:")
        self.input_precio = QLineEdit()

        """Se agregan los labels y combo boxes al layout"""
        layout.addWidget(logo_label)
        layout.addWidget(label_comboTipo)
        layout.addWidget(self.comboTipo)
        layout.addWidget(label_comboGama)
        layout.addWidget(self.comboGama)
        layout.addWidget(label_precio)
        layout.addWidget(self.input_precio)

        """Se crea label reutilizable para error y confirmacion"""
        self.error_label=QLabel()
        self.error_label.hide()
        layout.addWidget(self.error_label)

        """Se crea boton de confirmar reserva y de volver a la página anterior"""
        self.button1 = QPushButton("Confirmar")
        layout.addWidget(self.button1)
        self.button1.clicked.connect(self.ClickConfirmar)

        self.button2 = QPushButton("Volver")
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.Volver)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()
    
    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def showError(self, text, color):
        self.error_label.clear()
        self.error_label.setText(text)
        coloraplicado= "color: " + color
        self.error_label.setStyleSheet(coloraplicado)
        self.error_label.show()

    def openOperacionRealizada(self, legajo, contraseña):
        self.window1 = OperacionRealizadaAdmin(legajo, contraseña)
        self.window1.show() 

    def ClickConfirmar(self):
        tipo = self.comboTipo.currentText().lower()
        gama = self.comboGama.currentText().lower()
        precio = self.input_precio.text()
        validado = True
        if val.validarprecio(precio)==False:
            self.showError("El precio indicado no es válido", "red")
        else:
            Administrador.diccEmpleados[self.legajo].modifPreciosAutos(tipo,gama,precio) 
            self.showError("El cambio de precio fue realizado exitosamente", "green")
            self.openOperacionRealizada(self.legajo, self.contraseña)
            self.close()
        
    def Volver(self):
        self.close()
        self.window = AdminWindow(self.legajo, self.contraseña)
        self.window.show()    

class FinalizarAlquiler(QWidget):
    def __init__(self, legajo, contraseña):
        super().__init__()
        self.setWindowTitle("Finalización de alquiler")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo desde MainWindow el valor de DNI, usuario y contraseña"""
        self.legajo=int(legajo)
        self.contraseña=contraseña

    def initUI(self):
        layout = QVBoxLayout()

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        # Label
        label_idalq= QLabel("Ingresa el id del alquiler a finalizar:")
        layout.addWidget(label_idalq)

        # Input Box
        self.input_idalq = QLineEdit()
        layout.addWidget(self.input_idalq)

        self.error_label=QLabel()
        self.error_label.hide()
        layout.addWidget(self.error_label)


        self.button = QPushButton("Continuar")
        self.button.clicked.connect(self.confirmButtonClicked)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Volver")
        self.button2.clicked.connect(self.Volver)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()
    
    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def showError(self, text, color):
        self.error_label.clear()
        self.error_label.setText(text)
        coloraplicado= "color: " + color
        self.error_label.setStyleSheet(coloraplicado)
        self.error_label.show()

    def openOperacionRealizada(self, legajo, contraseña):
        self.window1 = OperacionRealizadaAdmin(legajo, contraseña)
        self.window1.show() 

    def confirmButtonClicked(self):
        idalq= self.input_idalq.text().strip()
        validado=True

        if val.validarexistenciaclave(idalq, Alquiler.setAlquileres) == False:  
            validado=False
            self.showError("Ingrese un id de alquiler válido", "red")
        else:
            self.showError("El alquiler fue terminado exitosamente", "green")
            self.close()
            Administrador.diccEmpleados[self.legajo].finalizarAlquiler(idalq)
            util.escribirCsv('Alquileres.csv', Alquiler.diccAlquileres)
            self.openOperacionRealizada(self.legajo, self.contraseña)
    
    def Volver(self):
        self.close()
        self.window = AdminWindow(self.legajo, self.contraseña)
        self.window.show()   

class GestionEconomica(QWidget):
    def __init__(self, legajo, contraseña):
        super().__init__()
        self.setWindowTitle('NoVoyEnTren.com')
        self.setMinimumSize(700, 700)
        self.center()
        self.legajo= int(legajo)
        self.contraseña=contraseña
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        # Create buttons
        self.button1 = QPushButton('Consultar ventas de un día en particular')
        self.button1.clicked.connect(self.openVentasPorDia)

        self.button2 = QPushButton('Consultar ventas de un mes')
        self.button2.clicked.connect(self.openVentasPorMes)

        # Add buttons to the layout
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # Set the central widget and apply the style sheet
        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def openVentasPorDia(self):
        self.close()
        self.window1 = VentasPorDia(self.legajo, self.contraseña)
        self.window1.show()

    def openVentasPorMes(self):
        self.close()
        self.window2 = VentasPorMes(self.legajo, self.contraseña)
        self.window2.show()

class VentasPorDia(QWidget):
    def __init__(self,legajo, contraseña):
        super().__init__()
        self.setWindowTitle("Gestion económica: ventas por dia")
        self.setMinimumSize(700, 700)
        self.center()
        self.legajo=int(legajo)
        self.contraseña=contraseña
        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()

        # First Calendar
        label1 = QLabel("Seleccione fecha de interés:")
        layout.addWidget(label1)
        self.calendar1 = QCalendarWidget()
        # self.calendar1.setGeometry(50, 50, 200, 150)  # Set initial size
        self.calendar1.setFixedSize(400, 400)  # Set fixed size
        layout.addWidget(self.calendar1)


        """Se crea label reutilizable de confirmación y de error, oculto por defecto."""
        self.label=QLabel()
        self.label.hide()
        layout.addWidget(self.label)

        """Se crea boton de confirmar reserva y de volver a la página anterior"""
        self.button1 = QPushButton("Confirmar")
        layout.addWidget(self.button1)
        self.button1.clicked.connect(self.ClickConfirmar)

        self.button2 = QPushButton("Volver")
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.Volver)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def showError(self, text, color):
        self.label.clear()
        self.label.setText(text)
        coloraplicado= "color: " + color
        self.label.setStyleSheet(coloraplicado)
        self.label.show()

    def ClickConfirmar(self):
        fecha_interes = self.calendar1.selectedDate().toString("dd-MM-yyyy")

        if val.validarFechaAConsultar(fecha_interes)==False:
            self.showError("No hay resultados para la fecha indicada.", "red")
        else:
            sumaTotal = Administrador.diccEmpleados[self.legajo].consultarVentasXDia(fecha_interes)
            self.showError("El total de ventas en " + fecha_interes + " es: " f"{sumaTotal}", "green")

    def Volver(self):
        self.close()
        self.window = MainWindow(self.dni, self.usuario, self.contraseña)
        self.window.show()

class VentasPorMes(QWidget):
    def __init__(self,legajo, contraseña):
        super().__init__()
        self.setWindowTitle("Gestion económica: ventas por mes")
        self.setMinimumSize(700, 700)
        self.center()
        self.legajo=int(legajo)
        self.contraseña=contraseña
        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()

        
        label1 = QLabel("Seleccione mes de interés:")
        layout.addWidget(label1)
        self.combobox = QComboBox(self)
        self.combobox.addItem("1")
        self.combobox.addItem("2")
        self.combobox.addItem("3")
        self.combobox.addItem("4")
        self.combobox.addItem("5")
        self.combobox.addItem("6")
        self.combobox.addItem("7")
        self.combobox.addItem("8")
        self.combobox.addItem("9")
        self.combobox.addItem("10")
        self.combobox.addItem("11")
        self.combobox.addItem("12")
        layout.addWidget(self.combobox)

        """Se crea label reutilizable de confirmación y de error, oculto por defecto."""
        self.label=QLabel()
        self.label.hide()
        layout.addWidget(self.label)

        """Se crea boton de confirmar reserva y de volver a la página anterior"""
        self.button1 = QPushButton("Confirmar")
        layout.addWidget(self.button1)
        self.button1.clicked.connect(self.ClickConfirmar)

        self.button2 = QPushButton("Volver")
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.Volver)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def showError(self, text, color):
        self.label.clear()
        self.label.setText(text)
        coloraplicado= "color: " + color
        self.label.setStyleSheet(coloraplicado)
        self.label.show()

    def ClickConfirmar(self):
        mes = str(self.combobox.currentText())

        if val.validarMesAConsultar(mes)==False:
            self.showError("No hay resultados el mes indicado.", "red")
        else:
            sumaTotal = Administrador.diccEmpleados[self.legajo].consultarVentasXMes(mes)
            self.showError("El total de ventas en " + mes + " es: " f"{sumaTotal}", "green")

    def Volver(self):
        self.close()
        self.window = MainWindow(self.dni, self.usuario, self.contraseña)
        self.window.show()

"""Se crea ventana de registro de usuarios"""
class RegistroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registro de usuario')
        self.setMinimumSize(700,700)
        self.center()

        """Se crea el layout y central widget"""
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        """Label de bienvenida"""
        welcome_label = QLabel('Registrese en nuestra plataforma', self)
        welcome_label.setAlignment(Qt.AlignCenter)

        """Se crean los label e input boxes"""
        label_dni = QLabel("DNI:", central_widget)
        self.input_dni = QLineEdit(central_widget)

        label_nombre = QLabel("Nombre:", central_widget)
        self.input_nombre = QLineEdit(central_widget)

        label_apellido = QLabel("Apellido:", central_widget)
        self.input_apellido = QLineEdit(central_widget)

        label_fecnac = QLabel("Fecha de nacimiento: (DD-MM-YYYY)", central_widget)
        self.input_fecnac = QLineEdit(central_widget)

        label_usuario = QLabel("Usuario:", central_widget)
        self.input_usuario = QLineEdit(central_widget)

        label_email = QLabel("Email:", central_widget)   
        self.input_email = QLineEdit(central_widget)

        label_contraseña = QLabel("Contraseña:", central_widget)
        self.input_contraseña = QLineEdit(central_widget)
        self.input_contraseña.setEchoMode(QLineEdit.Password)

        label_confirmarcontraseña = QLabel("Confirmar contraseña:", central_widget)
        self.input_confirmarcontraseña = QLineEdit(central_widget)
        self.input_confirmarcontraseña.setEchoMode(QLineEdit.Password)

        """Creo un label que informa cuando se registró el usuario exitosamente. Está escondido por defecto, se muestra al pasar la validación de los datos"""
        self.confirmado_label = QLabel("Usted ha sido registrado exitosamente!.", central_widget)
        self.confirmado_label.setStyleSheet("color: green")
        self.confirmado_label.hide()

        """Se agregan todos los widgets al layout"""
        layout.addWidget(logo_label)
        layout.addWidget(welcome_label)
        layout.addWidget(label_dni)
        layout.addWidget(self.input_dni)
        layout.addWidget(label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(label_apellido)
        layout.addWidget(self.input_apellido)
        layout.addWidget(label_fecnac)
        layout.addWidget(self.input_fecnac)
        layout.addWidget(label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(label_email)
        layout.addWidget(self.input_email)
        layout.addWidget(label_contraseña)
        layout.addWidget(self.input_contraseña)
        layout.addWidget(label_confirmarcontraseña)
        layout.addWidget(self.input_confirmarcontraseña)
        layout.addWidget(self.confirmado_label)

        """Se crean botones de registro y volver atrás"""
        button1 = QPushButton('Registrarse', central_widget)
        button1.clicked.connect(self.validacionRegistro)
        layout.addWidget(button1)

        button2 = QPushButton('Volver', central_widget)
        button2.clicked.connect(self.Volver)
        layout.addWidget(button2)
        
        """Se setea el central widget y estilo de la ventana"""
        self.setCentralWidget(central_widget)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    """Se crea método para mostrar el label de confirmación"""
    def show_Confirmado(self):
        self.confirmado_label.show()
    
    """Se crea método para ubicar el PlaceholderText cuando hay algún error en los datos ingresados"""
    def PlaceholderText(self, input, text):
        input.clear()
        input.setPlaceholderText(text)
        palette = input.palette()
        placeholder_color = QColor(255, 0, 0)  # Red color
        palette.setColor(QPalette.PlaceholderText, placeholder_color)
        input.setPalette(palette)

    """Se crea método para abrir la ventana de confirmación de la operación realizada"""
    def openRegistroRealizado(self, dni, usuario, contraseña):
        self.window=RegistroRealizadoUsuario(dni, usuario, contraseña)
        self.window.show()

    """Se crea método para volver a LoginWindow"""
    def Volver(self):
        self.close()
        self.window = LoginWindow()
        self.window.show()     
    
    """Se crea método para validar los datos ingresados y ejecutar el registro"""
    def validacionRegistro(self):
        dni= self.input_dni.text()
        nombre= self.input_nombre.text()
        apellido= self.input_apellido.text()
        fecnac= self.input_fecnac.text()
        usuario=self.input_usuario.text()
        email=self.input_email.text()
        contraseña= self.input_contraseña.text()
        confcontraseña=self.input_confirmarcontraseña.text()

        validado=True

        if val.validardni(dni)==False:
            validado=False
            self.PlaceholderText(self.input_dni, "Ingrese un DNI válido")
        
        if val.validarnombre(nombre)==False:
            validado=False
            self.PlaceholderText(self.input_nombre, "Reingrese el nombre de forma correcta")
        
        if val.validarnombre(apellido)==False:
            validado=False
            self.PlaceholderText(self.input_apellido, "Reingrese el apellido de forma correcta")
       
        if val.validarusuario(usuario)==False:
            validado=False
            self.PlaceholderText(self.input_usuario, "Reingrese el usuario de forma correcta")
        
        if val.validarFechaNac(fecnac)==False:
            validado=False
            self.PlaceholderText(self.input_fecnac, "Reingrese una fecha de nacimiento válida (Mayor 18 años)")
        
        if val.validarcontraseña(contraseña)==False:
            validado=False
            self.PlaceholderText(self.input_contraseña, "Reingrese una contraseña entre 6 y 20 caracteres")
        
        if contraseña != confcontraseña:
            validado=False
            self.PlaceholderText(self.input_confirmarcontraseña, "Las contraseñas deben coincidir")       
        
        if validado==True:
            self.show_Confirmado() #VER SI SE PUEDE HACER UNA VENTANA EMERGENTE PARA VOLVER... NO SE SI LLEGAMOS. 
            Usuarios.agregarUsuario(dni, usuario, nombre, apellido, fecnac, email, contraseña)
            util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
            self.openRegistroRealizado(dni, usuario, contraseña)


class RegistroRealizadoUsuario(QWidget):
    def __init__(self, dni, usuario, contraseña):
        super().__init__()
        self.setWindowTitle("Cancelación de reservas")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo desde RegistroWindow el valor de DNI, usuario y contraseña"""
        self.dni=dni
        self.usuario=usuario
        self.contraseña=contraseña

    def initUI(self):
        layout = QVBoxLayout()

        # Label
        label_aviso = QLabel("Su operación fue realizada exitosamente!")
        label_aviso.setStyleSheet("color: green")
        layout.addWidget(label_aviso)

        self.button2 = QPushButton("Ir al Inicio")
        self.button2.clicked.connect(self.IrAlInicio)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def IrAlInicio(self):
        self.close()
        self.window1=RegistroWindow()
        self.window1.close()
        self.window = MainWindow(self.dni, self.usuario, self.contraseña)
        self.window.show()  


class MainWindow(QMainWindow):
    def __init__(self, dni, usuario, contraseña):
        super().__init__()
        self.setWindowTitle('NoVoyEnTren.com')
        self.setMinimumSize(600, 600)
        self.center()

        """Traigo desde la ventana de inicio los datos de usuario y dni"""
        self.dni=dni
        self.usuario=usuario
        self.contraseña=contraseña

        # Create a central widget and a layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)

        # Create a logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('novoyentrenLOGO.png').scaled(250,250, aspectRatioMode=True)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        # Create buttons
        self.button1 = QPushButton('Hacer una Reserva', central_widget)
        self.button1.setIcon(QIcon('icon1.png'))  # Replace with the path to your button icon
        self.button1.clicked.connect(self.openReserva)

        self.button2 = QPushButton('Cancelar una Reserva existente', central_widget)
        self.button2.setIcon(QIcon('icon2.png'))  # Replace with the path to your button icon
        self.button2.clicked.connect(self.openCancelacion)

        self.button5= QPushButton('Ver tus reservas actuales', central_widget)
        self.button5.clicked.connect(self.openReservasExistentes)

        self.button6=QPushButton('Mostrar datos personales', central_widget)
        self.button6.clicked.connect(self.openVerDatosPersonales)

        self.button3 = QPushButton('Cambiar datos personales', central_widget)
        self.button3.setIcon(QIcon('icon3.png'))  # Replace with the path to your button icon
        self.button3.clicked.connect(self.openCambioDatos)

        self.button4 = QPushButton('Eliminar tu cuenta', central_widget)
        self.button4.setIcon(QIcon('icon3.png'))  # Replace with the path to your button icon
        self.button4.clicked.connect(self.openEliminarUsuario)

        # Add buttons to the layout
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)

        # Set the central widget and apply the style sheet
        self.setCentralWidget(central_widget)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def openReserva(self):
        self.close()
        self.window1 = CrearReserva(self.dni, self.usuario, self.contraseña)
        self.window1.show()

    def openCancelacion(self):
        self.close()
        self.window2 = Cancelacion(self.dni, self.usuario, self.contraseña)
        self.window2.show()

    def openCambioDatos(self):
        self.close()
        self.window3 = CambioDatos(self.dni, self.usuario, self.contraseña)
        self.window3.show()
    
    def openEliminarUsuario(self):
        self.close()
        self.window4 = EliminarUsuario(self.dni, self.usuario, self.contraseña)
        self.window4.show()

    def openReservasExistentes(self):
        self.close()
        self.window5=ReservasExistentes(self.dni, self.usuario, self.contraseña)
        self.window5.show()

    def openVerDatosPersonales(self):
        self.close()
        self.window6=verDatosPersonales(self.dni, self.usuario, self.contraseña)
        self.window6.show()

class ReservasExistentes(QWidget):
    def __init__(self, dni, usuario, contraseña):
        super().__init__()
        self.setWindowTitle("Ver reservas existentes")
        self.setMinimumSize(600,600)
        self.center()
        self.dni=dni
        self.usuario=usuario
        self.contraseña=contraseña
        self.initUI()

        """Traigo desde RegistroWindow el valor de DNI, usuario y contraseña"""
        

    def initUI(self):
        layout = QVBoxLayout()

        # Label
        label_aviso = QLabel("Sus reservas existentes son:")
        layout.addWidget(label_aviso)
        
        self.label_info = QLabel(self)
        self.label_info.setWordWrap(True)
        layout.addWidget(self.label_info)

        texto= Usuarios.diccUsuarios[self.dni].mostrarMisReservas()
        self.label_info.setText(texto)

        self.button2 = QPushButton("Volver")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def Volver(self):
        self.close()
        self.window = MainWindow(self.dni, self.usuario, self.contraseña)
        self.window.show() 

class verDatosPersonales(QWidget):
    def __init__(self, dni, usuario, contraseña):
        super().__init__()
        self.setWindowTitle("Ver datos personales")
        self.setMinimumSize(600,600)
        self.center()
        self.dni=dni
        self.usuario=usuario
        self.contraseña=contraseña
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label
        label_aviso = QLabel("Sus datos personales son:")
        layout.addWidget(label_aviso)
        
        self.label_info = QLabel(self)
        self.label_info.setWordWrap(True)
        layout.addWidget(self.label_info)

        texto= Usuarios.diccUsuarios[self.dni].__str__()
        self.label_info.setText(texto)

        self.button2 = QPushButton("Volver")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def Volver(self):
        self.close()
        self.window = MainWindow(self.dni, self.usuario, self.contraseña)
        self.window.show() 

class CrearReserva(QWidget):
    def __init__(self,dni, usuario, contraseña):
        super().__init__()
        self.setWindowTitle("Elegi tus fechas de alquiler")
        self.setMinimumSize(600, 600)
        self.initUI()

        """Traigo desde MainWindow el valor de DNI, usuario y contraseña"""
        self.dni= dni
        self.usuario=usuario
        self.contraseña=contraseña

    def initUI(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # First Calendar
        label1 = QLabel("Fecha de Inicio")
        layout.addWidget(label1)
        self.calendar1 = QCalendarWidget()
        layout.addWidget(self.calendar1)

        # Second Calendar
        label2 = QLabel("Fecha de Fin")
        layout.addWidget(label2)
        self.calendar2 = QCalendarWidget()
        layout.addWidget(self.calendar2)

        """Labels y combo boxes de tipo y gama de auto que se desea alquilar"""
        label_comboTipo = QLabel("Seleccione el tipo de vehículo que desea alquilar")
        label_comboGama = QLabel("Seleccione la gama de vehículo que desea alquilar")
        self.comboTipo = QComboBox(self)
        self.comboGama = QComboBox(self)

        # Add options to combo boxes
        self.comboTipo.addItem("Sedan")
        self.comboTipo.addItem("Pick-up")
        self.comboTipo.addItem("SUV")
        self.comboTipo.addItem("Deportivo")

        self.comboGama.addItem("Baja")
        self.comboGama.addItem("Media")
        self.comboGama.addItem("Alta")

        """Se agregan los labels y combo boxes al layout"""
        layout.addWidget(label_comboTipo)
        layout.addWidget(self.comboTipo)
        layout.addWidget(label_comboGama)
        layout.addWidget(self.comboGama)

        """Se crea label reutilizable de confirmación y de error, oculto por defecto."""
        self.error_label=QLabel()
        self.error_label.hide()
        layout.addWidget(self.error_label)

        """Se crea boton de confirmar reserva y de volver a la página anterior"""
        self.button1 = QPushButton("Confirmar")
        layout.addWidget(self.button1)
        self.button1.clicked.connect(self.ClickConfirmar)

        self.button2 = QPushButton("Volver")
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.Volver)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()
    
    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def openReservaRealizada(self, dni, usuario, contraseña, idres):
        self.window1 = ReservaRealizadaUsuario(dni, usuario, contraseña, idres)
        self.window1.show()

    def showError(self, text, color):
        self.error_label.clear()
        self.error_label.setText(text)
        coloraplicado= "color: " + color
        self.error_label.setStyleSheet(coloraplicado)
        self.error_label.show()

    def ClickConfirmar(self):

        tipo = self.comboTipo.currentText().lower()
        gama = self.comboGama.currentText().lower()
        fecha_inicio = self.calendar1.selectedDate().toString("dd-MM-yyyy")
        fecha_fin = self.calendar2.selectedDate().toString("dd-MM-yyyy")
        validado = True

        if val.validarAgregarFechaInicio(fecha_inicio)==False:
            self.showError("Seleccione una fecha de inicio con más de 5 días de anticipación, y fecha de fin posterior.", "red")
            validado = False
        
        if val.validarFechaFin(fecha_inicio, fecha_fin)==False:
            self.showError("Seleccione una fecha de inicio con más de 5 días de anticipación, y fecha de fin posterior.", "red")
            validado = False
        
        if validado == True:
            auto = Vehiculos.asignarauto(fecha_inicio,fecha_fin,tipo,gama)

            if auto== None:
                self.showError("Lo sentimos, no hay autos disponibles según lo pedido. Pruebe cambiando el tipo y gama de auto", "red")
            else:
                self.showError("La reserva fue realizada exitosamente", "green")
                self.close()
                Usuarios.diccUsuarios[self.dni].agregarReserva(auto, fecha_inicio, fecha_fin)
                util.escribirCsv('Reservas.csv', Reserva.diccReservas)
                idreserva= Reserva.cantReservas
                self.openReservaRealizada(self.dni, self.usuario, self.contraseña, idreserva)

    def Volver(self):
        self.close()
        self.window = MainWindow(self.dni, self.usuario, self.contraseña)
        self.window.show()            


class Cancelacion(QWidget):
    def __init__(self, dni, usuario, contraseña):
        super().__init__()
        self.setWindowTitle("Cancelación de reservas")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo desde MainWindow el valor de DNI, usuario y contraseña"""
        self.dni=dni
        self.usuario=usuario
        self.contraseña=contraseña

    def initUI(self):
        layout = QVBoxLayout()

        # Label
        label_idres = QLabel("Ingresa tu código de reserva:")
        layout.addWidget(label_idres)

        # Input Box
        self.input_idres = QLineEdit()
        layout.addWidget(self.input_idres)

        """Se crea label reutilizable de confirmación y de error, oculto por defecto."""
        self.error_label=QLabel()
        self.error_label.hide()
        layout.addWidget(self.error_label)

        # Button
        self.button = QPushButton("Continuar")
        self.button.clicked.connect(self.confirmButtonClicked)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Volver")
        self.button2.clicked.connect(self.Volver)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def showError(self, text, color):
        self.error_label.clear()
        self.error_label.setText(text)
        coloraplicado= "color: " + color
        self.error_label.setStyleSheet(coloraplicado)
        self.error_label.show()

    def openOperacionRealizada(self, dni, usuario, contraseña):
        self.window1 = OperacionRealizadaUsuario(dni, usuario, contraseña)
        self.window1.show()

    def confirmButtonClicked(self):
        idres= self.input_idres.text().strip()
        validado=True

        if val.validarexistenciaclave(idres, Reserva.setReservas)==False:
            validado=False
            self.showError("Ingrese un id de reserva válido", "red")
        else:
            self.close()
            self.showError("La reserva fue cancelada exitosamente", "green")
            Usuarios.diccUsuarios[self.dni].cancelarReserva(idres)
            util.escribirCsv('Reservas.csv', Reserva.diccReservas)
            self.openOperacionRealizada(self.dni, self.usuario, self.contraseña)
    
    def Volver(self):
        self.close()
        self.window = MainWindow(self.dni, self.usuario, self.contraseña)
        self.window.show()     

class ReservaRealizadaUsuario(QWidget):
    def __init__(self, dni, usuario, contraseña, idres):
        super().__init__()
        self.setWindowTitle("Operación realizada")
        self.setMinimumSize(600,600)
        self.center()
        self.dni=dni
        self.usuario=usuario
        self.contraseña=contraseña
        self.idres=idres

        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()

        # Label
        label_aviso = QLabel("Su operación fue realizada exitosamente!")
        label_aviso.setStyleSheet("color: green")
        layout.addWidget(label_aviso)

        label_idres = QLabel(f"El id de su reserva es {self.idres}")
        label_idres.setStyleSheet("color: green")
        layout.addWidget(label_idres)

        self.button2 = QPushButton("Volver al Inicio")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()
    
    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def Volver(self):
        self.close()
        self.window = MainWindow(self.dni,self.usuario, self.contraseña)
        self.window.show()


class OperacionRealizadaUsuario(QWidget):
    def __init__(self, dni, usuario, contraseña):
        super().__init__()
        self.setWindowTitle("Operación realizada")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo desde MainWindow el valor de DNI, usuario y contraseña"""
        self.dni=dni
        self.usuario=usuario
        self.contraseña=contraseña


    def initUI(self):
        layout = QVBoxLayout()

        # Label
        label_aviso = QLabel("Su operación fue realizada exitosamente!")
        label_aviso.setStyleSheet("color: green")
        layout.addWidget(label_aviso)

        self.button2 = QPushButton("Volver al Inicio")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()
    
    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def Volver(self, ventana):
        self.close()
        self.window = MainWindow(self.dni,self.usuario, self.contraseña)
        self.window.show()

class finalizarOperacionUsuario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operación realizada")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo desde MainWindow el valor de DNI, usuario y contraseña"""

    def initUI(self):
        layout = QVBoxLayout()

        # Label
        label_aviso = QLabel("Su operación fue realizada exitosamente!")
        label_aviso.setStyleSheet("color: green")
        layout.addWidget(label_aviso)

        self.button2 = QPushButton("Volver al Inicio")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.button1=QPushButton("Cerrar Programa")
        self.button1.clicked.connect(self.close)
        layout.addWidget(self.button1)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()
    
    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def Volver(self):
        self.close()
        self.window = LoginWindow()
        self.window.show()

class CambioDatos(QWidget):
    def __init__(self,dni, usuario, contraseña):
        super().__init__()
        self.setWindowTitle('Cambiar datos personales')
        self.setMinimumSize(600, 600)
        self.center()
        self.initUI()

        """Traigo el valor de DNI, usuario y contraseña desde MainWindow"""
        self.dni=dni
        self.usuario=usuario
        self.contraseña=contraseña

    def initUI(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Label
        label_atributo= QLabel("Ingrese el atributo a cambiar:")
        label_valor = QLabel("Ingrese el valor por el que desea modificar")
        self.label_confirmado = QLabel("El dato ha sido cambiado satisfactoriamente", central_widget)
        self.label_confirmado.setStyleSheet("color: green")
        self.label_confirmado.hide()
        
        """Creacion de combo box con sus opciones e input box para el atributo y el valor a cambiar"""
        self.combo_atributo = QComboBox(self)
        self.input_valor = QLineEdit(central_widget)

        self.combo_atributo.addItem("DNI")
        self.combo_atributo.addItem("Nombre")
        self.combo_atributo.addItem("Apellido")
        self.combo_atributo.addItem("Fecha de nacimiento")
        self.combo_atributo.addItem("Email")
        self.combo_atributo.addItem("Contraseña")

        """Se agregan los widgets al layout"""
        layout.addWidget(label_atributo)
        layout.addWidget(self.combo_atributo)
        layout.addWidget(label_valor)
        layout.addWidget(self.input_valor)
        layout.addWidget(self.label_confirmado)

        """Creacion de botones para continuar hacia validación y volver a pagina anterior"""
        self.button = QPushButton("Continuar")
        self.button.clicked.connect(self.ClickContinuar)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Volver")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        """Se aplica el estilo a la ventana"""
        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        center_point = screen_geometry.center()

        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def show_confirmado(self):
        self.label_confirmado.show()

    def Volver(self):
        self.close()
        self.window = MainWindow(self.dni, self.usuario, self.contraseña)
        self.window.show()    

    def openOperacionRealizada(self, dni, usuario, contraseña):
        self.window1 = OperacionRealizadaUsuario(dni, usuario, contraseña)
        self.window1.show()

    def PlaceholderText(self, text):
        self.input_valor.clear()
        self.input_valor.setPlaceholderText(text)
        palette = self.input_valor.palette()
        placeholder_color = QColor(255, 0, 0)  # Red color
        palette.setColor(QPalette.PlaceholderText, placeholder_color)
        self.input_valor.setPalette(palette)

    def ClickContinuar(self):
        atributo= self.combo_atributo.currentText().strip().lower()
        valor = self.input_valor.text()     

        match atributo:

            case 'dni':
                if val.validardni(valor)==False:
                        self.PlaceholderText("Ingrese DNI válido")
                else:
                        Usuarios.diccUsuarios[self.dni].cambiar_dato(self.dni,atributo,valor)
                        util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
                        self.show_confirmado()  
                        self.close()
                        self.openOperacionRealizada(self.dni, self.usuario, self.contraseña)

            case 'nombre':
                    if val.validarnombre(valor)==False:
                        self.PlaceholderText("Ingrese un nombre válido (sin números ni caracteres especiales)")
                    else:
                        Usuarios.diccUsuarios[self.dni].cambiar_dato(self.dni,atributo,valor)
                        util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
                        self.show_confirmado()
                        self.close()
                        self.openOperacionRealizada(self.dni, self.usuario, self.contraseña)

            case 'apellido':
                if val.validarnombre(valor)==False:
                        self.PlaceholderText("Ingrese un apellido válido (sin números ni caracteres especiales)")
                else:
                        Usuarios.diccUsuarios[self.dni].cambiar_dato(self.dni,atributo,valor)
                        util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
                        self.show_confirmado()
                        self.close()
                        self.openOperacionRealizada(self.dni, self.usuario, self.contraseña)

            case 'fecha de nacimiento':  
                if val.validarFecha(valor)==False:
                        self.PlaceholderText("Ingrese una fecha de nacimiento válida (debe ser mayor de edad)")
                else:
                        Usuarios.diccUsuarios[self.dni].cambiar_dato(self.dni,atributo,valor)
                        util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
                        self.show_confirmado()
                        sef.close()
                        self.openOperacionRealizada(self.dni, self.usuario, self.contraseña)

            case 'email':
                if val.validaremail(valor)==False:
                        self.PlaceholderText("Ingrese un email válido")
                else:
                        Usuarios.diccUsuarios[self.dni].cambiar_dato(self.dni,atributo,valor)
                        util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
                        self.show_confirmado()
                        self.close()
                        self.openOperacionRealizada(self.dni, self.usuario, self.contraseña)
              
            case 'contraseña':
                if val.validarcontraseña(valor)==False:
                        self.PlaceholderText("Ingrese una contraseña válida")
                else:
                        
                        Usuarios.diccUsuarios[self.dni].cambiar_dato(self.dni,atributo,valor)
                        util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
                        self.show_confirmado()
                        self.close()
                        self.openOperacionRealizada(self.dni, self.usuario, self.contraseña)

class EliminarUsuario(QWidget):
    def __init__(self, dni, usuario, contraseña):
        super().__init__()
        self.setWindowTitle("Eliminar usuario")
        self.setMinimumSize(600,600)
        self.center()
        self.initUI()

        """Traigo desde MainWindow el valor de DNI, usuario y contraseña"""
        self.dni=dni
        self.usuario=usuario
        self.contraseña=contraseña

    def initUI(self):
        layout = QVBoxLayout()

        # Label
        label_dni = QLabel("Ingresa tu DNI:")
        label_contra1 = QLabel("Ingresa tu Contraseña:")
        label_contra2 = QLabel("Confirma tu Contraseña:")
        
        # Input Box
        self.input_dni = QLineEdit()
        self.input_contra1= QLineEdit()
        self.input_contra2= QLineEdit()

        layout.addWidget(label_dni)
        layout.addWidget(self.input_dni)
        layout.addWidget(label_contra1)
        layout.addWidget(self.input_contra1)
        layout.addWidget(label_contra2)
        layout.addWidget(self.input_contra2)

        self.error_label=QLabel()
        self.error_label.hide()
        layout.addWidget(self.error_label)

        self.button = QPushButton("Continuar")
        self.button.clicked.connect(self.confirmButtonClicked)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Volver")
        self.button2.clicked.connect(self.Volver)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        with open('Estilo.qss', 'r') as est:
            style = est.read()
            self.setStyleSheet(style)        
        self.show()
    
    def center(self):
        # Get the screen's geometry
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        # Calculate the center point
        center_point = screen_geometry.center()

        # Adjust the window position
        new_x = int(center_point.x() - window_geometry.width() / 2)
        new_y = int(center_point.y() - window_geometry.height() / 2)
        self.move(new_x, new_y)

    def showError(self, text, color):
        self.error_label.clear()
        self.error_label.setText(text)
        coloraplicado= "color: " + color
        self.error_label.setStyleSheet(coloraplicado)
        self.error_label.show()
    
    def clearInputs(self):
        self.input_dni.clear()
        self.input_contra1.clear()
        self.input_contra2.clear()
    
    def finalizarOperacion(self):
        self.window1 = finalizarOperacionUsuario()
        self.window1.show()

    def confirmButtonClicked(self):
        dni= self.input_dni.text().strip()
        contra1=self.input_contra1.text().strip()
        contra2=self.input_contra2.text().strip()
        validado=True

        if val.validardni(dni)==False:
            validado=False
            self.showError("Ingrese un DNI válido", "red")
            self.input_dni.clear()
        
        if contra1 != contra2 or val.validarcontraseña(contra1)==False:
            validado=False
            self.showError("Las contraseñas no coinciden o es inválida", "red")
            self.input_contra1.clear()
            self.input_contra2.clear()

        if val.validarexistenciaPersona(dni, contra1, Usuarios.setdnis)==False:
            validado=False
            self.showError("Los datos no coinciden con una persona registrada", "red")
            self.clearInputs()
        else:
            self.showError("La cuenta fue eliminada exitosamente", "green")
            Usuarios.diccUsuarios[dni].darDeBajaUsuario()
            util.escribirCsv('Usuarios.csv', Usuarios.diccUsuarios)
            self.close()
            self.finalizarOperacion()

    def Volver(self):
        self.close()
        self.window = MainWindow(self.dni, self.usuario, self.contraseña)
        self.window.show() 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

