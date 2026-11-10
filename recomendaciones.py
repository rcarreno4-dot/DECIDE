# recomendaciones.py
# Sistema avanzado de recomendaciones personalizadas

RECOMENDACIONES_POR_COMPETENCIA = {
    "autoconocimiento": {
        "bajo": "Es importante desarrollar tu autoconocimiento emocional. Practica la meditación, lleva un diario emocional donde registres qué te hace sentir diferentes emociones. Identifica patrones en tu comportamiento.",
        "medio": "Tu autoconocimiento está en desarrollo. Continúa practicando técnicas de introspección. Busca feedback de personas de confianza sobre cómo te perciben.",
        "alto": "¡Excelente autoconocimiento! Tienes claridad sobre tus emociones. Comparte tus experiencias con otros para ayudarles a desarrollar esta competencia también.",
        "muy_alto": "Eres muy consciente de tus emociones. Considera ayudar a otros a desarrollar su autoconocimiento mediante coaching o mentoría."
    },
    "autorregulacion": {
        "bajo": "Trabajar en la autorregulación es fundamental. Practica técnicas de respiración, mindfulness y toma pausas antes de reaccionar. Identifica tus disparadores emocionales.",
        "medio": "Tu autorregulación está mejorando. Sigue practicando técnicas de calma bajo presión. El ejercicio físico y la meditación pueden ayudarte.",
        "alto": "Buena autorregulación. Mantienes la calma en situaciones difíciles. Sigue practicando para mantener este nivel.",
        "muy_alto": "¡Excepcional autorregulación! Eres un modelo de control emocional. Considera enseñar a otros cómo manejar sus emociones."
    },
    "empatia": {
        "bajo": "Desarrollar empatía es clave para las relaciones. Intenta escuchar activamente sin juzgar. Practica ponerte en el lugar del otro. Lee historias diversas.",
        "medio": "Tu empatía está creciendo. Continúa practicando la escucha activa. Busca comprender diferentes perspectivas.",
        "alto": "Excelente empatía. Eres consciente de las emociones de otros. Sigue siendo compassivo y apoyo para quienes te rodean.",
        "muy_alto": "Empatía excepcional. Tienes un don natural para entender a otros. Usa esto para ayudar y apoyar a la gente."
    },
    "comunicacion": {
        "bajo": "La comunicación es fundamental. Practica expresar tus sentimientos de forma clara. Toma cursos de oratoria. Escucha más, habla menos.",
        "medio": "Tu comunicación está mejorando. Sigue practicando la asertividad. Aprende a dar feedback constructivo.",
        "alto": "Buena comunicación. Expresas tus ideas claramente. Mantén practicando para comunicar mejor en situaciones de estrés.",
        "muy_alto": "Comunicación excepcional. Eres muy claro y asertivo. Ayuda a otros a mejorar su comunicación."
    },
    "trabajo_equipo": {
        "bajo": "El trabajo en equipo requiere práctica. Busca oportunidades de colaboración. Aprende a confiar en otros y a pedir ayuda.",
        "medio": "Tu colaboración está mejorando. Sigue buscando proyectos grupales. Aprende a valorar las contribuciones de otros.",
        "alto": "Buen trabajo en equipo. Colaboras bien con otros. Mantén esta actitud positiva hacia la colaboración.",
        "muy_alto": "Excepcional trabajo en equipo. Eres un activo valioso para cualquier grupo. Lidera iniciativas colaborativas."
    },
    "toma_decisiones": {
        "bajo": "Mejorar en la toma de decisiones es importante. Analiza opciones antes de actuar. Pide consejo cuando sea necesario.",
        "medio": "Tu toma de decisiones está mejorando. Continúa analizando pros y contras antes de decidir.",
        "alto": "Buen análisis en tus decisiones. Mantienes una visión objetiva. Sigue confiando en tu criterio.",
        "muy_alto": "Excelente toma de decisiones. Eres reflexivo y objetivo. Podrías ser un buen consejero para otros."
    },
    "tolerancia_frustracion": {
        "bajo": "Desarrollar tolerancia a la frustración es crucial. Practica técnicas de relajación. Busca ver los obstáculos como oportunidades.",
        "medio": "Tu tolerancia está mejorando. Sigue usando técnicas de manejo del estrés. Recuerda que los fracasos son aprendizajes.",
        "alto": "Buena tolerancia. Manejas bien la frustración. Mantén esta actitud resiliente.",
        "muy_alto": "Excepcional tolerancia a la frustración. Ves desafíos como oportunidades. Inspira a otros con tu actitud positiva."
    },
    "manejo_conflictos": {
        "bajo": "Aprender a manejar conflictos es esencial. Busca soluciones ganadoras para ambas partes. Evita ataques personales.",
        "medio": "Tu manejo de conflictos mejora. Continúa buscando diálogos constructivos. Aprende a negociar.",
        "alto": "Buen manejo de conflictos. Buscas soluciones ganadoras. Mantén este enfoque colaborativo.",
        "muy_alto": "Excepcional resolución de conflictos. Eres un mediador natural. Considera ayudar a resolver conflictos en tu comunidad."
    },
    "resiliencia": {
        "bajo": "Desarrollar resiliencia te ayudará a recuperarte de dificultades. Busca apoyo social. Celebra pequeños logros.",
        "medio": "Tu resiliencia está en desarrollo. Mantén una red de apoyo fuerte. Aprende de cada desafío.",
        "alto": "Buena resiliencia. Te recuperas bien de adversidades. Sigue fortaleciendo tu capacidad de adaptación.",
        "muy_alto": "Resiliencia excepcional. Eres un ejemplo de fortaleza. Ayuda a otros a desarrollar su resiliencia."
    }
}

