from banda import Banda
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from opciones import *
from datetime import datetime
import sys
import os


class VentanaMaestra(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Las Mejores Bandas de Argentina")
        self.setGeometry(100, 100, 1000, 700)
        
        #QGridLayout va a ayudar a posicionar con mayor facilidad las etiquetas y botones, al definir una grilla con índices donde se ingresarán estos objetos
        layoutPrincipal = QGridLayout()
        
        opciones = ["1. Grabar en un archivo txt la cantidad de bandas y el nombre de su solista de un barrio",
                    "2. Grabar en un archivo txt el promedio de bandas inscritas por barrio hasta una fecha",
                    "3. Visualizar para cada barrio, según el género musical más tocado, la personalidad que prevalece",
                    "4. Visualizar la información de una banda ingresando el nombre solista",
                    "5. Visualizar los barrios (ordenados en forma decreciente por cantidad de bandas)",
                    "6. Visualizar la cantidad de bandas por barrio (ordenado por barrio alfabéticamente)",
                    "7. Almacenar y mostrar la cantidad de bandas, discos y la cantidad de integrantes por género musical",
                    "8. Grabar en un archivo txt el promedio de integrantes por género musical",
                    "9. Visualizar gráficamente las 10 primeras bandas con más presencia en las redes sociales",
                    "10. Grabar en un archivo txt de cada barrio cual es el género de música que las bandas tocan más",
                    "11. Dado un año mostrar gráficamente la cantidad de bandas inscritas por mes y el género predominante",
                    "12. Determinar cual es el género musical más común de las bandas inscritas en un determinado periodo de tiempo",
                    "13. Visualizar para cada genero musical los diferentes estilos que este posee y cual es el género que tiene más estilos",
                    "14. Grabar en un archivo txt las bandas que hayan grabado discos hasta una determinada fecha",
                    "15. Salir"]
        
        #Las etiquetas son estáticas y no van a devolver nada al interaccionar con ellas, así que las creamos con un ciclo sin importar de después poder 
        # acceder a ellas a través de atributos de la instancia
        for idx, opcion in enumerate(opciones):
            layoutPrincipal.addWidget(QLabel(opcion), idx, 0)
        
        seleccionOpcion1, seleccionOpcion2, seleccionOpcion3 = QPushButton(), QPushButton(), QPushButton()
        seleccionOpcion4, seleccionOpcion5, seleccionOpcion6 = QPushButton(), QPushButton(), QPushButton()
        seleccionOpcion7, seleccionOpcion8, seleccionOpcion9 = QPushButton(), QPushButton(), QPushButton()
        seleccionOpcion10, seleccionOpcion11, seleccionOpcion12 = QPushButton(), QPushButton(), QPushButton()
        seleccionOpcion13, seleccionOpcion14, seleccionOpcion15 = QPushButton(), QPushButton(), QPushButton()
        
        botonesSeleccion = [seleccionOpcion1, seleccionOpcion2, seleccionOpcion3, seleccionOpcion4, seleccionOpcion5,
                            seleccionOpcion6, seleccionOpcion7, seleccionOpcion8, seleccionOpcion9, seleccionOpcion10,
                            seleccionOpcion11, seleccionOpcion12, seleccionOpcion13, seleccionOpcion14, seleccionOpcion15]
        
        #Vamos a tener varios objetos llamando a la función opcionElegida, por lo cuál tenemos que crear funciones lambda para poder 
        #pasar los valores requeridos a través de los argumentos de la función y así conocer qué opción fue elegida al presionar cierto botón
        #Además definimos características y posiciones en el layout de todos los botones
        for idx, boton in enumerate(botonesSeleccion):
            folder_path = os.path.dirname(__file__)
            boton.setIcon(QIcon(f'{folder_path}/arrow-right.png')) #Icono que se agrega al botón hallado en la misma carpeta este script
            boton.setIconSize(QSize(60, 60))
            boton.pressed.connect(lambda num_opcion=idx+1: self.opcionElegida(num_opcion))
            layoutPrincipal.addWidget(boton, idx, 1)
        
        seleccionOpcion15.setShortcut("esc") #Se puede salir del programa con escape o apretando botones de la interfaz
        
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)
        
    #Usamos self sobre las ventanas para no perder la referencia y no se cierren al instante. No usamos match-case porque no tenemos python 3.10
    def opcionElegida(self, num_opcion):
        mostrarVentana = True
        if num_opcion == 1: 
            self.nueva_ventana = VentanaOpcion1()
        if num_opcion == 2: 
            self.nueva_ventana = VentanaOpcion2()
        if num_opcion == 3: 
            self.nueva_ventana = VentanaTabla(opcion3(), "Personalidad predominante por barrio")
        if num_opcion == 4: 
            self.nueva_ventana = VentanaOpcion4()
        if num_opcion == 5: 
            self.nueva_ventana = VentanaTabla(opcion5(), "Barrios ordenados por cantidad de bandas")
        if num_opcion == 6: 
            self.nueva_ventana = VentanaTabla(opcion6(), "Barrios ordenados alfabeticamente")
        if num_opcion == 7: 
            self.nueva_ventana = VentanaTabla(opcion7(), "Cantidad de bandas, discos e integrantes por género musical")
        if num_opcion == 8: 
            self.nueva_ventana = VentanaTabla(opcion8(), "Promedio de integrantes por género musical")
        if num_opcion == 9: 
            opcion9()
            mostrarVentana = False
        if num_opcion == 10: 
            self.nueva_ventana = VentanaTabla(opcion10(), "Género musical predominante por barrio")
        if num_opcion == 11: 
            self.nueva_ventana = VentanaOpcion11()
        if num_opcion == 12: 
            self.nueva_ventana = VentanaOpcion12()
        if num_opcion == 13: 
            data = opcion13()
            self.nueva_ventana = VentanaTabla(data[1:], "Estilos por género musical")
            self.ventana_resultado = VentanaTexto(data[0][0], f"Resultado") #Mostramos el resultado único en una ventana aparte
            self.ventana_resultado.show()
        if num_opcion == 14: 
            self.nueva_ventana = VentanaOpcion14()
        if num_opcion == 15:
            self.close()
            mostrarVentana = False
        
        #Se puede dar el caso que lo accionado no es un QMainWindow, como la opción 9 que va a devolver un gráfico de matplotlib, 
        # así que llamar una ventana no existente arrojaría un error
        if mostrarVentana:
            self.nueva_ventana.show()
        

