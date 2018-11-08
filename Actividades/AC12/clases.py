import json
from datetime import datetime
from hashlib import blake2b

RECETAS_LOCK_PATH = 'RecetasLockJSON.json'
INGREDIENTES_PATH = 'ingredientes.txt'
'''
=====================================
NO BORRAR NI CAMBIAR!
'''
SUPER_SECRET_KEY = b'IIC2233'
'''
=====================================
'''


class Receta:
    """Clase que modela una receta del 'PyKitchen' cookbook"""

    def __init__(self, nombre='', ingredientes=None, alinos=None):
        self.nombre = nombre
        self.ingredientes = ingredientes or []
        self.alinos = alinos or []
        self.llave_segura = None

    @property
    def verificada(self):
        """Property que nos indica si una receta fue limpiada o no."""
        return hasattr(
            self, 'llave_segura') and self.llave_segura == self.encriptar()

    def encriptar(self):
        """Funcion que encripta el valor a partir de una llave secreta"""
        encriptador = blake2b(key=SUPER_SECRET_KEY, digest_size=16)
        encriptador.update(self.nombre.encode())

        return encriptador.hexdigest()

    @staticmethod
    def abrir_ingredientes():
        """Genera las líneas del archivo ingredientes.txt"""
        with open(INGREDIENTES_PATH, encoding='utf-8') as fp:
            yield from map(lambda x: x.strip(), fp)

    def abrir_recetas_lock(self):
        """
        Funcion para abrir el archivo que indica los atributos
        de las recetas
        """
        pass

    def __setstate__(self, state):
        """
        Deserializa

        Elimina los atributos incorrectos y los ingredientes inválidos.
        """
        pass

    def __getstate__(self):
        """
        Serializa

        Recuerda colocar el atributo llave_segura.
        """
        pass


class Comida:
    def __init__(self,
                 nombre='',
                 nivel_preparacion=0.0,
                 ingredientes=None,
                 alinos=None,
                 fecha_ingreso=None):
        self.nombre = nombre
        self.nivel_preparacion = nivel_preparacion
        self.ingredientes = ingredientes or []
        self.alinos = alinos or []

        ''' Recuerda cambiar aqui el nivel de preparacion de acuerdo a la fecha
        de ingreso!'''

    @property
    def quemado(self):
        return self.nivel_preparacion > 100

    @property
    def preparado(self):
        return self.nivel_preparacion >= 100

    @staticmethod
    def date_a_str(fecha):
        return fecha.strftime('%Y-%m-%d-%H-%M-%S')

    @staticmethod
    def str_a_date(fecha_str):
        return datetime.strptime(fecha_str, '%Y-%m-%d-%H-%M-%S')

    @classmethod
    def de_receta(cls, receta):
        return cls(receta.nombre, 0.0, receta.ingredientes, receta.alinos)


class ComidaEncoder(json.JSONEncoder):
    """Utiliza esta clase para codificar en json"""

    pass