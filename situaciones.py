# situaciones.py
# Banco de situaciones para la evaluación

SITUACIONES = [
    # ========== LABORALES ==========
    {
        "id": 1,
        "titulo": "Trabajo en equipo bajo presión",
        "descripcion": "Estás trabajando en un proyecto grupal y uno de tus compañeros no cumple con su parte. La entrega es mañana.",
        "categoria": "laboral",
        "opciones": [
            {
                "texto": "Hago su trabajo y no digo nada.",
                "puntuaciones": {"autoconocimiento": 1, "autorregulacion": 2, "empatia": 3, "comunicacion": 1, "trabajo_equipo": 2, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Le escribo molesto y le digo que siempre es irresponsable.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 2, "trabajo_equipo": 1, "toma_decisiones": 2, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Hablo con él para conocer qué ocurrió y buscamos una solución.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 5, "comunicacion": 5, "trabajo_equipo": 5, "toma_decisiones": 5, "tolerancia_frustracion": 4, "manejo_conflictos": 5, "resiliencia": 4}
            },
            {
                "texto": "Redistribuyo el trabajo entre todos y damos lo mejor de nosotros.",
                "puntuaciones": {"autoconocimiento": 4, "autorregulacion": 4, "empatia": 4, "comunicacion": 4, "trabajo_equipo": 5, "toma_decisiones": 4, "tolerancia_frustracion": 4, "manejo_conflictos": 4, "resiliencia": 4}
            }
        ]
    },
    {
        "id": 2,
        "titulo": "Crítica pública del jefe",
        "descripcion": "Tu jefe te hace una crítica sobre tu trabajo frente a toda el equipo. Te sientes humillado.",
        "categoria": "laboral",
        "opciones": [
            {
                "texto": "Respondo defensivamente argumentando mis razones inmediatamente.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 2, "comunicacion": 2, "trabajo_equipo": 1, "toma_decisiones": 2, "tolerancia_frustracion": 1, "manejo_conflictos": 2, "resiliencia": 1}
            },
            {
                "texto": "Me quedo callado y rumio el incidente el resto del día.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 2, "comunicacion": 1, "trabajo_equipo": 2, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 2, "resiliencia": 2}
            },
            {
                "texto": "Tomo tiempo para calmarme y luego solicito una reunión privada con mi jefe.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 4, "comunicacion": 5, "trabajo_equipo": 4, "toma_decisiones": 5, "tolerancia_frustracion": 5, "manejo_conflictos": 5, "resiliencia": 5}
            }
        ]
    },
    {
        "id": 3,
        "titulo": "Sobrecarga de trabajo",
        "descripcion": "Tu jefe te encarga múltiples proyectos urgentes sin dar más tiempo. Sabes que es imposible hacer todo bien.",
        "categoria": "laboral",
        "opciones": [
            {
                "texto": "Digo que sí a todo y espero poder hacerlo de alguna manera.",
                "puntuaciones": {"autoconocimiento": 1, "autorregulacion": 2, "empatia": 2, "comunicacion": 1, "trabajo_equipo": 2, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Rechazo tajantemente los proyectos y me enojo.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 2, "trabajo_equipo": 1, "toma_decisiones": 2, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Hablo con mi jefe sobre las prioridades y busco una solución realista.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 4, "empatia": 3, "comunicacion": 5, "trabajo_equipo": 4, "toma_decisiones": 5, "tolerancia_frustracion": 4, "manejo_conflictos": 4, "resiliencia": 4}
            }
        ]
    },
    {
        "id": 4,
        "titulo": "Error costoso en el proyecto",
        "descripcion": "Cometiste un error que provocó pérdidas de dinero a la empresa. Todos lo saben.",
        "categoria": "laboral",
        "opciones": [
            {
                "texto": "Culpo a alguien más o busco excusas.",
                "puntuaciones": {"autoconocimiento": 1, "autorregulacion": 1, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Me siento terriblemente avergonzado y considero renunciar.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 2, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Asumo la responsabilidad, presento un plan para mitigarlo y aprendo de ello.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 4, "comunicacion": 5, "trabajo_equipo": 4, "toma_decisiones": 5, "tolerancia_frustracion": 5, "manejo_conflictos": 4, "resiliencia": 5}
            }
        ]
    },
    {
        "id": 5,
        "titulo": "Conflicto con compañero de trabajo",
        "descripcion": "Tu compañero constantemente te critica en las reuniones y cuestiona tus ideas sin respetar tu opinión.",
        "categoria": "laboral",
        "opciones": [
            {
                "texto": "Critico sus ideas de la misma manera en las próximas reuniones.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 2, "trabajo_equipo": 1, "toma_decisiones": 2, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Evito participar en las reuniones para no enfrentarme a él.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 2, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Hablo con él en privado para entender sus preocupaciones y buscar un entendimiento.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 5, "comunicacion": 5, "trabajo_equipo": 5, "toma_decisiones": 5, "tolerancia_frustracion": 4, "manejo_conflictos": 5, "resiliencia": 4}
            }
        ]
    },

    # ========== ACADÉMICOS ==========
    {
        "id": 6,
        "titulo": "Fracaso académico",
        "descripcion": "Has estudiado mucho para un examen pero sacaste una mala calificación. Te sientes decepcionado.",
        "categoria": "academico",
        "opciones": [
            {
                "texto": "Culpo al profesor y digo que fue un examen injusto.",
                "puntuaciones": {"autoconocimiento": 1, "autorregulacion": 2, "empatia": 1, "comunicacion": 2, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Me desmorono y pierdo la confianza en mis habilidades.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Analizo qué salió mal, reconozco mis debilidades y ajusto mi estrategia.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 4, "empatia": 3, "comunicacion": 3, "trabajo_equipo": 3, "toma_decisiones": 5, "tolerancia_frustracion": 5, "manejo_conflictos": 3, "resiliencia": 5}
            }
        ]
    },
    {
        "id": 7,
        "titulo": "Presentación ante la clase",
        "descripcion": "Tienes que hacer una presentación importante frente a toda la clase y te sientes muy nervioso.",
        "categoria": "academico",
        "opciones": [
            {
                "texto": "Me preparo al último minuto esperando que todo salga bien.",
                "puntuaciones": {"autoconocimiento": 1, "autorregulacion": 2, "empatia": 2, "comunicacion": 2, "trabajo_equipo": 2, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 2, "resiliencia": 2}
            },
            {
                "texto": "Pido permiso para no presentar o presentar en privado.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 2, "comunicacion": 2, "trabajo_equipo": 2, "toma_decisiones": 2, "tolerancia_frustracion": 2, "manejo_conflictos": 2, "resiliencia": 2}
            },
            {
                "texto": "Me preparo con tiempo, practico varias veces y reconozco mis nervios como naturales.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 3, "comunicacion": 5, "trabajo_equipo": 4, "toma_decisiones": 5, "tolerancia_frustracion": 5, "manejo_conflictos": 3, "resiliencia": 5}
            }
        ]
    },
    {
        "id": 8,
        "titulo": "Trabajo grupal desigual",
        "descripcion": "En un trabajo grupal, algunos compañeros no participan y tú acabas haciendo la mayoría.",
        "categoria": "academico",
        "opciones": [
            {
                "texto": "Hago todo yo solo para asegurar una buena calificación.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 2, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 2, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Me enojo con ellos pero sigo haciendo el trabajo.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 2, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Reúno al equipo, defino responsabilidades claras y hago seguimiento.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 4, "empatia": 4, "comunicacion": 5, "trabajo_equipo": 5, "toma_decisiones": 5, "tolerancia_frustracion": 4, "manejo_conflictos": 4, "resiliencia": 4}
            }
        ]
    },
    {
        "id": 9,
        "titulo": "Presión de calificaciones",
        "descripcion": "Tienes varios exámenes difíciles en pocas semanas y sientes que no puedes con todo.",
        "categoria": "academico",
        "opciones": [
            {
                "texto": "Dejo de estudiar y me desmorono.",
                "puntuaciones": {"autoconocimiento": 1, "autorregulacion": 1, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Estudio obsesivamente sin dormir lo suficiente.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 2, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Hago un plan de estudio equilibrado y pido ayuda si la necesito.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 3, "comunicacion": 5, "trabajo_equipo": 4, "toma_decisiones": 5, "tolerancia_frustracion": 5, "manejo_conflictos": 3, "resiliencia": 5}
            }
        ]
    },

    # ========== RELACIONES INTERPERSONALES ==========
    {
        "id": 10,
        "titulo": "Discusión con un amigo",
        "descripcion": "Tu mejor amigo dice algo que no está de acuerdo con tus valores y te sientes ofendido.",
        "categoria": "relaciones",
        "opciones": [
            {
                "texto": "Finjo que no pasó nada para evitar conflicto.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 2, "comunicacion": 1, "trabajo_equipo": 2, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Exploto de rabia y le digo todo lo que pienso sin filtrar.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Le expreso calmadamente por qué me molestó y escucho su perspectiva.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 5, "comunicacion": 5, "trabajo_equipo": 5, "toma_decisiones": 4, "tolerancia_frustracion": 4, "manejo_conflictos": 5, "resiliencia": 4}
            }
        ]
    },
    {
        "id": 11,
        "titulo": "Malentendido con pareja",
        "descripcion": "Tu pareja malinterpretó algo que dijiste y ahora se siente herida. Intentas explicar pero ella no te escucha.",
        "categoria": "relaciones",
        "opciones": [
            {
                "texto": "También me enojo y le digo que es su problema si no entiende.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Me callo y dejo que el silencio siga creciendo.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Le pido que me escuche, reconozco sus emociones y aclaro el malentendido.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 5, "comunicacion": 5, "trabajo_equipo": 4, "toma_decisiones": 5, "tolerancia_frustracion": 5, "manejo_conflictos": 5, "resiliencia": 5}
            }
        ]
    },
    {
        "id": 12,
        "titulo": "Diferencia de opiniones políticas",
        "descripcion": "Un amigo cercano expresa opiniones políticas muy diferentes a las tuyas. Sientes que va contra tus principios.",
        "categoria": "relaciones",
        "opciones": [
            {
                "texto": "Ataco sus ideas agresivamente y lo acuso de ser mal persona.",
                "puntuaciones": {"autoconocimiento": 1, "autorregulacion": 1, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Dejo de hablar con él para no tener que lidiar con la diferencia.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Valoro la amistad, reconozco que podemos pensar diferente y respeto su opinión.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 5, "comunicacion": 5, "trabajo_equipo": 5, "toma_decisiones": 4, "tolerancia_frustracion": 4, "manejo_conflictos": 4, "resiliencia": 4}
            }
        ]
    },
    {
        "id": 13,
        "titulo": "Sentimientos de celos",
        "descripcion": "Tu amigo sale constantemente con alguien nuevo y te sientes dejado de lado. Sientes celos y resentimiento.",
        "categoria": "relaciones",
        "opciones": [
            {
                "texto": "Le reclamo y le exijo que pase más tiempo conmigo.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 2, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Me alejo silenciosamente y espero que se dé cuenta de que me daño.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 2, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Reconozco mis celos, hablo con él sobre mis sentimientos e incluyo a su nueva pareja.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 4, "comunicacion": 5, "trabajo_equipo": 5, "toma_decisiones": 4, "tolerancia_frustracion": 4, "manejo_conflictos": 4, "resiliencia": 4}
            }
        ]
    },

    # ========== SITUACIONES BAJO PRESIÓN ==========
    {
        "id": 14,
        "titulo": "Presión múltiple",
        "descripcion": "Tienes varias responsabilidades importantes al mismo tiempo y sientes que no das abasto.",
        "categoria": "presion",
        "opciones": [
            {
                "texto": "Me abrumo y abandono todas las tareas.",
                "puntuaciones": {"autoconocimiento": 1, "autorregulacion": 1, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Hago todo rápidamente sin importar la calidad.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 2, "toma_decisiones": 2, "tolerancia_frustracion": 2, "manejo_conflictos": 2, "resiliencia": 2}
            },
            {
                "texto": "Respiro profundo, priorizo las tareas y pido ayuda si es necesario.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 3, "comunicacion": 5, "trabajo_equipo": 5, "toma_decisiones": 5, "tolerancia_frustracion": 5, "manejo_conflictos": 3, "resiliencia": 5}
            }
        ]
    },
    {
        "id": 15,
        "titulo": "Problema inesperado",
        "descripcion": "Surgió un problema urgente que no esperabas a mitad de tu día ocupado. Necesitas una solución rápida.",
        "categoria": "presion",
        "opciones": [
            {
                "texto": "Entro en pánico y no sé qué hacer.",
                "puntuaciones": {"autoconocimiento": 1, "autorregulacion": 1, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Actúo impulsivamente sin pensar en las consecuencias.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 2, "trabajo_equipo": 1, "toma_decisiones": 2, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 2}
            },
            {
                "texto": "Me tomo 5 minutos para calmarme, evalúo opciones y elijo la mejor solución.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 3, "comunicacion": 4, "trabajo_equipo": 4, "toma_decisiones": 5, "tolerancia_frustracion": 5, "manejo_conflictos": 3, "resiliencia": 5}
            }
        ]
    },
    {
        "id": 16,
        "titulo": "Crítica imprevista",
        "descripcion": "Alguien te critica públicamente en un momento en que no estabas preparado. Te sientes atrapado y emocional.",
        "categoria": "presion",
        "opciones": [
            {
                "texto": "Respondo agresivamente o con sarcasmo.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 1, "empatia": 1, "comunicacion": 2, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 1, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Me paralizo y no sé qué decir.",
                "puntuaciones": {"autoconocimiento": 2, "autorregulacion": 2, "empatia": 1, "comunicacion": 1, "trabajo_equipo": 1, "toma_decisiones": 1, "tolerancia_frustracion": 2, "manejo_conflictos": 1, "resiliencia": 1}
            },
            {
                "texto": "Respiro, reconozco mis emociones y respondo con calma y madurez.",
                "puntuaciones": {"autoconocimiento": 5, "autorregulacion": 5, "empatia": 4, "comunicacion": 5, "trabajo_equipo": 3, "toma_decisiones": 4, "tolerancia_frustracion": 5, "manejo_conflictos": 5, "resiliencia": 5}
            }
        ]
    }
]

def obtener_situaciones():
    """Retorna la lista de situaciones"""
    return SITUACIONES

def obtener_situacion(id_situacion):
    """Retorna una situación específica por ID"""
    for sit in SITUACIONES:
        if sit["id"] == id_situacion:
            return sit
    return None

def contar_situaciones():
    """Retorna el número total de situaciones"""
    return len(SITUACIONES)
