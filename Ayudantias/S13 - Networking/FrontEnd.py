from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor


class VentanaPrincipal(QWidget):

    servidor_signal = pyqtSignal(dict)
    terminar_conexion_signal = pyqtSignal()


    def __init__(self, cliente, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre_usuario = ""
        # Ventana Chat
        self.ventana_chat = VentanaChat(self.servidor_signal, self.terminar_conexion_signal)

        # Conexion de Señales
        self.servidor_signal.connect(cliente.send)
        self.terminar_conexion_signal.connect(cliente.terminar_conexion)

        # Instancias de UI
        self.setWindowTitle("DCChat")
        self.setGeometry(400, 200, 640, 480)

        self.label_titulo = QLabel("DCChat", self)
        label_titulo_font = self.label_titulo.font()
        label_titulo_font.setBold(True)
        label_titulo_font.setPointSize(48)
        self.label_titulo.setFont(label_titulo_font)
        self.label_titulo.setStyleSheet("color: darkblue")

        self.label_usuario = QLabel("Username: ", self)
        label_usuario_font = self.label_usuario.font()
        label_usuario_font.setBold(True)
        label_usuario_font.setPointSize(12)
        self.label_usuario.setFont(label_usuario_font)
        self.label_usuario.setStyleSheet("color: darkblue")

        self.usuario_line_edit = QLineEdit("", self)
        usuario_line_edit_font = self.usuario_line_edit.font()
        usuario_line_edit_font.setPointSize(10)
        self.usuario_line_edit.setFont(usuario_line_edit_font)
        self.usuario_line_edit.setStyleSheet("color: darkblue; background: transparent")

        self.boton_usuario = QPushButton("\t\tIngresar\t\t", self)
        boton_usuario_font = self.boton_usuario.font()
        boton_usuario_font.setBold(True)
        boton_usuario_font.setPointSize(12)
        self.boton_usuario.setFont(boton_usuario_font)
        self.boton_usuario.setStyleSheet(
            "QPushButton{color: darkblue; background: transparent; border: 2px solid darkblue; border-radius: 8px}"
            "QPushButton:pressed{color: #fcf7e3; background-color: darkblue}")
        self.boton_usuario.clicked.connect(self.manejo_boton)

        # Alineación de UI
        self.init_setUp()

    def init_setUp(self):
        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(self.label_usuario)
        hbox.addWidget(self.usuario_line_edit)
        hbox.addStretch(2)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(2)
        hbox1.addWidget(self.boton_usuario)
        hbox1.addStretch(2)

        title_hbox = QHBoxLayout()
        title_hbox.addStretch(1)
        title_hbox.addWidget(self.label_titulo)
        title_hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(title_hbox)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addStretch(3)

        self.setLayout(vbox)

    def manejo_boton(self):
        if len(self.usuario_line_edit.text()) != 0:
            self.nombre_usuario = self.usuario_line_edit.text()
            self.ventana_chat.nombre_usuario = self.nombre_usuario
            mensaje = {"status": "nuevo_usuario", "data": self.nombre_usuario}
            self.servidor_signal.emit(mensaje)
            self.close()
            self.ventana_chat.show()


class VentanaChat(QWidget):
    
    def __init__(self, servidor_signal, terminar_conexion_signal, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Señales
        self.servidor_signal = servidor_signal
        self.terminar_conexion_signal = terminar_conexion_signal

        # Log
        self.chat_log = ""

        # instancias de UI
        self.setWindowTitle("DCChat")
        self.setGeometry(400, 200, 640, 480)

        self.label_titulo = QLabel("DCChat", self)
        label_titulo_font = self.label_titulo.font()
        label_titulo_font.setBold(True)
        label_titulo_font.setPointSize(48)
        self.label_titulo.setFont(label_titulo_font)
        self.label_titulo.setStyleSheet("color: darkblue")

        self.chat_log_label = QLabel("", self)
        chat_log_label_font = self.chat_log_label.font()
        chat_log_label_font.setPointSize(12)
        self.chat_log_label.setFont(chat_log_label_font)
        self.chat_log_label.setStyleSheet("color: darkblue")

        self.users_scroll = QScrollArea(self)
        self.users_scroll.setWidgetResizable(True)
        self.users_scroll.setStyleSheet("background-color: transparent")

        self.usuario_line_edit = QLineEdit("", self)
        usuario_line_edit_font = self.usuario_line_edit.font()
        usuario_line_edit_font.setPointSize(12)
        self.usuario_line_edit.setFont(usuario_line_edit_font)
        self.usuario_line_edit.setStyleSheet("color: darkblue")

        self.boton_usuario = QPushButton("\t\tEnviar\t\t", self)
        boton_usuario_font = self.boton_usuario.font()
        boton_usuario_font.setBold(True)
        boton_usuario_font.setPointSize(12)
        self.boton_usuario.setFont(boton_usuario_font)
        self.boton_usuario.setStyleSheet(
            "QPushButton{color: darkblue; background: transparent; border: 2px solid darkblue; border-radius: 8px}"
            "QPushButton:pressed{color: #fcf7e3; background-color: darkblue}")
        self.boton_usuario.clicked.connect(self.manejo_boton)

        # Alineación de UI
        self.init_setUp()

    def init_setUp(self):

        self.label_titulo.setGeometry(250, 20, 100, 50)
        self.chat_log_label.setGeometry(90, 80, 300, 300)
        self.users_scroll.setWidget(self.chat_log_label)
        self.users_scroll.setGeometry(90, 80, 300, 300)
        self.chat_log_label.setAlignment(Qt.AlignTop)
        self.usuario_line_edit.setGeometry(90, 400, 350, 50)
        self.usuario_line_edit.setFocus()
        self.boton_usuario.setGeometry(475, 400, 80, 50)

    def manejo_boton(self):
        mensaje = {"status": "mensaje", "data": {"usuario": self.nombre_usuario, 
                                                "contenido": self.usuario_line_edit.text()}}
        self.servidor_signal.emit(mensaje)
        self.usuario_line_edit.setText("")

    def actualizar_chat(self, contenido):
        print(contenido)
        self.chat_log += f"{contenido}\n"
        self.chat_log_label.setText(self.chat_log)
