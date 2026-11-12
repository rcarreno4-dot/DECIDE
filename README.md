# 🧠 DECIDE v2.0 - Evaluación de Competencias Emocionales y Resolución de Conflictos

[![Licencia](https://img.shields.io/badge/Licencia-Educativa-blue.svg)](LICENSE)
[![Normas APA](https://img.shields.io/badge/Formato-APA%207ma%20Edici%C3%B3n-green.svg)](PROYECTO_FINAL_DECIDE_v2_APA7.docx)
[![Plataforma](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6.svg?logo=windows)](Instalador_DECIDE_v2.exe)
[![Tecnología](https://img.shields.io/badge/Stack-React%2018%20%7C%20Tailwind%20%7C%20Flask-purple.svg)](web/index.html)

**DECIDE v2.0** es una plataforma interactiva psicométrica basada en **Tests de Juicio Situacional (Situational Judgement Tests - SJT)** desarrollada para evaluar, diagnosticar y potenciar competencias socioemocionales, habilidades sociales y estrategias de resolución pacífica de conflictos en entornos académicos y profesionales.

---

## 📂 Directorio de Entregables Principales del Proyecto

Para la entrega y sustentación formal ante el docente, el repositorio cuenta con los siguientes documentos y herramientas listos para su uso:

| Recurso / Entregable | Formato | Descripción |
| :--- | :--- | :--- |
| **Documento del Trabajo de Semestre** | [`.docx`](1_DOCUMENTOS_ENTREGA/PROYECTO_FINAL_DECIDE_v2_APA7.docx) / [`.md`](1_DOCUMENTOS_ENTREGA/PROYECTO_FINAL_ESTRUCTURA_APA.md) | Informe académico formal en **Normas APA (7.ª Edición)** con las 11 fases de la rúbrica (Diagnóstico, Problema, Objetivos, Justificación, Bases Teóricas, Metodología, Análisis, Propuesta de Mejora, Reflexión y Referencias). |
| **Manual de Usuario** | [`.docx`](1_DOCUMENTOS_ENTREGA/MANUAL_DE_USUARIO_DECIDE_v2.docx) / [`.md`](1_DOCUMENTOS_ENTREGA/MANUAL_DE_USUARIO.md) | Guía de operación paso a paso, instalación, pantallas, preguntas frecuentes y solución de problemas. |
| **Guía de Sustentación Oral** | [`.md`](1_DOCUMENTOS_ENTREGA/ESTRUCTURA_PRESENTACION_SUSTENTACION.md) | Guion cronometrado (10-12 min), checklist de recursos a mostrar y respuestas fundamentadas para posibles preguntas del docente. |
| **Instalador Autónomo de Escritorio** | [`.exe`](2_INSTALADOR_WINDOWS/Instalador_DECIDE_v2.exe) | Instalador independiente (29 MB) para cualquier computador Windows 10/11 sin necesidad de Python ni conexión a internet. |
| **Aplicación Web / Código Fuente** | Python / React | Módulos Flask (`app_web.py`), base de datos SQLite (`basedatos.py`) e interfaz React 18 (`web/index.html`). |

---

## 🎯 Competencias Evaluadas (9 Dimensiones Psicométricas)

El instrumento evalúa 16 escenarios situacionales ponderados algorítmicamente (1 a 5 puntos) y los normaliza porcentualmente en:

1. 🧠 **Autoconocimiento:** Identificación de emociones propias y sus detonantes.
2. 🧘 **Autorregulación:** Manejo de impulsos y contención de la reactividad.
3. ❤️ **Empatía:** Comprensión y validación de las emociones ajenas.
4. 🗣️ **Comunicación Asertiva:** Expresión clara y respetuosa de derechos e ideas.
5. 🤝 **Trabajo en Equipo:** Cooperación priorizando el beneficio colectivo.
6. ⚡ **Toma de Decisiones:** Análisis ponderado de consecuencias éticas y prácticas.
7. 🔥 **Tolerancia a la Frustración:** Adaptación constructiva ante el error o el retraso.
8. ⚔️ **Manejo de Conflictos:** Desescalamiento y aplicación de negociación ganar-ganar.
9. 💪 **Resiliencia:** Capacidad de aprendizaje y recuperación frente a la adversidad.

---

## 🏛️ Articulación Curricular (Clases 14ta, 15ta y 16ta)

Las 9 competencias se organizan en los dos macro-ejes temáticos del curso:
- **Eje A: Habilidades Sociales e Interacción con el Entorno:** Fundamentado en la evolución histórica de las habilidades sociales (Salter, Wolpe, Bandura, Caballo) y su estructura conductual, cognitiva y fisiológica.
- **Eje B: Resolución Pacífica de Conflictos Emocionales:** Fundamentado en el **Modelo de Negociación por Principios de Harvard (Fisher, Ury & Patton)** y la autorregulación fisiológica (Técnica STOP).

---

## 🚀 Opciones de Ejecución

### Opción 1: Con el Instalador Ejecutable (Para cualquier PC con Windows)
1. Ejecutar **`Instalador_DECIDE_v2.exe`**.
2. Presionar **"Instalar DECIDE v2.0"**.
3. Se generará el acceso directo en el Escritorio y la aplicación se abrirá en `http://localhost:5000`.

### Opción 2: Desde el Código Fuente con Python
```bash
# 1. Clonar el repositorio
git clone https://github.com/rcarreno4-dot/DECIDE.git
cd DECIDE

# 2. Instalar dependencias mínimas
pip install flask flask-cors

# 3. Iniciar el lanzador con panel de control de escritorio
python lanzador_app.py
```

---

## 📊 Sistema de Gamificación
- **Puntos de Experiencia (XP):** 100 XP por cada evaluación situacional finalizada.
- **6 Rangos Progresivos:** Novato 🥚 → Principiante 🌱 → Intermedio 🌿 → Avanzado 🌳 → Experto 🏔️ → Maestro 👑.
- **12 Logros Desbloqueables:** Reconocimientos específicos al demostrar altos niveles de empatía, asertividad, resiliencia y mediación pacífica.

---

## 🛡️ Aspectos Éticos y Seguridad de Datos
Cumpliendo con los estándares bioéticos de la **Ley 1090 de 2006** en Colombia para la evaluación psicosocial, el sistema incluye:
- Autenticación por **PIN de 4 dígitos** por usuario.
- Almacenamiento seguro en base de datos local SQLite (`decide_datos.db`).
- Módulo de **Reflexión Personal** editable y persistente para la autoevaluación cualitativa.

---

## 👨‍💻 Autor y Créditos
- **Autor:** Carlos Andrés Carreño
- **Asignatura:** Inteligencia Emocional y Habilidades Sociales
- **Fecha de Entrega:** Noviembre de 2026
- **Repositorio GitHub:** [https://github.com/rcarreno4-dot/DECIDE](https://github.com/rcarreno4-dot/DECIDE)
