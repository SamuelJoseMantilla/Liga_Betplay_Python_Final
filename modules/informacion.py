"""
modules/informacion.py
----------------------
Modulo 7: submenu que reune las opciones de consulta.
"""

from core.data import ligaBetplay
from modules.equipos import elegir_equipo
from modules.planta_tecnica import mostrar_plantel
from modules.jugadores import mostrar_jugadores
from modules.estadisticas import mostrar_estadisticas
from menu.main_menu import titulo, sub_menu, mostrar_menu
from utils.helpers import limpiar_pantalla, pausar


def mostrar_informacion():
    """Submenu de consulta para un equipo seleccionado."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- MOSTRAR INFORMACION ---\n')
    print('Elija el equipo que desea consultar:')

    nombre = elegir_equipo()
    if nombre is None:
        return

    while True:
        limpiar_pantalla()
        print(titulo())
        print('\nEquipo seleccionado: ' + nombre + '\n')
        mostrar_menu(sub_menu())

        opcion = input('\nSeleccione una opcion: ')

        if opcion == '1':
            mostrar_plantel(ligaBetplay[nombre])
        elif opcion == '2':
            mostrar_jugadores(ligaBetplay[nombre])
        elif opcion == '3':
            mostrar_estadisticas(ligaBetplay[nombre])
        elif opcion == '4':
            mostrar_plantel(ligaBetplay[nombre])
            mostrar_jugadores(ligaBetplay[nombre])
            mostrar_estadisticas(ligaBetplay[nombre])
        elif opcion == '5':
            break
        else:
            print('Opcion no valida.')
            pausar()
