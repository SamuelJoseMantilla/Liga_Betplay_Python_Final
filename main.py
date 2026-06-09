"""
main.py
-------
Punto de entrada de la aplicacion Liga BetPlay.
Muestra el menu principal y delega en los modulos correspondientes.
"""

import os
from core.data import ligaBetplay, calendario
from core.persistence import guardar_todo
from menu.main_menu import titulo, main_menu, mostrar_menu
from modules.equipos import reg_equipo
from modules.planta_tecnica import reg_plantel_tecnico
from modules.jugadores import reg_jugadores
from modules.partidos import programar_partido
from modules.resultados import registrar_resultado
from modules.informacion import mostrar_informacion
from modules.estadisticas import tabla_posiciones
from utils.helpers import limpiar_pantalla, pausar


def ejecutar_opcion(opcion):
    """Enruta la opcion elegida al modulo correspondiente."""
    try:
        if opcion == '1':
            reg_equipo()
        elif opcion == '2':
            reg_plantel_tecnico()
        elif opcion == '3':
            reg_jugadores()
        elif opcion == '4':
            programar_partido()
        elif opcion == '5':
            registrar_resultado()
        elif opcion == '6':
            mostrar_informacion()
        elif opcion == '7':
            tabla_posiciones()
        elif opcion == '0':
            return False
        else:
            print('Opcion no valida, seleccione una opcion del menu.')
            pausar()
    except Exception as e:
        # Manejo de errores centralizado
        print(f'\nOcurrio un error inesperado: {e}')
        pausar()
    return True


def main():
    """Bucle principal del programa."""
    continuar = True
    while continuar:
        limpiar_pantalla()
        print(titulo())
        mostrar_menu(main_menu())
        opcion = input('\nSeleccione una opcion: ')
        continuar = ejecutar_opcion(opcion)

    # Guardado final al salir
    guardar_todo(ligaBetplay, calendario)
    print('\nDatos guardados correctamente.')
    print('Gracias por usar el programa.')


if __name__ == '__main__':
    main()
