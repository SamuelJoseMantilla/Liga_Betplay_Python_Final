"""
core/data.py
------------
Almacena las estructuras de datos globales de la aplicacion.
Los datos se cargan desde JSON al iniciar el programa.
"""

from core.persistence import cargar_equipos, cargar_partidos

# Diccionario principal: nombre del equipo -> datos del equipo
ligaBetplay = cargar_equipos()

# Lista de partidos programados
calendario = cargar_partidos()


def limpiar_datos():
    """Resetea la liga (util para pruebas o reinicio)."""
    ligaBetplay.clear()
    calendario.clear()
