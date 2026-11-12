# lanzador_app.py
# Punto de entrada y panel de control nativo para DECIDE v2.0

import os
import sys
import time
import socket
import threading
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

# Ajustar directorio base en modo empaquetado (PyInstaller)
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

import app_web

def buscar_puerto_libre(puerto_inicial=5000, intentos=30):
    """Encuentra un puerto TCP disponible para evitar conflictos."""
    for p in range(puerto_inicial, puerto_inicial + intentos):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('0.0.0.0', p))
                return p
            except OSError:
                continue
    return puerto_inicial

class PanelControlDECIDE(tk.Tk):
    """Ventana nativa de escritorio para controlar la aplicación DECIDE."""
    
    def __init__(self, puerto):
        super().__init__()
        self.puerto = puerto
        self.url = f"http://localhost:{puerto}"
        
        self.title("DECIDE v2.0 - Panel de Aplicación")
        self.geometry("480x320")
        self.resizable(False, False)
        self.configure(bg="#0f172a")  # Slate 900
        
        # Centrar ventana
        self.update_idletasks()
        ancho = 480
        alto = 320
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        
        self.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)
        self.crear_widgets()
        
        # Abrir el navegador automáticamente al iniciar
        self.after(1200, self.abrir_navegador)

    def crear_widgets(self):
        # Cabecera moderna
        header = tk.Frame(self, bg="#1e293b", height=75)
        header.pack(fill="x", side="top")
        
        tk.Label(
            header,
            text="🧠 DECIDE v2.0",
            font=("Segoe UI", 16, "bold"),
            bg="#1e293b",
            fg="#38bdf8"
        ).pack(anchor="w", padx=20, pady=(12, 2))
        
        tk.Label(
            header,
            text="Evaluador de Inteligencia Emocional y Habilidades Sociales",
            font=("Segoe UI", 9),
            bg="#1e293b",
            fg="#94a3b8"
        ).pack(anchor="w", padx=20, pady=(0, 10))
        
        # Contenedor central
        cuerpo = tk.Frame(self, bg="#0f172a", padx=20, pady=15)
        cuerpo.pack(fill="both", expand=True)
        
        # Tarjeta de estado
        card_estado = tk.Frame(cuerpo, bg="#1e293b", relief="flat", padx=15, pady=12)
        card_estado.pack(fill="x", pady=(0, 15))
        
        tk.Label(
            card_estado,
            text="🟢 Servidor local activo y listo",
            font=("Segoe UI", 10, "bold"),
            bg="#1e293b",
            fg="#4ade80"
        ).pack(anchor="w", pady=(0, 4))
        
        self.lbl_url = tk.Label(
            card_estado,
            text=f"Dirección: {self.url}",
            font=("Segoe UI", 9),
            bg="#1e293b",
            fg="#cbd5e1"
        )
        self.lbl_url.pack(anchor="w")
        
        # Botón principal de apertura
        btn_abrir = tk.Button(
            cuerpo,
            text="🚀 Abrir DECIDE en Navegador",
            font=("Segoe UI", 11, "bold"),
            bg="#2563eb",
            fg="#ffffff",
            activebackground="#1d4ed8",
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            command=self.abrir_navegador
        )
        btn_abrir.pack(fill="x", ipady=8, pady=(0, 8))
        
        # Fila de acciones secundarias
        fila_sec = tk.Frame(cuerpo, bg="#0f172a")
        fila_sec.pack(fill="x")
        
        btn_copiar = tk.Button(
            fila_sec,
            text="📋 Copiar Enlace",
            font=("Segoe UI", 9),
            bg="#334155",
            fg="#e2e8f0",
            relief="flat",
            cursor="hand2",
            command=self.copiar_enlace
        )
        btn_copiar.pack(side="left", fill="x", expand=True, ipady=4, padx=(0, 5))
        
        btn_salir = tk.Button(
            fila_sec,
            text="🛑 Detener y Salir",
            font=("Segoe UI", 9),
            bg="#991b1b",
            fg="#ffffff",
            activebackground="#7f1d1d",
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            command=self.cerrar_aplicacion
        )
        btn_salir.pack(side="right", fill="x", expand=True, ipady=4, padx=(5, 0))
        
        # Pie de ventana
        tk.Label(
            self,
            text="Mantén esta ventana abierta mientras utilices la plataforma DECIDE.",
            font=("Segoe UI", 8),
            bg="#0f172a",
            fg="#64748b"
        ).pack(side="bottom", pady=8)

    def abrir_navegador(self):
        try:
            webbrowser.open(self.url)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el navegador:\n{e}")

    def copiar_enlace(self):
        self.clipboard_clear()
        self.clipboard_append(self.url)
        messagebox.showinfo("Copiado", f"Enlace copiado al portapapeles:\n{self.url}")

    def cerrar_aplicacion(self):
        self.destroy()
        os._exit(0)

def main():
    puerto = buscar_puerto_libre(int(os.environ.get("PORT", 5000)))
    
    # Iniciar servidor Flask en hilo en segundo plano
    hilo_flask = threading.Thread(
        target=lambda: app_web.app.run(host="0.0.0.0", port=puerto, debug=False, use_reloader=False),
        daemon=True
    )
    hilo_flask.start()
    
    # Iniciar ventana nativa de control (bloqueante en hilo principal)
    panel = PanelControlDECIDE(puerto)
    panel.mainloop()

if __name__ == "__main__":
    main()
