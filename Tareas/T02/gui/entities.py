import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QLabel, QWidget

_SCALE = 0.5
_PATH = os.path.dirname(os.path.abspath(__file__))
DEBUGGING = True


class Entity(QWidget):
    def __init__(self, base_image, parent=None):
        super().__init__(parent)
        self._base_label = QLabel(self)
        self._base_image = base_image

        self._decor_label = None
        self._decor_pixmap = None

        self.__pixmap = None

        self.__x = 50
        self.__y = 60
        self.__angle = 0
        self.setAlignment(Qt.AlignCenter)
        self.updatePixmap()
        self.setFixedSize(73 * _SCALE, 73 * _SCALE)

        if DEBUGGING:
            self.setStyleSheet("border: 1px solid black")

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        self.__angle = angle
        self.updatePixmap()

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, cord):
        self.__x = cord
        self.move(self.x, self.y)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, cord):
        self.__y = cord
        self.move(self.x, self.y)

    def add_decoration(self, path):
        if path is None:
            self._decor_label.deleteLater()
            self._decor_label = None
        else:
            self._decor_label = QLabel(self)
            self._decor_pixmap = QPixmap(path)
            self._decor_pixmap = self._decor_pixmap.scaled(
                self._decor_pixmap.width() * _SCALE,
                self._decor_pixmap.height() * _SCALE)
            self._decor_pixmap = self._decor_pixmap.transformed(
                QTransform().rotate(self.angle))
            self._decor_label.setPixmap(self._decor_pixmap)
            self._decor_label.setAlignment(Qt.AlignCenter)
            self._decor_label.show()

    def updatePixmap(self):
        path = self._base_image
        self.__pixmap = QPixmap(path)
        self.__pixmap = self.__pixmap.scaled(self.__pixmap.width() * _SCALE,
                                             self.__pixmap.height() * _SCALE)
        self.__pixmap = self.__pixmap.transformed(QTransform().rotate(
            self.angle))
        self._base_label.setPixmap(self.__pixmap)
        self.setFixedSize(self.__pixmap.width(), self.__pixmap.height())

    def setFixedSize(self, x, y):
        super().setFixedSize(x, y)
        self._base_label.setFixedSize(x, y)

    def setAlignment(self, alignment):
        self._base_label.setAlignment(alignment)


class Human(Entity):
    path = _PATH + os.sep + "assets" + os.sep + "humans" + os.sep
    LUDOPATA = "ludopata"
    KIBITZER = "kibitzer"
    DIECIOCHERO = "dieciochero"
    GANADOR = "ganador"
    MILLONARIO = "millonario"

    def __init__(self, personality, x=0, y=0, parent=None):
        super().__init__(self.path + f"human_{personality}.png", parent=parent)
        self.personality = personality
        self.x = x
        self.y = y
        self.setFixedSize(73 * _SCALE, 73 * _SCALE)

    def change_personality(self, new_perso):
        self.personality = new_perso
        self._base_image = f"{self.path}human_{self.personality}.png"
        self.updatePixmap()

    def updatePixmap(self):
        path = self._base_image
        self.__pixmap = QPixmap(path)
        self.__pixmap = self.__pixmap.scaled(self.__pixmap.width() * _SCALE,
                                             self.__pixmap.height() * _SCALE)
        self.__pixmap = self.__pixmap.transformed(QTransform().rotate(
            self.angle))
        self._base_label.setPixmap(self.__pixmap)


class Building(Entity):
    path = _PATH + os.sep + "assets" + os.sep + "buildings" + os.sep
    RESTOBAR = "restobar"
    TAROT = "tarot"
    BANOS = "baños"

    def __init__(self, type_, x=0, y=0, parent=None):
        super().__init__(self.path + f"building_{type_}.png", parent=parent)
        self.x = x
        self.y = y


class Game(Entity):
    path = _PATH + os.sep + "assets" + os.sep + "games" + os.sep
    TRAGAMONEDAS = "tragamonedas"
    RULETA = "ruleta"

    def __init__(self, type_, x=0, y=0, parent=None):
        super().__init__(self.path + f"game_{type_}.png", parent=parent)
        self.x = x
        self.y = y
