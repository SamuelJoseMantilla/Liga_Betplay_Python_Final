"""
modules/planta_tecnica.py
-------------------------
Modulo 2: registro y consulta del cuerpo tecnico de un equipo.
"""

from core.data import ligaBetplay
from core.persistence import guardar_equipos
from modules.equipos import elegir_equipo
from utils.helpers import limpiar_pantalla, pausar, leer_texto
from menu.main_menu import titulo


def reg_plantel_tecnico():
    """Pide los datos del cuerpo tecnico para un equipo."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- REGISTRO DE PLANTA TECNICA ---\n')
    print('Primero elija el equipo:')

    nombre = elegir_equipo()
    if nombre is None:
        return

    equipo = ligaBetplay[nombre]

    print('\nIngrese los datos de la planta tecnica de: ' + nombre + '\n')
    equipo['plantel_tecnico']['director_tecnico'] = leer_texto('Nombre del director tecnico: ')
    equipo['plantel_tecnico']['preparador_arqueros'] = leer_texto('Nombre del preparador de arqueros: ')
    equipo['plantel_tecnico']['preparador_fisico'] = leer_texto('Nombre del preparador fisico: ')
    equipo['plantel_tecnico']['medico'] = leer_texto('Nombre del medico: ')
    equipo['plantel_tecnico']['fisioterapeuta'] = leer_texto('Nombre del fisioterapeuta: ')

    guardar_equipos(ligaBetplay)

    print('\nPlanta tecnica de ' + nombre + ' registrada correctamente!')
    pausar()


def mostrar_plantel(equipo):
    """Muestra el plantel tecnico de un equipo."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- PLANTEL TECNICO: ' + equipo['nombre'] + ' ---\n')
    pt = equipo['plantel_tecnico']
    print('Director tecnico      : ' + pt['director_tecnico'])
    print('Preparador de arqueros: ' + pt['preparador_arqueros'])
    print('Preparador fisico     : ' + pt['preparador_fisico'])
    print('Medico                : ' + pt['medico'])
    print('Fisioterapeuta        : ' + pt['fisioterapeuta'])
    pausar()
