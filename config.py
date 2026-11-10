# config.py
# Configuración centralizada del proyecto DECIDE

import os

# Información de la aplicación
APP_NAME = "DECIDE"
APP_VERSION = "2.0"
APP_DESCRIPTION = "Evaluador de Competencias Emocionales"

# Base de datos
DB_FILE = "decide_datos.db"
DB_BACKUP_ENABLED = True

# Configuración de interfaz
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
FONT_FAMILY = "Arial"

# Configuración de evaluación
NUM_SITUACIONES = 16  # Total de situaciones disponibles
NUM_COMPETENCIAS = 9  # Total de competencias a evaluar
PUNTOS_POR_EVALUACION = 100

# Sistema de niveles
NIVELES_DEFINICION = {
    0: {"nombre": "Novato", "rango": (0, 99), "icono": "🥚"},
    1: {"nombre": "Principiante", "rango": (100, 299), "icono": "🌱"},
    2: {"nombre": "Intermedio", "rango": (300, 599), "icono": "🌿"},
    3: {"nombre": "Avanzado", "rango": (600, 999), "icono": "🌳"},
    4: {"nombre": "Experto", "rango": (1000, 1999), "icono": "🏔️"},
    5: {"nombre": "Maestro", "rango": (2000, float('inf')), "icono": "👑"}
}

# Configuración de recomendaciones
RECOMENDACIONES_HABILITADAS = True
LOGROS_HABILITADOS = True

# Debug
DEBUG_MODE = False

# Temas de colores
COLORES = {
    "primario": "#0066cc",
    "exito": "#2ecc71",
    "advertencia": "#e67e22",
    "error": "#e74c3c",
    "texto": "#1a1a1a",
    "fondo": "#ffffff"
}

def obtener_ruta_base():
    """Obtiene la ruta base del proyecto"""
    return os.path.dirname(os.path.abspath(__file__))

def obtener_ruta_db():
    """Obtiene la ruta completa de la base de datos"""
    return os.path.join(obtener_ruta_base(), DB_FILE)
