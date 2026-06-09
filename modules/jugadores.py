"""
modules/jugadores.py
--------------------
Modulo 3: registro y consulta de jugadores.
"""

from core.data import ligaBetplay
from core.persistence import guardar_equipos
from modules.equipos import elegir_equipo
from utils.helpers import limpiar_pantalla, pausar, leer_texto, leer_entero
from menu.main_menu import titulo


def reg_jugadores():
    """Registra uno o varios jugadores para un equipo."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- REGISTRO DE JUGADORES ---\n')
    print('Elija el equipo al que le va a agregar jugadores:')

    nombre = elegir_equipo()
    if nombre is None:
        return

    equipo = ligaBetplay[nombre]

    while True:
        limpiar_pantalla()
        print(titulo())
        print('\n--- REGISTRO DE JUGADORES ---')
        print('Equipo: ' + nombre)
        print('Jugadores registrados: ' + str(len(equipo['jugadores'])) + '\n')

        nombre_jugador = leer_texto('Nombre del jugador: ')
        nacionalidad = leer_texto('Nacionalidad: ')
        posicion = leer_texto('Posicion (ej: Delantero, Portero...): ')
        camiseta = leer_entero('Numero de camiseta: ', minimo=1, maximo=99)
        edad = leer_entero('Edad del jugador: ', minimo=10, maximo=60)

        jugador = {
            'nombre_jugador': nombre_jugador,
            'nacionalidad': nacionalidad,
            'posicion': posicion,
            'numero_camiseta': camiseta,
            'edad': edad
        }
        equipo['jugadores'].append(jugador)

        print('\nJugador ' + nombre_jugador + ' agregado correctamente!')

        otro = input('\nDesea agregar otro jugador? (s/n): ').lower()
        if otro != 's':
            break

    guardar_equipos(ligaBetplay)
    pausar()


def mostrar_jugadores(equipo):
    """Muestra el listado de jugadores de un equipo."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- JUGADORES: ' + equipo['nombre'] + ' ---\n')

    if len(equipo['jugadores']) == 0:
        print('No hay jugadores registrados para este equipo.')
    else:
        print('N  Nombre               Posicion       Camiseta  Edad  Nacionalidad')
        print('-' * 68)
        for i in range(len(equipo['jugadores'])):
            j = equipo['jugadores'][i]
            print(str(i + 1) + '.  ' +
                  j['nombre_jugador'].ljust(20) +
                  j['posicion'].ljust(15) +
                  str(j['numero_camiseta']).ljust(10) +
                  str(j['edad']).ljust(6) +
                  j['nacionalidad'])

    pausar()
