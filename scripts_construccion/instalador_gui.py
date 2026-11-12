# instalador_gui.py
# Asistente de Instalación Gráfico para DECIDE v2.0

import os
import sys
import zipfile
import shutil
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

def obtener_ruta_recurso(nombre):
    """Obtiene la ruta del recurso bundled en PyInstaller o en directorio actual."""
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        ruta = Path(sys._MEIPASS) / nombre
        if ruta.exists():
            return ruta
    return Path(__file__).resolve().parent / nombre

class AsistenteInstalacion(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Instalador de DECIDE v2.0")
        self.geometry("560x420")
        self.resizable(False, False)
        
        # Centrar ventana en pantalla
        self.update_idletasks()
        ancho = 560
        alto = 420
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        
        # Estilo visual moderno
        self.configure(bg="#f8fafc")
        
        # Variables de estado
        localappdata = os.environ.get("LOCALAPPDATA", str(Path.home()))
        self.ruta_destino = tk.StringVar(value=str(Path(localappdata) / "DECIDE_v2"))
        self.crear_escritorio = tk.BooleanVar(value=True)
        self.crear_inicio = tk.BooleanVar(value=True)
        self.ejecutar_al_finalizar = tk.BooleanVar(value=True)
        
        self.crear_interfaz_bienvenida()

    def crear_interfaz_bienvenida(self):
        """Pantalla principal del asistente de instalación."""
        for w in self.winfo_children():
            w.destroy()
            
        # Banner Superior
        header = tk.Frame(self, bg="#1e293b", height=80)
        header.pack(fill="x", side="top")
        
        tk.Label(
            header,
            text="🧠 DECIDE v2.0 - Asistente de Instalación",
            font=("Segoe UI", 14, "bold"),
            bg="#1e293b",
            fg="#ffffff"
        ).pack(anchor="w", padx=20, pady=(15, 2))
        
        tk.Label(
            header,
            text="Evaluador de Competencias Emocionales y Habilidades Sociales",
            font=("Segoe UI", 9),
            bg="#1e293b",
            fg="#94a3b8"
        ).pack(anchor="w", padx=20, pady=(0, 10))
        
        # Contenedor Central
        cuerpo = tk.Frame(self, bg="#f8fafc", padx=25, pady=15)
        cuerpo.pack(fill="both", expand=True)
        
        tk.Label(
            cuerpo,
            text="Este asistente instalará DECIDE v2.0 en su equipo como una aplicación de escritorio nativa, lista para la entrega académica y uso inmediato.",
            font=("Segoe UI", 9),
            bg="#f8fafc",
            fg="#334155",
            justify="left",
            wraplength=500
        ).pack(anchor="w", pady=(0, 15))
        
        # Selector de Carpeta
        lbl_dir = tk.Label(cuerpo, text="Carpeta de Instalación:", font=("Segoe UI", 9, "bold"), bg="#f8fafc", fg="#1e293b")
        lbl_dir.pack(anchor="w", pady=(0, 4))
        
        f_dir = tk.Frame(cuerpo, bg="#f8fafc")
        f_dir.pack(fill="x", pady=(0, 15))
        
        e_dir = tk.Entry(f_dir, textvariable=self.ruta_destino, font=("Segoe UI", 9), bg="#ffffff", relief="solid", bd=1)
        e_dir.pack(side="left", fill="x", expand=True, ipady=4, padx=(0, 8))
        
        btn_examinar = tk.Button(
            f_dir, text="Examinar...", font=("Segoe UI", 8),
            bg="#e2e8f0", fg="#1e293b", relief="groove",
            command=self.examinar_carpeta
        )
        btn_examinar.pack(side="right", ipady=2, ipadx=8)
        
        # Opciones de accesos directos
        lbl_opc = tk.Label(cuerpo, text="Accesos Directos:", font=("Segoe UI", 9, "bold"), bg="#f8fafc", fg="#1e293b")
        lbl_opc.pack(anchor="w", pady=(0, 4))
        
        chk_escritorio = tk.Checkbutton(
            cuerpo, text="Crear acceso directo en el Escritorio",
            variable=self.crear_escritorio, font=("Segoe UI", 9),
            bg="#f8fafc", fg="#1e293b", activebackground="#f8fafc"
        )
        chk_escritorio.pack(anchor="w", pady=1)
        
        chk_inicio = tk.Checkbutton(
            cuerpo, text="Crear acceso directo en el Menú Inicio de Windows",
            variable=self.crear_inicio, font=("Segoe UI", 9),
            bg="#f8fafc", fg="#1e293b", activebackground="#f8fafc"
        )
        chk_inicio.pack(anchor="w", pady=1)
        
        # Barra Inferior de Botones
        footer = tk.Frame(self, bg="#e2e8f0", height=55)
        footer.pack(fill="x", side="bottom")
        
        btn_cancelar = tk.Button(
            footer, text="Cancelar", font=("Segoe UI", 9),
            bg="#cbd5e1", fg="#1e293b", relief="groove",
            command=self.destroy
        )
        btn_cancelar.pack(side="right", padx=(5, 20), pady=12, ipadx=10)
        
        btn_instalar = tk.Button(
            footer, text="Instalar DECIDE v2.0", font=("Segoe UI", 9, "bold"),
            bg="#2563eb", fg="#ffffff", activebackground="#1d4ed8", activeforeground="#ffffff",
            relief="flat", cursor="hand2",
            command=self.iniciar_proceso_instalacion
        )
        btn_instalar.pack(side="right", padx=5, pady=12, ipadx=15)

    def examinar_carpeta(self):
        seleccion = filedialog.askdirectory(initialdir=self.ruta_destino.get(), title="Seleccionar Carpeta de Instalación")
        if seleccion:
            self.ruta_destino.set(str(Path(seleccion) / "DECIDE_v2"))

    def iniciar_proceso_instalacion(self):
        """Muestra la barra de progreso e inicia la copia en un hilo separado."""
        for w in self.winfo_children():
            w.destroy()
            
        header = tk.Frame(self, bg="#1e293b", height=80)
        header.pack(fill="x", side="top")
        
        tk.Label(
            header, text="Instalando DECIDE v2.0...",
            font=("Segoe UI", 14, "bold"), bg="#1e293b", fg="#ffffff"
        ).pack(anchor="w", padx=20, pady=(15, 2))
        
        tk.Label(
            header, text="Por favor espere mientras se configuran los archivos.",
            font=("Segoe UI", 9), bg="#1e293b", fg="#94a3b8"
        ).pack(anchor="w", padx=20, pady=(0, 10))
        
        cuerpo = tk.Frame(self, bg="#f8fafc", padx=25, pady=40)
        cuerpo.pack(fill="both", expand=True)
        
        self.lbl_estado = tk.Label(
            cuerpo, text="Preparando la instalación...",
            font=("Segoe UI", 9), bg="#f8fafc", fg="#475569"
        )
        self.lbl_estado.pack(anchor="w", pady=(0, 10))
        
        self.barra_progreso = ttk.Progressbar(cuerpo, mode="indeterminate", length=500)
        self.barra_progreso.pack(fill="x", pady=(0, 20))
        self.barra_progreso.start(10)
        
        # Ejecutar en segundo plano
        hilo = threading.Thread(target=self._hilo_instalacion, daemon=True)
        hilo.start()

    def _hilo_instalacion(self):
        try:
            destino = Path(self.ruta_destino.get())
            destino.mkdir(parents=True, exist_ok=True)
            
            self._actualizar_estado("Extrayendo archivos del sistema...")
            
            # Buscar archivo zip empaquetado
            payload_zip = obtener_ruta_recurso("app_payload.zip")
            if payload_zip.exists():
                with zipfile.ZipFile(payload_zip, 'r') as zip_ref:
                    zip_ref.extractall(destino)
            else:
                # Si estamos en modo desarrollo o fuente, copiar dist/DECIDE_v2
                origen = Path(__file__).resolve().parent / "dist" / "DECIDE_v2"
                if origen.exists():
                    for item in origen.iterdir():
                        d_item = destino / item.name
                        if item.is_dir():
                            shutil.copytree(item, d_item, dirs_exist_ok=True)
                        else:
                            shutil.copy2(item, d_item)
                else:
                    raise Exception("No se encontró el paquete de instalación (app_payload.zip o dist/DECIDE_v2).")
            
            # Crear desinstalador
            self._actualizar_estado("Generando desinstalador...")
            self._crear_desinstalador(destino)
            
            # Crear accesos directos
            exe_path = destino / "DECIDE_v2.exe"
            
            if self.crear_escritorio.get():
                self._actualizar_estado("Creando acceso directo en el Escritorio...")
                escritorio = Path(os.path.expandvars(r"%USERPROFILE%\Desktop"))
                if not escritorio.exists():
                    escritorio = Path(os.environ.get("USERPROFILE", "")) / "OneDrive" / "Desktop"
                if escritorio.exists():
                    self._crear_acceso_directo(exe_path, escritorio / "DECIDE v2.0.lnk")
                    
            if self.crear_inicio.get():
                self._actualizar_estado("Creando acceso directo en el Menú Inicio...")
                menu_inicio = Path(os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"))
                if menu_inicio.exists():
                    self._crear_acceso_directo(exe_path, menu_inicio / "DECIDE v2.0.lnk")
            
            self._actualizar_estado("Finalizando instalación...")
            self.after(500, self.crear_interfaz_finalizada)
            
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Error de Instalación", f"Ocurrió un error:\n{e}"))
            self.after(0, self.crear_interfaz_bienvenida)

    def _actualizar_estado(self, texto):
        self.after(0, lambda: self.lbl_estado.config(text=texto))

    def _crear_acceso_directo(self, ruta_exe, ruta_lnk):
        cmd = f"""$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('{ruta_lnk}'); $s.TargetPath = '{ruta_exe}'; $s.WorkingDirectory = '{ruta_exe.parent}'; $s.Description = 'DECIDE v2.0 - Evaluador de Inteligencia Emocional'; $s.Save()"""
        subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)

    def _crear_desinstalador(self, destino):
        bat = destino / "Desinstalar_DECIDE.bat"
        contenido = f"""@echo off
title Desinstalar DECIDE v2.0
echo ===================================================================
echo     Desinstalador de DECIDE v2.0
echo ===================================================================
echo.
set /p resp="Seguro que deseas desinstalar DECIDE v2.0? (S/N): "
if /i not "%resp%"=="S" exit /b

echo Eliminando accesos directos...
del "%USERPROFILE%\\Desktop\\DECIDE v2.0.lnk" 2>nul
del "%USERPROFILE%\\OneDrive\\Desktop\\DECIDE v2.0.lnk" 2>nul
del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\DECIDE v2.0.lnk" 2>nul

echo Eliminando archivos del programa...
cd /d %LOCALAPPDATA%
rmdir /s /q "{destino}" 2>nul

echo.
echo DECIDE v2.0 ha sido desinstalado correctamente de su equipo.
pause
"""
        with open(bat, "w", encoding="utf-8") as f:
            f.write(contenido)

    def crear_interfaz_finalizada(self):
        """Pantalla de éxito."""
        for w in self.winfo_children():
            w.destroy()
            
        header = tk.Frame(self, bg="#166534", height=80)
        header.pack(fill="x", side="top")
        
        tk.Label(
            header, text="✓ ¡Instalación Completada con Éxito!",
            font=("Segoe UI", 14, "bold"), bg="#166534", fg="#ffffff"
        ).pack(anchor="w", padx=20, pady=(15, 2))
        
        tk.Label(
            header, text="DECIDE v2.0 ya está instalado y configurado en su equipo.",
            font=("Segoe UI", 9), bg="#166534", fg="#bbf7d0"
        ).pack(anchor="w", padx=20, pady=(0, 10))
        
        cuerpo = tk.Frame(self, bg="#f8fafc", padx=25, pady=25)
        cuerpo.pack(fill="both", expand=True)
        
        tk.Label(
            cuerpo,
            text=f"La aplicación se instaló correctamente en:\n{self.ruta_destino.get()}\n\nPuede abrirla en cualquier momento desde el acceso directo de su Escritorio o desde el Menú Inicio de Windows sin ninguna ventana de consola.",
            font=("Segoe UI", 9), bg="#f8fafc", fg="#334155",
            justify="left", wraplength=500
        ).pack(anchor="w", pady=(0, 20))
        
        chk_ejecutar = tk.Checkbutton(
            cuerpo, text="Ejecutar DECIDE v2.0 ahora mismo",
            variable=self.ejecutar_al_finalizar, font=("Segoe UI", 9, "bold"),
            bg="#f8fafc", fg="#1e293b", activebackground="#f8fafc"
        )
        chk_ejecutar.pack(anchor="w", pady=5)
        
        footer = tk.Frame(self, bg="#e2e8f0", height=55)
        footer.pack(fill="x", side="bottom")
        
        btn_finalizar = tk.Button(
            footer, text="Finalizar", font=("Segoe UI", 9, "bold"),
            bg="#166534", fg="#ffffff", activebackground="#14532d", activeforeground="#ffffff",
            relief="flat", cursor="hand2",
            command=self.finalizar
        )
        btn_finalizar.pack(side="right", padx=20, pady=12, ipadx=20)

    def finalizar(self):
        if self.ejecutar_al_finalizar.get():
            exe_path = Path(self.ruta_destino.get()) / "DECIDE_v2.exe"
            if exe_path.exists():
                subprocess.Popen([str(exe_path)], cwd=str(exe_path.parent))
        self.destroy()

if __name__ == "__main__":
    app = AsistenteInstalacion()
    app.mainloop()
