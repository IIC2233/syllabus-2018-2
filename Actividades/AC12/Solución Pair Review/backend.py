import json
import os
import os.path as path
import pickle

from clases import Comida, ComidaEncoder

BOOK_PATH = 'recetas.book'


class PyKitchen:
    def __init__(self):
        self.recetas = []
        self.comidas = []
        self.despachadas = []

    def cargar_recetas(self):
        with open(BOOK_PATH, mode='rb') as fp:
            self.recetas.extend(pickle.load(fp))

    def guardar_recetas(self):
        with open(BOOK_PATH, mode='wb') as fp:
            pickle.dump(self.recetas, fp)

    def cocinar(self):
        recetas_validas = filter(lambda r: r.verificada, self.recetas)
        for receta in recetas_validas:
            comida = Comida.de_receta(receta)
            file_path = path.join('horno', f'{comida.nombre}.json')
            with open(file_path, encoding='utf-8', mode='w') as fp:
                json.dump(comida, fp, cls=ComidaEncoder)

    def despachar_y_botar(self):
        for filename in os.listdir('horno'):
            if not filename.endswith('.json'):
                continue
            path_comida = path.join('horno', filename)
            with open(path_comida, encoding='utf-8') as fp:
                comida = json.load(
                    fp, object_hook=lambda dict_: Comida(**dict_))

                if comida.preparado and not comida.quemado:
                    self.despachadas.append(comida)
                elif not comida.preparado:
                    self.comidas.append(comida)
                else:
                    print(comida.nombre)