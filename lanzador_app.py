# lanzador_app.py
# Punto de entrada unificado y silencioso para DECIDE v2.0 (Modo App Nativa)

import os
import sys
import time
import socket
import threading
import subprocess
import webbrowser
from pathlib import Path

# Ajustar directorio base en modo empaquetado (PyInstaller)
if getattr(sys, 'frozen', False):
    os.chdir(Path(sys.executable).resolve().parent)
else:
    os.chdir(Path(__file__).resolve().parent)

def buscar_puerto_libre(puerto_inicial=5000, intentos=25):
    """Encuentra un puerto TCP disponible para evitar conflictos."""
    for p in range(puerto_inicial, puerto_inicial + intentos):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', p))
                return p
            except OSError:
                continue
    return puerto_inicial

def abrir_interfaz_como_app(url):
    """Abre la URL en modo ventana de aplicación nativa (sin barra de direcciones ni pestañas)."""
    time.sleep(1.2)
    
    candidatos = [
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LocalAppData%\Microsoft\Edge\Application\msedge.exe")
    ]
    
    ejecutable = None
    for ruta in candidatos:
        if os.path.isfile(ruta):
            ejecutable = ruta
            break
            
    if ejecutable:
        try:
            # Iniciar en modo App (ventana nativa independiente)
            proc = subprocess.Popen([
                ejecutable,
                f"--app={url}",
                "--window-size=1280,820",
                "--app-title=DECIDE v2.0"
            ])
            # Esperar a que el usuario cierre la ventana para apagar el servidor
            proc.wait()
            os._exit(0)
        except Exception:
            webbrowser.open(url)
    else:
        webbrowser.open(url)

def iniciar_servidor_web():
    """Inicia el servidor Flask en segundo plano y la ventana de la aplicación."""
    import app_web
    
    puerto = buscar_puerto_libre(int(os.environ.get("PORT", 5000)))
    url = f"http://127.0.0.1:{puerto}"
    
    # Lanzar la ventana de aplicación en hilo separado
    hilo = threading.Thread(target=abrir_interfaz_como_app, args=(url,), daemon=True)
    hilo.start()
    
    # Iniciar servidor Flask
    try:
        app_web.app.run(host="127.0.0.1", port=puerto, debug=False)
    except Exception:
        pass

def main():
    iniciar_servidor_web()

if __name__ == "__main__":
    main()
