import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCalendarWidget
from PyQt5.QtGui import QIcon, QFont, QTextCharFormat, QColor, QBrush
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox, QComboBox)
import csv
import sys
import os

al_vacas = []
al_vacas2 = []
al_vacas3 = []

class Ventana(QMainWindow):# HERECIA 
    
    def __init__(self, nombre, vacaciones,departamento,empresa, fiestas, permisos):

        super().__init__()
        self.nombre = nombre
        self.vacaciones = vacaciones
        self.fiestas = fiestas
        self.permisos = permisos
        self.departamento = departamento
        self.empresa = empresa
        self.personalizarVentana()
        self.personalizarComponentes(opcionseleccionada="VACACIONES")       

    def personalizarVentana(self):

        self.setFixedSize(480, 480) # Ubicar la ventana en el centro de la pantalla no se puede redimensionar la ventana 
        self.setWindowTitle("SELECCIONE DIAS DE VACACIONES") # Título para la ventana
        self.setStyleSheet("background-color: lightgray;") # Color de fondo para la ventana
        ruta_relativa = "data/calendariopng.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizarComponentes(self, opcionseleccionada):

        self.lblSolicitud = QLabel("SOLICITUD DE: ", self)
        self.lblSolicitud.setFont(QFont("Courier New", 10))
        self.lblSolicitud.setStyleSheet("color: #000000;")
        self.lblSolicitud.setAlignment(Qt.AlignLeft)
        self.lblSolicitud.setGeometry(10, 10, 480, 20)

        self.lblSolicitud2 = QLabel("DIAS: ", self)
        self.lblSolicitud2.setFont(QFont("Courier New", 10))
        self.lblSolicitud2.setStyleSheet("color: #000000;")
        self.lblSolicitud2.setAlignment(Qt.AlignLeft)
        self.lblSolicitud2.setGeometry(300, 10, 480, 20)

        self.lblN = QLabel("NOMBRE: ", self)
        self.lblN.setFont(QFont("Courier New", 10))
        self.lblN.setStyleSheet("color: #000000;")
        self.lblN.setAlignment(Qt.AlignLeft)
        self.lblN.setGeometry(10, 30, 480, 20) 

        self.txtNombre = QLineEdit(self)
        self.txtNombre.setGeometry(120, 30, 150, 20)
        self.txtNombre.setFont(QFont("Courier New", 9))
        self.txtNombre.setAlignment(Qt.AlignLeft)
        self.txtNombre.setStyleSheet("color: blue;")
        self.txtNombre.setText(str(self.nombre))
        self.txtNombre.setReadOnly(True)  

        self.lblE = QLabel("EMPRESA: ", self)
        self.lblE.setFont(QFont("Courier New", 10))
        self.lblE.setStyleSheet("color: #000000;")
        self.lblE.setAlignment(Qt.AlignLeft)
        self.lblE.setGeometry(10, 50, 480, 20)  

        self.txtEmpresa = QLineEdit(self)
        self.txtEmpresa.setGeometry(120, 50, 150, 20)
        self.txtEmpresa.setFont(QFont("Courier New", 9))
        self.txtEmpresa.setAlignment(Qt.AlignLeft)
        self.txtEmpresa.setStyleSheet("color: blue;")
        self.txtEmpresa.setText(str(self.empresa))
        self.txtEmpresa.setReadOnly(True)

        self.lblD = QLabel("DEPARTAMENTO: ", self)
        self.lblD.setFont(QFont("Courier New", 10))
        self.lblD.setStyleSheet("color: #000000;")
        self.lblD.setAlignment(Qt.AlignLeft)
        self.lblD.setGeometry(10, 70, 480, 20)

        self.txtDepartamento = QLineEdit(self)
        self.txtDepartamento.setGeometry(120, 70, 150, 20)
        self.txtDepartamento.setFont(QFont("Courier New", 9))
        self.txtDepartamento.setAlignment(Qt.AlignLeft)
        self.txtDepartamento.setStyleSheet("color: blue;")
        self.txtDepartamento.setText(str(self.departamento))
        self.txtDepartamento.setReadOnly(True)

        self.lblFecha = QLabel("AQUI SE PONE LA FECHA SELECCIONADA", self)
        self.lblFecha.setFont(QFont("Courier New", 12))
        self.lblFecha.setStyleSheet("color: #FF0000;")
        self.lblFecha.setAlignment(Qt.AlignCenter)
        self.lblFecha.setGeometry(0, 410, 480, 20) 

        self.calendario = QCalendarWidget(self)
        self.calendario.setGridVisible(True)
        self.calendario.setGeometry(10, 100, 460, 250)
        self.calendario.clicked[QDate].connect(self.mostrarFechaSeleccionada)

        self.btoSalir = QPushButton("SALIR", self)
        self.btoSalir.setGeometry(380, 380, 80, 20)
        self.btoSalir.setFont(QFont("Courier New", 0, 8))
        self.btoSalir.setStyleSheet("background-color: black; color: white;")
        self.btoSalir.clicked.connect(self.salir)

        self.btoBuscar = QPushButton("ENVIAR", self)
        self.btoBuscar.setGeometry(20, 380, 80, 20)
        self.btoBuscar.setFont(QFont("Courier New", 0, 8))
        self.btoBuscar.setStyleSheet("background-color: black; color: white;")
        self.btoBuscar.clicked.connect(self.enviar) 

        self.txtFecha2 = QLineEdit(self)
        self.txtFecha2.setGeometry(300, 30, 60, 20)
        self.txtFecha2.setFont(QFont("Courier New", 9))
        self.txtFecha2.setAlignment(Qt.AlignLeft)
        self.txtFecha2.setStyleSheet("color: blue;")
        self.txtFecha2.setReadOnly(True)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Vacaciones", "Fiestas locales", "Otros permisos"])
        self.comboBox.setCurrentIndex(0)  # Opción por defecto
        self.comboBox.setGeometry(370, 30, 100, 20)                                                                    
        
    def mostrarFechaSeleccionada(self, fecha):
        festivos = ["25/12/2024","01/01/2024", "29/03/2024","01/05/2024","15/08/2024","12/10/2024","01/11/2024","06/12/2024"]
        fecha_str = "{:02d}/{:02d}/{:04d}".format(fecha.day(), fecha.month(), fecha.year(),id)  
        if fecha_str in festivos:
            QMessageBox.information(self,"INFORMACION","DIAS FESTIVO")
        else:
            opcion_seleccionada = self.comboBox.currentText()
            if opcion_seleccionada == "Vacaciones":
                fecha_str = "{:02d}/{:02d}/{:04d}".format(fecha.day(), fecha.month(), fecha.year(),id)   
                if fecha_str not in al_vacas and fecha_str not in al_vacas2 and fecha_str not in al_vacas3:
                    al_vacas.append(fecha_str)
                    self.vacaciones = self.vacaciones - 1
                    self.txtFecha2.setText(str(self.vacaciones))
                    self.lblFecha.setText(fecha_str)
                    for i in range (len(al_vacas)):
                        self.marcarDiaCalendario()
                        if self.vacaciones < 0:
                            self.vacaciones = 0
                            self.txtFecha2.setText(str(self.vacaciones))
                            self.lblFecha.setText("DIAS INSUFICIENTES")
                            QMessageBox.information(self,"INFORMACION","DIAS INSUFICIENTES")
                            al_vacas.remove(fecha_str) 
                            self.NoMarcarDiaCalendario()
                            break
                else:
                    self.EliminarDias(fecha_str)

            elif opcion_seleccionada == "Fiestas locales":
                fecha_str = "{:02d}/{:02d}/{:04d}".format(fecha.day(), fecha.month(), fecha.year(),id)   
                if fecha_str not in al_vacas and fecha_str not in al_vacas2 and fecha_str not in al_vacas3:
                    al_vacas2.append(fecha_str)
                    self.fiestas = self.fiestas - 1
                    self.txtFecha2.setText(str(self.fiestas))
                    self.lblFecha.setText(fecha_str)
                    for i in range (len(al_vacas2)):
                        self.marcarDiaCalendario2()
                        if self.fiestas < 0:
                            self.fiestas = 0
                            self.txtFecha2.setText(str(self.fiestas))
                            self.lblFecha.setText("DIAS INSUFICIENTES")
                            QMessageBox.information(self,"INFORMACION","DIAS INSUFICIENTES")
                            al_vacas2.remove(fecha_str) 
                            self.NoMarcarDiaCalendario()
                            break
                else:
                    self.EliminarDias(fecha_str)

            elif opcion_seleccionada == "Otros permisos":
                fecha_str = "{:02d}/{:02d}/{:04d}".format(fecha.day(), fecha.month(), fecha.year(),id)   
                if fecha_str not in al_vacas and fecha_str not in al_vacas2 and fecha_str not in al_vacas3:
                    al_vacas3.append(fecha_str)
                    self.permisos = self.permisos - 1
                    self.txtFecha2.setText(str(self.permisos))
                    self.lblFecha.setText(fecha_str)
                    for i in range (len(al_vacas3)):
                        self.marcarDiaCalendario3()
                        if self.permisos < 0:
                            self.permisos = 0
                            self.txtFecha2.setText(str(self.permisos))
                            self.lblFecha.setText("DIAS INSUFICIENTES")
                            QMessageBox.information(self,"INFORMACION","DIAS INSUFICIENTES")
                            al_vacas3.remove(fecha_str) 
                            self.NoMarcarDiaCalendario()
                            break
                else:
                    self.EliminarDias(fecha_str)

    def marcarDiaCalendario(self):
        select_format = QTextCharFormat()
        select_format.setBackground(QBrush(QColor("lightgreen")))
        self.calendario.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendario.setDateTextFormat(self.calendario.selectedDate(),select_format)

    def marcarDiaCalendario2(self):
        select_format = QTextCharFormat()
        select_format.setBackground(QBrush(QColor("lightblue")))
        self.calendario.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendario.setDateTextFormat(self.calendario.selectedDate(),select_format)

    def marcarDiaCalendario3(self):
        select_format = QTextCharFormat()
        select_format.setBackground(QBrush(QColor("lightpink")))
        self.calendario.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendario.setDateTextFormat(self.calendario.selectedDate(),select_format)

    def NoMarcarDiaCalendario(self):
        select_format = QTextCharFormat()
        select_format.setBackground(QBrush(QColor("lightgrey")))
        self.calendario.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendario.setDateTextFormat(self.calendario.selectedDate(),select_format)  

    def EliminarDias(self,fecha_str):
        if fecha_str in al_vacas:
            al_vacas.remove(fecha_str)
            self.vacaciones = self.vacaciones + 1
            self.txtFecha2.setText(str(self.vacaciones))
            self.lblFecha.setText("DIA ELIMINADO")
            self.NoMarcarDiaCalendario()
        if fecha_str in al_vacas2:
            al_vacas2.remove(fecha_str)
            self.fiestas = self.fiestas + 1
            self.txtFecha2.setText(str(self.fiestas))
            self.lblFecha.setText("DIA ELIMINADO")
            self.NoMarcarDiaCalendario()
        if fecha_str in al_vacas3:
            al_vacas3.remove(fecha_str)
            self.permisos = self.permisos + 1
            self.txtFecha2.setText(str(self.permisos))
            self.lblFecha.setText("DIA ELIMINADO")
            self.NoMarcarDiaCalendario() 

    def enviar(self):
        with open('data/data.csv', mode="w",newline="") as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow(al_vacas)
        with open('data/data2.csv', mode="w",newline="") as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow(al_vacas2)
        with open('data/data3.csv', mode="w",newline="") as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow(al_vacas3)
        ruta_relativa = "generar_pdf.py"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        os.system(f"python {ruta_absoluta}")
        ruta_relativa2 = "generar_correo.py"
        ruta_absoluta2 = os.path.abspath(ruta_relativa2)
        os.system(f"python {ruta_absoluta2}")
        self.close()
        sys.exit()

    def salir(self):
        sys.exit()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

#TERMINADO EL 25/06/2024
#DIEGO HIGUERA TRIGUERO