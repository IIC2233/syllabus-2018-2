import json
import re
from time import sleep

import requests

from credenciales import API_KEY


API_URL = "https://api.nasa.gov/planetary/apod"
DIR_IMAGENES = 'imagenes'
PATH_RESULTADOS = 'resultados.txt'


def limpiar_fecha(linea):
    '''
    Esta función se encarga de limpiar el texto introducido a las fechas

    :param linea: str
    :return: str
    '''
    pass


def chequear_fecha(fecha):
    '''
    Esta función debe chequear si la fecha cumple el formato especificado

    :param fecha: str
    :return: bool
    '''
    pass


def obtener_fechas(path):
    '''
    Esta función procesa las fechas para devolver aquellas que son útiles
    para realizar las consultas a la API

    :param path: str
    :return: iterable
    '''
    pass


def obtener_info(fecha):
    '''
    Recibe una fecha y retorna un diccionario
    con el título, la fecha y el url de la imagen
    :param fecha: str
    :return: dict
    '''
    pass


def escribir_respuesta(datos):
    '''
    Esta función debe escribir las respuestas de la API en el archivo
    resultados.txt

    :param datos_respuesta: dict
    '''
    pass


def descargar_imagen(url, path):
    '''
    Recibe la url de una imagen y guarda los datos en un archivo en path

    :param url: str
    :param path: str
    '''
    respuesta = requests.get(url, stream=True)
    if respuesta.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in respuesta:
                f.write(chunk)


if __name__ == "__main__":
    PATH_FECHAS = 'fechas_secretas.txt'

    for fecha in obtener_fechas(PATH_FECHAS):
        respuesta = obtener_info(fecha)
        escribir_respuesta(respuesta)
