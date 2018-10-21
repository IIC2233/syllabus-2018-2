import os
import shutil
from random import choice, randint

# Número de archivos por dir que habrá
num_por_dir = 5

# Nombre de los dir
nombres_dir_ = ["potato{}".format(i) for i in range(num_por_dir)]

# Poner nombres de archivos
archivos = ["marcianozurdo.pep", "marciano64.png"]

# Profundidad de carpetas que habrá
prof_l = 2


# Creo las num_por_dir ** prof_l carpetas
def crear_carpetas_ocultas(cwd=os.getcwd(),
                           lista_dir=None,
                           profundidad_lim=prof_l,
                           profundidad_actual=0):
    if lista_dir is None:
        lista_dir = nombres_dir_
    profundidad_actual += 1
    for nombre in lista_dir:
        if not os.path.exists(cwd + os.path.sep + nombre):
            os.makedirs(cwd + os.path.sep + nombre)
    if profundidad_actual < profundidad_lim:
        for directorio in os.listdir(cwd):
            try:
                if directorio in nombres_dir_:
                    crear_carpetas_ocultas(
                        cwd + "/" + directorio,
                        profundidad_actual=profundidad_actual)
            except OSError as err:
                print(err, "no debió pasar, revirsar código")


def crear_archivos_error(cwd=os.getcwd(), lista_dir=None):
    if lista_dir is None:
        lista_dir = nombres_dir_
    if not os.listdir(cwd):
        with open(cwd + "/error.asd", "w") as file:
            file.write("error" * int(randint(0, 1000)))
    for directorio in os.listdir(cwd):
        if directorio in lista_dir:
            crear_archivos_error(cwd + "/" + directorio)


def mover_archivos(cwd=os.getcwd(),
                   lista_archivos=None,
                   profundidad_lim=prof_l):
    if lista_archivos is None:
        lista_archivos = archivos
    for archivo in lista_archivos:
        move_to = cwd
        for _ in range(profundidad_lim):
            move_to += "/" + choice(nombres_dir_)
        shutil.move("{}/{}".format(cwd, archivo), "{}/{}".format(
            move_to, archivo))


crear_carpetas_ocultas()
crear_archivos_error()
mover_archivos()
'''
Una vez ejecutado esconder.py, los archivos se habrán escondido dentro
de varias subcarpetas, por lo tanto, si luego no puede encontralos y
desea continuar la actividad sin hacer esta parte puede descargalos
nuevamente desde el Syllabus.
'''