class VentanaOpcion1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OPCION 1")
        self.setGeometry(900, 300, 500, 250)
        
        layoutPrincipal = QVBoxLayout()
        
        layoutBarrio = QHBoxLayout()
        self.labelBarrio = QLabel("Barrio: ")
        layoutBarrio.addWidget(self.labelBarrio)
        
        names = Banda.barrios
        completer = QCompleter(names) #Este objeto QCompleter acelera la introducción de datos del usuario al ayudarlo con la autocompletado
        completer.setCaseSensitivity(Qt.CaseInsensitive) # Volvemos la búsqueda para autocompletar no sensible a mayúsculas

        self.lineEditBarrio = QLineEdit()
        self.lineEditBarrio.setCompleter(completer)
        self.lineEditBarrio.returnPressed.connect(self.seleccionarBarrio) #Acepta la tecla Enter para confirmar el input
        layoutBarrio.addWidget(self.lineEditBarrio)
        
        layoutPrincipal.addLayout(layoutBarrio)
        
        self.botonSeleccionarBarrio = QPushButton()
        self.botonSeleccionarBarrio.setText("Aceptar")
        self.botonSeleccionarBarrio.clicked.connect(self.seleccionarBarrio)
        self.botonSeleccionarBarrio.setShortcut("Return")
        layoutPrincipal.addWidget(self.botonSeleccionarBarrio)
        
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)
    
    #Podemos acceder a este método llenando el campo de texto y apretando Enter, o apretando el botón Aceptar en la interfaz
    def seleccionarBarrio(self):
        barrio = self.lineEditBarrio.text().upper()
        
        if barrio in Banda.barrios:
            data = opcion1(barrio)
            self.nueva_ventana = VentanaTabla(data[1:], f"Bandas de {barrio}")
            self.nueva_ventana.show()
            self.ventana_resultado = VentanaTexto(data[0][0], f"Resultado")
            self.ventana_resultado.show()
            self.close() #Una vez que corrimos la opcion, la cerramos. Si se quiere ver el resultado con otro input en la opción, hay que volver a iniciarla
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Barrio no hallado en los registros")
            msg.setWindowTitle("Error")
            msg.exec_()
        

