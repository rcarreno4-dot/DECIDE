# 🧠 DECIDE - Evaluador de Competencias Emocionales

Una aplicación interactiva completa para evaluar y desarrollar competencias emocionales mediante situaciones de toma de decisiones, gamificación y seguimiento personalizado.

## 📋 Características Principales

### Evaluación
- ✅ **16 situaciones realistas** en múltiples categorías (laboral, académico, relaciones, presión)
- ✅ Múltiples opciones de respuesta con puntuación diferenciada
- ✅ Cálculo automático de 9 competencias emocionales
- ✅ Perfil emocional personalizado con visualización en tiempo real

### Gamificación
- ✅ **Sistema de puntos y niveles** (6 niveles: Novato → Maestro)
- ✅ **12 logros desbloqueables** según desempeño
- ✅ Barra de progreso hacia el siguiente nivel
- ✅ Puntos por cada evaluación completada

### Persistencia y Seguimiento
- ✅ **Base de datos SQLite** para guardar evaluaciones
- ✅ Historial completo de evaluaciones
- ✅ Comparación de resultados a lo largo del tiempo
- ✅ Gestión de múltiples usuarios

### Recomendaciones Personalizadas
- ✅ **Recomendaciones adaptadas** por competencia
- ✅ Diferentes estrategias según nivel actual
- ✅ Plan de desarrollo personalizado
- ✅ Próximos pasos prioritarios

### Interfaz
- ✅ Interfaz gráfica moderna con Tkinter
- ✅ Sistema de login/registro de usuarios
- ✅ Menú principal con múltiples opciones
- ✅ Visualización intuitiva de resultados y logros

## 🎯 Competencias Evaluadas

1. 🧠 Autoconocimiento
2. 🧘 Autorregulación
3. ❤️ Empatía
4. 🗣️ Comunicación asertiva
5. 🤝 Trabajo en equipo
6. ⚡ Toma de decisiones
7. 🔥 Tolerancia a la frustración
8. ⚔️ Manejo de conflictos
9. 💪 Resiliencia

## 📁 Estructura del Proyecto

```
AppCarlos/
├── main.py                      # Punto de entrada
├── interfaz_mejorada.py         # Interfaz gráfica mejorada
├── interfaz.py                  # Interfaz gráfica básica (MVP)
├── competencias.py              # Definición de competencias
├── situaciones.py               # Banco de 16 situaciones
├── evaluador.py                 # Motor de evaluación
├── basedatos.py                 # Gestión de base de datos SQLite
├── gamificacion.py              # Sistema de logros y niveles
├── recomendaciones.py           # Generación de recomendaciones
├── resultados.py                # Cálculo de resultados
├── requirements.txt             # Dependencias
├── decide_datos.db              # Base de datos SQLite (generado)
└── README.md                    # Este archivo
```

## 🚀 Instalación

1. Clonar o descargar el proyecto
2. Instalar dependencias (opcionalmente):
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar:
   ```bash
   python main.py
   ```

## 🎮 Cómo Usar

### Primera vez
1. Inicia la aplicación
2. Ingresa tu nombre para crear una cuenta
3. Selecciona "Nueva Evaluación"
4. Responde las 16 situaciones honestamente
5. Visualiza tu perfil emocional con recomendaciones

### Menú Principal
- **📝 Nueva Evaluación**: Realiza una nueva evaluación completa
- **📊 Mis Resultados**: Ve el historial de todas tus evaluaciones
- **🏆 Mis Logros**: Visualiza tus logros desbloqueados y nivel actual
- **🚪 Cambiar Usuario**: Cambia de usuario

## 📊 Sistema de Niveles

| Nivel | Nombre | Rango de Puntos | Icono |
|-------|--------|-----------------|-------|
| 0 | Novato | 0-99 | 🥚 |
| 1 | Principiante | 100-299 | 🌱 |
| 2 | Intermedio | 300-599 | 🌿 |
| 3 | Avanzado | 600-999 | 🌳 |
| 4 | Experto | 1000-1999 | 🏔️ |
| 5 | Maestro | 2000+ | 👑 |

## 🏆 Logros Disponibles

- 🚀 Primer paso: Completa tu primera evaluación
- 📚 Estudiante dedicado: Completa 5 evaluaciones
- 🏆 Experto en autoconocimiento: Completa 10 evaluaciones
- 🧠 Autoconsciente: Nivel alto en autoconocimiento
- ❤️ Empático: Nivel alto en empatía
- 🧘 Zen: Nivel alto en autorregulación
- 🗣️ Comunicador: Nivel alto en comunicación asertiva
- 🤝 Teamwork: Nivel alto en trabajo en equipo
- ⚔️ Pacificador: Nivel alto en manejo de conflictos
- 💪 Resiliente: Nivel alto en resiliencia
- ⭐ Maestro emocional: Todas las competencias altas
- 📈 Progresión: Mejora consistente entre evaluaciones

## 📈 Fases del Proyecto

**Fase 1 ✅ COMPLETADA**: Evaluación MVP + Tkinter  
**Fase 2 ✅ COMPLETADA**: Gamificación + Seguimiento histórico  
**Fase 3 ✅ COMPLETADA**: Base de datos SQLite + Sistema de usuarios  
**Fase 4 ✅ COMPLETADA**: Recomendaciones avanzadas + Interfaz mejorada  
**Fase 5 (Futura)**: Visualizaciones gráficas (Matplotlib/Plotly)  
**Fase 6 (Futura)**: Sistema de administrador para crear situaciones  
**Fase 7 ✅ COMPLETADA**: Aplicación web (Flask/React + Tailwind + Bootstrap + Animaciones)

## 🌐 Edición Web Moderna (React + Tailwind + Bootstrap)

Para ejecutar la versión web interactiva con animaciones fluidas, medidores SVG y confetti:

```bash
# En terminal:
python app_web.py

# O con 1 clic:
Doble clic en iniciar_web.bat
```
Abre en tu navegador: `http://localhost:5000`
