from main import pokemones_por_entrenador, \
    mismos_pokemones, diferentes_pokemones, cargar_pokemones, \
    cargar_solicitudes, cargar_entrenadores, sistema

'''
Demás está decir que el programa funciona bien y si el programa se cae, revisen
bien el error, puede ser por identacion o quizás por qué :c
'''

############################################################################
"""
Poblando el sistema.
Ya se hacen los llamados a las funciones, puedes imprimirlos para ver si se
cargaron bien.
"""

entrenadores = cargar_entrenadores('entrenadores.txt')
pokemones = cargar_pokemones('pokemones.txt')
solicitudes = cargar_solicitudes('solicitudes.txt')

# print(entrenadores)
# print(pokemones)
# print(solicitudes)

################################   MENU   ##################################
"""
Menú.
¡No debes cambiar nada! Simplemente nota que es un menú que pide input del
usuario, y en el caso en que este responda con "1" ó "2", entonces se hace
el llamado a la función. En otro caso, el programa termina.
"""

eleccion = input('Ingrese el modo de lectura de solicitudes:\n'
             '1: Orden de llegada\n'
             '2: Orden Inverso de llegada\n'
             '>\t')

if eleccion in {"1", "2"}:
    resultados_simulacion = sistema(eleccion, entrenadores,
                                    pokemones, solicitudes)
else:
    exit()

if eleccion == '1':
    print('-'*40)
    print('|', ' '*11, 'Orden normal', ' '*11, '|')
    print('-'*40)

    resultados = []
    valor_1 = pokemones_por_entrenador("2", resultados_simulacion)
    valor_1.sort()
    resultados.append(str(valor_1))
    valor_2 = pokemones_por_entrenador("156", resultados_simulacion)
    valor_2.sort()
    resultados.append(str(valor_2))
    valor_3 = mismos_pokemones('34', '64', resultados_simulacion)
    valor_3.sort()
    resultados.append(str(valor_3))
    valor_4 = mismos_pokemones("24", "65", resultados_simulacion)
    valor_4.sort()
    resultados.append(str(valor_4))
    valor_5 = diferentes_pokemones("6", "65", resultados_simulacion)
    valor_5.sort()
    resultados.append(str(valor_5))
    valor_6 = diferentes_pokemones("10", "6", resultados_simulacion)
    valor_6.sort()
    resultados.append(str(valor_6))

    with open('results_1.txt', encoding='utf8') as file:
        reales = [file.readline().strip() for i in range(7)]
        # Esto indicará el #valor malo del test.
        final = [i + 1 for i in range(6) if resultados[i] != reales[i]]
        if len(final) == 0:
            print('No hay errores! :D')
        else:
            print('Tests no aprobados:')
            print(final)

elif eleccion == '2':
    print('-'*40)
    print('|', ' '*11, 'Orden inverso', ' '*10, '|')
    print('-'*40)

    resultados = []
    valor_1 = pokemones_por_entrenador("2", resultados_simulacion)
    valor_1.sort()
    resultados.append(str(valor_1))
    valor_2 = pokemones_por_entrenador("156", resultados_simulacion)
    valor_2.sort()
    resultados.append(str(valor_2))
    valor_3 = mismos_pokemones("16", "30", resultados_simulacion)
    valor_3.sort()
    resultados.append(str(valor_3))
    valor_4 = mismos_pokemones("24", "65", resultados_simulacion)
    valor_4.sort()
    resultados.append(str(valor_4))
    valor_5 = diferentes_pokemones("24", "38", resultados_simulacion)
    valor_5.sort()
    resultados.append(str(valor_5))
    valor_6 = diferentes_pokemones("10", "6", resultados_simulacion)
    valor_6.sort()
    resultados.append(str(valor_6))

    with open('results_2.txt', encoding='utf8') as file:
        reales = [file.readline().strip() for i in range(7)]
        # Esto indicará el #valor malo del test.
        final = [i+1 for i in range(6) if resultados[i] != reales[i]]
        if len(final) == 0:
            print('No hay errores! :D')
        else:
            print('Tests no aprobados:')
            print(final)
