# lanzador_app.py
# Punto de entrada unificado y silencioso para DECIDE v2.0 (Modo App Nativa)

import os
import sys
import time
import socket
import threading
import subprocess
import urllib.request
import webbrowser
import traceback
from pathlib import Path

# Ajustar directorio base en modo empaquetado (PyInstaller)
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).resolve().parent
    os.chdir(BASE_DIR)
else:
    BASE_DIR = Path(__file__).resolve().parent
    os.chdir(BASE_DIR)

LOG_FILE = BASE_DIR / "debug_decide.log"

def log_debug(msg):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")
    except Exception:
        pass

def buscar_puerto_libre(puerto_inicial=5000, intentos=30):
    """Encuentra un puerto TCP disponible para evitar conflictos."""
    for p in range(puerto_inicial, puerto_inicial + intentos):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', p))
                return p
            except OSError:
                continue
    return puerto_inicial

def esperar_servidor_listo(puerto, tiempo_max=25):
    """Espera activamente a que el servidor Flask responda antes de abrir la interfaz."""
    inicio = time.time()
    url_health = f"http://127.0.0.1:{puerto}/api/health"
    log_debug(f"Esperando respuesta de salud en {url_health}...")
    while time.time() - inicio < tiempo_max:
        try:
            with urllib.request.urlopen(url_health, timeout=1) as res:
                if res.status == 200:
                    log_debug(f"Servidor listo y respondiendo 200 OK en el puerto {puerto}")
                    return True
        except Exception:
            time.sleep(0.3)
    log_debug("Tiempo de espera agotado esperando que el servidor inicie.")
    return False

def abrir_interfaz_como_app(puerto):
    """Abre la aplicación en modo ventana nativa aislada una vez que Flask está 100% listo."""
    url = f"http://127.0.0.1:{puerto}"
    
    # 1. Esperar a que el servidor esté completamente disponible
    listo = esperar_servidor_listo(puerto)
    if not listo:
        log_debug("No se pudo confirmar que el servidor estuviera listo.")
    
    # 2. Directorio de perfil aislado
    dir_temp = Path(os.environ.get("TEMP", "."))
    perfil = dir_temp / "decide_app_profile"
    try:
        perfil.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass
        
    candidatos = [
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%LocalAppData%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe")
    ]
    
    ejecutable = None
    for ruta in candidatos:
        if os.path.isfile(ruta):
            ejecutable = ruta
            break
            
    if ejecutable:
        log_debug(f"Abriendo con ejecutable: {ejecutable}")
        try:
            proc = subprocess.Popen([
                ejecutable,
                f"--app={url}",
                f"--user-data-dir={perfil}",
                "--window-size=1280,820",
                "--app-title=DECIDE v2.0 - Evaluador Emocional",
                "--no-first-run",
                "--no-default-browser-check"
            ])
            proc.wait()
            log_debug("Ventana cerrada por el usuario. Finalizando servidor.")
            os._exit(0)
        except Exception as e:
            log_debug(f"Error abriendo modo app: {e}. Usando webbrowser.")
            webbrowser.open(url)
    else:
        log_debug("No se encontró Edge o Chrome. Usando webbrowser predeterminado.")
        webbrowser.open(url)

def iniciar_servidor_web():
    """Inicia el servidor Flask y la ventana de la aplicación."""
    log_debug("Iniciando lanzador DECIDE...")
    try:
        import app_web
    except Exception as e:
        log_debug(f"ERROR importando app_web: {traceback.format_exc()}")
        return
    
    puerto = buscar_puerto_libre(int(os.environ.get("PORT", 5000)))
    log_debug(f"Puerto asignado: {puerto}")
    
    hilo = threading.Thread(target=abrir_interfaz_como_app, args=(puerto,), daemon=True)
    hilo.start()
    
    try:
        log_debug(f"Arrancando Flask en 127.0.0.1:{puerto}")
        app_web.app.run(host="127.0.0.1", port=puerto, debug=False)
    except Exception as e:
        log_debug(f"ERROR en app_web.app.run: {traceback.format_exc()}")

def main():
    try:
        iniciar_servidor_web()
    except Exception as e:
        log_debug(f"ERROR no manejado en main: {traceback.format_exc()}")

if __name__ == "__main__":
    main()
