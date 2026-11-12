# lanzador_app.py
# Punto de entrada unificado y ejecutable para DECIDE v2.0

import os
import sys
import time
import socket
import threading
import webbrowser
from pathlib import Path

# Configurar encoding seguro para consola de Windows
if sys.platform.startswith('win'):
    try:
        import io
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        if hasattr(sys.stderr, 'buffer'):
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

# Ajustar directorio base en modo empaquetado (PyInstaller)
if getattr(sys, 'frozen', False):
    os.chdir(Path(sys.executable).resolve().parent)
else:
    os.chdir(Path(__file__).resolve().parent)

def buscar_puerto_libre(puerto_inicial=5000, intentos=20):
    """Encuentra un puerto TCP disponible para evitar conflictos."""
    for p in range(puerto_inicial, puerto_inicial + intentos):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', p))
                return p
            except OSError:
                continue
    return puerto_inicial

def abrir_navegador_demorado(url, demora=1.5):
    """Abre la aplicación automáticamente en el navegador web del sistema."""
    time.sleep(demora)
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Nota: Abre manualmente tu navegador en: {url}")

def iniciar_servidor_web():
    """Inicia el servidor Flask y la interfaz web moderna."""
    import app_web
    
    puerto = buscar_puerto_libre(int(os.environ.get("PORT", 5000)))
    url = f"http://localhost:{puerto}"
    
    print("\n" + "=" * 68)
    print("  DECIDE v2.0 - Evaluador de Competencias Emocionales")
    print("  Habilidades Sociales y Resolucion Pacifica de Conflictos")
    print("=" * 68)
    print(f"\n [OK] Servidor web iniciado en: {url}")
    print(" [OK] Abriendo interfaz en tu navegador predeterminado...")
    print("\n -> Manten esta consola abierta mientras utilices la aplicacion.")
    print(" -> Para cerrar la aplicacion, simplemente cierra esta ventana.\n")
    print("=" * 68 + "\n", flush=True)
    
    # Abrir navegador en hilo secundario
    hilo = threading.Thread(target=abrir_navegador_demorado, args=(url,), daemon=True)
    hilo.start()
    
    # Iniciar servidor Flask
    try:
        app_web.app.run(host="127.0.0.1", port=puerto, debug=False)
    except KeyboardInterrupt:
        print("\nServidor cerrado correctamente.")

def iniciar_interfaz_escritorio():
    """Inicia la interfaz gráfica tradicional de Tkinter."""
    from interfaz_mejorada import main as main_gui
    print("Iniciando DECIDE - Interfaz de Escritorio (Tkinter)...")
    main_gui()

def main():
    if "--escritorio" in sys.argv or "--gui" in sys.argv:
        iniciar_interfaz_escritorio()
    else:
        iniciar_servidor_web()

if __name__ == "__main__":
    main()
