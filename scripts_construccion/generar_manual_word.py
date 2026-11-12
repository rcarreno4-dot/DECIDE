# -*- coding: utf-8 -*-
"""
Script para generar el Manual de Usuario en Microsoft Word (.docx)
con diseño editorial profesional, tipografía limpia y tablas organizadas.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_border(cell, **kwargs):
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

def generar_manual_word():
    doc = docx.Document()

    for s in doc.sections:
        s.top_margin = Inches(1)
        s.bottom_margin = Inches(1)
        s.left_margin = Inches(1)
        s.right_margin = Inches(1)

    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Calibri'
    font.size = Pt(11)
    font.color.rgb = RGBColor(35, 40, 50)

    # PORTADA MANUAL
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(80)

    p_tit = doc.add_paragraph()
    p_tit.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t = p_tit.add_run("MANUAL DE USUARIO Y GUÍA DE OPERACIÓN\nDECIDE v2.0")
    r_t.bold = True
    r_t.font.size = Pt(22)
    r_t.font.color.rgb = RGBColor(30, 64, 175) # Azul institucional

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Plataforma Psicométrica de Evaluación de Competencias Emocionales,\nHabilidades Sociales y Resolución Pacífica de Conflictos")
    r_sub.font.size = Pt(13)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(100, 116, 139)
    p_sub.paragraph_format.space_after = Pt(72)

    p_aut = doc.add_paragraph()
    p_aut.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_aut.paragraph_format.line_spacing = 1.3
    r_a = p_aut.add_run("Autor del Proyecto: Carlos Andrés Carreño\n")
    r_a.bold = True
    p_aut.add_run("Facultad de Ciencias Humanas y de la Educación\n")
    p_aut.add_run("Asignatura: Inteligencia Emocional y Habilidades Sociales\n")
    p_aut.add_run("Versión de Software: 2.0 (Edición Web & Escritorio)\n")
    p_aut.add_run("Noviembre de 2026")

    doc.add_page_break()

    # Helpers
    def add_h1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(14)
        r.font.color.rgb = RGBColor(30, 64, 175)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(12)
        r.font.color.rgb = RGBColor(51, 65, 85)
        return p

    def add_body(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.space_after = Pt(6)
        p.add_run(text)
        return p

    def add_tip(title, text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.right_indent = Inches(0.4)
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(6)
        r_head = p.add_run(f"💡 {title}: ")
        r_head.bold = True
        r_head.font.color.rgb = RGBColor(30, 64, 175)
        r_b = p.add_run(text)
        r_b.italic = True
        return p

    # 1. INTRODUCCIÓN
    add_h1("1. Introducción y Propósito del Software")
    add_body(
        "DECIDE v2.0 es una solución tecnológica e interactiva desarrollada con el objetivo de evaluar, "
        "diagnosticar y retroalimentar de forma rigurosa las competencias socioemocionales de los estudiantes. "
        "Basado en la metodología de Tests de Juicio Situacional (Situational Judgement Tests - SJT), el sistema "
        "enfrenta al evaluado a 16 escenarios dilemáticos contextualizados en el ámbito universitario, profesional, "
        "interpersonal y situaciones bajo presión."
    )
    add_body(
        "A través de un motor psicométrico automatizado, la aplicación calcula los puntajes en 9 competencias emocionales "
        "clave y los clasifica en dos macro-ejes indispensables para la convivencia pacífica: (a) Habilidades Sociales para "
        "el Control e Interacción con el Entorno, y (b) Resolución Pacífica de Conflictos Emocionales."
    )

    # 2. REQUISITOS DEL SISTEMA
    add_h1("2. Requisitos Técnicos del Sistema")
    add_body(
        "La plataforma ha sido optimizada para operar de manera autónoma, ligera y sin necesidad de conexión activa a internet:"
    )
    add_body("• Sistema Operativo: Microsoft Windows 10 o Windows 11 (64 bits).")
    add_body("• Navegador Web Compatible: Microsoft Edge, Google Chrome, Mozilla Firefox o Brave (versión moderna).")
    add_body("• Espacio Libre en Almacenamiento: Menos de 120 MB.")
    add_body("• Memoria RAM: 2 GB como mínimo (4 GB recomendados).")
    add_tip("Independencia de Red", "DECIDE v2.0 se ejecuta en un servidor local seguro en tu propio computador, por lo cual puedes utilizarlo en aulas sin señal de internet sin ningún inconveniente.")

    # 3. INSTALACIÓN
    add_h1("3. Guía de Instalación y Puesta en Marcha")
    add_h2("3.1 Instalación en un Solo Clic")
    add_body("1. Localiza el archivo ejecutable 'Instalador_DECIDE_v2.exe' en tu carpeta o memoria USB.")
    add_body("2. Ejecuta el archivo con doble clic. Aparecerá la ventana gráfica del instalador con interfaz moderna.")
    add_body("3. Presiona el botón 'Instalar DECIDE v2.0'.")
    add_body("4. El proceso tardará menos de 10 segundos. Se creará automáticamente un acceso directo en tu Escritorio titulado 'DECIDE v2.0'.")
    add_body("5. La aplicación se iniciará de forma automática inmediatamente.")

    add_h2("3.2 Portabilidad a Otros Computadores")
    add_body(
        "Si necesitas llevar la aplicación a la universidad o al computador de un docente, solo necesitas copiar el archivo "
        "'Instalador_DECIDE_v2.exe' (pesa aproximadamente 29 MB). No se requiere instalar Python, NodeJS ni paquetes "
        "adicionales en el computador receptor."
    )

    # 4. PANEL DE CONTROL
    add_h1("4. Panel de Control de Escritorio")
    add_body(
        "Cuando DECIDE v2.0 está en funcionamiento, se despliega una consola visual de control con tema oscuro. "
        "Este panel te permite gestionar la aplicación de forma amigable mediante tres opciones fundamentales:"
    )
    add_body("• [ 🚀 Abrir DECIDE en Navegador ]: Abre o recarga la aplicación en tu navegador web predeterminado.")
    add_body("• [ 📋 Copiar Enlace ]: Copia la dirección local 'http://localhost:5000' para abrirla en otra ventana o navegador.")
    add_body("• [ 🛑 Detener y Salir ]: Apaga el servidor local de manera limpia y cierra todos los procesos en segundo plano.")

    # 5. FUNCIONALIDADES PASO A PASO
    add_h1("5. Funcionalidades y Guía de Uso Paso a Paso")

    add_h2("5.1 Inicio de Sesión y Protección por PIN")
    add_body(
        "Al iniciar DECIDE, siempre serás recibido en la pantalla de bienvenida. Debes ingresar tu nombre de usuario "
        "y un PIN de 4 dígitos numéricos (ejemplo: 1234). Este mecanismo previene confusiones entre múltiples evaluados "
        "en el mismo computador y asegura la total confidencialidad de tus datos."
    )

    add_h2("5.2 Panel Principal (Dashboard)")
    add_body(
        "El Dashboard resume el estado actual del participante: nombre, rango gamificado (desde Novato hasta Maestro), "
        "puntos de experiencia acumulados y accesos directos para iniciar un nuevo test situacional o explorar el historial."
    )

    add_h2("5.3 Realización de la Evaluación Situacional (16 Dilemas)")
    add_body(
        "En la pestaña 'Test Situacional' se presentarán secuencialmente 16 escenarios del mundo real. Cada uno cuenta "
        "con una contextualización clara y 4 opciones de conducta posibles. Puedes retroceder ('← Anterior') para revisar "
        "decisiones y avanzar ('Siguiente →') conociendo en todo momento tu porcentaje de avance en la barra superior."
    )

    add_h2("5.4 Interpretación de Resultados y Gráficos Visuales")
    add_body("Al culminar la pregunta 16 y presionar 'Finalizar Evaluación', el sistema despliega el reporte integral:")
    add_body("1. Medidor Circular (Gauge): Porcentaje global de madurez emocional con código de color.")
    add_body("2. Mapa Radar SVG (Telaraña): Representación poligonal de las 9 competencias (Autoconocimiento, Autorregulación, Empatía, Asertividad, Trabajo en Equipo, Toma de Decisiones, Frustración, Conflictos y Resiliencia).")
    add_body("3. Macro-Ejes del Curso: Calificación desglosada y diagnóstico cualitativo para Habilidades Sociales e Interacción con el Entorno, y Resolución Pacífica de Conflictos.")
    add_body("4. Recomendaciones Personalizadas: Sugerencias específicas de mejora según tus puntuaciones.")

    add_h2("5.5 Registro de la Reflexión Personal")
    add_body(
        "En la parte inferior de tus resultados, encontrarás el editor de 'Reflexión Personal'. Allí podrás redactar "
        "tus aprendizajes sobre el control emocional y tus compromisos de desarrollo. Al pulsar 'Guardar Reflexión', "
        "el texto quedará almacenado de forma permanente en la base de datos y en tu historial para la sustentación oral."
    )

    add_h2("5.6 Consulta de Historial y Logros")
    add_body(
        "La pestaña 'Historial' te permite examinar todas tus evaluaciones pasadas, comparar tus avances y revisar reflexiones "
        "anteriores. La pestaña 'Logros' muestra las 12 medallas obtenibles a medida que completas evaluaciones y alcanzas niveles altos."
    )

    add_h2("5.7 Metodología APA Integrada")
    add_body(
        "La pestaña 'Metodología APA' expone en vivo la fundamentación epistemológica, las bases teóricas de Salovey-Mayer y Goleman, "
        "la metodología de Harvard para resolución de conflictos y el marco legal, facilitando la consulta de fuentes durante las defensas académicas."
    )

    # 6. SOLUCIÓN DE PROBLEMAS
    add_h1("6. Preguntas Frecuentes y Solución de Inconvenientes")
    
    t_faq = doc.add_table(rows=5, cols=2)
    t_faq.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_faq.autofit = False

    faq_headers = ["Pregunta o Inconveniente", "Solución Recomendada"]
    for j, h in enumerate(faq_headers):
        cell = t_faq.cell(0, j)
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True
        set_cell_border(cell, top='single', top_sz='12', bottom='single', bottom_sz='8')

    faqs = [
        ("Cerré la ventana del navegador por error", "Abre el Panel de Control en tu barra de tareas y haz clic en '[ 🚀 Abrir DECIDE en Navegador ]'."),
        ("El navegador muestra 'Página no encontrada' o error de conexión", "Asegúrate de que la ventana del Panel de Control de DECIDE esté abierta antes de ingresar a localhost:5000."),
        ("Deseo cerrar el programa por completo", "Presiona el botón '[ 🛑 Detener y Salir ]' en la ventana del Panel de Control."),
        ("¿Cómo muevo mi base de datos a otro equipo?", "El archivo 'decide_datos.db' contiene tus registros y puedes copiarlo si deseas transferir tus evaluaciones a otro PC.")
    ]

    for i, (p_txt, r_txt) in enumerate(faqs, start=1):
        c0 = t_faq.cell(i, 0)
        c0.text = p_txt
        c0.paragraphs[0].runs[0].bold = True
        set_cell_border(c0)

        c1 = t_faq.cell(i, 1)
        c1.text = r_txt
        if i == len(faqs):
            set_cell_border(c1, bottom='single', bottom_sz='12')
            set_cell_border(c0, bottom='single', bottom_sz='12')
        else:
            set_cell_border(c1)

    out_file = "MANUAL_DE_USUARIO_DECIDE_v2.docx"
    doc.save(out_file)
    print(f"Manual generado con éxito en: {os.path.abspath(out_file)}")

if __name__ == "__main__":
    generar_manual_word()
