# -*- coding: utf-8 -*-
"""
Copy definitivo de los 10 sets de La Fiore Academy.

Convenciones de marcado:
  *texto*  -> resaltado (dorado en portada, verde en titulares interiores)
  **texto**-> negrita + dorado en el subtitulo de portada

Linea editorial: contenido que hace crecer al profesional.
Los "NO" describen practicas mejorables del propio profesional,
nunca defectos de clientas, clientes ni colegas.
"""

SETS = [
    # ---------------------------------------------------------------- SET 01
    {
        "id": 1,
        "vol": "04",
        "publico": "Barberos",
        "portada": {
            "titulo": "*Barbero:* el corte parte antes de tomar la tijera",
            "sub": "Tres minutos de **diagnóstico** que cambian cuánto vale tu servicio.",
        },
        "paginas": [
            {
                "ante": "EL ERROR DE PARTIR AL TIRO",
                "titulo": "SIÉNTALO Y *PREGUNTA*",
                "no": "Empezar a cortar apenas se sienta.",
                "no_icono": "tijera_prisa",
                "si": "Tres preguntas antes de encender la máquina.",
                "si_icono": "persona_preguntas",
                "frase_a": "Sin diagnóstico no hay servicio.",
                "frase_b": "Hay repetición.",
            },
            {
                "ante": "LAS PREGUNTAS DE ORO",
                "titulo": "PREGUNTA *LO CORRECTO*",
                "no": "“¿Lo mismo de siempre?”",
                "no_icono": "bocadillo_repetir",
                "si": "“¿Cómo te acomodó el corte anterior?”",
                "si_icono": "persona_escucha",
                "frase_a": "La pregunta correcta",
                "frase_b": "abre la venta correcta.",
            },
            {
                "ante": "TU CRITERIO VALE",
                "titulo": "PROPÓN, *NO OBEDEZCAS*",
                "no": "Hacer tal cual pide, aunque no le vaya.",
                "no_icono": "persona_obedece",
                "si": "Sugerir el ajuste que le quedará mejor.",
                "si_icono": "persona_propone",
                "frase_a": "El cliente pide un corte.",
                "frase_b": "Paga por criterio.",
            },
            {
                "ante": "EL CIERRE TÉCNICO",
                "titulo": "NOMBRA *LO QUE HICISTE*",
                "no": "Terminar en silencio y cobrar.",
                "no_icono": "bocadillo_mudo",
                "si": "Explicar qué hiciste y cómo mantenerlo.",
                "si_icono": "bocadillo_explica",
                "frase_a": "La técnica que se nombra",
                "frase_b": "se valora y se paga.",
            },
        ],
        "cierre": {
            "ante": "EL TICKET SUBE CON CRITERIO",
            "titulo": "COBRA POR *CRITERIO*",
            "icono": "etiqueta_sube",
            "cta": "Aplica una de estas cuatro esta semana y guárdalo para tu próxima jornada.",
        },
    },

    # ---------------------------------------------------------------- SET 02
    {
        "id": 2,
        "vol": "05",
        "publico": "Estilistas",
        "portada": {
            "titulo": "*Estilista:* el color que cobras barato es el que mejor sabes hacer",
            "sub": "Cuatro claves para cobrar lo que vale un **trabajo técnico**.",
        },
        "paginas": [
            {
                "ante": "EL VALOR NO ES EL RELOJ",
                "titulo": "COBRA *TÉCNICA*",
                "no": "Cobrar el color por hora de reloj.",
                "no_icono": "reloj",
                "si": "Cobrar diagnóstico, técnica y resultado.",
                "si_icono": "documento_checks",
                "frase_a": "El tiempo se gasta.",
                "frase_b": "El criterio se cobra.",
            },
            {
                "ante": "NARRA EL PROCESO",
                "titulo": "EXPLICA *EN SIMPLE*",
                "no": "Aplicar en silencio de principio a fin.",
                "no_icono": "persona_muda",
                "si": "Contar qué haces y por qué, en simple.",
                "si_icono": "bocadillo_simple",
                "frase_a": "Lo que la clienta entiende",
                "frase_b": "lo paga sin dudar.",
            },
            {
                "ante": "EL REGISTRO",
                "titulo": "LA FOTO *DEL RESULTADO*",
                "no": "Dejarla ir sin registro del trabajo.",
                "no_icono": "camara_tachada",
                "si": "Antes y después con buena luz.",
                "si_icono": "antes_despues",
                "frase_a": "Tu portafolio trabaja",
                "frase_b": "mientras tú descansas.",
            },
            {
                "ante": "EL RETORNO",
                "titulo": "MANTENCIÓN *PROGRAMADA*",
                "no": "“Vuelve cuando se lave el color.”",
                "no_icono": "calendario_duda",
                "si": "Agendar el retoque con fecha técnica.",
                "si_icono": "calendario_fecha",
                "frase_a": "El color dura semanas.",
                "frase_b": "La clienta, años.",
            },
        ],
        "cierre": {
            "ante": "EL COLOR ES TU MEJOR VITRINA",
            "titulo": "TU TÉCNICA *VALE*",
            "icono": "estrella_destello",
            "cta": "Guárdalo y aplícalo con tu próxima clienta de color.",
        },
    },

    # ---------------------------------------------------------------- SET 03
    {
        "id": 3,
        "vol": "06",
        "publico": "Manicuristas",
        "portada": {
            "titulo": "*Manicurista:* agenda llena no siempre es buen negocio",
            "sub": "Cuatro claves para que cada hora de trabajo **valga más**.",
        },
        "paginas": [
            {
                "ante": "EL NÚMERO QUE IMPORTA",
                "titulo": "CONOCE *TU HORA*",
                "no": "Medir el éxito por días ocupados.",
                "no_icono": "calendario_lleno",
                "si": "Saber cuánto deja cada servicio por hora.",
                "si_icono": "reloj_moneda",
                "frase_a": "Estar ocupada y ser rentable",
                "frase_b": "no son lo mismo.",
            },
            {
                "ante": "MENOS ES MÁS",
                "titulo": "POTENCIA *TUS FUERTES*",
                "no": "Ofrecer de todo para no perder a nadie.",
                "no_icono": "carta_larga",
                "si": "Impulsar los tres servicios que más dejan.",
                "si_icono": "grafico_barras",
                "frase_a": "Menos carta,",
                "frase_b": "más maestría.",
            },
            {
                "ante": "SUMA EN LA MISMA CITA",
                "titulo": "COMBOS *CON SENTIDO*",
                "no": "Descuentos sueltos para llenar huecos.",
                "no_icono": "etiqueta_descuento",
                "si": "Manicure + tratamiento en una misma cita.",
                "si_icono": "combo_suma",
                "frase_a": "El combo sube el ticket",
                "frase_b": "sin bajar tu valor.",
            },
            {
                "ante": "EL CAMINO LARGO",
                "titulo": "SUBE *EL ESTÁNDAR*",
                "no": "Esperar que el precio suba solo.",
                "no_icono": "reloj_espera",
                "si": "Formarte y mostrar la mejora.",
                "si_icono": "nivel_sube",
                "frase_a": "Primero el estándar.",
                "frase_b": "Después el precio.",
            },
        ],
        "cierre": {
            "ante": "TU HORA ES TU SUELDO",
            "titulo": "HAZ QUE TU HORA *VALGA*",
            "icono": "reloj_moneda",
            "cta": "Calcula cuánto deja tu servicio estrella por hora y guárdalo.",
        },
    },

    # ---------------------------------------------------------------- SET 04
    {
        "id": 4,
        "vol": "07",
        "publico": "Todos",
        "portada": {
            "titulo": "Tu próximo cliente *te elige por lo que ve*",
            "sub": "Cuatro claves para un **portafolio** que vende solo.",
        },
        "paginas": [
            {
                "ante": "LA BASE",
                "titulo": "MISMA LUZ, *MISMO FONDO*",
                "no": "Fotos con luz distinta cada vez.",
                "no_icono": "luces_dispares",
                "si": "Un rincón fijo con buena luz para todas.",
                "si_icono": "rincon_luz",
                "frase_a": "La consistencia comunica",
                "frase_b": "estándar profesional.",
            },
            {
                "ante": "EL FORMATO QUE VENDE",
                "titulo": "ANTES Y *DESPUÉS*",
                "no": "Mostrar solo el resultado final.",
                "no_icono": "foto_una",
                "si": "El cambio completo en una sola imagen.",
                "si_icono": "antes_despues",
                "frase_a": "La transformación vende.",
                "frase_b": "El resultado confirma.",
            },
            {
                "ante": "EL PERMISO",
                "titulo": "PREGUNTA *PRIMERO*",
                "no": "Publicar sin avisar.",
                "no_icono": "telefono_publica",
                "si": "Pedir permiso y etiquetar si acepta.",
                "si_icono": "bocadillo_permiso",
                "frase_a": "El permiso también",
                "frase_b": "es parte del servicio.",
            },
            {
                "ante": "EL PÚBLICO",
                "titulo": "PUBLICA PARA *CLIENTES*",
                "no": "Contenido para impresionar colegas.",
                "no_icono": "dos_personas",
                "si": "Contenido donde el cliente se imagina ahí.",
                "si_icono": "telefono_cliente",
                "frase_a": "El cliente no evalúa técnica.",
                "frase_b": "Compra el resultado.",
            },
        ],
        "cierre": {
            "ante": "TU FEED ES TU VITRINA",
            "titulo": "MUESTRA TU *ESTÁNDAR*",
            "icono": "telefono_grid",
            "cta": "Elige tu rincón de fotos hoy y guárdalo como referencia.",
        },
    },

    # ---------------------------------------------------------------- SET 05
    {
        "id": 5,
        "vol": "08",
        "publico": "Barberos",
        "portada": {
            "titulo": "*Barbero:* el cliente nuevo decide en la primera visita si habrá segunda",
            "sub": "Cuatro claves para convertirlo en **cliente fijo**.",
        },
        "paginas": [
            {
                "ante": "LA MEMORIA",
                "titulo": "APRÉNDETE *SU NOMBRE*",
                "no": "Atenderlo como número de agenda.",
                "no_icono": "documento_numeros",
                "si": "Nombre, gusto y un detalle, anotados.",
                "si_icono": "ficha_persona",
                "frase_a": "El que se siente recordado,",
                "frase_b": "vuelve.",
            },
            {
                "ante": "EL QUE LLEGA PERDIDO",
                "titulo": "GUÍA CON *DOS OPCIONES*",
                "no": "“¿Qué te hago?” a quemarropa.",
                "no_icono": "bocadillo_seco",
                "si": "Dos propuestas claras según su estilo.",
                "si_icono": "dos_opciones",
                "frase_a": "El nuevo no sabe pedir.",
                "frase_b": "Tú sabes proponer.",
            },
            {
                "ante": "EL DETALLE",
                "titulo": "EL EXTRA *QUE NO COBRAS*",
                "no": "Hacer lo justo y necesario.",
                "no_icono": "check_simple",
                "si": "Un detalle de más: cejas, toalla, consejo.",
                "si_icono": "estrella_destello",
                "frase_a": "Lo inesperado",
                "frase_b": "es lo que se comenta.",
            },
            {
                "ante": "EL PUENTE",
                "titulo": "LA SEGUNDA CITA, *HOY*",
                "no": "Esperar que vuelva por casualidad.",
                "no_icono": "calendario_vacio",
                "si": "Proponer la fecha antes de que pague.",
                "si_icono": "calendario_fecha",
                "frase_a": "El cliente fijo se construye",
                "frase_b": "en la primera visita.",
            },
        ],
        "cierre": {
            "ante": "LA PRIMERA VISITA LO DECIDE",
            "titulo": "CONVIÉRTELO EN *FIJO*",
            "icono": "persona_estrella",
            "cta": "Aplícalo con tu próximo cliente nuevo y guárdalo.",
        },
    },

    # ---------------------------------------------------------------- SET 06
    {
        "id": 6,
        "vol": "09",
        "publico": "Manicuristas",
        "portada": {
            "titulo": "*Manicurista:* la mantención es tu sueldo fijo",
            "sub": "Cuatro claves para que la clienta **vuelva con fecha**.",
        },
        "paginas": [
            {
                "ante": "EL RETIRO",
                "titulo": "EL RETIRO *ES SERVICIO*",
                "no": "Tratarlo como trámite menor.",
                "no_icono": "mano_apurada",
                "si": "Retiro cuidadoso: protege la uña y tu firma.",
                "si_icono": "mano_cuidado",
                "frase_a": "Cómo retiras",
                "frase_b": "también habla de ti.",
            },
            {
                "ante": "LA FECHA",
                "titulo": "FECHA TÉCNICA, *NO AZAR*",
                "no": "“Vuelve cuando se vea feo.”",
                "no_icono": "calendario_duda",
                "si": "Indicar las semanas exactas de mantención.",
                "si_icono": "calendario_tres_sem",
                "frase_a": "El regreso con fecha",
                "frase_b": "es agenda asegurada.",
            },
            {
                "ante": "EL RECORDATORIO",
                "titulo": "RECUERDA *CON CARIÑO*",
                "no": "Esperar que ella se acuerde sola.",
                "no_icono": "reloj_espera",
                "si": "Mensaje de cuidado al acercarse la fecha.",
                "si_icono": "telefono_mensaje",
                "frase_a": "Recordar es cuidar,",
                "frase_b": "no cobrar.",
            },
            {
                "ante": "LA CONSTANCIA",
                "titulo": "PREMIA *LA PUNTUAL*",
                "no": "Rebajas improvisadas a cualquiera.",
                "no_icono": "etiqueta_descuento",
                "si": "Beneficio claro por mantención al día.",
                "si_icono": "etiqueta_estrella",
                "frase_a": "Premia la constancia,",
                "frase_b": "no la insistencia.",
            },
        ],
        "cierre": {
            "ante": "LA RECURRENCIA SE DISEÑA",
            "titulo": "AGENDA *ASEGURADA*",
            "icono": "calendario_checks",
            "cta": "Define hoy tus semanas de mantención por servicio y guárdalo.",
        },
    },

    # ---------------------------------------------------------------- SET 07
    {
        "id": 7,
        "vol": "10",
        "publico": "Todos",
        "portada": {
            "titulo": "Una queja bien atendida *fideliza más que un servicio perfecto*",
            "sub": "Cuatro claves para convertir un reclamo en una **clienta de años**.",
        },
        "paginas": [
            {
                "ante": "LA ESCUCHA",
                "titulo": "ESCUCHA SIN *DEFENDERTE*",
                "no": "Explicar de inmediato por qué no fue culpa tuya.",
                "no_icono": "bocadillos_choque",
                "si": "Escuchar completo y agradecer el aviso.",
                "si_icono": "persona_escucha",
                "frase_a": "Quien reclama",
                "frase_b": "todavía quiere volver.",
            },
            {
                "ante": "LA REPARACIÓN",
                "titulo": "REPARA *SIN CARAS*",
                "no": "Arreglar “como un favor”.",
                "no_icono": "bocadillo_favor",
                "si": "Reparar rápido y con la mejor actitud.",
                "si_icono": "reparacion_ok",
                "frase_a": "La garantía se nota en el trato,",
                "frase_b": "no en el papel.",
            },
            {
                "ante": "EL APRENDIZAJE",
                "titulo": "ANOTA *LA CAUSA*",
                "no": "Olvidar el reclamo apenas se va.",
                "no_icono": "documento_equis",
                "si": "Registrar la causa y ajustar el proceso.",
                "si_icono": "documento_checks",
                "frase_a": "El reclamo repetido",
                "frase_b": "es un proceso sin dueño.",
            },
            {
                "ante": "EL CIERRE",
                "titulo": "CIERRA *EL CÍRCULO*",
                "no": "Quedarte sin saber si quedó conforme.",
                "no_icono": "interrogacion_circulo",
                "si": "Mensaje a los días: “¿cómo siguió todo?”.",
                "si_icono": "telefono_mensaje",
                "frase_a": "El seguimiento convierte",
                "frase_b": "el error en lealtad.",
            },
        ],
        "cierre": {
            "ante": "EL RECLAMO ES UNA OPORTUNIDAD",
            "titulo": "CONVIÉRTELO EN *LEALTAD*",
            "icono": "persona_estrella",
            "cta": "Guárdalo para el día que llegue un reclamo. Va a llegar.",
        },
    },

    # ---------------------------------------------------------------- SET 08
    {
        "id": 8,
        "vol": "11",
        "publico": "Todos",
        "portada": {
            "titulo": "*Recomendar no es vender*",
            "sub": "Cuatro claves para que el producto **se venda solo**.",
        },
        "paginas": [
            {
                "ante": "EL MOMENTO",
                "titulo": "RECETA, *NO OFREZCAS*",
                "no": "“¿Te llevas algo?” en la caja.",
                "no_icono": "bocadillo_caja",
                "si": "Indicarlo durante el servicio, aplicándolo.",
                "si_icono": "frasco_aplica",
                "frase_a": "Si lo indicas tú,",
                "frase_b": "es cuidado profesional.",
            },
            {
                "ante": "LA CONEXIÓN",
                "titulo": "CONECTA CON *SU PROBLEMA*",
                "no": "Recitar los beneficios del envase.",
                "no_icono": "frasco_texto",
                "si": "“Esto resuelve lo que me contaste.”",
                "si_icono": "frasco_conecta",
                "frase_a": "El producto correcto",
                "frase_b": "se vende solo.",
            },
            {
                "ante": "LA MEDIDA",
                "titulo": "UNA VEZ, *SIN PRESIÓN*",
                "no": "Insistir hasta conseguir el sí.",
                "no_icono": "bocadillos_insiste",
                "si": "Decirlo una vez y cambiar de tema.",
                "si_icono": "bocadillo_una_vez",
                "frase_a": "La presión vende hoy",
                "frase_b": "y pierde mañana.",
            },
            {
                "ante": "LA COHERENCIA",
                "titulo": "USA LO *QUE VENDES*",
                "no": "Recomendar lo que no conoces.",
                "no_icono": "frasco_duda",
                "si": "Ofrecer solo lo que tú usarías.",
                "si_icono": "frasco_estrella",
                "frase_a": "Tu credibilidad vale más",
                "frase_b": "que cualquier margen.",
            },
        ],
        "cierre": {
            "ante": "LA VENTA SIN VENDER",
            "titulo": "RECOMIENDA CON *CRITERIO*",
            "icono": "frasco_check",
            "cta": "Elige el producto que de verdad usarías y empieza por ahí.",
        },
    },

    # ---------------------------------------------------------------- SET 09
    {
        "id": 9,
        "vol": "12",
        "publico": "Dueños de salón",
        "portada": {
            "titulo": "Tu salón atiende *como tú le enseñaste*",
            "sub": "Cuatro claves para que tu equipo sostenga tu **estándar**.",
        },
        "paginas": [
            {
                "ante": "LA BASE",
                "titulo": "ESCRIBE *EL ESTÁNDAR*",
                "no": "Reglas que viven solo en tu cabeza.",
                "no_icono": "cabeza_reglas",
                "si": "Protocolo de una página, visible para todos.",
                "si_icono": "documento_checks",
                "frase_a": "Lo que no está escrito",
                "frase_b": "no se puede pedir.",
            },
            {
                "ante": "EL EJEMPLO",
                "titulo": "MUESTRA, *NO SUPONGAS*",
                "no": "Asumir que “ya saben atender”.",
                "no_icono": "dos_personas",
                "si": "Modelar tú primero la atención completa.",
                "si_icono": "persona_modelo",
                "frase_a": "El equipo copia lo que ve,",
                "frase_b": "no lo que oye.",
            },
            {
                "ante": "LA CORRECCIÓN",
                "titulo": "CORRIGE *EN PRIVADO*",
                "no": "Corregir delante del cliente.",
                "no_icono": "correccion_publica",
                "si": "Feedback breve, en privado y con ejemplo.",
                "si_icono": "correccion_privada",
                "frase_a": "Se corrige el proceso,",
                "frase_b": "no a la persona.",
            },
            {
                "ante": "EL REFUERZO",
                "titulo": "CELEBRA *EL ESTÁNDAR*",
                "no": "Notar únicamente los errores.",
                "no_icono": "documento_equis",
                "si": "Reconocer a quien atiende como acordaron.",
                "si_icono": "estrella_destello",
                "frase_a": "Lo que se celebra,",
                "frase_b": "se repite.",
            },
        ],
        "cierre": {
            "ante": "EL ESTÁNDAR ES DE TODOS",
            "titulo": "TU EQUIPO, TU *SELLO*",
            "icono": "equipo_sello",
            "cta": "Escribe tu protocolo de una página esta semana y guárdalo.",
        },
    },

    # ---------------------------------------------------------------- SET 10
    {
        "id": 10,
        "vol": "13",
        "publico": "Todos",
        "portada": {
            "titulo": "El precio *no se justifica. Se comunica*",
            "sub": "Cuatro claves para hablar de precio con **seguridad**.",
        },
        "paginas": [
            {
                "ante": "LA CLARIDAD",
                "titulo": "PRECIOS *A LA VISTA*",
                "no": "Responder “depende” a cuánto cuesta.",
                "no_icono": "bocadillo_depende",
                "si": "Lista clara, escrita y pareja para todos.",
                "si_icono": "lista_precios",
                "frase_a": "El precio visible",
                "frase_b": "filtra y da confianza.",
            },
            {
                "ante": "EL ORDEN",
                "titulo": "EL VALOR *PRIMERO*",
                "no": "Soltar el número en seco.",
                "no_icono": "etiqueta_sola",
                "si": "Qué incluye y cuánto dura; luego, el precio.",
                "si_icono": "valor_y_precio",
                "frase_a": "Primero el valor.",
                "frase_b": "Después la cifra.",
            },
            {
                "ante": "EL ALZA",
                "titulo": "ANUNCIA *SIN PERDÓN*",
                "no": "“Es que ha subido todo…”",
                "no_icono": "bocadillo_disculpa",
                "si": "Alza con fecha, motivo y anticipación.",
                "si_icono": "calendario_aviso",
                "frase_a": "Quien se disculpa por cobrar",
                "frase_b": "enseña a regatear.",
            },
            {
                "ante": "LA FIRMEZA",
                "titulo": "SOSTÉN *TU PRECIO*",
                "no": "Descuento apenas alguien duda.",
                "no_icono": "etiqueta_descuento",
                "si": "Beneficios con regla clara, no rebajas.",
                "si_icono": "etiqueta_estrella",
                "frase_a": "El precio firme",
                "frase_b": "construye categoría.",
            },
        ],
        "cierre": {
            "ante": "EL PRECIO ES COMUNICACIÓN",
            "titulo": "COMUNICA TU *VALOR*",
            "icono": "etiqueta_firme",
            "cta": "Revisa cómo está escrita tu lista de precios hoy. Guárdalo.",
        },
    },
]


