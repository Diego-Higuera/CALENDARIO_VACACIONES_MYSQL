import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QWidget, QMessageBox, QVBoxLayout, QDialog, QTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import mysql.connector
from mysql.connector import Error

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pesonalizarVentana()
        self.personalizarComponentes()

    def pesonalizarVentana(self):
        self.setWindowTitle("ADMIN")  # Crear una ventana y poner un título
        self.setFixedSize(480, 330)  # Poner un ancho y altura a la ventana y no redimensiona
        self.setStyleSheet("background-color: lightgray;")  # Color de fondo

        # Cambiar el icono de la ventana con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "data/contrasena.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))

        # Centrar la ventana en la pantalla
        self.pnlPrincipal = QWidget()  # Crear un contenedor principal
        self.setCentralWidget(self.pnlPrincipal)  # Establecer el contenedor principal para nuestra ventana

    def personalizarComponentes(self):
        self.lblSolicitud = QLabel("", self)
        self.lblSolicitud.setFont(QFont("Courier New", 10))
        self.lblSolicitud.setStyleSheet("color: #000000;")
        self.lblSolicitud.setAlignment(Qt.AlignLeft)
        self.lblSolicitud.setGeometry(100, 100, 480, 20)

        self.botAñadir = QPushButton("AÑADIR", self.pnlPrincipal)
        self.botAñadir.setFont(QFont("Courier New", 8))
        self.botAñadir.setStyleSheet("background-color: black; color: white;")
        self.botAñadir.setGeometry(190, 180, 100, 20)
        self.botAñadir.clicked.connect(self.anadirUsuario)

        self.botBorrar = QPushButton("BORRAR", self.pnlPrincipal)
        self.botBorrar.setFont(QFont("Courier New", 8))
        self.botBorrar.setStyleSheet("background-color: black; color: white;")
        self.botBorrar.setGeometry(50, 180, 100, 20)
        self.botBorrar.clicked.connect(self.borrarUsuario)

        self.botModificar = QPushButton("MODIFICAR", self.pnlPrincipal)
        self.botModificar.setFont(QFont("Courier New", 8))
        self.botModificar.setStyleSheet("background-color: black; color: white;")
        self.botModificar.setGeometry(330, 180, 100, 20)
        self.botModificar.clicked.connect(self.modificarUsuario)

        self.botMostrar = QPushButton("MOSTRAR", self.pnlPrincipal)
        self.botMostrar.setFont(QFont("Courier New", 8))
        self.botMostrar.setStyleSheet("background-color: black; color: white;")
        self.botMostrar.setGeometry(190, 220, 100, 20)
        self.botMostrar.clicked.connect(self.mostrarUsuarios)

        self.txtNombre = QLineEdit(self)
        self.txtNombre.setGeometry(120, 30, 100, 20)
        self.txtNombre.setFont(QFont("Courier New", 9))
        self.txtNombre.setAlignment(Qt.AlignLeft)
        self.txtNombre.setStyleSheet("color: blue;")

        self.lblSolicitud = QLabel("NOMBRE: ", self)
        self.lblSolicitud.setFont(QFont("Courier New", 10))
        self.lblSolicitud.setStyleSheet("color: #000000;")
        self.lblSolicitud.setAlignment(Qt.AlignLeft)
        self.lblSolicitud.setGeometry(10, 30, 80, 20)

        self.txtPassword = QLineEdit(self)
        self.txtPassword.setGeometry(120, 60, 100, 20)
        self.txtPassword.setFont(QFont("Courier New", 9))
        self.txtPassword.setAlignment(Qt.AlignLeft)
        self.txtPassword.setStyleSheet("color: blue;")

        self.lblSolicitud = QLabel("PASSWORD: ", self)
        self.lblSolicitud.setFont(QFont("Courier New", 10))
        self.lblSolicitud.setStyleSheet("color: #000000;")
        self.lblSolicitud.setAlignment(Qt.AlignLeft)
        self.lblSolicitud.setGeometry(10, 60, 80, 20)

        self.txtEmpresa = QLineEdit(self)
        self.txtEmpresa.setGeometry(120, 90, 100, 20)
        self.txtEmpresa.setFont(QFont("Courier New", 9))
        self.txtEmpresa.setAlignment(Qt.AlignLeft)
        self.txtEmpresa.setStyleSheet("color: blue;")

        self.lblSolicitud = QLabel("EMPRESA: ", self)
        self.lblSolicitud.setFont(QFont("Courier New", 10))
        self.lblSolicitud.setStyleSheet("color: #000000;")
        self.lblSolicitud.setAlignment(Qt.AlignLeft)
        self.lblSolicitud.setGeometry(10, 90, 80, 20)

        self.txtDepartamento = QLineEdit(self)
        self.txtDepartamento.setGeometry(120, 120, 100, 20)
        self.txtDepartamento.setFont(QFont("Courier New", 9))
        self.txtDepartamento.setAlignment(Qt.AlignLeft)
        self.txtDepartamento.setStyleSheet("color: blue;")

        self.lblSolicitud = QLabel("DEPARTAMENTO: ", self)
        self.lblSolicitud.setFont(QFont("Courier New", 10))
        self.lblSolicitud.setStyleSheet("color: #000000;")
        self.lblSolicitud.setAlignment(Qt.AlignLeft)
        self.lblSolicitud.setGeometry(10, 120, 110, 20)

        self.txtVacaciones = QLineEdit(self)
        self.txtVacaciones.setGeometry(350, 30, 100, 20)
        self.txtVacaciones.setFont(QFont("Courier New", 9))
        self.txtVacaciones.setAlignment(Qt.AlignLeft)
        self.txtVacaciones.setStyleSheet("color: blue;")

        self.lblSolicitud = QLabel("VACACIONES: ", self)
        self.lblSolicitud.setFont(QFont("Courier New", 10))
        self.lblSolicitud.setStyleSheet("color: #000000;")
        self.lblSolicitud.setAlignment(Qt.AlignLeft)
        self.lblSolicitud.setGeometry(250, 30, 80, 20)

        self.txtFiestas = QLineEdit(self)
        self.txtFiestas.setGeometry(350, 60, 100, 20)
        self.txtFiestas.setFont(QFont("Courier New", 9))
        self.txtFiestas.setAlignment(Qt.AlignLeft)
        self.txtFiestas.setStyleSheet("color: blue;")

        self.lblSolicitud = QLabel("FIESTAS: ", self)
        self.lblSolicitud.setFont(QFont("Courier New", 10))
        self.lblSolicitud.setStyleSheet("color: #000000;")
        self.lblSolicitud.setAlignment(Qt.AlignLeft)
        self.lblSolicitud.setGeometry(250, 60, 80, 20)

        self.txtPermisos = QLineEdit(self)
        self.txtPermisos.setGeometry(350, 90, 100, 20)
        self.txtPermisos.setFont(QFont("Courier New", 9))
        self.txtPermisos.setAlignment(Qt.AlignLeft)
        self.txtPermisos.setStyleSheet("color: blue;")

        self.lblSolicitud = QLabel("PERMISOS: ", self)
        self.lblSolicitud.setFont(QFont("Courier New", 10))
        self.lblSolicitud.setStyleSheet("color: #000000;")
        self.lblSolicitud.setAlignment(Qt.AlignLeft)
        self.lblSolicitud.setGeometry(250, 90, 80, 20)

    def obtenerDatosUsuario(self):
        return (
            self.txtNombre.text(),
            self.txtPassword.text(),
            int(self.txtVacaciones.text()),
            int(self.txtFiestas.text()),
            int(self.txtPermisos.text()),
            self.txtEmpresa.text(),
            self.txtDepartamento.text()
        )

    def borrarUsuario(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="user_data"
            )

            if conn.is_connected():
                print("Conexión exitosa a la base de datos")
        
            cursor = conn.cursor()
            # Verificar si el usuario existe
            nombre_usuario = self.txtNombre.text()
            check_query = "SELECT COUNT(*) FROM users WHERE nombre = %s"
            cursor.execute(check_query, (nombre_usuario,))
            result = cursor.fetchone()

            if result[0] == 0:
                QMessageBox.warning(self, "ADVERTENCIA", "EL USUARIO NO EXISTE")
                return
            delete_query = "DELETE FROM users WHERE nombre = %s"
            nombre_a_eliminar = self.txtNombre.text()
        
            cursor.execute(delete_query, (nombre_a_eliminar,))
            conn.commit()
            QMessageBox.information(self, "INFORMACION", "USUARIO ELIMINADO CORRECTAMENTE")
            print("Usuario eliminado exitosamente")
        
        except Error as e:
            print("Error al conectar a la base de datos", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("Conexión cerrada")
    
    def modificarUsuario(self):
        try:
            permisos = self.txtPermisos.text()
            vacaciones = self.txtVacaciones.text()
            fiestas = self.txtFiestas.text()

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="user_data"
            )

            if conn.is_connected():
                print("Conexión exitosa a la base de datos")
        
            cursor = conn.cursor()
            # Verificar si el usuario existe
            nombre_usuario = self.txtNombre.text()
            check_query = "SELECT COUNT(*) FROM users WHERE nombre = %s"
            cursor.execute(check_query, (nombre_usuario,))
            result = cursor.fetchone()

            # Validar que permisos, vacaciones y fiestas sean números
            if not permisos.isdigit() or not vacaciones.isdigit() or not fiestas.isdigit():
                QMessageBox.warning(self, "ADVERTENCIA", "Permisos, vacaciones y fiestas deben ser números")
                return

            if result[0] == 0:
                QMessageBox.warning(self, "ADVERTENCIA", "EL USUARIO NO EXISTE")
                return
            update_query = """
            UPDATE users 
            SET password = %s, vacaciones = %s, fiestas = %s, permisos = %s, empresa = %s, departamento = %s
            WHERE nombre = %s
            """
        
            datos_modificados = self.obtenerDatosUsuario()
            cursor.execute(update_query, datos_modificados[1:] + (datos_modificados[0],))
            conn.commit()
            QMessageBox.information(self, "INFORMACION", "USUARIO MODIFICADO CORRECTAMENTE")
            print("Usuario modificado exitosamente")
        
        except Error as e:
            print("Error al conectar a la base de datos", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("Conexión cerrada")
    
    def anadirUsuario(self):
        try:
            permisos = self.txtPermisos.text()
            vacaciones = self.txtVacaciones.text()
            fiestas = self.txtFiestas.text()
        

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="user_data"
            )

            if conn.is_connected():
                print("Conexión exitosa a la base de datos")
        
            cursor = conn.cursor()

            check_query = "SELECT COUNT(*) FROM users WHERE nombre = %s"
            nombre_usuario = self.txtNombre.text()
            cursor.execute(check_query, (nombre_usuario,))
            result = cursor.fetchone()

            # Validar que permisos, vacaciones y fiestas sean números
            if not permisos.isdigit() or not vacaciones.isdigit() or not fiestas.isdigit():
                QMessageBox.warning(self, "ADVERTENCIA", "Permisos, vacaciones y fiestas deben ser números")
                return

            if result[0] > 0:
                QMessageBox.warning(self, "ADVERTENCIA", "EL USUARIO YA EXISTE")
                return


            insert_query = """
            INSERT INTO users (nombre, password, vacaciones, fiestas, permisos, empresa, departamento) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
        
            nuevo_usuario = self.obtenerDatosUsuario()
            cursor.execute(insert_query, nuevo_usuario)
            conn.commit()
            QMessageBox.information(self, "INFORMACION", "USUARIO AÑADIDO CORRECTAMENTE")
            print("Usuario añadido exitosamente")
        
        except Error as e:
            print("Error al conectar a la base de datos", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("Conexión cerrada")

    def mostrarUsuarios(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="user_data"
            )

            if conn.is_connected():
                print("Conexión exitosa a la base de datos")
        
            cursor = conn.cursor()
            select_query = "SELECT * FROM users"
            cursor.execute(select_query)
            usuarios = cursor.fetchall()
        
            self.ventanaUsuarios = VentanaUsuarios(usuarios)
            self.ventanaUsuarios.exec_()
        
        except Error as e:
            print("Error al conectar a la base de datos", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("Conexión cerrada")


class VentanaUsuarios(QDialog):
    def __init__(self, usuarios):
        super().__init__()
        self.setWindowTitle("Lista de Usuarios")
        self.setFixedSize(400, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        layout.addWidget(self.textEdit)

        self.mostrarUsuarios(usuarios)

    def mostrarUsuarios(self, usuarios):
        texto = ""
        for usuario in usuarios:
            texto += f"Nombre: {usuario[1]}, Password: {usuario[2]}, Vacaciones: {usuario[3]}, Fiestas: {usuario[4]}, Permisos: {usuario[5]}, Empresa: {usuario[6]}, Departamento: {usuario[7]}\n"
        self.textEdit.setText(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

#TERMINADO EL 25/06/2024
#DIEGO HIGUERA TRIGUERO