def obtener_nivel_texto(puntuacion):
    """Convierte puntuación a nivel texto"""
    if puntuacion <= 20:
        return "bajo"
    elif puntuacion <= 40:
        return "medio"
    elif puntuacion <= 80:
        return "alto"
    else:
        return "muy_alto"

def generar_recomendaciones(resultados):
    """Genera recomendaciones personalizadas basadas en resultados"""
    recomendaciones = {}
    
    for competencia, datos in resultados.items():
        puntuacion = datos["puntuacion_normalizada"]
        nivel = obtener_nivel_texto(puntuacion)
        
        if competencia in RECOMENDACIONES_POR_COMPETENCIA:
            recomendaciones[competencia] = {
                "nivel": nivel,
                "puntuacion": puntuacion,
                "recomendacion": RECOMENDACIONES_POR_COMPETENCIA[competencia][nivel],
                "nombre": datos["nombre"]
            }
    
    return recomendaciones

def generar_plan_desarrollo(resultados):
    """Genera un plan de desarrollo personalizado"""
    if not resultados:
        return {}
    # Encontrar competencias con menor puntuación
    competencias_ordenadas = sorted(
        resultados.items(),
        key=lambda x: x[1]["puntuacion_normalizada"]
    )
    
    plan = {
        "enfoque_principal": competencias_ordenadas[0],
        "secundarios": competencias_ordenadas[1:3],
        "fortalezas": sorted(
            resultados.items(),
            key=lambda x: x[1]["puntuacion_normalizada"],
            reverse=True
        )[:3]
    }
    
    return plan

def calcular_proximos_pasos(resultados):
    """Calcula los próximos pasos para mejorar"""
    pasos = []
    
    for competencia, datos in resultados.items():
        puntuacion = datos["puntuacion_normalizada"]
        
        if puntuacion <= 40:
            pasos.append({
                "competencia": datos["nombre"],
                "prioridad": "ALTA",
                "accion": f"Enfocarse en mejorar {datos['nombre']} con ejercicios específicos",
                "meta": "Alcanzar 60%"
            })
        elif puntuacion <= 60:
            pasos.append({
                "competencia": datos["nombre"],
                "prioridad": "MEDIA",
                "accion": f"Continuar desarrollando {datos['nombre']}",
                "meta": "Alcanzar 80%"
            })
    
    return sorted(pasos, key=lambda x: x["prioridad"] == "ALTA", reverse=True)
