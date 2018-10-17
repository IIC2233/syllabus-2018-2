import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from backend import CountChecker, Character


class MainWindow(QWidget):

    check_count_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)

        self.name_label = QLabel('Apriete "Jugar" 5 veces para comenzar', self)
        self.contador_label = QLabel('0', self)
        self.main_game_button = QPushButton('Jugar', self)
        self.contador = 0

        # Se conecta el boton con la función check_count
        self.main_game_button.clicked.connect(self.check_count)

        # Se Instancia el CountChecker.
        self.spell_checker = CountChecker(self)
        self.check_count_signal.connect(self.spell_checker.check)

        vbox = QVBoxLayout()
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.contador_label)
        vbox.addWidget(self.main_game_button)
        self.setLayout(vbox)

    def check_count(self):
        """
        Función que incrementa el contador y envía una señal al CheckCount con la cuenta.
        También actualiza el label del contador.
        :return: none
        """
        self.contador += 1
        self.contador_label.setText(str(self.contador))
        self.check_count_signal.emit(self.contador)

    def open_window(self, state):
        """
        Función que dado un estado, cambia la ventana de inicio por la del juego.
        :param state: bool
        :return: none
        """
        if state:
            self.hide()
            self.maingame = MainGame()
            self.maingame.show()


class MainGame(QWidget):

    move_character_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)

        self._frame = 1

        # Se setea la imagen de fondo.
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('sprite/background.png'))

        # Se instancia el personaje del backend y se conecta move_character_signal con la función
        # move de Character.
        self.backend_character = Character(self, 0, 485)
        self.move_character_signal.connect(self.backend_character.move)

        # Se crea el personaje en el frontend.
        self.front_character = QLabel(self)
        self.front_character.setPixmap(QPixmap('sprite/Super MarioR.png'))
        self.front_character.move(0, 485)

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        if value > 3:
            self._frame = 1
        else:
            self._frame = value

    def keyPressEvent(self, e):
        """
        Dada la presión de una tecla se llama a esta función. Al apretarse una tecla chequeamos si
        esta dentro de las teclas del control del juego y de ser así, se envía una señal al backend
        con la acción además de actualizar el sprite.
        :param e: QKeyEvent
        :return:
        """
        self.frame += 1
        if e.key() == Qt.Key_D:
            self.front_character.setPixmap(QPixmap(f'sprite/Super Mario - Walk{self.frame}.png'))
            self.move_character_signal.emit('R')
        if e.key() == Qt.Key_A:
            self.front_character.setPixmap(QPixmap(f'sprite/Super Mario - Walk{self.frame}L.png'))
            self.move_character_signal.emit('L')
        if e.key() == Qt.Key_Space:
            self.front_character.setPixmap(QPixmap(f'sprite/Super Mario - Jump{self.backend_character.direction}.png'))
            self.move_character_signal.emit('Jump')
        if e.key() == Qt.Key_S:
            self.front_character.setPixmap(QPixmap(f'sprite/Super Mario - Duck{self.backend_character.direction}.png'))

    def keyReleaseEvent(self, e):
        """
        Dado que se deje de presionar una tecla se llama a esta función. Al apretarse una tecla chequeamos si
        esta dentro de las teclas del control del juego y de ser así, se actualiza el sprite.
        :param e: QKeyEvent
        :return:
        """
        if e.key() == Qt.Key_S:
            self.front_character.setPixmap(QPixmap(f'sprite/Super Mario{self.backend_character.direction}.png'))

    def update_position(self, event):
        """
        Función que recibe un diccionario con las cordenadas del personaje y las actualiza en el
        frontend.
        :param event: dict
        :return: none
        """
        self.front_character.move(event['x'], event['y'])


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())