class VentanaOpcion2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OPCION 2")
        self.setGeometry(500, 100, 1000, 700)
        
        layoutPrincipal = QVBoxLayout()
        
        self.labelFecha = QLabel("Seleccione una fecha limite")
        layoutPrincipal.addWidget(self.labelFecha)
        
        self.calendario = QCalendarWidget()
        fecha_min, fecha_max = min(Banda.fechas), max(Banda.fechas)
        # No se debe permitir al usuario ingresar fechas que no están en los registros, por ello usamos el método setDateRange que inhabilita las fechas no existentes
        self.calendario.setDateRange(QDate(fecha_min.year, fecha_min.month, fecha_min.day), QDate(fecha_max.year, fecha_max.month, fecha_max.day))
        self.calendario.clicked.connect(self.obtenerFecha)
        layoutPrincipal.addWidget(self.calendario)
        
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)
    
    
    def obtenerFecha(self):
        fecha = self.calendario.selectedDate()
        fecha = QDate.toPyDate(fecha) #Este método devuelve un objeto de tipo datetime.date con formato %Y-%m-%d, y lo tenemos que convertir a datetime.datetime
        fecha = datetime.strptime(str(fecha), "%Y-%m-%d")
        self.nueva_ventana = VentanaTexto(opcion2(fecha), "Resultado")
        self.nueva_ventana.show()
        self.close()


class VentanaOpcion4(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OPCION 4")
        self.setGeometry(900, 300, 500, 250)
        
        layoutPrincipal = QVBoxLayout()
        
        layoutBanda = QHBoxLayout()
        self.labelBanda = QLabel("Banda / Nombre solista: ")
        layoutBanda.addWidget(self.labelBanda)
        
        nombres = Banda.nombre_bandas
        completer = QCompleter(nombres)
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.lineEditBandas = QLineEdit()
        self.lineEditBandas.setCompleter(completer)
        self.lineEditBandas.returnPressed.connect(self.seleccionarBanda)
        layoutBanda.addWidget(self.lineEditBandas)
        
        layoutPrincipal.addLayout(layoutBanda)
        
        self.botonSeleccionarBanda = QPushButton()
        self.botonSeleccionarBanda.setText("Aceptar")
        self.botonSeleccionarBanda.clicked.connect(self.seleccionarBanda)
        layoutPrincipal.addWidget(self.botonSeleccionarBanda)
        
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)
    
    #Podemos acceder a este método llenando el campo de texto y apretando Enter, o apretando el botón Aceptar en la interfaz
    def seleccionarBanda(self):
        nombreBanda = self.lineEditBandas.text().upper()
        
        if nombreBanda in Banda.nombre_bandas:
            self.nueva_ventana = VentanaTexto(opcion4(nombreBanda), f"Datos de la banda {nombreBanda}")
            self.nueva_ventana.show()
            self.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Banda no hallada en los registros")
            msg.setWindowTitle("Error")
            msg.exec_()


class VentanaOpcion11(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OPCION 11")
        self.setGeometry(900, 300, 300, 150)
        
        layoutPrincipal = QVBoxLayout()
        
        layoutAnio = QHBoxLayout()
        self.labelAnio = QLabel("Anio: ")
        layoutAnio.addWidget(self.labelAnio)
        
        self.spinBoxAnio = QSpinBox()
        anio_min, anio_max = min(fecha.year for fecha in Banda.fechas), max(fecha.year for fecha in Banda.fechas)
        self.spinBoxAnio.setMinimum(anio_min)
        self.spinBoxAnio.setMaximum(anio_max)
        layoutAnio.addWidget(self.spinBoxAnio)
        
        layoutPrincipal.addLayout(layoutAnio)
        
        self.botonSeleccionarAnio = QPushButton()
        self.botonSeleccionarAnio.setText("Aceptar")
        self.botonSeleccionarAnio.clicked.connect(self.botonSeleccionarAnio_click)
        layoutPrincipal.addWidget(self.botonSeleccionarAnio)
        
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)
    
    
    def botonSeleccionarAnio_click(self):
        anio = self.spinBoxAnio.value()
        opcion11(anio)
        self.close()


