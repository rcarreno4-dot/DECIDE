# app_web.py
# Servidor web Flask y API REST para DECIDE con React + Tailwind + Bootstrap

import os
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from basedatos import BaseDatos
from evaluador import Evaluador
from situaciones import obtener_situaciones
from competencias import obtener_competencias
from gamificacion import SistemaGamificacion
from recomendaciones import generar_recomendaciones, generar_plan_desarrollo, calcular_proximos_pasos
from resultados import calcular_puntuacion_general

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIST = BASE_DIR / "frontend" / "dist"

app = Flask(__name__, static_folder=str(FRONTEND_DIST) if FRONTEND_DIST.exists() else None)
bd = BaseDatos()

# CORS manual para soportar desarrollo con Vite (localhost:5173 u otros)
@app.after_request
def habilitar_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "app": "DECIDE v2.0 - Web Edition"})

@app.route("/api/usuario/login", methods=["POST", "OPTIONS"])
def login_usuario():
    if request.method == "OPTIONS":
        return jsonify({}), 200
    datos = request.get_json() or {}
    nombre = datos.get("nombre", "").strip()[:40]
    pin = str(datos.get("pin", "")).strip()
    
    if not nombre:
        return jsonify({"error": "El nombre es obligatorio"}), 400
    if not pin or len(pin) != 4 or not pin.isdigit():
        return jsonify({"error": "Ingresa un PIN de 4 dígitos numéricos (ej. 1234) para proteger tu cuenta"}), 400
    
    usuario_id, error = bd.autenticar_o_registrar_usuario(nombre, pin)
    if error:
        return jsonify({"error": error}), 401
    puntos = bd.obtener_puntos(usuario_id)
    nivel, info_nivel = SistemaGamificacion.calcular_nivel(puntos)
    progreso, sig_nivel, icono_sig = SistemaGamificacion.obtener_progreso_nivel(puntos)
    
    return jsonify({
        "id": usuario_id,
        "nombre": nombre,
        "puntos": puntos,
        "nivel": nivel,
        "info_nivel": info_nivel,
        "progreso_nivel": {
            "progreso": round(progreso, 1),
            "siguiente_nivel": sig_nivel,
            "icono_siguiente": icono_sig
        }
    })

@app.route("/api/competencias", methods=["GET"])
def listar_competencias():
    return jsonify(obtener_competencias())

@app.route("/api/situaciones", methods=["GET"])
def listar_situaciones():
    return jsonify(obtener_situaciones())

@app.route("/api/evaluacion/enviar", methods=["POST", "OPTIONS"])
def procesar_evaluacion():
    if request.method == "OPTIONS":
        return jsonify({}), 200
    datos = request.get_json() or {}
    usuario_id = datos.get("usuario_id")
    respuestas = datos.get("respuestas", [])
    
    if not usuario_id:
        return jsonify({"error": "Falta el ID del usuario"}), 400
    if not respuestas:
        return jsonify({"error": "No se enviaron respuestas"}), 400
    
    situaciones_dict = {s["id"]: s for s in obtener_situaciones()}
    evaluador = Evaluador()
    
    for r in respuestas:
        s_id = r.get("situacion_id")
        op_idx = r.get("opcion_indice")
        if s_id in situaciones_dict and 0 <= op_idx < len(situaciones_dict[s_id]["opciones"]):
            opcion = situaciones_dict[s_id]["opciones"][op_idx]
            evaluador.registrar_respuesta(s_id, op_idx, opcion["puntuaciones"])
            
    resultados = evaluador.calcular_resultados()
    puntuacion_general = calcular_puntuacion_general(resultados)
    
    # Persistir en base de datos
    bd.guardar_evaluacion(usuario_id, resultados, puntuacion_general)
    
    # Comprobar logros desbloqueados
    historial = bd.obtener_evaluaciones(usuario_id)
    nuevos_codigos = SistemaGamificacion.verificar_logros_desbloqueos(
        usuario_id,
        historial,
        resultados,
        bd
    )
    
    nuevos_logros_detalle = []
    for cod in nuevos_codigos:
        if cod in SistemaGamificacion.LOGROS:
            info = SistemaGamificacion.LOGROS[cod]
            nuevos_logros_detalle.append({
                "tipo": cod,
                "nombre": info["nombre"],
                "descripcion": info["descripcion"],
                "icono": info["icono"]
            })
            
    recs = generar_recomendaciones(resultados)
    plan = generar_plan_desarrollo(resultados)
    proximos_pasos = calcular_proximos_pasos(resultados)
    
    puntos_actuales = bd.obtener_puntos(usuario_id)
    nivel_actual, info_nivel = SistemaGamificacion.calcular_nivel(puntos_actuales)
    progreso, sig_nivel, icono_sig = SistemaGamificacion.obtener_progreso_nivel(puntos_actuales)
    
    return jsonify({
        "resultados": resultados,
        "puntuacion_general": puntuacion_general,
        "nuevos_logros": nuevos_logros_detalle,
        "recomendaciones": recs,
        "plan_desarrollo": plan,
        "proximos_pasos": proximos_pasos,
        "gamificacion": {
            "puntos": puntos_actuales,
            "nivel": nivel_actual,
            "info_nivel": info_nivel,
            "progreso": round(progreso, 1),
            "siguiente_nivel": sig_nivel,
            "icono_siguiente": icono_sig
        }
    })

