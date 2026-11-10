# gamificacion.py
# Sistema de gamificación para DECIDE

class SistemaGamificacion:
    """Sistema de gamificación con logros, niveles y puntos"""
    
    LOGROS = {
        "primer_evaluacion": {
            "nombre": "🚀 Primer paso",
            "descripcion": "Completaste tu primera evaluación",
            "icono": "🌟"
        },
        "cinco_evaluaciones": {
            "nombre": "📚 Estudiante dedicado",
            "descripcion": "Completaste 5 evaluaciones",
            "icono": "📚"
        },
        "diez_evaluaciones": {
            "nombre": "🏆 Experto en autoconocimiento",
            "descripcion": "Completaste 10 evaluaciones",
            "icono": "🏆"
        },
        "autoconocimiento_alto": {
            "nombre": "🧠 Autoconsciente",
            "descripcion": "Alcanzaste nivel alto en autoconocimiento",
            "icono": "🧠"
        },
        "empatia_alta": {
            "nombre": "❤️ Empático",
            "descripcion": "Alcanzaste nivel alto en empatía",
            "icono": "❤️"
        },
        "autorregulacion_alta": {
            "nombre": "🧘 Zen",
            "descripcion": "Alcanzaste nivel alto en autorregulación",
            "icono": "🧘"
        },
        "comunicacion_alta": {
            "nombre": "🗣️ Comunicador",
            "descripcion": "Alcanzaste nivel alto en comunicación asertiva",
            "icono": "🗣️"
        },
        "trabajo_equipo_alto": {
            "nombre": "🤝 Teamwork",
            "descripcion": "Alcanzaste nivel alto en trabajo en equipo",
            "icono": "🤝"
        },
        "manejo_conflictos_alto": {
            "nombre": "⚔️ Pacificador",
            "descripcion": "Alcanzaste nivel alto en manejo de conflictos",
            "icono": "⚔️"
        },
        "resiliencia_alta": {
            "nombre": "💪 Resiliente",
            "descripcion": "Alcanzaste nivel alto en resiliencia",
            "icono": "💪"
        },
        "todas_competencias_altas": {
            "nombre": "⭐ Maestro emocional",
            "descripcion": "Todas tus competencias están en nivel alto o muy alto",
            "icono": "⭐"
        },
        "mejora_consistente": {
            "nombre": "📈 Progresión",
            "descripcion": "Mejoraste tu puntuación general en 2 evaluaciones consecutivas",
            "icono": "📈"
        }
    }
    
    NIVELES = {
        0: {"nombre": "Novato", "rango_puntos": (0, 99), "icono": "🥚"},
        1: {"nombre": "Principiante", "rango_puntos": (100, 299), "icono": "🌱"},
        2: {"nombre": "Intermedio", "rango_puntos": (300, 599), "icono": "🌿"},
        3: {"nombre": "Avanzado", "rango_puntos": (600, 999), "icono": "🌳"},
        4: {"nombre": "Experto", "rango_puntos": (1000, 1999), "icono": "🏔️"},
        5: {"nombre": "Maestro", "rango_puntos": (2000, float('inf')), "icono": "👑"}
    }
    
    @staticmethod
    def calcular_nivel(puntos):
        """Calcula el nivel basado en los puntos acumulados"""
        for nivel, info in SistemaGamificacion.NIVELES.items():
            if info["rango_puntos"][0] <= puntos < info["rango_puntos"][1]:
                return nivel, info
        return 5, SistemaGamificacion.NIVELES[5]
    
    @staticmethod
    def obtener_progreso_nivel(puntos):
        """Obtiene el progreso hacia el siguiente nivel"""
        nivel_actual, info_nivel = SistemaGamificacion.calcular_nivel(puntos)
        
        if nivel_actual == 5:
            return 100, "Maestro", "👑"
        
        nivel_siguiente = nivel_actual + 1
        info_siguiente = SistemaGamificacion.NIVELES[nivel_siguiente]
        
        puntos_necesarios_actual = info_nivel["rango_puntos"][0]
        puntos_necesarios_siguiente = info_siguiente["rango_puntos"][0]
        
        puntos_en_rango = puntos - puntos_necesarios_actual
        total_rango = puntos_necesarios_siguiente - puntos_necesarios_actual
        
        progreso = (puntos_en_rango / total_rango) * 100
        
        return min(progreso, 100), info_siguiente["nombre"], info_siguiente["icono"]
    
    @staticmethod
    def verificar_logros_desbloqueos(usuario_id, evaluaciones, resultados, basedatos):
        """
        Verifica qué logros se han desbloqueado basándose en el progreso
        
        Returns:
            Lista de nuevos logros desbloqueados
        """
        nuevos_logros = []
        logros_existentes = {logro["tipo"] for logro in basedatos.obtener_logros(usuario_id)}
        
        # Logro: Primera evaluación
        if len(evaluaciones) == 1 and "primer_evaluacion" not in logros_existentes:
            basedatos.desbloquear_logro(
                usuario_id, 
                "primer_evaluacion",
                SistemaGamificacion.LOGROS["primer_evaluacion"]["descripcion"]
            )
            nuevos_logros.append("primer_evaluacion")
        
        # Logro: 5 evaluaciones
        if len(evaluaciones) >= 5 and "cinco_evaluaciones" not in logros_existentes:
            basedatos.desbloquear_logro(
                usuario_id,
                "cinco_evaluaciones",
                SistemaGamificacion.LOGROS["cinco_evaluaciones"]["descripcion"]
            )
            nuevos_logros.append("cinco_evaluaciones")
        
        # Logro: 10 evaluaciones
        if len(evaluaciones) >= 10 and "diez_evaluaciones" not in logros_existentes:
            basedatos.desbloquear_logro(
                usuario_id,
                "diez_evaluaciones",
                SistemaGamificacion.LOGROS["diez_evaluaciones"]["descripcion"]
            )
            nuevos_logros.append("diez_evaluaciones")
        
        # Logros por competencias altas
        competencias_altas = {
            comp: logro for comp, logro in [
                ("autoconocimiento", "autoconocimiento_alto"),
                ("empatia", "empatia_alta"),
                ("autorregulacion", "autorregulacion_alta"),
                ("comunicacion", "comunicacion_alta"),
                ("trabajo_equipo", "trabajo_equipo_alto"),
                ("manejo_conflictos", "manejo_conflictos_alto"),
                ("resiliencia", "resiliencia_alta")
            ]
        }
        
        for comp, logro in competencias_altas.items():
            if comp in resultados and resultados[comp]["puntuacion_normalizada"] >= 80:
                if logro not in logros_existentes:
                    basedatos.desbloquear_logro(
                        usuario_id,
                        logro,
                        SistemaGamificacion.LOGROS[logro]["descripcion"]
                    )
                    nuevos_logros.append(logro)
        
        # Logro: Todas las competencias altas
        todas_altas = all(
            resultados.get(comp, {}).get("puntuacion_normalizada", 0) >= 60
            for comp in [
                "autoconocimiento", "empatia", "autorregulacion",
                "comunicacion", "trabajo_equipo", "manejo_conflictos", "resiliencia"
            ]
        )
        
        if todas_altas and "todas_competencias_altas" not in logros_existentes:
            basedatos.desbloquear_logro(
                usuario_id,
                "todas_competencias_altas",
                SistemaGamificacion.LOGROS["todas_competencias_altas"]["descripcion"]
            )
            nuevos_logros.append("todas_competencias_altas")
        
        # Logro: Mejora consistente
        if len(evaluaciones) >= 2 and "mejora_consistente" not in logros_existentes:
            if evaluaciones[0]["puntuacion_general"] > evaluaciones[1]["puntuacion_general"]:
                basedatos.desbloquear_logro(
                    usuario_id,
                    "mejora_consistente",
                    SistemaGamificacion.LOGROS["mejora_consistente"]["descripcion"]
                )
                nuevos_logros.append("mejora_consistente")
        
        return nuevos_logros
