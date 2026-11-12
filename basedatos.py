# basedatos.py
# Módulo para la persistencia de datos con SQLite

import sys
import sqlite3
import json
from datetime import datetime
from pathlib import Path

class BaseDatos:
    """Gestiona la base de datos SQLite de DECIDE"""
    
    def __init__(self, archivo_db=None):
        if archivo_db is None:
            if getattr(sys, 'frozen', False):
                base_dir = Path(sys.executable).resolve().parent
            else:
                base_dir = Path(__file__).resolve().parent
            archivo_db = str(base_dir / "decide_datos.db")
        self.archivo_db = archivo_db
        self.inicializar_bd()
    
    def inicializar_bd(self):
        """Inicializa la base de datos con las tablas necesarias"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            # Tabla de usuarios
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE NOT NULL,
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabla de evaluaciones
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS evaluaciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER NOT NULL,
                    fecha_evaluacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    resultados JSON NOT NULL,
                    puntuacion_general REAL NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                )
            """)
            
            # Tabla de logros/gamificación
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS logros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER NOT NULL,
                    tipo_logro TEXT NOT NULL,
                    descripcion TEXT,
                    fecha_obtenido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                )
            """)
            
            # Asegurar columna pin en tabla usuarios
            cursor.execute("PRAGMA table_info(usuarios)")
            columnas = [col[1] for col in cursor.fetchall()]
            if "pin" not in columnas:
                cursor.execute("ALTER TABLE usuarios ADD COLUMN pin TEXT DEFAULT ''")
            
            # Asegurar columna reflexion_personal en tabla evaluaciones
            cursor.execute("PRAGMA table_info(evaluaciones)")
            columnas_eval = [col[1] for col in cursor.fetchall()]
            if "reflexion_personal" not in columnas_eval:
                cursor.execute("ALTER TABLE evaluaciones ADD COLUMN reflexion_personal TEXT DEFAULT ''")
            
            # Tabla de puntos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS puntos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER NOT NULL,
                    total_puntos INTEGER DEFAULT 0,
                    ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(usuario_id),
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                )
            """)
            
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error inicializando BD: {e}")
    
    @staticmethod
    def _hashear_pin(pin):
        """Genera un hash SHA-256 seguro para el PIN"""
        if not pin:
            return ""
        import hashlib
        return hashlib.sha256(str(pin).strip().encode()).hexdigest()
    
    def autenticar_o_registrar_usuario(self, nombre, pin):
        """
        Autentica un usuario con su PIN o lo registra si no existe.
        Retorna (usuario_id, mensaje_error)
        """
        nombre = nombre.strip()
        pin = str(pin).strip()
        pin_hash = self._hashear_pin(pin)
        
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            cursor.execute("SELECT id, pin FROM usuarios WHERE LOWER(nombre) = LOWER(?)", (nombre,))
            row = cursor.fetchone()
            
            if row:
                user_id, stored_pin = row[0], row[1]
                # Si el usuario ya existía sin PIN registrado (usuario legado), asociar este nuevo PIN
                if not stored_pin:
                    cursor.execute("UPDATE usuarios SET pin = ? WHERE id = ?", (pin_hash, user_id))
                    conn.commit()
                    conn.close()
                    return user_id, None
                
                # Si el PIN coincide
                if stored_pin == pin_hash:
                    conn.close()
                    return user_id, None
                
                # PIN incorrecto
                conn.close()
                return None, f"El nombre '{nombre}' ya está registrado con otro PIN. Si eres tú, verifica tu PIN. Si eres otro participante, añade tu apellido o alias (ej. '{nombre} Pérez' o '{nombre}2')."
            
            # Si el usuario no existe, crearlo con su PIN
            cursor.execute("INSERT INTO usuarios (nombre, pin) VALUES (?, ?)", (nombre, pin_hash))
            usuario_id = cursor.lastrowid
            cursor.execute("INSERT INTO puntos (usuario_id, total_puntos) VALUES (?, 0)", (usuario_id,))
            conn.commit()
            conn.close()
            return usuario_id, None
            
        except sqlite3.Error as e:
            return None, f"Error en base de datos: {e}"
    
    def crear_usuario(self, nombre):
        """Crea un nuevo usuario"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            cursor.execute("INSERT INTO usuarios (nombre) VALUES (?)", (nombre,))
            usuario_id = cursor.lastrowid
            
            # Crear registro de puntos inicial
            cursor.execute("INSERT INTO puntos (usuario_id, total_puntos) VALUES (?, 0)", (usuario_id,))
            
            conn.commit()
            conn.close()
            return usuario_id
        except sqlite3.IntegrityError:
            return self.obtener_usuario_id(nombre)
    
    def obtener_usuario_id(self, nombre):
        """Obtiene el ID de un usuario por nombre"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            cursor.execute("SELECT id FROM usuarios WHERE nombre = ?", (nombre,))
            resultado = cursor.fetchone()
            conn.close()
            
            return resultado[0] if resultado else None
        except sqlite3.Error as e:
            print(f"Error obteniendo usuario: {e}")
            return None
    
    def guardar_evaluacion(self, usuario_id, resultados, puntuacion_general, reflexion_personal=""):
        """Guarda los resultados de una evaluación"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            resultados_json = json.dumps(resultados, ensure_ascii=False)
            
            cursor.execute("""
                INSERT INTO evaluaciones (usuario_id, resultados, puntuacion_general, reflexion_personal)
                VALUES (?, ?, ?, ?)
            """, (usuario_id, resultados_json, puntuacion_general, reflexion_personal))
            evaluacion_id = cursor.lastrowid
            
            conn.commit()
            conn.close()
            
            # Agregar puntos
            self.agregar_puntos(usuario_id, 100)
            
            return True, evaluacion_id
        except sqlite3.Error as e:
            print(f"Error guardando evaluación: {e}")
            return False, None

    def actualizar_reflexion(self, evaluacion_id, reflexion_personal):
        """Actualiza la reflexión personal de una evaluación existente"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            cursor.execute("UPDATE evaluaciones SET reflexion_personal = ? WHERE id = ?", (reflexion_personal, evaluacion_id))
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Error actualizando reflexión: {e}")
            return False
    
    def obtener_evaluaciones(self, usuario_id):
        """Obtiene el historial de evaluaciones de un usuario"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id, fecha_evaluacion, resultados, puntuacion_general, reflexion_personal
                FROM evaluaciones
                WHERE usuario_id = ?
                ORDER BY fecha_evaluacion DESC
            """, (usuario_id,))
            
            evaluaciones = []
            for row in cursor.fetchall():
                evaluaciones.append({
                    "id": row[0],
                    "fecha": row[1],
                    "resultados": json.loads(row[2]),
                    "puntuacion_general": row[3],
                    "reflexion_personal": row[4] if len(row) > 4 and row[4] else ""
                })
            
            conn.close()
            return evaluaciones
        except sqlite3.Error as e:
            print(f"Error obteniendo evaluaciones: {e}")
            return []
    
    def agregar_puntos(self, usuario_id, puntos):
        """Agrega puntos a un usuario"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            cursor.execute("""
                UPDATE puntos 
                SET total_puntos = total_puntos + ?,
                    ultima_actualizacion = CURRENT_TIMESTAMP
                WHERE usuario_id = ?
            """, (puntos, usuario_id))
            
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error agregando puntos: {e}")
    
    def obtener_puntos(self, usuario_id):
        """Obtiene los puntos totales de un usuario"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            cursor.execute("SELECT total_puntos FROM puntos WHERE usuario_id = ?", (usuario_id,))
            resultado = cursor.fetchone()
            conn.close()
            
            return resultado[0] if resultado else 0
        except sqlite3.Error as e:
            print(f"Error obteniendo puntos: {e}")
            return 0
    
    def desbloquear_logro(self, usuario_id, tipo_logro, descripcion):
        """Desbloquea un logro para un usuario"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO logros (usuario_id, tipo_logro, descripcion)
                VALUES (?, ?, ?)
            """, (usuario_id, tipo_logro, descripcion))
            
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Error desbloqueando logro: {e}")
            return False
    
    def obtener_logros(self, usuario_id):
        """Obtiene los logros desbloqueados de un usuario"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT tipo_logro, descripcion, fecha_obtenido
                FROM logros
                WHERE usuario_id = ?
                ORDER BY fecha_obtenido DESC
            """, (usuario_id,))
            
            logros = []
            for row in cursor.fetchall():
                logros.append({
                    "tipo": row[0],
                    "descripcion": row[1],
                    "fecha": row[2]
                })
            
            conn.close()
            return logros
        except sqlite3.Error as e:
            print(f"Error obteniendo logros: {e}")
            return []
