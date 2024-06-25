import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit,QMessageBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import mysql.connector
import calendario_mysql 
import csv
import admin
os

def borrar():
    with open('data/data.csv', "w") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(["1"])
    with open('data/data2.csv', "w") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(["2"])
    with open('data/data3.csv', "w") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(["3"])
    with open('data/data4.csv', "w") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(["4"])
    with open('data/data5.csv', "w") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(["5"])
    with open('data/data6.csv', "w") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(["6"])

class VentanaPython(QMainWindow):

    def __init__(self):
        super().__init__()
        self.pesonalizarVentana()
        self.personalizarComponentes()

    def pesonalizarVentana(self):
        self.setWindowTitle("LOGIN")
        self.setFixedSize(480, 330)
        self.setStyleSheet("background-color: lightgray;")
        self.pnlPrincipal = QWidget()
        self.setCentralWidget(self.pnlPrincipal)
        ruta_relativa = "data/contrasena.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))

    def personalizarComponentes(self):
        self.lblLogin = QLabel("LOGIN", self.pnlPrincipal)
        self.lblLogin.setFont(QFont("Courier New", 12))
        self.lblLogin.setStyleSheet("color: #FF0000;")
        self.lblLogin.setAlignment(Qt.AlignCenter)
        self.lblLogin.setGeometry(190, 60, 100, 20)
        self.txtLogin = QLineEdit(self.pnlPrincipal)
        self.txtLogin.setGeometry(190, 90, 100, 20)
        self.txtLogin.setFont(QFont("Courier New", 9))
        self.txtLogin.setAlignment(Qt.AlignCenter)
        self.txtLogin.setStyleSheet("color: blue;")
        self.lblPassword = QLabel("PASSWORD", self.pnlPrincipal)
        self.lblPassword.setFont(QFont("Courier New", 12))
        self.lblPassword.setStyleSheet("color: #FF0000;")
        self.lblPassword.setAlignment(Qt.AlignCenter)
        self.lblPassword.setGeometry(190, 120, 100, 20)
        self.txtPassword = QLineEdit(self.pnlPrincipal)
        self.txtPassword.setGeometry(190, 150, 100, 20)
        self.txtPassword.setFont(QFont("Courier New", 9))
        self.txtPassword.setAlignment(Qt.AlignCenter)
        self.txtPassword.setStyleSheet("color: blue;")
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.botAceptar = QPushButton("ACEPTAR", self.pnlPrincipal)
        self.botAceptar.setFont(QFont("Courier New", 8))
        self.botAceptar.setStyleSheet("background-color: black; color: white;")
        self.botAceptar.setGeometry(190, 180, 100, 20)
        self.botAceptar.clicked.connect(self.botAceptarClic)
        self.lblE = QLabel("", self)
        self.lblE.setFont(QFont("Courier New", 12))
        self.lblE.setStyleSheet("color: #FF0000;")
        self.lblE.setAlignment(Qt.AlignCenter)
        self.lblE.setGeometry(0, 250, 480, 20)

    def botAceptarClic(self):
        login = self.txtLogin.text()
        password1 = self.txtPassword.text()
        if login == "admin" and password1 == "1234":
             
            QMessageBox.information(self,"INFORMACION","ADMIN") 
            self.objeto_ventana_menu = admin.Ventana()
            self.objeto_ventana_menu.show()
            self.close()
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_data"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, vacaciones, departamento, empresa, fiestas, permisos FROM users WHERE nombre=%s AND password=%s", (login, password1))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            QMessageBox.information(self, "INFORMACION", "USUARIO CORRECTO")
            nombre, vacaciones, departamento, empresa, fiestas, permisos = result
            self.abrirVentana(nombre, vacaciones, departamento, empresa, fiestas, permisos)
            borrar()
            with open('data/data4.csv', "w") as file:
                escritor_csv = csv.writer(file)
                escritor_csv.writerow([nombre])
            with open('data/data5.csv', "w") as file:
                escritor_csv = csv.writer(file)
                escritor_csv.writerow([empresa])
            with open('data/data6.csv', "w") as file:
                escritor_csv = csv.writer(file)
                escritor_csv.writerow([departamento])
        else:
            if login != "admin" and password1 != "1234":
                QMessageBox.information(self, "INFORMACION", "USUARIO INCORRECTO")

    def abrirVentana(self, nombre, vacaciones, departamento, empresa, fiestas, permisos,):
        self.objeto_ventana_menu = calendario_mysql.Ventana(nombre, vacaciones, departamento, empresa, fiestas, permisos)
        self.objeto_ventana_menu.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPython()
    ventana.show()
    sys.exit(app.exec_())

#TERMINADO EL 25/06/2024
#DIEGO HIGUERA TRIGUERO