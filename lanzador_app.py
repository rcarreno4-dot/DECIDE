# -*- coding: utf-8 -*-
"""
lanzador_app.py - Punto de Entrada de Escritorio Nativo para DECIDE v2.0.
Abre la aplicación en una ventana nativa de escritorio independiente de Windows
(sin pestañas de navegador, sin barra de direcciones URL, sin apariencia web).
"""

import os
import sys
import time
import socket
import threading
import logging
from pathlib import Path

# Ajustar directorio base en modo congelado (PyInstaller) o desarrollo
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).resolve().parent
    # Redirigir stdout/stderr si no hay consola para evitar errores de I/O
    if sys.stdout is None:
        sys.stdout = open(os.devnull, 'w')
    if sys.stderr is None:
        sys.stderr = open(os.devnull, 'w')
else:
    BASE_DIR = Path(__file__).resolve().parent

os.chdir(BASE_DIR)

import app_web

def buscar_puerto_libre(puerto_inicial=5000, intentos=50):
    """Busca un puerto TCP libre en localhost."""
    for p in range(puerto_inicial, puerto_inicial + intentos):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', p))
                return p
            except OSError:
                continue
    return puerto_inicial

def iniciar_servidor_flask(puerto):
    """Inicia el servidor backend Flask en segundo plano silenciando logs."""
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    
    # Iniciar Flask en 127.0.0.1 en el puerto asignado
    app_web.app.run(host='127.0.0.1', port=puerto, debug=False, use_reloader=False)

def main():
    puerto = buscar_puerto_libre(5000)
    
    # Iniciar Flask en un hilo independiente (daemon)
    t = threading.Thread(target=iniciar_servidor_flask, args=(puerto,), daemon=True)
    t.start()
    
    # Esperar 350ms para que Flask levante el socket
    time.sleep(0.35)
    
    url_local = f"http://127.0.0.1:{puerto}"
    
    # Intentar abrir la ventana nativa de escritorio con pywebview (Edge WebView2)
    try:
        import webview
        
        # Crear la ventana de aplicación de escritorio pura
        window = webview.create_window(
            title="DECIDE v2.0 - Evaluador de Competencias Emocionales",
            url=url_local,
            width=1240,
            height=820,
            min_size=(960, 640),
            resizable=True,
            text_select=True,
            easy_drag=True
        )
        
        # Iniciar bucle de eventos nativo de Windows
        webview.start(private_mode=False)
        
    except Exception as e:
        # Fallback de contingencia si el motor WebView2 no respondiera
        import webbrowser
        webbrowser.open(url_local)
        
        # Mantener el proceso vivo
        try:
            while True:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            pass
            
    finally:
        # Al cerrar la ventana, terminar todos los subprocesos de forma inmediata y limpia
        os._exit(0)

if __name__ == '__main__':
    main()
