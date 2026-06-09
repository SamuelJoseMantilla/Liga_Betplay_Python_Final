"""
menu/main_menu.py
-----------------
Opciones de menu que se muestran al usuario.
"""


def titulo():
    """Retorna el titulo principal del programa."""
    return '------------------------------\n  LIGA BETPLAY\n------------------------------'


def main_menu():
    """Opciones del menu principal."""
    return [
        '1. Registro de equipos',
        '2. Registro planta tecnica',
        '3. Registro jugadores',
        '4. Programacion de partidos',
        '5. Registro de estadisticas',
        '6. Mostrar informacion',
        '7. Tabla de posiciones',
        '0. Salir'
    ]


def sub_menu():
    """Submenu usado en 'Mostrar informacion'."""
    return [
        '1. Ver plantel tecnico',
        '2. Ver jugadores',
        '3. Ver estadisticas',
        '4. Ver todo',
        '5. Regresar al menu principal'
    ]


def mostrar_menu(opciones):
    """Imprime una lista de opciones en pantalla."""
    for item in opciones:
        print(item)