class VentanaOpcion12(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OPCION 12")
        self.setGeometry(500, 100, 100, 100)
        
        layoutPrincipal = QVBoxLayout()
        
        layoutFechaInicial = QHBoxLayout()
        self.labelFechaInicial = QLabel("Fecha inicial: ")
        layoutFechaInicial.addWidget(self.labelFechaInicial)
        self.editorFechaInicial = QDateEdit()
        self.editorFechaInicial.setMinimumDate(min(fecha for fecha in Banda.fechas))
        self.editorFechaInicial.setMaximumDate(max(fecha for fecha in Banda.fechas))
        layoutFechaInicial.addWidget(self.editorFechaInicial)
        layoutPrincipal.addLayout(layoutFechaInicial)
        
        layoutFechaFinal = QHBoxLayout()
        self.labelFechaFinal = QLabel("Fecha final: ")
        layoutFechaFinal.addWidget(self.labelFechaFinal)
        self.editorFechaFinal = QDateEdit()
        self.editorFechaFinal.setMinimumDate(min(fecha for fecha in Banda.fechas))
        self.editorFechaFinal.setMaximumDate(max(fecha for fecha in Banda.fechas))
        layoutFechaFinal.addWidget(self.editorFechaFinal)
        layoutPrincipal.addLayout(layoutFechaFinal)
        
        self.botonAceptarFechas = QPushButton()
        self.botonAceptarFechas.setText("Aceptar")
        self.botonAceptarFechas.clicked.connect(self.botonAceptarFechas_click)
        layoutPrincipal.addWidget(self.botonAceptarFechas)
        
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)
    
    
    def botonAceptarFechas_click(self):
        if self.editorFechaInicial.date() >= self.editorFechaFinal.date():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ingresar una fecha final mayor a la inicial")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            fechaInicial, fechaFinal = QDate.toPyDate(self.editorFechaInicial.date()), QDate.toPyDate(self.editorFechaFinal.date())
            fechaInicial, fechaFinal = datetime.strptime(str(fechaInicial), "%Y-%m-%d"), datetime.strptime(str(fechaFinal), "%Y-%m-%d")
            self.nueva_ventana = VentanaTexto(opcion12(fechaInicial, fechaFinal), "Genero musical mas comun")
            self.nueva_ventana.show()
            self.close()


class VentanaOpcion14(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OPCION 14")
        self.setGeometry(500, 100, 1000, 700)
        
        layoutPrincipal = QVBoxLayout()
        
        self.labelAnio = QLabel("Seleccione una fecha limite")
        layoutPrincipal.addWidget(self.labelAnio)
        
        self.calendario = QCalendarWidget()
        fecha_min, fecha_max = min(Banda.fechas), max(Banda.fechas)
        self.calendario.setDateRange(QDate(fecha_min.year, fecha_min.month, fecha_min.day), QDate(fecha_max.year, fecha_max.month, fecha_max.day))
        self.calendario.clicked.connect(self.obtenerFecha_click)
        layoutPrincipal.addWidget(self.calendario)
        
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)
    
    
    def obtenerFecha_click(self):
        fecha = self.calendario.selectedDate()
        fecha = QDate.toPyDate(fecha) #Este método devuelve un objeto de tipo datetime.date con formato %Y-%m-%d, y lo tenemos que convertir a datetime.datetime
        fecha = datetime.strptime(str(fecha), "%Y-%m-%d")
        self.nueva_ventana = VentanaTabla(opcion14(fecha), f"Bandas que grabaron discos hasta el {fecha.day}/{fecha.month}/{fecha.year}")
        self.nueva_ventana.show()
        self.close()

#Esta va a ser la clase base para generar el modelo de las tablas donde se mostrarán los datos, después con la ayuda del objeto QTableView
class ModeloTabular(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.datos = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.datos[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.datos)

    def columnCount(self, index):
        return len(self.datos[0])


class VentanaTabla(QMainWindow): #Se muestran los datos en un QTableView
    def __init__(self, data, titulo):
        super().__init__()
        
        self.setWindowTitle(titulo)
        self.setGeometry(600, 200, 1000, 700)
        
        self.tabla = QTableView()
        self.modelo = ModeloTabular(data)
        self.tabla.setModel(self.modelo)
        self.setCentralWidget(self.tabla)


class VentanaTexto(QMainWindow): #Se muestran los datos en un QLabel
    def __init__(self, texto, titulo):
        super().__init__()
        
        self.setWindowTitle(titulo)
        self.setGeometry(400, 200, 100, 100)
        layoutPrincipal = QVBoxLayout()
        
        self.label = QLabel(texto)
        layoutPrincipal.addWidget(self.label)
        
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Cargamos el estilo de los widgets desde el archivo qss (Qt Style Sheet)
    with open(folder_path  + '/estilo.qss', 'r') as f:
        estilo = f.read()
    app.setStyleSheet(estilo)
    
    window = VentanaMaestra()
    window.show()
    app.exec()