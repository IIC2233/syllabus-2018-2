import unittest
import json
import os

from backend import PyKitchen
from clases import Receta, Comida, ComidaEncoder
from datetime import datetime, timedelta


class TestRecetaClass(unittest.TestCase):

    def setUp(self):
        with open(f'testing{os.sep}test_samples.json', encoding='utf-8') as fp:
            self.test_samples = json.load(fp)

    def test_elimina_ingredientes(self):
        """Prueba si se eliminan ingredientes contaminados"""
        receta = Receta()
        choripan = self.test_samples['choripan']
        receta.__setstate__(choripan)
        msg = 'Los ingredientes no fueron eliminados correctamente'
        removed = 'zapatilla' not in receta.__dict__['ingredientes']
        self.assertEqual(removed, True, msg)

    def test_elimina_atributos(self):
        """Comprueba si se eliminan atributos extras"""
        receta = Receta()
        choripan = self.test_samples['choripan']
        receta.__setstate__(choripan)
        msg = f'Algunos atributos no fueron eliminados: {receta.__dict__}'
        has_attrs = 'dummy_attr' in receta.__dict__
        self.assertEqual(has_attrs, False, msg)

    def test_llave_segura(self):
        """Comprueba si se agrega la llave segura y si es valida"""
        receta = Receta('Empanadas', ['pino', 'huevo', 'masa'])
        msg = 'No se agrega la llave segura'
        has_llave = 'llave_segura' in receta.__getstate__()
        if has_llave:
            eq = receta.__getstate__()['llave_segura'] == receta.encriptar()
        self.assertEqual(has_llave and eq, True, msg)


class TestComidaClass(unittest.TestCase):

    def test_calcula_fecha_quemado(self):
        """comprueba si se calcula bien cuando un producto esta quemado"""
        fecha = datetime.now() - timedelta(minutes=110)
        fecha_str = Comida.date_a_str(fecha)
        comida = Comida('Empanadas', 10, ['pino', 'huevo', 'masa'],
                        fecha_ingreso=fecha_str)
        msg = "La clase no controla el quemado en el init"
        self.assertEqual(comida.quemado, True, msg)

    def test_calcula_preparado(self):
        """comprueba si se calcula bien cuando un producto esta preparado"""
        fecha = datetime.now() - timedelta(minutes=100)
        fecha_str = Comida.date_a_str(fecha)
        comida = Comida('Empanadas', 0, ['pino', 'huevo', 'masa'],
                        fecha_ingreso=fecha_str)
        msg = "La clase no controla el producto preparado en el init"
        self.assertEqual(comida.preparado, True, msg)
