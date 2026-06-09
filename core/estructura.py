"""
core/estructura.py
------------------
Define los moldes (plantillas) de datos que usa la aplicacion.
"""


def estructura_equipo():
    """Retorna la estructura base (vacia) de un equipo nuevo."""
    return {
        'nombre': '',
        'ciudad': '',
        'plantel_tecnico': {
            'director_tecnico': '',
            'preparador_arqueros': '',
            'preparador_fisico': '',
            'medico': '',
            'fisioterapeuta': ''
        },
        'jugadores': [],
        'estadisticas': {
            'partidos_jugados': 0,
            'victorias': 0,
            'empates': 0,
            'derrotas': 0,
            'goles_a_favor': 0,
            'goles_en_contra': 0,
            'puntos': 0
        }
    }
