"""
modules/estadisticas.py
-----------------------
Modulo 6: muestra estadisticas individuales y la tabla de posiciones.
"""

from core.data import ligaBetplay
from utils.helpers import limpiar_pantalla, pausar
from menu.main_menu import titulo


def mostrar_estadisticas(equipo):
    """Muestra las estadisticas de un equipo."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- ESTADISTICAS: ' + equipo['nombre'] + ' ---\n')
    e = equipo['estadisticas']
    dif = e['goles_a_favor'] - e['goles_en_contra']
    print('Partidos jugados : ' + str(e['partidos_jugados']))
    print('Victorias        : ' + str(e['victorias']))
    print('Empates          : ' + str(e['empates']))
    print('Derrotas         : ' + str(e['derrotas']))
    print('Goles a favor    : ' + str(e['goles_a_favor']))
    print('Goles en contra  : ' + str(e['goles_en_contra']))
    print('Diferencia       : ' + str(dif))
    print('Puntos           : ' + str(e['puntos']))
    pausar()


def tabla_posiciones():
    """Muestra la tabla de posiciones ordenada por puntos y diferencia de gol."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- TABLA DE POSICIONES ---\n')

    if len(ligaBetplay) == 0:
        print('No hay equipos registrados.')
        pausar()
        return

    lista_equipos = list(ligaBetplay.values())

    # Ordenamiento burbuja por puntos y diferencia de gol
    for i in range(len(lista_equipos)):
        for j in range(i + 1, len(lista_equipos)):
            pts_i = lista_equipos[i]['estadisticas']['puntos']
            pts_j = lista_equipos[j]['estadisticas']['puntos']
            dif_i = lista_equipos[i]['estadisticas']['goles_a_favor'] - lista_equipos[i]['estadisticas']['goles_en_contra']
            dif_j = lista_equipos[j]['estadisticas']['goles_a_favor'] - lista_equipos[j]['estadisticas']['goles_en_contra']

            if pts_i < pts_j or (pts_i == pts_j and dif_i < dif_j):
                lista_equipos[i], lista_equipos[j] = lista_equipos[j], lista_equipos[i]

    print('Pos  Equipo                PJ   PG   PE   PP   GF   GC   Dif  Pts')
    print('-' * 68)

    for i in range(len(lista_equipos)):
        eq = lista_equipos[i]
        e = eq['estadisticas']
        dif = e['goles_a_favor'] - e['goles_en_contra']
        pos = str(i + 1) + '.'
        print(pos.ljust(5) +
              eq['nombre'].ljust(22) +
              str(e['partidos_jugados']).ljust(5) +
              str(e['victorias']).ljust(5) +
              str(e['empates']).ljust(5) +
              str(e['derrotas']).ljust(5) +
              str(e['goles_a_favor']).ljust(5) +
              str(e['goles_en_contra']).ljust(5) +
              str(dif).ljust(5) +
              str(e['puntos']))

    pausar()
