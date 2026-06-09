"""
utils/helpers.py
----------------
Funciones auxiliares reutilizables en toda la aplicacion.
"""

import os
import sys

def limpiar_pantalla():
    """
    Limpia la consola en Windows, Linux y macOS.
    """
    os.system("cls" if sys.platform.startswith("win") else "clear")



def pausar():
    """Muestra un mensaje y espera que el usuario presione Enter."""
    input('\nPresione Enter para continuar...')


def leer_texto(mensaje):
    """Lee un texto no vacio desde teclado."""
    while True:
        valor = input(mensaje).strip()
        if valor != '':
            return valor
        print('Error: el valor no puede estar vacio.')


def leer_entero(mensaje, minimo=None, maximo=None):
    """Lee un entero validado, con rango opcional."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f'Error: el valor debe ser mayor o igual a {minimo}.')
                continue
            if maximo is not None and valor > maximo:
                print(f'Error: el valor debe ser menor o igual a {maximo}.')
                continue
            return valor
        except ValueError:
            print('Error: ingrese un numero entero valido.')
