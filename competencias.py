# competencias.py
# Definición de las 9 competencias emocionales del proyecto DECIDE

COMPETENCIAS = {
    "autoconocimiento": {
        "nombre": "🧠 Autoconocimiento",
        "descripcion": "Capacidad para reconocer e identificar las propias emociones y su impacto",
        "puntuacion": 0
    },
    "autorregulacion": {
        "nombre": "🧘 Autorregulación",
        "descripcion": "Capacidad para controlar impulsos y manejar emociones negativas",
        "puntuacion": 0
    },
    "empatia": {
        "nombre": "❤️ Empatía",
        "descripcion": "Capacidad para comprender las emociones y perspectivas de otras personas",
        "puntuacion": 0
    },
    "comunicacion": {
        "nombre": "🗣️ Comunicación Asertiva",
        "descripcion": "Capacidad para expresar pensamientos y emociones adecuadamente",
        "puntuacion": 0
    },
    "trabajo_equipo": {
        "nombre": "🤝 Trabajo en Equipo",
        "descripcion": "Capacidad para colaborar y relacionarse efectivamente con otros",
        "puntuacion": 0
    },
    "toma_decisiones": {
        "nombre": "⚡ Toma de Decisiones",
        "descripcion": "Capacidad para analizar situaciones antes de actuar",
        "puntuacion": 0
    },
    "tolerancia_frustracion": {
        "nombre": "🔥 Tolerancia a la Frustración",
        "descripcion": "Capacidad para reaccionar adecuadamente ante obstáculos",
        "puntuacion": 0
    },
    "manejo_conflictos": {
        "nombre": "⚔️ Manejo de Conflictos",
        "descripcion": "Capacidad para resolver desacuerdos de manera constructiva",
        "puntuacion": 0
    },
    "resiliencia": {
        "nombre": "💪 Resiliencia",
        "descripcion": "Capacidad para afrontar situaciones difíciles y recuperarse",
        "puntuacion": 0
    }
}

def obtener_competencias():
    """Retorna el diccionario de competencias"""
    return COMPETENCIAS

def inicializar_puntuaciones():
    """Reinicia todas las puntuaciones a 0"""
    for comp in COMPETENCIAS.values():
        comp["puntuacion"] = 0
