# resultados.py
# Módulo para generar y mostrar resultados

def mostrar_resultados_texto(resultados):
    """Genera un string con los resultados en formato texto"""
    texto = "\n" + "="*60 + "\n"
    texto += "📊 TU PERFIL DECIDE - COMPETENCIAS EMOCIONALES\n"
    texto += "="*60 + "\n\n"
    
    for competencia, datos in resultados.items():
        texto += f"{datos['nombre']}\n"
        texto += f"Puntuación: {datos['puntuacion_normalizada']}%\n"
        texto += f"Nivel: {datos['nivel']['nivel']}\n"
        texto += f"Descripción: {datos['descripcion']}\n"
        texto += "-"*60 + "\n\n"
    
    return texto

def generar_recomendaciones(resultados):
    """Genera recomendaciones personalizadas basadas en los resultados"""
    recomendaciones = {}
    
    for competencia, datos in resultados.items():
        puntuacion = datos['puntuacion_normalizada']
        
        if puntuacion <= 20:
            recomendaciones[competencia] = {
                "prioridad": "alta",
                "mensaje": f"Es importante trabajar en {datos['nombre']}. Considera buscar ayuda profesional o realizar ejercicios específicos."
            }
        elif puntuacion <= 40:
            recomendaciones[competencia] = {
                "prioridad": "media",
                "mensaje": f"{datos['nombre']} está en desarrollo. Practica con situaciones desafiantes."
            }
        elif puntuacion <= 60:
            recomendaciones[competencia] = {
                "prioridad": "baja",
                "mensaje": f"Tu nivel en {datos['nombre']} es adecuado. Puedes seguir mejorando."
            }
        else:
            recomendaciones[competencia] = {
                "prioridad": "ninguna",
                "mensaje": f"¡Excelente nivel en {datos['nombre']}! Sigue así."
            }
    
    return recomendaciones

def calcular_puntuacion_general(resultados):
    """Calcula la puntuación general promedio"""
    if not resultados:
        return 0
    
    total = sum(datos['puntuacion_normalizada'] for datos in resultados.values())
    return round(total / len(resultados), 1)