# --------------------------------------------------------------------------
# validaciones de linea editorial
# --------------------------------------------------------------------------

PALABRAS_PROHIBIDAS = ["OFICIO"]

MAX_NO_SI = 50
MAX_FRASE = 34


def _todos_los_textos(s):
    yield s["portada"]["titulo"]
    yield s["portada"]["sub"]
    for p in s["paginas"]:
        for k in ("ante", "titulo", "no", "si", "frase_a", "frase_b"):
            yield p[k]
    yield s["cierre"]["ante"]
    yield s["cierre"]["titulo"]
    yield s["cierre"]["cta"]


def validar():
    """Revisa reglas duras de contenido. Devuelve lista de errores."""
    errores = []
    for s in SETS:
        et = "SET %02d" % s["id"]
        for t in _todos_los_textos(s):
            for mala in PALABRAS_PROHIBIDAS:
                if mala.lower() in t.lower():
                    errores.append("%s: palabra prohibida '%s' en: %s" % (et, mala, t))
        for i, p in enumerate(s["paginas"], start=2):
            for k in ("no", "si"):
                if len(p[k]) > MAX_NO_SI:
                    errores.append("%s p%d: '%s' tiene %d caracteres (max %d)"
                                   % (et, i, p[k], len(p[k]), MAX_NO_SI))
            for k in ("frase_a", "frase_b"):
                if len(p[k]) > MAX_FRASE:
                    errores.append("%s p%d: frase '%s' tiene %d caracteres (max %d)"
                                   % (et, i, p[k], len(p[k]), MAX_FRASE))
    return errores


def por_id(set_id):
    for s in SETS:
        if s["id"] == set_id:
            return s
    raise KeyError("set %s no existe" % set_id)


if __name__ == "__main__":
    errs = validar()
    if errs:
        print("\n".join(errs))
    else:
        print("Contenido OK: %d sets, %d laminas." % (len(SETS), len(SETS) * 6))
