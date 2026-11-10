# evaluador.py
# Motor de evaluación de competencias

from competencias import COMPETENCIAS

class Evaluador:
    """Clase para evaluar y calcular competencias emocionales"""
    
    def __init__(self):
        self.respuestas = []
        self.puntuaciones = self._inicializar_puntuaciones()
    
    def _inicializar_puntuaciones(self):
        """Inicializa un diccionario con todas las competencias en 0"""
        return {comp: 0 for comp in COMPETENCIAS.keys()}
    
    def registrar_respuesta(self, id_situacion, opcion_indice, puntuaciones_opcion):
        """
        Registra una respuesta del usuario
        
        Args:
            id_situacion: ID de la situación
            opcion_indice: Índice de la opción seleccionada
            puntuaciones_opcion: Diccionario con las puntuaciones de esa opción
        """
        self.respuestas.append({
            "situacion_id": id_situacion,
            "opcion": opcion_indice,
            "puntuaciones": puntuaciones_opcion
        })
        
        # Acumular puntuaciones
        for competencia, puntuacion in puntuaciones_opcion.items():
            self.puntuaciones[competencia] += puntuacion
    
    def retroceder_respuesta(self):
        """Elimina la última respuesta registrada y descuenta sus puntuaciones"""
        if self.respuestas:
            ultima = self.respuestas.pop()
            for competencia, puntuacion in ultima["puntuaciones"].items():
                self.puntuaciones[competencia] -= puntuacion
            return ultima
        return None
    
    def calcular_resultados(self):
        """
        Calcula los resultados finales
        
        Returns:
            Diccionario con los resultados normalizados y el nivel
        """
        num_respuestas = len(self.respuestas)
        
        if num_respuestas == 0:
            return {}
        
        resultados = {}
        
        for competencia, puntuacion_total in self.puntuaciones.items():
            # Normalizar a escala de 0-100
            puntuacion_max = num_respuestas * 5  # Max 5 puntos por respuesta
            puntuacion_normalizada = (puntuacion_total / puntuacion_max) * 100
            
            # Determinar nivel
            nivel = self._determinar_nivel(puntuacion_normalizada)
            
            resultados[competencia] = {
                "puntuacion_total": puntuacion_total,
                "puntuacion_normalizada": round(puntuacion_normalizada, 1),
                "nivel": nivel,
                "nombre": COMPETENCIAS[competencia]["nombre"],
                "descripcion": COMPETENCIAS[competencia]["descripcion"]
            }
        
        return resultados
    
    def _determinar_nivel(self, puntuacion):
        """Determina el nivel basado en la puntuación normalizada (0-100)"""
        if puntuacion <= 20:
            return {"codigo": "rojo", "nivel": "🔴 Necesita fortalecimiento"}
        elif puntuacion <= 40:
            return {"codigo": "naranja", "nivel": "🟠 En desarrollo"}
        elif puntuacion <= 60:
            return {"codigo": "amarillo", "nivel": "🟡 Adecuado"}
        elif puntuacion <= 80:
            return {"codigo": "verde", "nivel": "🟢 Alto"}
        else:
            return {"codigo": "azul", "nivel": "⭐ Muy alto"}
    
    def obtener_progreso(self):
        """Retorna el progreso actual de evaluación"""
        return {
            "respuestas_completadas": len(self.respuestas),
            "puntuaciones_actuales": self.puntuaciones.copy()
        }
    
    def reiniciar(self):
        """Reinicia la evaluación"""
        self.respuestas = []
        self.puntuaciones = self._inicializar_puntuaciones()
