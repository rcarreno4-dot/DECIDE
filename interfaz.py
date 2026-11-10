# interfaz.py
# Interfaz gráfica con Tkinter

import tkinter as tk
from tkinter import ttk, messagebox
from situaciones import obtener_situaciones, obtener_situacion
from evaluador import Evaluador
from resultados import mostrar_resultados_texto

class InterfazDECIDE:
    """Interfaz gráfica para DECIDE"""
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("DECIDE - Evaluador de Competencias Emocionales")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        
        self.evaluador = Evaluador()
        self.situaciones = obtener_situaciones()
        self.situacion_actual = 0
        self.opcion_seleccionada = tk.StringVar()
        
        self.configurar_estilos()
        self.mostrar_pantalla_inicio()
    
    def configurar_estilos(self):
        """Configura los estilos de la interfaz"""
        estilo = ttk.Style()
        estilo.theme_use("clam")
        
        # Colores
        estilo.configure("Titulo.TLabel", font=("Arial", 18, "bold"), foreground="#1a1a1a")
        estilo.configure("Subtitulo.TLabel", font=("Arial", 12, "bold"), foreground="#333333")
        estilo.configure("Normal.TLabel", font=("Arial", 10), foreground="#555555")
        estilo.configure("Boton.TButton", font=("Arial", 10))
    
    def limpiar_ventana(self):
        """Limpia todos los widgets de la ventana"""
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    def mostrar_pantalla_inicio(self):
        """Muestra la pantalla de inicio"""
        self.limpiar_ventana()
        
        frame_principal = ttk.Frame(self.ventana, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(frame_principal, text="🧠 DECIDE", style="Titulo.TLabel")
        titulo.pack(pady=20)
        
        # Subtítulo
        subtitulo = ttk.Label(
            frame_principal,
            text="Evaluador de Competencias Emocionales",
            style="Subtitulo.TLabel"
        )
        subtitulo.pack(pady=10)
        
        # Descripción
        descripcion = ttk.Label(
            frame_principal,
            text="Descubre cómo reaccionas ante diferentes situaciones\ny conoce tus fortalezas emocionales.",
            style="Normal.TLabel",
            justify=tk.CENTER
        )
        descripcion.pack(pady=30)
        
        # Info de situaciones
        info = ttk.Label(
            frame_principal,
            text=f"Te presentaremos {len(self.situaciones)} situaciones diferentes.",
            style="Normal.TLabel"
        )
        info.pack(pady=20)
        
        # Botón comenzar
        boton_comenzar = ttk.Button(
            frame_principal,
            text="🚀 Comenzar Evaluación",
            command=self.mostrar_situacion,
            style="Boton.TButton"
        )
        boton_comenzar.pack(pady=20)
        
        # Información adicional
        info_extra = ttk.Label(
            frame_principal,
            text="No hay respuestas correctas o incorrectas.\nResponde honestamente según cómo actuarías realmente.",
            style="Normal.TLabel",
            justify=tk.CENTER,
            foreground="#999999"
        )
        info_extra.pack(pady=30)
    
    def mostrar_situacion(self):
        """Muestra la situación actual"""
        if self.situacion_actual >= len(self.situaciones):
            self.mostrar_resultados()
            return
        
        self.limpiar_ventana()
        
        situacion = self.situaciones[self.situacion_actual]
        
        frame_principal = ttk.Frame(self.ventana, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Progreso
        progreso_txt = f"Situación {self.situacion_actual + 1}/{len(self.situaciones)}"
        progreso = ttk.Label(frame_principal, text=progreso_txt, style="Normal.TLabel", foreground="#0066cc")
        progreso.pack(pady=5)
        
        # Barra de progreso
        progreso_bar = ttk.Progressbar(
            frame_principal,
            length=400,
            mode="determinate",
            value=(self.situacion_actual / len(self.situaciones)) * 100
        )
        progreso_bar.pack(pady=10)
        
        # Título de la situación
        titulo = ttk.Label(frame_principal, text=situacion["titulo"], style="Subtitulo.TLabel")
        titulo.pack(pady=15)
        
        # Descripción
        descripcion = ttk.Label(
            frame_principal,
            text=situacion["descripcion"],
            style="Normal.TLabel",
            justify=tk.LEFT,
            wraplength=700
        )
        descripcion.pack(pady=15, fill=tk.X)
        
        # Frame para opciones
        frame_opciones = ttk.Frame(frame_principal)
        frame_opciones.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # Opciones de respuesta
        self.opcion_seleccionada.set("")
        
        for i, opcion in enumerate(situacion["opciones"]):
            rb = ttk.Radiobutton(
                frame_opciones,
                text=opcion["texto"],
                variable=self.opcion_seleccionada,
                value=str(i),
                style="Normal.TLabel"
            )
            rb.pack(anchor=tk.W, pady=10, padx=20)
        
        # Frame para botones
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(pady=20)
        
        # Botón siguiente
        boton_siguiente = ttk.Button(
            frame_botones,
            text="Siguiente →",
            command=self.procesar_respuesta,
            style="Boton.TButton"
        )
        boton_siguiente.pack(side=tk.RIGHT, padx=5)
        
        # Botón atrás (si no es la primera)
        if self.situacion_actual > 0:
            boton_atras = ttk.Button(
                frame_botones,
                text="← Atrás",
                command=self.ir_atras,
                style="Boton.TButton"
            )
            boton_atras.pack(side=tk.LEFT, padx=5)
    
    def procesar_respuesta(self):
        """Procesa la respuesta seleccionada"""
        if not self.opcion_seleccionada.get():
            messagebox.showwarning("Advertencia", "Por favor, selecciona una opción.")
            return
        
        indice_opcion = int(self.opcion_seleccionada.get())
        situacion = self.situaciones[self.situacion_actual]
        opcion = situacion["opciones"][indice_opcion]
        
        # Registrar respuesta
        self.evaluador.registrar_respuesta(
            situacion["id"],
            indice_opcion,
            opcion["puntuaciones"]
        )
        
        self.situacion_actual += 1
        self.mostrar_situacion()
    
    def ir_atras(self):
        """Va a la situación anterior"""
        if self.situacion_actual > 0:
            self.situacion_actual -= 1
            ultima = self.evaluador.retroceder_respuesta()
            self.mostrar_situacion()
            if ultima is not None:
                self.opcion_seleccionada.set(str(ultima.get("opcion", "")))
    
    def mostrar_resultados(self):
        """Muestra los resultados de la evaluación"""
        self.limpiar_ventana()
        
        resultados = self.evaluador.calcular_resultados()
        
        frame_principal = ttk.Frame(self.ventana, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(frame_principal, text="📊 Tu Perfil DECIDE", style="Titulo.TLabel")
        titulo.pack(pady=20)
        
        # Frame scrollable para resultados
        canvas = tk.Canvas(frame_principal)
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Mostrar cada competencia
        for competencia, datos in resultados.items():
            frame_competencia = ttk.Frame(scrollable_frame, relief=tk.SOLID, borderwidth=1)
            frame_competencia.pack(fill=tk.X, pady=10, padx=5)
            
            # Nombre y nivel
            nombre_nivel = ttk.Label(
                frame_competencia,
                text=f"{datos['nombre']}: {datos['nivel']['nivel']}",
                style="Subtitulo.TLabel"
            )
            nombre_nivel.pack(anchor=tk.W, padx=10, pady=5)
            
            # Puntuación
            puntuacion = ttk.Label(
                frame_competencia,
                text=f"Puntuación: {datos['puntuacion_normalizada']}%",
                style="Normal.TLabel"
            )
            puntuacion.pack(anchor=tk.W, padx=10)
            
            # Descripción
            desc = ttk.Label(
                frame_competencia,
                text=datos['descripcion'],
                style="Normal.TLabel",
                foreground="#666666",
                wraplength=700
            )
            desc.pack(anchor=tk.W, padx=10, pady=(0, 5))
        
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botones de acción
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(pady=20)
        
        boton_reiniciar = ttk.Button(
            frame_botones,
            text="🔄 Realizar nuevamente",
            command=self.reiniciar_evaluacion,
            style="Boton.TButton"
        )
        boton_reiniciar.pack(side=tk.LEFT, padx=5)
        
        boton_salir = ttk.Button(
            frame_botones,
            text="Salir",
            command=self.ventana.quit,
            style="Boton.TButton"
        )
        boton_salir.pack(side=tk.LEFT, padx=5)
    
    def reiniciar_evaluacion(self):
        """Reinicia la evaluación"""
        self.evaluador.reiniciar()
        self.situacion_actual = 0
        self.opcion_seleccionada.set("")
        self.mostrar_pantalla_inicio()

def main():
    """Función principal"""
    ventana = tk.Tk()
    app = InterfazDECIDE(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
