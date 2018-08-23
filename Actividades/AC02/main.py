from collections import namedtuple


# NO MODIFICAR ESTA FUNCION
def foreach(function, iterable):
    for elem in iterable:
        function(elem)


# Named tuples para cada entidad
Ciudad = namedtuple("Ciudad", ["sigla_pais", "nombre"])
Pais = namedtuple("Pais", ["sigla", "nombre"])
Persona = namedtuple("Persona", [
    "nombre", "apellido", "edad", "sexo", "ciudad_residencia",
    "area_de_trabajo", "sueldo"
])

###########################


def leer_ciudades(ruta_archivo_ciudades):
    '''
    :param ruta_archivo_ciudades: str
    :return: generador
    '''
    pass


def leer_paises(ruta_archivo_paises):
    '''
    :param ruta_archivo_paises: str
    :return: generador
    '''
    pass


def leer_personas(ruta_archivo_personas):
    '''
    :param ruta_archivo_personas: str
    :return: generador
    '''
    pass


def sigla_de_pais(nombre_pais, paises):
    '''
    :param nombre_pais: str
    :param paises: iterable de Paises (instancias)
    :return: sigla correspondiente al pais nombre_pais: str
    '''
    pass


def ciudades_por_pais(nombre_pais, paises, ciudades):
    '''
    :param nombre_pais: str
    :param paises: iterable de Paises (instancias)
    :param ciudades: iterable de Ciudades (instancias)
    :return: generador
    '''
    pass


def personas_por_pais(nombre_pais, paises, ciudades, personas):
    '''
    :param nombre_pais: str
    :param paises: iterable de Paises (instancias)
    :param ciudades: iterable de Ciudades (instancias)
    :param personas: iterable de Personas (instancias)
    :return: generador
    '''
    pass


def sueldo_promedio(personas):
    '''
    :param personas: iterable de Personas (lista de instancias)
    :return: promedio (int o float)
    '''
    pass


def cant_personas_por_area_de_trabajo(personas):
    '''
    :param personas: iterable de Personas (lista de instancias)
    :return: dict
    '''
    pass


if __name__ == '__main__':
    RUTA_PAISES = "Paises.txt"
    RUTA_CIUDADES = "Ciudades.txt"
    RUTA_PERSONAS = "Personas.txt"

    # (1) Ciudades en Chile
    ciudades_chile = ciudades_por_pais('Chile', leer_paises(RUTA_PAISES),
                                       leer_ciudades(RUTA_CIUDADES))
    # foreach(ciudades_chile,
    #         lambda ciudad: print(ciudad.sigla_pais, ciudad.nombre))

    # (2) Personas en Chile
    personas_chile = personas_por_pais('Chile', leer_paises(RUTA_PAISES),
                                       leer_ciudades(RUTA_CIUDADES),
                                       leer_personas(RUTA_PERSONAS))
    # foreach(personas_chile, lambda p: print(p.nombre, p.ciudad_residencia))

    # (3) Sueldo promedio de personas del mundo
    sueldo_mundo = sueldo_promedio(leer_personas(RUTA_PERSONAS))
    # print('Sueldo promedio: ', sueldo_mundo)

    # (4) Cantidad de personas por profesion
    dicc = cant_personas_por_area_de_trabajo(leer_personas(RUTA_PERSONAS))
    # foreach(dicc.items(), lambda elem: print(f"{elem[0]}: {elem[1]}"))