@app.route("/api/usuario/<int:usuario_id>/historial", methods=["GET"])
def historial_usuario(usuario_id):
    evaluaciones = bd.obtener_evaluaciones(usuario_id)
    return jsonify(evaluaciones)

@app.route("/api/usuario/<int:usuario_id>/logros", methods=["GET"])
def logros_usuario(usuario_id):
    logros_bd = bd.obtener_logros(usuario_id)
    puntos = bd.obtener_puntos(usuario_id)
    nivel, info_nivel = SistemaGamificacion.calcular_nivel(puntos)
    progreso, sig_nivel, icono_sig = SistemaGamificacion.obtener_progreso_nivel(puntos)
    
    # Mapear con la definición completa de logros
    todos_los_logros = []
    logros_desbloqueados_tipos = {l["tipo"]: l["fecha"] for l in logros_bd}
    
    for tipo, info in SistemaGamificacion.LOGROS.items():
        desbloqueado = tipo in logros_desbloqueados_tipos
        todos_los_logros.append({
            "tipo": tipo,
            "nombre": info["nombre"],
            "descripcion": info["descripcion"],
            "icono": info["icono"],
            "desbloqueado": desbloqueado,
            "fecha": logros_desbloqueados_tipos.get(tipo)
        })
        
    return jsonify({
        "puntos": puntos,
        "nivel": nivel,
        "info_nivel": info_nivel,
        "progreso_nivel": {
            "progreso": round(progreso, 1),
            "siguiente_nivel": sig_nivel,
            "icono_siguiente": icono_sig
        },
        "logros": todos_los_logros,
        "total_desbloqueados": len(logros_bd)
    })

# Servir frontend estático compilado en producción
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def servir_frontend(path):
    dist_dir = FRONTEND_DIST
    if dist_dir.exists() and (dist_dir / "index.html").exists():
        if path != "" and (dist_dir / path).exists():
            return send_from_directory(str(dist_dir), path)
        return send_from_directory(str(dist_dir), "index.html")
    
    web_dir = BASE_DIR / "web"
    if web_dir.exists():
        if path != "" and (web_dir / path).exists():
            return send_from_directory(str(web_dir), path)
        return send_from_directory(str(web_dir), "index.html")

    return jsonify({
        "mensaje": "Servidor backend de DECIDE activo."
    })

@app.errorhandler(404)
def no_encontrado(e):
    # Si es ruta de API, responder JSON
    if request.path.startswith("/api/"):
        return jsonify({"error": "Recurso no encontrado"}), 404
    # Si no, redirigir a frontend
    return servir_frontend("")

@app.errorhandler(500)
def error_servidor(e):
    return jsonify({"error": "Error interno del servidor", "detalle": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f" Servidor DECIDE Web iniciado en http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
