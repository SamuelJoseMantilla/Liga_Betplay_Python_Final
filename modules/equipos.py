"""
modules/equipos.py
------------------
Modulo 1: registro de equipos y selector reutilizable.
"""

from core.data import ligaBetplay
from core.estructura import estructura_equipo
from core.persistence import guardar_equipos
from utils.helpers import limpiar_pantalla, pausar, leer_texto
from menu.main_menu import titulo


def elegir_equipo():
    """Muestra los equipos registrados y permite elegir uno."""
    if len(ligaBetplay) == 0:
        print('No hay equipos registrados todavia.')
        pausar()
        return None

    nombres = list(ligaBetplay.keys())

    print('\nEquipos registrados:')
    for i in range(len(nombres)):
        print(str(i + 1) + '. ' + nombres[i])
    print('0. Cancelar')

    opcion = input('\nSeleccione el numero del equipo: ')

    if opcion == '0':
        return None

    try:
        indice = int(opcion) - 1
    except ValueError:
        print('Opcion no valida.')
        pausar()
        return None

    if 0 <= indice < len(nombres):
        return nombres[indice]

    print('Opcion no valida.')
    pausar()
    return None


def reg_equipo():
    """Registra un equipo nuevo en la liga."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- REGISTRO DE EQUIPO ---\n')

    nombre = leer_texto('Ingrese el nombre del equipo: ')

    if nombre in ligaBetplay:
        print('Ese equipo ya esta registrado.')
        pausar()
        return

    ciudad = leer_texto('Ingrese la ciudad del equipo: ')

    equipo = estructura_equipo()
    equipo['nombre'] = nombre
    equipo['ciudad'] = ciudad

    ligaBetplay[nombre] = equipo
    guardar_equipos(ligaBetplay)

    print('\nEl equipo ' + nombre + ' fue registrado correctamente!')
    pausar()
