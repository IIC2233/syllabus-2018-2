import threading
import time
from itertools import chain
from random import randint


def desencriptar(nombre_archivo):
    """
    Esta simple (pero útil) función te permite descifrar un archivo encriptado.
    Dado el path de un archivo, devuelve un string del contenido desencriptado.
    """

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        murcielago, numeros = "murcielago", "0123456789"
        dic = dict(chain(zip(murcielago, numeros), zip(numeros, murcielago)))
        return "".join(
            dic.get(char, char) for linea in archivo for char in linea.lower())


if __name__ == "__main__":
    pass
