# -*- coding: utf-8 -*-
"""
Lanzador de Escritorio 100% Nativo para DECIDE v2.0.
Abre la aplicación en una ventana de escritorio independiente (sin navegador, sin pestañas, sin barra URL).
"""

import os
import sys
import time
import socket
import threading
import webview
import app_web

def encontrar_puerto_libre(inicio=5000, fin=5050):
    for puerto in range(inicio, fin):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', puerto))
                return puerto
            except OSError:
                continue
    return 5000

def iniciar_servidor_interno(puerto):
    # Desactivar logs ruidosos de Flask
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    
    app_web.app.run(host='127.0.0.1', port=puerto, debug=False, use_reloader=False)

def main():
    puerto = encontrar_puerto_libre(5000)
    
    # Iniciar backend Flask en un hilo en segundo plano
    t = threading.Thread(target=iniciar_servidor_interno, args=(puerto,), daemon=True)
    t.start()
    
    # Pequeña espera para asegurar que el puerto esté escuchando
    time.sleep(0.4)
    
    # Crear ventana nativa de Windows (Desktop Window)
    # Sin barra de direcciones, sin pestañas, interfaz 100% de software de escritorio
    window = webview.create_window(
        title="DECIDE v2.0 - Evaluador de Competencias Emocionales",
        url=f"http://127.0.0.1:{puerto}",
        width=1240,
        height=820,
        min_size=(960, 640),
        resizable=True,
        text_select=True
    )
    
    # Iniciar el bucle de la ventana gráfica
    webview.start(private_mode=False)
    
    # Al cerrar la ventana, terminar todos los subprocesos de inmediato
    os._exit(0)

if __name__ == '__main__':
    main()
