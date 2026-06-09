"""
modules/partidos.py
-------------------
Modulo 4: programacion de partidos (fecha, local, visitante).
"""

from core.data import ligaBetplay, calendario
from core.persistence import guardar_partidos
from utils.helpers import limpiar_pantalla, pausar
from menu.main_menu import titulo


def validar_fecha(fecha):
    """Valida que la fecha tenga formato dd/mm/aaaa y valores correctos."""
    partes = fecha.split('/')
    if len(partes) != 3:
        return False
    dia, mes, anio = partes
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False
    if not (1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and int(anio) >= 2000):
        return False
    return True


def pedir_fecha():
    """Pide y valida una fecha en formato dd/mm/aaaa."""
    while True:
        fecha = input('Ingrese la fecha del partido (dd/mm/aaaa): ')
        if validar_fecha(fecha):
            return fecha
        print('Formato invalido. Ejemplo: 15/06/2025')


def elegir_entre_equipos(mensaje, excluir=None):
    """Muestra los equipos disponibles y permite elegir uno.
    Si se pasa 'excluir', ese nombre no se mostrara como opcion.
    """
    nombres = [n for n in ligaBetplay.keys() if n != excluir]

    print('\nEquipos disponibles:')
    for i in range(len(nombres)):
        print(str(i + 1) + '. ' + nombres[i])

    while True:
        opcion = input(mensaje)
        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(nombres):
                return nombres[indice]
            print('Opcion no valida.')
        except ValueError:
            print('Ingrese un numero.')


def programar_partido():
    """Programa un partido nuevo en el calendario."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- PROGRAMACION DE PARTIDOS ---')
    print('Aqui solo se programa la fecha y los equipos.')
    print('El resultado se ingresa en la opcion 5.\n')

    if len(ligaBetplay) < 2:
        print('Necesita al menos 2 equipos registrados para programar un partido.')
        pausar()
        return

    fecha = pedir_fecha()

    equipo_local = elegir_entre_equipos('\nSeleccione el equipo LOCAL (numero): ')
    equipo_visitante = elegir_entre_equipos(
        'Seleccione el equipo VISITANTE (numero): ',
        excluir=equipo_local
    )

    # evitar duplicados
    for p in calendario:
        if p['fecha'] == fecha and p['local'] == equipo_local and p['visitante'] == equipo_visitante:
            print('\nEse partido ya esta programado para esa fecha.')
            pausar()
            return

    partido = {
        'fecha': fecha,
        'local': equipo_local,
        'visitante': equipo_visitante,
        'jugado': False,
        'goles_local': None,
        'goles_visitante': None
    }
    calendario.append(partido)
    guardar_partidos(calendario)

    print('\nPartido programado correctamente!')
    print('Fecha    : ' + fecha)
    print('Local    : ' + equipo_local)
    print('Visitante: ' + equipo_visitante)
    pausar()
