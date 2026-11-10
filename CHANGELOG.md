# CHANGELOG - DECIDE

## [2.0] - 2026-08-23

### 🚀 Características Agregadas

#### Evaluación Expandida
- **+11 situaciones** (de 5 a 16 situaciones)
- Categorías: Laboral (5), Académico (5), Relaciones (4), Presión (3)
- Mayor variedad de escenarios realistas

#### Sistema de Gamificación
- Sistema de puntos (100 puntos por evaluación)
- 6 niveles de progresión (Novato → Maestro)
- 12 logros desbloqueables
- Barra de progreso visual hacia el siguiente nivel
- Badges y reconocimientos por competencias altas

#### Base de Datos
- SQLite para persistencia de datos
- Almacenamiento de múltiples usuarios
- Historial completo de evaluaciones
- Sistema de logros desbloqueados
- Gestión de puntos por usuario

#### Recomendaciones Avanzadas
- Recomendaciones personalizadas por competencia
- Diferentes consejos según nivel actual
- Plan de desarrollo personalizado
- Próximos pasos prioritarios
- Acciones específicas para cada nivel

#### Interfaz Mejorada
- Sistema de login/registro de usuarios
- Menú principal reorganizado
- Visualización de nivel y puntos en tiempo real
- Pantalla de resultados con barra de progreso
- Sección de recomendaciones personalizadas
- Historial de evaluaciones
- Panel de logros con progreso

#### Configuración
- Archivo config.py centralizado
- Variables de configuración globales
- Fácil personalización

### 🔄 Cambios

- Interfaz refactorizada en `interfaz_mejorada.py`
- Módulo de recomendaciones más robusto
- Sistema de gamificación independiente
- Base de datos con múltiples tablas

### 📚 Documentación

- Guía de uso completa (GUIA_USO.md)
- README actualizado con características v2.0
- CHANGELOG (este archivo)
- Código comentado y documentado

### ✅ Testing

- ✓ Interfaz gráfica funcional
- ✓ Base de datos funcionando
- ✓ Sistema de gamificación integrado
- ✓ Guardado y recuperación de datos
- ✓ Multi-usuario soportado

---

## [1.0] - 2026-08-23

### 🎯 MVP Inicial

#### Características Base
- 5 situaciones iniciales
- 9 competencias emocionales
- Motor de evaluación funcional
- Interfaz básica con Tkinter
- Cálculo de resultados normalizado
- Sistema de niveles de desarrollo (🔴🟠🟡🟢⭐)
- Módulo de resultados

#### Archivos
- `main.py`: Punto de entrada
- `interfaz.py`: UI básica
- `competencias.py`: Definición de competencias
- `situaciones.py`: Banco inicial de situaciones
- `evaluador.py`: Motor de evaluación
- `resultados.py`: Cálculo de resultados
- `requirements.txt`: Dependencias

---

## Plan Futuro

### [3.0] - Visualizaciones Avanzadas
- [ ] Gráficos radar de competencias
- [ ] Gráficos de progreso temporal
- [ ] Comparación entre evaluaciones
- [ ] Exportación de reportes
- [ ] Análisis de tendencias

### [4.0] - Sistema de Administrador
- [ ] Interfaz de administrador
- [ ] Crear/editar situaciones
- [ ] Crear/editar competencias
- [ ] Gestión de usuarios avanzada
- [ ] Reportes de grupo

### [5.0] - Aplicación Web
- [ ] Backend con Flask/FastAPI
- [ ] Frontend con React/Vue
- [ ] Sincronización en la nube
- [ ] Modo colaborativo
- [ ] Compartir resultados

### [6.0] - IA y Análisis
- [ ] Recomendaciones basadas en IA
- [ ] Predicción de mejora
- [ ] Análisis de patrones
- [ ] Feedback automático mejorado

---

**Última actualización**: 23 de Agosto de 2026
