import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QPushButton, QApplication, QLabel)
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from backend import PyKitchen
import os

cwd = os.getcwd()
os.chdir(f'.{os.sep}gui')
QtName, QtClass = uic.loadUiType(f"pykitchen.ui")
os.chdir(cwd)


class Cookbook(QtName, QtClass):
    def __init__(self, pykitchen):
        super().__init__()
        self.setupUi(self)
        oImage = QImage(f"gui{os.sep}pykitchen.png")
        sImage = oImage.scaled(QSize(800, 410))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.backend = pykitchen
        self.cocinarButton.clicked.connect(self.backend.cocinar)
        self.despacharButton.clicked.connect(self.backend.despachar_y_botar)
        self.guardarButton.clicked.connect(self.backend.guardar_recetas)
        self.cargarButton.clicked.connect(self.backend.cargar_recetas)
