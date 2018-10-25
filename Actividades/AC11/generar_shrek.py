import os
import shutil
from random import choice, randint

# Número de archivos por dir que habrá
num_por_dir = 5

# Nombre de los dir
nombres_dir_ = ["shrek{}".format(i) for i in range(num_por_dir)]

# Poner nombres de archivos
archivos = ["himno.shrek"]

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


def decode_enunciado():
    if os.path.isfile('AC11_100_REAL_NO_FAKE.pdf'):
        os.remove('AC11_100_REAL_NO_FAKE.pdf')
    with open('archivo_secreto_no_abrir.jojo', 'rb') as file:
        byts = list()
        for b in file:
            byts.append(b)
        byts[0] = byts[0][1:]
        with open('AC11.pdf', 'wb') as out:
            for i in byts:
                out.write(i)


if __name__ == "__main__":
    crear_carpetas_ocultas()
    crear_archivos_error()
    mover_archivos()
    decode_enunciado()
