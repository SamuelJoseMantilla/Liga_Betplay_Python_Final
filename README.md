# ⚽ Liga BetPlay - Sistema de Gestión de Torneo

Aplicación de consola en Python para gestionar una liga de fútbol: registro de equipos, cuerpo técnico, jugadores, programación de partidos, resultados y tabla de posiciones.

---

## 📌 Objetivo

Reestructurar la versión original (un solo archivo) en un proyecto **modular y profesional**, separando responsabilidades en carpetas y archivos independientes, con manejo de errores y un punto de entrada único.

---

## 📁 Estructura del Proyecto

```
liga_betplay/
│
├── main.py                    # Punto de entrada (if __name__ == '__main__')
│
├── core/                      # Nucleo del sistema
│   ├── __init__.py
│   ├── data.py                # Almacenes globales (cargan desde JSON)
│   ├── estructura.py          # Moldes/plantillas de datos
│   └── persistence.py         # Guardar/cargar datos en JSON
│
├── data/                      # Archivos JSON (se crean al usar el programa)
│   ├── equipos.json
│   └── partidos.json
│
├── modules/                   # Modulos funcionales (cada opcion del menu)
│   ├── __init__.py
│   ├── equipos.py             # Modulo 1 - Registro y selector de equipos
│   ├── planta_tecnica.py      # Modulo 2 - Cuerpo tecnico
│   ├── jugadores.py           # Modulo 3 - Jugadores
│   ├── partidos.py            # Modulo 4 - Programacion de partidos
│   ├── resultados.py          # Modulo 5 - Registro de resultados
│   ├── informacion.py         # Modulo 6 - Submenu de consultas
│   └── estadisticas.py        # Modulo 7 - Tabla de posiciones
│
├── menu/                      # Opciones de menu (UNICA fuente de menus)
│   ├── __init__.py
│   └── main_menu.py           # titulo(), main_menu(), sub_menu()
│
├── utils/                     # Utilidades comunes
│   ├── __init__.py
│   └── helpers.py             # limpiar_pantalla, pausar, leer_texto, leer_entero
│
└── README.md
```
## 🧩 Opciones del Menú

| # | Opción                      | Módulo                |
|---|-----------------------------|-----------------------|
| 1 | Registro de equipos         | `modules/equipos.py`  |
| 2 | Registro planta técnica     | `modules/planta_tecnica.py` |
| 3 | Registro jugadores          | `modules/jugadores.py`|
| 4 | Programación de partidos    | `modules/partidos.py` |
| 5 | Registro de estadísticas    | `modules/resultados.py`|
| 6 | Mostrar información         | `modules/informacion.py`|
| 7 | Tabla de posiciones         | `modules/estadisticas.py`|
| 0 | Salir                       | -                     |


## 🧠 Buenas Prácticas Aplicadas

- **Modularidad**: cada responsabilidad en su propio archivo.
- **Reutilización**: `helpers.py` con funciones comunes (validar enteros, leer texto, pausar).
- **Manejo de errores**: `try/except` en `main.py` y `core/persistence.py`.
- **Validación de entradas**: `leer_entero` con rangos, `leer_texto` que no permite vacíos.
- **Punto de entrada único**: `main.py` con `if __name__ == '__main__'`.
- **Menús centralizados**: todas las opciones viven en `menu/main_menu.py`.
- **Persistencia en JSON**: los datos se guardan automaticamente y persisten entre ejecuciones.

