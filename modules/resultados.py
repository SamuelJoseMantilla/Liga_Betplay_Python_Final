"""
modules/resultados.py
---------------------
Modulo 5: registro de resultados de los partidos.
"""

from core.data import ligaBetplay, calendario
from core.persistence import guardar_equipos, guardar_partidos
from modules.partidos import validar_fecha
from utils.helpers import limpiar_pantalla, pausar, leer_entero
from menu.main_menu import titulo


def registrar_resultado():
    """Pide una fecha, muestra los partidos y registra el resultado elegido."""
    limpiar_pantalla()
    print(titulo())
    print('\n--- REGISTRO DE RESULTADOS ---\n')

    if len(calendario) == 0:
        print('No hay partidos programados. Use la opcion 4 primero.')
        pausar()
        return

    # pedir y validar la fecha
    while True:
        fecha = input('Ingrese la fecha a consultar (dd/mm/aaaa): ')
        if validar_fecha(fecha):
            break
        print('Formato invalido. Ejemplo: 15/06/2025')

    partidos_fecha = [p for p in calendario if p['fecha'] == fecha]

    if len(partidos_fecha) == 0:
        print('\nNo hay partidos programados para el ' + fecha)
        pausar()
        return

    print('\nPartidos del ' + fecha + ':')
    print('-' * 55)
    for i in range(len(partidos_fecha)):
        p = partidos_fecha[i]
        estado = 'Jugado' if p['jugado'] else 'Pendiente'
        print(str(i + 1) + '. ' + p['local'] + ' vs ' + p['visitante'] + '  [' + estado + ']')
    print('-' * 55)
    print('0. Cancelar')

    # elegir partido
    while True:
        opcion = input('\nSeleccione el partido: ')
        if opcion == '0':
            return
        try:
            indice = int(opcion) - 1
        except ValueError:
            print('Ingrese un numero.')
            continue
        if 0 <= indice < len(partidos_fecha):
            partido = partidos_fecha[indice]
            break
        print('Opcion no valida.')

    if partido['jugado']:
        print('\nEse partido ya tiene resultado registrado:')
        print(partido['local'] + ' ' + str(partido['goles_local']) +
              ' - ' + str(partido['goles_visitante']) + ' ' + partido['visitante'])
        pausar()
        return

    # goles
    print('\nIngresando resultado para: ' + partido['local'] + ' vs ' + partido['visitante'] + '\n')
    goles_local = leer_entero('Goles de ' + partido['local'] + ': ', minimo=0)
    goles_visitante = leer_entero('Goles de ' + partido['visitante'] + ': ', minimo=0)

    partido['goles_local'] = goles_local
    partido['goles_visitante'] = goles_visitante
    partido['jugado'] = True

    # actualizar estadisticas
    local = ligaBetplay[partido['local']]
    visita = ligaBetplay[partido['visitante']]

    local['estadisticas']['partidos_jugados'] += 1
    visita['estadisticas']['partidos_jugados'] += 1
    local['estadisticas']['goles_a_favor'] += goles_local
    local['estadisticas']['goles_en_contra'] += goles_visitante
    visita['estadisticas']['goles_a_favor'] += goles_visitante
    visita['estadisticas']['goles_en_contra'] += goles_local

    if goles_local > goles_visitante:
        local['estadisticas']['victorias'] += 1
        local['estadisticas']['puntos'] += 3
        visita['estadisticas']['derrotas'] += 1
        resultado = 'GANO: ' + partido['local']
    elif goles_visitante > goles_local:
        visita['estadisticas']['victorias'] += 1
        visita['estadisticas']['puntos'] += 3
        local['estadisticas']['derrotas'] += 1
        resultado = 'GANO: ' + partido['visitante']
    else:
        local['estadisticas']['empates'] += 1
        visita['estadisticas']['empates'] += 1
        local['estadisticas']['puntos'] += 1
        visita['estadisticas']['puntos'] += 1
        resultado = 'EMPATE'

    # resumen
    limpiar_pantalla()
    print(titulo())
    print('\n======================================')
    print('         RESULTADO DEL PARTIDO        ')
    print('======================================')
    print('Fecha: ' + fecha)
    print(partido['local'] + ' ' + str(goles_local) + ' - ' +
          str(goles_visitante) + ' ' + partido['visitante'])
    print('--------------------------------------')
    print(resultado)
    print('======================================\n')
    print('Estadisticas actualizadas:\n')

    for eq in [local, visita]:
        e = eq['estadisticas']
        dif = e['goles_a_favor'] - e['goles_en_contra']
        print(eq['nombre'] + ':')
        print('  PJ: ' + str(e['partidos_jugados']) +
              '  PG: ' + str(e['victorias']) +
              '  PE: ' + str(e['empates']) +
              '  PP: ' + str(e['derrotas']))
        print('  GF: ' + str(e['goles_a_favor']) +
              '  GC: ' + str(e['goles_en_contra']) +
              '  Dif: ' + str(dif) +
              '  Pts: ' + str(e['puntos']))
        print('')

    guardar_equipos(ligaBetplay)
    guardar_partidos(calendario)
    pausar()
