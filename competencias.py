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


PILARES_CURSO = {
    "habilidades_sociales": {
        "id": "habilidades_sociales",
        "titulo": "Habilidades Sociales e Interacción con el Entorno",
        "descripcion": "Competencias orientadas a la empatía, expresión asertiva, conexión interpersonal y colaboración colectiva.",
        "icono": "🤝",
        "competencias": ["autoconocimiento", "empatia", "comunicacion", "trabajo_equipo"]
    },
    "resolucion_conflictos": {
        "id": "resolucion_conflictos",
        "titulo": "Resolución Pacífica de Conflictos y Control Emocional",
        "descripcion": "Competencias dirigidas a la regulación de impulsos, toma prudente de decisiones, superación de frustraciones y mediación pacífica.",
        "icono": "⚔️",
        "competencias": ["autorregulacion", "toma_decisiones", "tolerancia_frustracion", "manejo_conflictos", "resiliencia"]
    }
}

def obtener_pilares():
    """Retorna la estructura de pilares temáticos del curso"""
    return PILARES_CURSO

def calcular_analisis_pilares(resultados):
    """Calcula el análisis cualitativo y cuantitativo para los 2 pilares académicos"""
    if not resultados:
        return {}
    
    analisis = {}
    for pilar_key, pilar in PILARES_CURSO.items():
        comps_pilar = [resultados[c]["puntuacion_normalizada"] for c in pilar["competencias"] if c in resultados]
        promedio = round(sum(comps_pilar) / len(comps_pilar), 1) if comps_pilar else 0
        
        if promedio >= 75:
            diagnostico = "Dominio sobresaliente en la interacción y madurez emocional. Capacidad natural para mediar y generar vínculos constructivos."
            propuesta = "Continuar fortaleciendo el liderazgo empático y servir como facilitador o mediador en dinámicas grupales complejas."
            estado = "Consolidado"
        elif promedio >= 55:
            diagnostico = "Desempeño adecuado con bases sólidas, pero con variabilidad en situaciones de alta presión o divergencia de opiniones."
            propuesta = "Implementar pausas conscientes antes de emitir juicios y practicar la escucha activa sin interrumpir en escenarios de desacuerdo."
            estado = "En Desarrollo Óptimo"
        else:
            diagnostico = "Área de oportunidad prioritaria. Se observa reactividad emocional o dificultades para exteriorizar necesidades con asertividad."
            propuesta = "Adoptar técnicas de desescalamiento pacífico de conflictos, comunicación 'Yo' y entrenamiento en autorregulación fisiológica."
            estado = "Requiere Fortalecimiento"

        analisis[pilar_key] = {
            "titulo": pilar["titulo"],
            "icono": pilar["icono"],
            "puntuacion": promedio,
            "estado": estado,
            "diagnostico": diagnostico,
            "propuesta": propuesta,
            "competencias_incluidas": [COMPETENCIAS[c]["nombre"] for c in pilar["competencias"] if c in COMPETENCIAS]
        }
        
    return analisis
