from gui.frontend import Cookbook
from backend import PyKitchen
from testing.test_alumno import TestRecetaClass, TestComidaClass
from PyQt5.QtWidgets import QApplication
import unittest

# 0: correr menu sin gui
# 1: correr menu con gui
# 2: correr tests
mode = 2
py = PyKitchen()

if __name__ == "__main__":
    if mode == 0:

        while True:
            print(f'Elige la opción a probar:\n'
                  f'[1] - Cocinar\n'
                  f'[2] - Despachar y botar\n'
                  f'[3] - Cargar recetas\n'
                  f'[4] - Guardar recetas\n')
            eleccion = input("Escribe tu eleccion: ")

            if eleccion == '1':
                py.cocinar()
            elif eleccion == '2':
                py.despachar_y_botar()
            elif eleccion == '3':
                py.cargar_recetas()
            elif eleccion == '4':
                py.guardar_recetas()
            else:
                print('Elección invalida\n')
                continue
    elif mode == 1:
        app = QApplication([])
        py = Cookbook(py)
        py.show()
        app.exec_()
    else:
        unittest.main(verbosity=2)
