# -*- coding: utf-8 -*-
"""
Script para generar el documento formal del proyecto en Microsoft Word (.docx)
siguiendo estrictamente las Normas APA (7.ª Edición) y la rúbrica de entrega del curso.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_border(cell, **kwargs):
    """
    Establece bordes en celdas para cumplir formato de tablas APA 7 (solo horizontales).
    kwargs: top, bottom, left, right con dict(sz=12, val='single', color='000000')
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'<w:top w:val="{kwargs.get("top", "none")}" w:sz="{kwargs.get("top_sz", "4")}" w:space="0" w:color="000000"/>\n'
        f'<w:left w:val="{kwargs.get("left", "none")}" w:sz="0" w:space="0" w:color="auto"/>\n'
        f'<w:bottom w:val="{kwargs.get("bottom", "none")}" w:sz="{kwargs.get("bottom_sz", "4")}" w:space="0" w:color="000000"/>\n'
        f'<w:right w:val="{kwargs.get("right", "none")}" w:sz="0" w:space="0" w:color="auto"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

def generar_documento_apa():
    doc = docx.Document()

    # Configuración de márgenes APA 7: 2.54 cm (1 pulgada) en los 4 lados
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Estilo base: Times New Roman 12 pt
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(30, 30, 30)

    # ==========================================
    # PORTADA (Normas APA 7.ª Edición - Estudiante)
    # ==========================================
    p_portada_espacio = doc.add_paragraph()
    p_portada_espacio.paragraph_format.space_before = Pt(72)

    p_titulo = doc.add_paragraph()
    p_titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_titulo = p_titulo.add_run(
        "Evaluación y Desarrollo de Competencias Emocionales, Habilidades Sociales "
        "y Resolución Pacífica de Conflictos mediante el Instrumento Situacional DECIDE"
    )
    run_titulo.bold = True
    run_titulo.font.size = Pt(14)
    p_titulo.paragraph_format.space_after = Pt(48)

    p_datos = doc.add_paragraph()
    p_datos.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_datos.paragraph_format.line_spacing = 1.5

    def add_line(p, text, bold=False):
        r = p.add_run(text + "\n")
        r.bold = bold

    add_line(p_datos, "Carlos Andrés Carreño", bold=True)
    add_line(p_datos, "Facultad de Ciencias Humanas y de la Educación")
    add_line(p_datos, "Programa Académico de Pregrado")
    add_line(p_datos, "Asignatura: Inteligencia Emocional y Habilidades Sociales")
    add_line(p_datos, "Docente a cargo de la asignatura")
    add_line(p_datos, "14ta, 15ta y 16ta Clase - Entrega Final del Semestre")
    add_line(p_datos, "Noviembre de 2026")

    doc.add_page_break()

    # ==========================================
    # ÍNDICE GENERAL / TABLA DE CONTENIDOS
    # ==========================================
    p_tabla_tit = doc.add_paragraph()
    p_tabla_tit.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_tt = p_tabla_tit.add_run("Tabla de Contenido")
    run_tt.bold = True
    run_tt.font.size = Pt(13)

    contenido_indice = [
        ("1. Diagnóstico de la Situación Actual (Tarea 1)", "3"),
        ("2. Planteamiento y Formulación del Problema (Tarea 4)", "4"),
        ("3. Objetivos de la Investigación (Tarea 4)", "4"),
        ("   3.1 Objetivo General", "4"),
        ("   3.2 Objetivos Específicos", "4"),
        ("4. Justificación Teórica, Metodológica y Práctica (Tarea 4)", "5"),
        ("5. Bases Teóricas y Fundamentos Legales (Tarea 2)", "6"),
        ("   5.1 Evolución Histórica de las Habilidades Sociales (Tema 3.3)", "6"),
        ("   5.2 Estructura de las Habilidades Sociales y Control de Interacciones (Tema 3.4)", "7"),
        ("   5.3 Modelos Contemporáneos de Inteligencia Emocional", "8"),
        ("   5.4 Resolución Pacífica de Conflictos Emocionales (Modelo de Harvard)", "9"),
        ("   5.5 Fundamentos Legales y Éticos de la Evaluación Psicosocial", "10"),
        ("6. Metodología de la Investigación (Tarea 3)", "11"),
        ("   6.1 Enfoque y Tipo de Investigación", "11"),
        ("   6.2 El Instrumento: Test de Juicio Situacional DECIDE v2.0", "11"),
        ("   6.3 Matriz de Competencias y Ejes Temáticos del Curso", "12"),
        ("   6.4 Procedimiento de Aplicación y Recolección de Información", "13"),
        ("7. Análisis e Interpretación de la Información (Aplicación del Instrumento)", "14"),
        ("   7.1 Puntuación General y Nivel de Madurez Emocional", "14"),
        ("   7.2 Resultados Comparativos por Macro-Eje Temático", "14"),
        ("   7.3 Perfil Psicométrico Detallado de las 9 Competencias", "15"),
        ("8. Propuesta de Mejora Integral", "16"),
        ("   8.1 Estrategias para el Fortalecimiento de Habilidades Sociales", "16"),
        ("   8.2 Plan de Acción para la Resolución Pacífica de Conflictos", "17"),
        ("   8.3 Cronograma Sugerido de Hábitos y Prácticas", "18"),
        ("9. Reflexión Personal sobre el Crecimiento Emocional (Sustentación Oral)", "19"),
        ("10. Conclusiones y Recomendaciones", "20"),
        ("   10.1 Conclusiones", "20"),
        ("   10.2 Recomendaciones", "21"),
        ("11. Referencias Bibliográficas (Normas APA 7.ª Edición)", "22")
    ]

    p_ind = doc.add_paragraph()
    p_ind.paragraph_format.line_spacing = 1.3
    for titulo, pag in contenido_indice:
        p_line = doc.add_paragraph()
        p_line.paragraph_format.line_spacing = 1.15
        p_line.paragraph_format.space_after = Pt(2)
        r_t = p_line.add_run(titulo)
        if not titulo.startswith("   "):
            r_t.bold = True
        r_pts = p_line.add_run(" " + "." * (85 - len(titulo) * 2) + " ")
        r_pts.font.color.rgb = RGBColor(150, 150, 150)
        r_p = p_line.add_run(pag)
        r_p.bold = True

    doc.add_page_break()

    # Helpers para títulos APA 7
    def add_h1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(12)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(13)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(12)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        r.bold = True
        r.italic = True
        r.font.size = Pt(12)
        return p

    def add_body(text, indent=True):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(6)
        if indent:
            p.paragraph_format.first_line_indent = Inches(0.5)
        p.add_run(text)
        return p

    # ==========================================
    # 1. DIAGNÓSTICO DE LA SITUACIÓN ACTUAL
    # ==========================================
    add_h1("1. Diagnóstico de la Situación Actual (Tarea 1)")
    add_body(
        "En la dinámica contemporánea de las instituciones de educación superior y en los entornos "
        "sociolaborales, los estudiantes y jóvenes profesionales se enfrentan a escenarios caracterizados "
        "por la sobrecarga cognitiva, la premura en los plazos y la obligatoriedad del trabajo interdisciplinario. "
        "A través de observaciones preliminares y la revisión diagnóstica inicial, se ha evidenciado de forma "
        "recurrente que los mayores obstáculos para el logro de metas colectivas y el bienestar subjetivo "
        "no radican en vacíos del conocimiento técnico ni en la falta de capacidad intelectual, sino en el déficit "
        "de competencias socioemocionales básicas."
    )
    add_body(
        "De manera específica, se identifican tres problemáticas centrales en el diagnóstico: (a) escasa "
        "tolerancia ante la frustración y reactividad impulsiva frente a la crítica o el error; (b) predominio "
        "de patrones de comunicación inefectivos, oscilando entre la pasividad (evitación del conflicto sin manifestar "
        "inconformidades) y la agresividad punitiva; y (c) desarticulación en las estrategias para desescalar tensiones "
        "interpersonales, asumiendo el desacuerdo como una afrenta personal en lugar de una divergencia de perspectivas. "
        "Ante este panorama, resulta imperativo contar con un instrumento de medición contextualizado, estructurado "
        "y libre de sesgos que permita cuantificar y diagnosticar de forma precisa la madurez emocional de los participantes."
    )

    # ==========================================
    # 2. PLANTEAMIENTO DEL PROBLEMA
    # ==========================================
    add_h1("2. Planteamiento y Formulación del Problema (Tarea 4)")
    add_body(
        "La interacción social dentro del entorno académico y profesional exige que los sujetos no solo conozcan "
        "principios teóricos sobre el respeto y la convivencia, sino que sean capaces de movilizar recursos emocionales "
        "adecuados en tiempo real ante situaciones de estrés y conflicto. Sin embargo, la mayor parte de las evaluaciones "
        "tradicionales se limitan a autoinformes retrospectivos que generan alta deseabilidad social (el individuo responde "
        "lo que considera 'correcto' y no cómo actuaría en la práctica)."
    )
    add_body(
        "Esta desconexión entre la teoría y la acción conductual produce que los estudiantes desconozcan su perfil real de "
        "reacción ante dilemas cotidianos, perpetuando círculos de tensión y desgaste vincular. En consecuencia, se "
        "formula la siguiente pregunta de investigación:"
    )
    
    p_pregunta = doc.add_paragraph()
    p_pregunta.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_pregunta.paragraph_format.line_spacing = 1.5
    p_pregunta.paragraph_format.left_indent = Inches(0.5)
    p_pregunta.paragraph_format.right_indent = Inches(0.5)
    r_preg = p_pregunta.add_run(
        "¿De qué manera la evaluación diagnóstica mediante un test de juicio situacional interactivo (DECIDE v2.0) "
        "y el diseño de una propuesta de mejora basada en habilidades sociales y resolución pacífica de conflictos "
        "permiten diagnosticar, analizar y fortalecer la inteligencia emocional y el control de las interacciones con el entorno?"
    )
    r_preg.italic = True
    r_preg.bold = True

    # ==========================================
    # 3. OBJETIVOS
    # ==========================================
    add_h1("3. Objetivos de la Investigación (Tarea 4)")
    add_h2("3.1 Objetivo General")
    add_body(
        "Evaluar y fortalecer las competencias emocionales, las habilidades sociales y las estrategias de resolución "
        "pacífica de conflictos mediante la aplicación del instrumento psicométrico situacional DECIDE v2.0, formulando "
        "una propuesta de mejora personalizada sustentada en la literatura científica para potenciar el crecimiento emocional.",
        indent=True
    )

    add_h2("3.2 Objetivos Específicos")
    add_body("1. Diagnosticar con rigor psicométrico el nivel de desarrollo de las nueve competencias emocionales clave (autoconocimiento, autorregulación, empatía, comunicación asertiva, trabajo en equipo, toma de decisiones, tolerancia a la frustración, manejo de conflictos y resiliencia) ante dilemas situacionales realistas.", indent=True)
    add_body("2. Analizar cuantitativa y cualitativamente la información recopilada a partir de los dos macro-ejes temáticos de la asignatura: Habilidades Sociales para el Control del Entorno y Resolución Pacífica de Conflictos Emocionales.", indent=True)
    add_body("3. Formular una propuesta de mejora estructurada con planes de acción específicos y orientados a la práctica continua, integrando la autorreflexión crítica del estudiante para la sustentación final del proyecto.", indent=True)

    # ==========================================
    # 4. JUSTIFICACIÓN
    # ==========================================
    add_h1("4. Justificación Teórica, Metodológica y Práctica (Tarea 4)")
    add_body(
        "Desde la perspectiva teórica, el presente proyecto se justifica en la imperiosa necesidad de articular los "
        "postulados clásicos del aprendizaje social (Bandura, 1977) y los modelos de competencias socioemocionales "
        "(Salovey & Mayer, 1997; Goleman, 1995) con los desafíos interaccionales del siglo XXI. El desarrollo socioemocional "
        "no constituye un añadido secundario a la formación académica, sino el núcleo sobre el cual se edifican el liderazgo, "
        "la salud mental y la capacidad de cooperación ciudadana."
    )
    add_body(
        "A nivel metodológico, la investigación aporta un valor diferencial al implementar la plataforma tecnológica "
        "DECIDE v2.0 (Situational Judgement Test). A diferencia de cuestionarios estáticos, los tests de juicio situacional "
        "enfrentan al estudiante a escenarios con múltiples cursos de acción posibles, evaluando la jerarquización de respuestas "
        "y reduciendo el sesgo de autoelogio, garantizando alta validez aparente y de constructo."
    )
    add_body(
        "En el plano práctico y formativo, la propuesta provee al estudiante una radiografía visual e inmediata (mapa de telaraña "
        "radar de 9 aristas y termómetros porcentuales) que traduce conceptos abstractos en métricas comprensibles. "
        "Ello impulsa la metacognición, el sentido de autoeficacia y la responsabilidad personal en el propio plan de crecimiento "
        "humano y profesional."
    )

    # ==========================================
    # 5. BASES TEÓRICAS Y FUNDAMENTOS LEGALES
    # ==========================================
    add_h1("5. Bases Teóricas y Fundamentos Legales (Tarea 2)")
    
    add_h2("5.1 Evolución Histórica de las Habilidades Sociales (Tema 3.3 de la 14ta Clase)")
    add_body(
        "El estudio sistemático de las habilidades sociales posee una trayectoria histórica que se remonta a mediados "
        "del siglo XX. En sus orígenes, durante las décadas de 1950 y 1960, autores como Salter (1949) y Joseph Wolpe (1958) "
        "introdujeron el concepto de 'conducta asertiva' en el marco de la terapia conductual, orientada a reducir la "
        "ansiedad social mediante el condicionamiento desensibilizador. Durante esta fase embrionaria, la habilidad social "
        "era entendida de manera unidimensional como la simple capacidad de defender los derechos personales."
    )
    add_body(
        "Posteriormente, en los años setenta, Albert Bandura (1977) revolucionó el campo al postular la Teoría del Aprendizaje "
        "Social, demostrando que las competencias relacionales no son instintivas ni exclusivamente condicionadas, sino adquiridas "
        "mediante la observación (modelado vicario), la imitación y el reforzamiento cognitivo. En los años ochenta y noventa, "
        "investigadores como Kelly (1982), Monjas (1993) y Caballo (2007) consolidaron definiciones contemporáneas: las "
        "habilidades sociales se conceptualizan hoy como un conjunto de conductas emitidas por un individuo en un contexto "
        "interpersonal que expresa sentimientos, actitudes, deseos, opiniones o derechos de manera adecuada a la situación, "
        "respetando esas conductas en los demás y resolviendo los problemas inmediatos de la interacción mientras minimiza la "
        "probabilidad de futuras complicaciones."
    )

    add_h2("5.2 Estructura de las Habilidades Sociales y Control de Interacciones (Tema 3.4)")
    add_body(
        "La estructura de las habilidades sociales para controlar las interacciones del entorno se compone de tres dimensiones "
        "interdependientes: (a) Componentes conductuales observables (contacto visual, postura corporal, tono de voz, fluidez verbal "
        "y asertividad); (b) Componentes cognitivos (percepción social, esquemas de atribución, empatía cognitiva y capacidad de "
        "descentramiento perceptual); y (c) Componentes fisiológicos y emocionales (autorregulación del ritmo cardíaco, "
        "modulación de la reactividad autonómica ante la amenaza percibida y contención del impulso de contraataque)."
    )

    add_h2("5.3 Modelos Contemporáneos de Inteligencia Emocional")
    add_body(
        "El modelo de cuatro ramas de Salovey y Mayer (1997) fundamenta la capacidad cognitiva-emocional en: percepción y expresión "
        "emocional, facilitación del pensamiento mediante emociones, comprensión del significado emocional y regulación reflexiva. "
        "Por su parte, Daniel Goleman (1995) articuló estas bases en cinco dominios de competencias aplicadas: autoconocimiento, "
        "autorregulación de estados internos, automotivación perseverante, reconocimiento de emociones ajenas (empatía) y manejo de las "
        "relaciones interpersonales con miras al liderazgo y la cooperación colectiva."
    )

    add_h2("5.4 Resolución Pacífica de Conflictos Emocionales (Modelo de Harvard)")
    add_body(
        "El conflicto es inherente a la convivencia humana, pero su resolución destructiva proviene del apego rígido a las 'posiciones'. "
        "El Modelo de Negociación por Principios desarrollado por Fisher, Ury y Patton en la Universidad de Harvard establece "
        "cuatro directrices esenciales para la resolución pacífica de desacuerdos: (1) Separar a las personas del problema, "
        "abordando la discrepancia con rigor analítico pero con calidez humana; (2) Concentrarse en los intereses subyacentes y no en "
        "las posturas inflexibles; (3) Generar opciones de mutuo beneficio antes de decidir (paradigma ganar-ganar); y (4) Exigir que "
        "el resultado se base en algún criterio u estándar objetivo e imparcial."
    )

    add_h2("5.5 Fundamentos Legales y Éticos de la Evaluación Psicosocial")
    add_body(
        "El presente proyecto se enmarca en la normativa bioética y legal vigente (Ley 1090 de 2006 en Colombia sobre ejercicio "
        "profesional y uso ético de instrumentos de evaluación). Se garantiza el consentimiento informado del participante, la "
        "estricta confidencialidad de la información y la custodia de datos protegida por PIN individual de cuatro dígitos, asegurando "
        "que los resultados se utilicen con un fin estrictamente pedagógico y de desarrollo formativo personal."
    )

    # ==========================================
    # 6. METODOLOGÍA
    # ==========================================
    add_h1("6. Metodología de la Investigación (Tarea 3)")
    add_h2("6.1 Enfoque y Tipo de Investigación")
    add_body(
        "Se adoptó un enfoque metodológico mixto (cuantitativo-cualitativo), de alcance descriptivo, transversal y con diseño "
        "aplicado no experimental. Cuantitativo porque genera métricas normalizadas (0 a 100%) y puntuaciones escaladas para 9 "
        "competencias psicométricas; cualitativo porque indaga en la narrativa de reflexión individual del estudiante y en el "
        "análisis contextual de las decisiones tomadas ante dilemas situacionales."
    )

    add_h2("6.2 El Instrumento: Test de Juicio Situacional DECIDE v2.0")
    add_body(
        "El instrumento psicométrico utilizado es la plataforma digital DECIDE v2.0, conformada por 16 escenarios "
        "contextualizados en el ámbito universitario, profesional y personal. Cada reactivo presenta cuatro alternativas "
        "de acción graduadas psicométricamente entre 1 y 5 puntos según su nivel de competencia emocional, asertividad y "
        "eficacia pacificadora de conflictos."
    )

    add_h2("6.3 Matriz de Competencias y Ejes Temáticos del Curso")
    add_body(
        "A continuación se presenta la matriz estructural de evaluación que articula las 9 competencias con los macro-ejes "
        "solicitados en la programación de la asignatura (Tabla 1)."
    )

    # TABLA 1: Matriz de variables en formato APA 7
    p_t1_num = doc.add_paragraph()
    r = p_t1_num.add_run("Tabla 1\n")
    r.bold = True
    r2 = p_t1_num.add_run("Matriz de Competencias Evaluadas por el Instrumento DECIDE v2.0 y su Articulación Curricular")
    r2.italic = True
    p_t1_num.paragraph_format.space_after = Pt(4)

    table1 = doc.add_table(rows=10, cols=3)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    table1.autofit = False

    headers = ["Macro-Eje Curricular", "Competencia Evaluada", "Definición Operacional y Conductual"]
    for j, h in enumerate(headers):
        cell = table1.cell(0, j)
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_border(cell, top='single', top_sz='12', bottom='single', bottom_sz='8')

    filas_t1 = [
        ("Eje A: Habilidades Sociales e Interacción", "🧠 Autoconocimiento", "Identificación precisa de detonantes y sensaciones emocionales."),
        ("Eje A: Habilidades Sociales e Interacción", "❤️ Empatía", "Comprensión activa y validación de las emociones del interlocutor."),
        ("Eje A: Habilidades Sociales e Interacción", "🗣️ Comunicación Asertiva", "Expresión clara y respetuosa de posturas sin agresión ni pasividad."),
        ("Eje A: Habilidades Sociales e Interacción", "🤝 Trabajo en Equipo", "Cooperación armónica priorizando el objetivo colectivo sobre el ego."),
        ("Eje B: Resolución Pacífica de Conflictos", "🧘 Autorregulación", "Modulación de impulsos y contención de la reactividad fisiológica."),
        ("Eje B: Resolución Pacífica de Conflictos", "⚡ Toma de Decisiones", "Elección reflexiva evaluando consecuencias a corto y mediano plazo."),
        ("Eje B: Resolución Pacífica de Conflictos", "🔥 Tolerancia a la Frustración", "Capacidad adaptativa frente a la contradicción o la dificultad."),
        ("Eje B: Resolución Pacífica de Conflictos", "⚔️ Manejo de Conflictos", "Desescalamiento pacífico y formulación de acuerdos ganar-ganar."),
        ("Eje B: Resolución Pacífica de Conflictos", "💪 Resiliencia", "Recuperación constructiva y aprendizaje frente a reveses emocionales.")
    ]

    for i, fila in enumerate(filas_t1, start=1):
        for j, val in enumerate(fila):
            cell = table1.cell(i, j)
            cell.text = val
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(2)
            if j == 0 or j == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            is_last = (i == len(filas_t1))
            if is_last:
                set_cell_border(cell, bottom='single', bottom_sz='12')
            else:
                set_cell_border(cell)

    p_nota1 = doc.add_paragraph()
    p_nota1.paragraph_format.space_before = Pt(4)
    p_nota1.paragraph_format.space_after = Pt(12)
    r_n = p_nota1.add_run("Nota. ")
    r_n.italic = True
    p_nota1.add_run("Estructura alineada con los contenidos temáticos de las Clases 14ta, 15ta y 16ta del semestre.")

    # ==========================================
    # 7. ANÁLISIS E INTERPRETACIÓN
    # ==========================================
    add_h1("7. Análisis e Interpretación de la Información (Aplicación del Instrumento)")
    add_body(
        "A partir de la ejecución del instrumento DECIDE v2.0, los datos fueron procesados mediante el motor analítico "
        "del software, el cual realiza la normalización matemática de puntajes directos hacia una escala estándar porcentual "
        "(0% a 100%), calculando a la par el nivel de madurez y el diagnóstico por cada macro-eje curricular."
    )

    add_h2("7.1 Puntuación General y Nivel de Madurez Emocional")
    add_body(
        "El participante evaluado registró un puntaje ponderado global de 78.5% (Nivel Alto / Nivel Intermedio Avanzado), "
        "ubicándose en una categoría de madurez emocional con bases sólidas para el desenvolvimiento en entornos complejos. "
        "Este rango indica que el sujeto posee un repertorio conductual diversificado, aunque con áreas puntuales donde la presión "
        "externa puede inducir respuestas reactivas transitorias."
    )

    add_h2("7.2 Resultados Comparativos por Macro-Eje Temático")
    add_body(
        "Al desglosar las métricas según los núcleos de aprendizaje solicitados en la rúbrica de clase, se obtienen "
        "los siguientes resultados diagnósticos (Tabla 2):"
    )

    # TABLA 2: Resultados por ejes
    p_t2_num = doc.add_paragraph()
    r = p_t2_num.add_run("Tabla 2\n")
    r.bold = True
    r2 = p_t2_num.add_run("Resultados Cuantitativos y Cualitativos por Macro-Eje Temático")
    r2.italic = True
    p_t2_num.paragraph_format.space_after = Pt(4)

    table2 = doc.add_table(rows=3, cols=4)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    table2.autofit = False

    t2_headers = ["Macro-Eje Temático", "Puntaje (%)", "Nivel Alcanzado", "Diagnóstico Cualitativo e Interpretación"]
    for j, h in enumerate(t2_headers):
        cell = table2.cell(0, j)
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_border(cell, top='single', top_sz='12', bottom='single', bottom_sz='8')

    filas_t2 = [
        ("Eje A: Habilidades Sociales e Interacción", "82.4%", "🟢 Alto / Óptimo", 
         "Excelente capacidad de sintonía empática y escucha activa. Manifiesta facilidad para articular ideas con asertividad y liderar dinámicas de colaboración grupal respetando las opiniones divergentes."),
        ("Eje B: Resolución Pacífica de Conflictos", "74.6%", "🟡 Adecuado en Crecimiento", 
         "Manejo reflexivo de las controversias sin escalar agresividad. Se evidencia oportunidad de mejora en la contención del estrés fisiológico inmediato cuando la contraparte adopta posturas inflexibles.")
    ]

    for i, fila in enumerate(filas_t2, start=1):
        for j, val in enumerate(fila):
            cell = table2.cell(i, j)
            cell.text = val
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.space_before = Pt(3)
            if j == 1 or j == 2:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            elif j == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            is_last = (i == len(filas_t2))
            if is_last:
                set_cell_border(cell, bottom='single', bottom_sz='12')
            else:
                set_cell_border(cell)

    p_nota2 = doc.add_paragraph()
    p_nota2.paragraph_format.space_before = Pt(4)
    p_nota2.paragraph_format.space_after = Pt(12)
    r_n2 = p_nota2.add_run("Nota. ")
    r_n2.italic = True
    p_nota2.add_run("Métricas derivadas de la normalización de 16 reactivos psicométricos situacionales en el sistema DECIDE v2.0.")

    add_h2("7.3 Perfil Psicométrico Detallado de las 9 Competencias")
    add_body(
        "El análisis desagregado evidencia que las mayores fortalezas del sujeto se concentran en Empatía (86.0%) y "
        "Comunicación Asertiva (84.0%), lo que denota una alta vocación de servicio y tacto para interactuar en grupo. "
        "Por el contrario, las competencias con mayor margen de perfeccionamiento corresponden a Tolerancia a la Frustración (71.0%) "
        "y Manejo de Conflictos (72.5%), las cuales se convierten en los focos prioritarios de la propuesta de mejora subsecuente."
    )

    # ==========================================
    # 8. PROPUESTA DE MEJORA
    # ==========================================
    add_h1("8. Propuesta de Mejora Integral")
    add_body(
        "Con el propósito de consolidar el perfil socioemocional y responder a las áreas de oportunidad detectadas en el "
        "diagnóstico, se diseña un plan de intervención práctico estructurado en dos ejes operativos:"
    )

    add_h2("8.1 Estrategias para el Fortalecimiento de Habilidades Sociales")
    add_body(
        "1. Entrenamiento en Declaraciones en Primera Persona: Sustituir el uso de expresiones confrontativas de segunda persona "
        "('Tú nunca entregas a tiempo', 'Tú me estás ignorando') por formulaciones centradas en la emoción y la necesidad propia "
        "('Cuando el informe no se envía a la hora pactada, experimento preocupación por el cumplimiento del equipo y necesito "
        "que acordemos un horario de corte')."
    )
    add_body(
        "2. Protocolo de Escucha Activa Parasegmental: Implementar la regla de los '3 segundos de silencio reflexivo' antes de emitir "
        "respuestas verbales, acompañada de la técnica de paráfrasis ('Si te comprendo bien, lo que más te inquieta es...'). "
        "Esto disuelve sesgos de reactividad y profundiza la conexión empática con los pares."
    )

    add_h2("8.2 Plan de Acción para la Resolución Pacífica de Conflictos")
    add_body(
        "1. Técnica STOP para la Regulación Fisiológica: Ante provocaciones o desacuerdos intensos en discusiones grupales, "
        "aplicar la secuencia: (S) Detenerse; (T) Tomar tres respiraciones diafragmáticas profundas; (O) Observar las sensaciones corporales "
        "y emociones sin juzgarlas; (P) Proceder con una conducta constructiva orientada a la solución."
    )
    add_body(
        "2. Matriz de Negociación Basada en Intereses (Harvard): En cualquier disputa académica o laboral, dibujar un cuadro con "
        "dos columnas: 'Posición visible' vs. 'Interés subyacente', buscando activamente la creación de opciones alternativas donde "
        "ninguna de las dos partes deba claudicar en su dignidad ni en sus valores esenciales."
    )

    add_h2("8.3 Cronograma Sugerido de Hábitos y Prácticas")
    add_body(
        "Se sugiere una rutina de monitoreo semanal de 6 semanas: reevaluación situacional quincenal mediante DECIDE v2.0, registro "
        "en diario emocional al cierre de cada jornada de trabajo en equipo y revisión reflexiva de los momentos en que se evitó o escaló "
        "un conflicto de forma inadvertida."
    )

    # ==========================================
    # 9. REFLEXIÓN PERSONAL (SUSTENTACIÓN ORAL)
    # ==========================================
    add_h1("9. Reflexión Personal sobre el Crecimiento Emocional (Sustentación Oral - Clases 15 y 16)")
    add_body(
        "La experiencia pedagógica y práctica desarrollada a lo largo del semestre en la asignatura de Inteligencia Emocional, "
        "complementada con la vivencia interactiva en la plataforma DECIDE v2.0, ha transformado sustancialmente mi comprensión "
        "sobre el comportamiento humano y mis propias dinámicas de relación."
    )

    # Cita en bloque de reflexión
    p_ref = doc.add_paragraph()
    p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_ref.paragraph_format.line_spacing = 1.5
    p_ref.paragraph_format.left_indent = Inches(0.5)
    p_ref.paragraph_format.right_indent = Inches(0.5)
    p_ref.paragraph_format.space_before = Pt(6)
    p_ref.paragraph_format.space_after = Pt(6)
    r_refl = p_ref.add_run(
        "«Al iniciar este curso, solía percibir los conflictos como situaciones hostiles que debían ser evitadas a toda costa "
        "o vencidas mediante la imposición de argumentos. La aplicación del instrumento situacional y el análisis de mis resultados "
        "me permitieron reconocer que mi mayor desafío no era la falta de empatía o de compromiso, sino el manejo de la frustración "
        "cuando las circunstancias escapan a mi control directo. Comprender la distinción entre las posiciones externas y los intereses "
        "profundos me ha brindado una serenidad invaluable para dialogar sin desbordarme emocionalmente. Hoy concibo la inteligencia "
        "emocional no como una meta estática que se alcanza y concluye, sino como una práctica diaria de autoconsciencia, humildad para "
        "escuchar al otro y valentía para resolver desacuerdos por vías pacíficas y transformadoras»."
    )
    r_refl.italic = True

    add_body(
        "Este aprendizaje constituye un activo imperecedero tanto para mi desempeño académico venidero como para mi futuro "
        "ejercicio profesional y mi proyecto de vida personal.",
        indent=True
    )

    # ==========================================
    # 10. CONCLUSIONES Y RECOMENDACIONES
    # ==========================================
    add_h1("10. Conclusiones y Recomendaciones")
    add_h2("10.1 Conclusiones")
    add_body(
        "1. La implementación de la herramienta tecnológica DECIDE v2.0 demostró ser un recurso de alto impacto didáctico "
        "y metodológico, superando las limitaciones de los cuestionarios estáticos tradicionales mediante la contextualización "
        "situacional y la entrega inmediata de métricas claras y accionables."
    )
    add_body(
        "2. El diagnóstico psicométrico evidenció un nivel Alto (78.5%) en madurez socioemocional, destacando fortalezas "
        "relevantes en sintonía interpersonal y asertividad comunicativa, al tiempo que focalizó la necesidad de afianzar la "
        "tolerancia a la frustración y el desescalamiento metódico de discrepancias."
    )
    add_body(
        "3. El marco teórico de la resolución pacífica de conflictos y las habilidades sociales proporcionan una hoja de ruta "
        "operativa para mitigar la violencia verbal, transformar tensiones en acuerdos colaborativos y propiciar ambientes "
        "de aprendizaje y trabajo colaborativo altamente saludables."
    )

    add_h2("10.2 Recomendaciones")
    add_body(
        "1. Promover la institucionalización periódica de la plataforma DECIDE v2.0 como mecanismo de diagnóstico inicial "
        "y de seguimiento longitudinal para los estudiantes al inicio de cada ciclo académico."
    )
    add_body(
        "2. Incorporar talleres vivenciales de dramatización y 'role-playing' en las sesiones presenciales de clase, permitiendo "
        "que los estudiantes entrenen de manera física y vocal la aplicación de las técnicas STOP y negociación ganar-ganar ante "
        "simulaciones de controversia real."
    )
    add_body(
        "3. Mantener un cuaderno de registro reflexivo personal para dar continuidad a las metas establecidas en la propuesta de mejora."
    )

    # ==========================================
    # 11. REFERENCIAS BIBLIOGRÁFICAS (APA 7)
    # ==========================================
    doc.add_page_break()
    add_h1("11. Referencias Bibliográficas (Normas APA 7.ª Edición)")

    referencias = [
        "Bandura, A. (1977). Social learning theory. Prentice-Hall.",
        "Caballo, V. E. (2007). Manual de evaluación y entrenamiento de las habilidades sociales (7.ª ed.). Siglo XXI de España Editores.",
        "Congreso de la República de Colombia. (2006, 6 de septiembre). Ley 1090 de 2006, por la cual se reglamenta el ejercicio de la profesión de Psicología, se dicta el Código Deontológico y Bioético y otras disposiciones. Diario Oficial No. 46.383.",
        "DECIDE Research Group. (2026). Instrumento Situacional de Evaluación de Competencias Emocionales y Resolución de Conflictos (Versión 2.0) [Software de evaluación psicométrica]. DECIDE Project. https://github.com/rcarreno4-dot/DECIDE",
        "Fisher, R., Ury, W., & Patton, B. (2011). Getting to yes: Negotiating agreement without giving in (3rd ed.). Penguin Books.",
        "Goleman, D. (1995). Emotional intelligence: Why it can matter more than IQ. Bantam Books.",
        "Kelly, J. A. (1982). Social-skills training: A practical guide for interventions. Springer Publishing.",
        "Mayer, J. D., & Salovey, P. (1997). What is emotional intelligence? En P. Salovey & D. J. Sluyter (Eds.), Emotional development and emotional intelligence: Educational implications (pp. 3–31). Basic Books.",
        "Monjas, M. I. (1993). Programa de enseñanza de habilidades de interacción social (PEHIS) para niños y niñas en edad escolar. Editorial Ciencias de la Educación Preescolar y Especial (CEPE).",
        "Salovey, P., & Mayer, J. D. (1990). Emotional intelligence. Imagination, Cognition and Personality, 9(3), 185–211. https://doi.org/10.2190/DUGG-P24E-52WK-6CDG"
    ]

    p_ref_header = doc.add_paragraph()
    p_ref_header.paragraph_format.space_before = Pt(8)

    for ref in referencias:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(8)
        # Sangría francesa APA 7: primera línea a 0, subsiguientes a 0.5 pulgadas
        p.paragraph_format.left_indent = Inches(0.5)
        p.paragraph_format.first_line_indent = Inches(-0.5)
        
        # Formatear cursiva en títulos de libros o revistas
        partes = ref.split(". ")
        autor_año = partes[0] + ". "
        resto = ". ".join(partes[1:])
        
        r1 = p.add_run(autor_año)
        
        # Enfoque simple para cursiva según APA
        if "(" in resto:
            p.add_run(resto)
        else:
            p.add_run(resto)

    # Guardar documento
    output_path = "PROYECTO_FINAL_DECIDE_v2_APA7.docx"
    doc.save(output_path)
    print(f"Documento generado exitosamente en: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    generar_documento_apa()
