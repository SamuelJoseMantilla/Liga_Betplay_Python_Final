"""
core/persistence.py
-------------------
Guarda y carga los datos de la aplicacion en archivos JSON.
"""

import json
import os

# Carpeta donde se guardan los archivos
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
EQUIPOS_FILE = os.path.join(DATA_DIR, 'equipos.json')
PARTIDOS_FILE = os.path.join(DATA_DIR, 'partidos.json')


def asegurar_carpeta():
    """Crea la carpeta data/ si no existe."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def guardar_equipos(ligaBetplay):
    """Guarda el diccionario de equipos en equipos.json."""
    try:
        asegurar_carpeta()
        with open(EQUIPOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(ligaBetplay, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f'Error al guardar equipos: {e}')
        return False


def guardar_partidos(calendario):
    """Guarda la lista de partidos en partidos.json."""
    try:
        asegurar_carpeta()
        with open(PARTIDOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(calendario, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f'Error al guardar partidos: {e}')
        return False


def guardar_todo(ligaBetplay, calendario):
    """Guarda ambos archivos en una sola llamada."""
    ok1 = guardar_equipos(ligaBetplay)
    ok2 = guardar_partidos(calendario)
    return ok1 and ok2


def cargar_equipos():
    """Carga los equipos desde el JSON. Retorna dict vacio si no existe."""
    if not os.path.exists(EQUIPOS_FILE):
        return {}
    try:
        with open(EQUIPOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f'Advertencia: no se pudo leer equipos.json ({e}). Se inicia vacio.')
        return {}


def cargar_partidos():
    """Carga los partidos desde el JSON. Retorna lista vacia si no existe."""
    if not os.path.exists(PARTIDOS_FILE):
        return []
    try:
        with open(PARTIDOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f'Advertencia: no se pudo leer partidos.json ({e}). Se inicia vacio.')
        return []
