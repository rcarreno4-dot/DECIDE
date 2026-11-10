# interfaz_mejorada.py
# Interfaz gráfica mejorada con todas las características

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from situaciones import obtener_situaciones, obtener_situacion
from evaluador import Evaluador
from basedatos import BaseDatos
from gamificacion import SistemaGamificacion
from recomendaciones import generar_recomendaciones, obtener_nivel_texto

class InterfazDECIDEMejorada:
    """Interfaz gráfica mejorada para DECIDE"""
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("DECIDE - Evaluador de Competencias Emocionales v2.0")
        self.ventana.geometry("900x700")
        self.ventana.resizable(True, True)
        
        # Inicializar componentes
        self.bd = BaseDatos()
        self.evaluador = Evaluador()
        self.situaciones = obtener_situaciones()
        
        # Estado
        self.usuario_id = None
        self.usuario_nombre = None
        self.situacion_actual = 0
        self.opcion_seleccionada = tk.StringVar()
        
        self.configurar_estilos()
        self.mostrar_login()
    
    def configurar_estilos(self):
        """Configura los estilos de la interfaz"""
        estilo = ttk.Style()
        estilo.theme_use("clam")
        
        # Definir colores
        estilo.configure("Titulo.TLabel", font=("Arial", 20, "bold"), foreground="#1a1a1a")
        estilo.configure("Subtitulo.TLabel", font=("Arial", 14, "bold"), foreground="#333333")
        estilo.configure("Normal.TLabel", font=("Arial", 10), foreground="#555555")
        estilo.configure("Pequeno.TLabel", font=("Arial", 9), foreground="#777777")
        estilo.configure("Boton.TButton", font=("Arial", 10))
        estilo.configure("Verde.TLabel", font=("Arial", 10), foreground="#2ecc71")
        estilo.configure("Naranja.TLabel", font=("Arial", 10), foreground="#e67e22")
        estilo.configure("Rojo.TLabel", font=("Arial", 10), foreground="#e74c3c")
    
    def limpiar_ventana(self):
        """Limpia todos los widgets"""
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    def mostrar_login(self):
        """Muestra la pantalla de login"""
        self.limpiar_ventana()
        
        frame_principal = ttk.Frame(self.ventana, padding="30")
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
        
        # Frame para entrada
        frame_entrada = ttk.Frame(frame_principal)
        frame_entrada.pack(pady=30)
        
        # Etiqueta
        label_nombre = ttk.Label(frame_entrada, text="Tu nombre:", style="Normal.TLabel")
        label_nombre.pack(pady=10)
        
        # Input
        entrada_nombre = ttk.Entry(frame_entrada, width=30, font=("Arial", 11))
        entrada_nombre.pack(pady=5)
        entrada_nombre.focus()
        
        def iniciar_sesion():
            nombre = entrada_nombre.get().strip()
            if not nombre:
                messagebox.showwarning("Advertencia", "Por favor ingresa tu nombre")
                return
            
            self.usuario_nombre = nombre
            self.usuario_id = self.bd.crear_usuario(nombre)
            self.mostrar_menu_principal()
        
        # Botón iniciar
        boton_iniciar = ttk.Button(
            frame_entrada,
            text="Iniciar sesión",
            command=iniciar_sesion,
            style="Boton.TButton"
        )
        boton_iniciar.pack(pady=20)
        
        # Info
        info = ttk.Label(
            frame_principal,
            text="Bienvenido. Ingresa tu nombre para comenzar.",
            style="Pequeno.TLabel"
        )
        info.pack(pady=10)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        self.limpiar_ventana()
        
        frame_principal = ttk.Frame(self.ventana, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Encabezado con nombre de usuario
        frame_encabezado = ttk.Frame(frame_principal)
        frame_encabezado.pack(fill=tk.X, pady=10)
        
        usuario_label = ttk.Label(
            frame_encabezado,
            text=f"👤 {self.usuario_nombre}",
            style="Normal.TLabel"
        )
        usuario_label.pack(side=tk.LEFT)
        
        # Puntos y nivel
        puntos = self.bd.obtener_puntos(self.usuario_id)
        nivel, info_nivel = SistemaGamificacion.calcular_nivel(puntos)
        
        nivel_label = ttk.Label(
            frame_encabezado,
            text=f"Nivel: {info_nivel['icono']} {info_nivel['nombre']} | 🎯 {puntos} puntos",
            style="Normal.TLabel"
        )
        nivel_label.pack(side=tk.RIGHT)
        
        # Título
        titulo = ttk.Label(frame_principal, text="🧠 DECIDE", style="Titulo.TLabel")
        titulo.pack(pady=20)
        
        # Opciones
        frame_opciones = ttk.Frame(frame_principal)
        frame_opciones.pack(pady=30, fill=tk.BOTH, expand=True)
        
        # Botón Nueva evaluación
        boton_evaluacion = ttk.Button(
            frame_opciones,
            text="📝 Nueva Evaluación",
            command=self.iniciar_evaluacion,
            style="Boton.TButton"
        )
        boton_evaluacion.pack(pady=10, fill=tk.X, ipady=10)
        
        # Botón Ver resultados
        boton_resultados = ttk.Button(
            frame_opciones,
            text="📊 Mis Resultados",
            command=self.mostrar_historial,
            style="Boton.TButton"
        )
        boton_resultados.pack(pady=10, fill=tk.X, ipady=10)
        
        # Botón Ver logros
        boton_logros = ttk.Button(
            frame_opciones,
            text="🏆 Mis Logros",
            command=self.mostrar_logros,
            style="Boton.TButton"
        )
        boton_logros.pack(pady=10, fill=tk.X, ipady=10)
        
        # Botón Cambiar usuario
        boton_cambiar = ttk.Button(
            frame_opciones,
            text="🚪 Cambiar Usuario",
            command=self.mostrar_login,
            style="Boton.TButton"
        )
        boton_cambiar.pack(pady=10, fill=tk.X, ipady=10)
    
    def iniciar_evaluacion(self):
        """Inicia una nueva evaluación"""
        self.evaluador.reiniciar()
        self.situacion_actual = 0
        self.mostrar_situacion()
    
    def mostrar_situacion(self):
        """Muestra la situación actual"""
        if self.situacion_actual >= len(self.situaciones):
            self.mostrar_resultados_evaluacion()
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
        
        # Título
        titulo = ttk.Label(frame_principal, text=situacion["titulo"], style="Subtitulo.TLabel")
        titulo.pack(pady=15)
        
        # Descripción
        descripcion = ttk.Label(
            frame_principal,
            text=situacion["descripcion"],
            style="Normal.TLabel",
            justify=tk.LEFT,
            wraplength=800
        )
        descripcion.pack(pady=15, fill=tk.X)
        
        # Frame scrollable para opciones
        canvas = tk.Canvas(frame_principal, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Opciones de respuesta
        self.opcion_seleccionada.set("")
        
        for i, opcion in enumerate(situacion["opciones"]):
            rb = ttk.Radiobutton(
                scrollable_frame,
                text=opcion["texto"],
                variable=self.opcion_seleccionada,
                value=str(i),
                style="Normal.TLabel"
            )
            rb.pack(anchor=tk.W, pady=10, padx=20, fill=tk.X)
        
        canvas.pack(side="left", fill=tk.BOTH, expand=True, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        # Frame para botones
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(pady=20, fill=tk.X)
        
        # Botón siguiente
        boton_siguiente = ttk.Button(
            frame_botones,
            text="Siguiente →",
            command=self.procesar_respuesta,
            style="Boton.TButton"
        )
        boton_siguiente.pack(side=tk.RIGHT, padx=5)
        
        # Botón atrás
        if self.situacion_actual > 0:
            boton_atras = ttk.Button(
                frame_botones,
                text="← Atrás",
                command=self.ir_atras,
                style="Boton.TButton"
            )
            boton_atras.pack(side=tk.LEFT, padx=5)
        
        # Botón salir
        boton_salir = ttk.Button(
            frame_botones,
            text="✖ Cancelar",
            command=self.mostrar_menu_principal,
            style="Boton.TButton"
        )
        boton_salir.pack(side=tk.LEFT, padx=5)
    
    def procesar_respuesta(self):
        """Procesa la respuesta seleccionada"""
        if not self.opcion_seleccionada.get():
            messagebox.showwarning("Advertencia", "Por favor, selecciona una opción.")
            return
        
        indice_opcion = int(self.opcion_seleccionada.get())
        situacion = self.situaciones[self.situacion_actual]
        opcion = situacion["opciones"][indice_opcion]
        
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
    
    def mostrar_resultados_evaluacion(self):
        """Muestra los resultados de la evaluación completada"""
        self.limpiar_ventana()
        
        resultados = self.evaluador.calcular_resultados()
        from resultados import calcular_puntuacion_general
        puntuacion_general = calcular_puntuacion_general(resultados)
        
        # Guardar en BD
        self.bd.guardar_evaluacion(self.usuario_id, resultados, puntuacion_general)
        
        # Verificar logros
        evaluaciones = self.bd.obtener_evaluaciones(self.usuario_id)
        nuevos_logros = SistemaGamificacion.verificar_logros_desbloqueos(
            self.usuario_id,
            evaluaciones,
            resultados,
            self.bd
        )
        
        frame_principal = ttk.Frame(self.ventana, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(frame_principal, text="📊 Tu Perfil DECIDE", style="Titulo.TLabel")
        titulo.pack(pady=20)
        
        # Puntuación general
        puntuacion_label = ttk.Label(
            frame_principal,
            text=f"Puntuación General: {puntuacion_general}%",
            style="Subtitulo.TLabel"
        )
        puntuacion_label.pack(pady=10)
        
        # Nuevos logros
        if nuevos_logros:
            logros_texto = f"🏆 ¡Has desbloqueado {len(nuevos_logros)} nuevo(s) logro(s)!"
            logros_label = ttk.Label(
                frame_principal,
                text=logros_texto,
                style="Verde.TLabel"
            )
            logros_label.pack(pady=10)
        
        # Frame scrollable para resultados
        canvas = tk.Canvas(frame_principal, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Mostrar competencias
        for competencia, datos in resultados.items():
            frame_comp = ttk.Frame(scrollable_frame, relief=tk.SOLID, borderwidth=1)
            frame_comp.pack(fill=tk.X, pady=10, padx=5)
            
            # Nombre y nivel
            nombre_nivel = ttk.Label(
                frame_comp,
                text=f"{datos['nombre']}: {datos['nivel']['nivel']}",
                style="Subtitulo.TLabel"
            )
            nombre_nivel.pack(anchor=tk.W, padx=10, pady=5)
            
            # Puntuación con barra
            frame_barra = ttk.Frame(frame_comp)
            frame_barra.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
            
            puntuacion_label = ttk.Label(frame_barra, text=f"{datos['puntuacion_normalizada']}%", style="Normal.TLabel")
            puntuacion_label.pack(side=tk.LEFT)
            
            barra = ttk.Progressbar(
                frame_barra,
                length=300,
                mode="determinate",
                value=datos['puntuacion_normalizada']
            )
            barra.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        canvas.pack(side="left", fill=tk.BOTH, expand=True, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        # Botones
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(pady=20, fill=tk.X)
        
        boton_recomendaciones = ttk.Button(
            frame_botones,
            text="💡 Ver Recomendaciones",
            command=lambda: self.mostrar_recomendaciones(resultados),
            style="Boton.TButton"
        )
        boton_recomendaciones.pack(side=tk.LEFT, padx=5)
        
        boton_volver = ttk.Button(
            frame_botones,
            text="🏠 Volver al Menú",
            command=self.mostrar_menu_principal,
            style="Boton.TButton"
        )
        boton_volver.pack(side=tk.RIGHT, padx=5)
    
    def mostrar_recomendaciones(self, resultados):
        """Muestra recomendaciones personalizadas"""
        self.limpiar_ventana()
        
        recomendaciones = generar_recomendaciones(resultados)
        
        frame_principal = ttk.Frame(self.ventana, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(frame_principal, text="💡 Recomendaciones Personalizadas", style="Titulo.TLabel")
        titulo.pack(pady=20)
        
        # Canvas scrollable
        canvas = tk.Canvas(frame_principal, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Mostrar recomendaciones
        for competencia, data in recomendaciones.items():
            frame_rec = ttk.Frame(scrollable_frame, relief=tk.SOLID, borderwidth=1)
            frame_rec.pack(fill=tk.X, pady=10, padx=5)
            
            nombre_label = ttk.Label(
                frame_rec,
                text=data["nombre"],
                style="Subtitulo.TLabel"
            )
            nombre_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
            
            # Recomendación
            rec_label = ttk.Label(
                frame_rec,
                text=data["recomendacion"],
                style="Normal.TLabel",
                justify=tk.LEFT,
                wraplength=750
            )
            rec_label.pack(anchor=tk.W, padx=10, pady=(0, 10))
        
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botón volver
        boton_volver = ttk.Button(
            frame_principal,
            text="🔙 Volver",
            command=self.mostrar_menu_principal,
            style="Boton.TButton"
        )
        boton_volver.pack(pady=20)
    
    def mostrar_historial(self):
        """Muestra el historial de evaluaciones"""
        self.limpiar_ventana()
        
        evaluaciones = self.bd.obtener_evaluaciones(self.usuario_id)
        
        frame_principal = ttk.Frame(self.ventana, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(frame_principal, text="📊 Mis Evaluaciones", style="Titulo.TLabel")
        titulo.pack(pady=20)
        
        if not evaluaciones:
            info = ttk.Label(
                frame_principal,
                text="Aún no has completado evaluaciones. ¡Comienza una ahora!",
                style="Normal.TLabel"
            )
            info.pack(pady=20)
        else:
            # Canvas scrollable
            canvas = tk.Canvas(frame_principal, bg="white", highlightthickness=0)
            scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            for i, eval in enumerate(evaluaciones, 1):
                frame_eval = ttk.Frame(scrollable_frame, relief=tk.SOLID, borderwidth=1)
                frame_eval.pack(fill=tk.X, pady=10, padx=5)
                
                fecha_label = ttk.Label(
                    frame_eval,
                    text=f"Evaluación {i} - {eval['fecha']}",
                    style="Subtitulo.TLabel"
                )
                fecha_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
                
                puntuacion_label = ttk.Label(
                    frame_eval,
                    text=f"Puntuación General: {eval['puntuacion_general']}%",
                    style="Normal.TLabel"
                )
                puntuacion_label.pack(anchor=tk.W, padx=10)
            
            canvas.pack(side="left", fill=tk.BOTH, expand=True)
            scrollbar.pack(side="right", fill="y")
        
        # Botón volver
        boton_volver = ttk.Button(
            frame_principal,
            text="🏠 Volver",
            command=self.mostrar_menu_principal,
            style="Boton.TButton"
        )
        boton_volver.pack(pady=20)
    
    def mostrar_logros(self):
        """Muestra los logros desbloqueados"""
        self.limpiar_ventana()
        
        logros = self.bd.obtener_logros(self.usuario_id)
        puntos = self.bd.obtener_puntos(self.usuario_id)
        nivel, info_nivel = SistemaGamificacion.calcular_nivel(puntos)
        progreso, sig_nivel, icono_sig = SistemaGamificacion.obtener_progreso_nivel(puntos)
        
        frame_principal = ttk.Frame(self.ventana, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(frame_principal, text="🏆 Mis Logros", style="Titulo.TLabel")
        titulo.pack(pady=20)
        
        # Nivel y progreso
        frame_nivel = ttk.Frame(frame_principal, relief=tk.SOLID, borderwidth=1)
        frame_nivel.pack(fill=tk.X, pady=10)
        
        nivel_label = ttk.Label(
            frame_nivel,
            text=f"Nivel: {info_nivel['icono']} {info_nivel['nombre']}",
            style="Subtitulo.TLabel"
        )
        nivel_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        
        puntos_label = ttk.Label(
            frame_nivel,
            text=f"Puntos: {puntos}",
            style="Normal.TLabel"
        )
        puntos_label.pack(anchor=tk.W, padx=10)
        
        # Barra de progreso al siguiente nivel
        frame_progreso = ttk.Frame(frame_nivel)
        frame_progreso.pack(anchor=tk.W, padx=10, pady=(10, 10), fill=tk.X)
        
        progreso_label = ttk.Label(
            frame_progreso,
            text=f"Progreso a {icono_sig} {sig_nivel}:",
            style="Normal.TLabel"
        )
        progreso_label.pack(side=tk.LEFT)
        
        barra_prog = ttk.Progressbar(
            frame_progreso,
            length=200,
            mode="determinate",
            value=progreso
        )
        barra_prog.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        prog_txt = ttk.Label(
            frame_progreso,
            text=f"{progreso:.1f}%",
            style="Normal.TLabel"
        )
        prog_txt.pack(side=tk.LEFT, padx=5)
        
        # Logros desbloqueados
        if logros:
            frame_logros = ttk.Frame(frame_principal)
            frame_logros.pack(fill=tk.BOTH, expand=True, pady=20)
            
            for logro in logros:
                frame_logro = ttk.Frame(frame_logros, relief=tk.SOLID, borderwidth=1)
                frame_logro.pack(fill=tk.X, pady=5, padx=5)
                
                tipo_label = ttk.Label(
                    frame_logro,
                    text=f"✓ {logro['tipo']} - {logro['descripcion']}",
                    style="Verde.TLabel"
                )
                tipo_label.pack(anchor=tk.W, padx=10, pady=10)
        else:
            info = ttk.Label(
                frame_principal,
                text="¡Completa evaluaciones para desbloquear logros!",
                style="Normal.TLabel"
            )
            info.pack(pady=20)
        
        # Botón volver
        boton_volver = ttk.Button(
            frame_principal,
            text="🏠 Volver",
            command=self.mostrar_menu_principal,
            style="Boton.TButton"
        )
        boton_volver.pack(pady=20)

def main():
    """Función principal"""
    ventana = tk.Tk()
    app = InterfazDECIDEMejorada(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
