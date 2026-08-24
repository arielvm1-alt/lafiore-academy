# -*- coding: utf-8 -*-
"""
Captions de Instagram para cada set.

Estructura de cada uno:
  1. Observacion potente (el gancho).
  2. Que trae el carrusel.
  3. Instruccion de guardar.
  4. Ubicacion + handle + 5 hashtags del rubro chileno.
"""

CIERRE = "📍 Talagante · @La_Fiore_Academy"

HASHTAGS = {
    "barberos": "#barberoschile #barberiachile #cortemasculino #talagante #formacioncontinua",
    "estilistas": "#estilistaschile #coloristachile #peluqueriachile #talagante #formacioncontinua",
    "manicuristas": "#manicuristaschile #unaschile #manicurechile #talagante #formacioncontinua",
    "todos": "#barberoschile #manicuristaschile #estilistaschile #talagante #formacioncontinua",
    "duenos": "#salondebellezachile #barberiachile #emprendimientochile #talagante #formacioncontinua",
}

CUERPOS = {
    1: (
        "El corte no parte cuando tomas la tijera. Parte cuando te sientas a escuchar.\n"
        "Cuatro claves de diagnóstico que separan a quien ejecuta de quien cobra por criterio: "
        "las preguntas correctas, cuándo proponer en vez de obedecer y cómo cerrar nombrando tu técnica.\n"
        "Guárdalo y aplica una esta semana.",
        "barberos",
    ),
    2: (
        "El color que cobras barato suele ser justo el que mejor sabes hacer.\n"
        "Cuatro claves para dejar de cobrar por reloj y empezar a cobrar diagnóstico, técnica y resultado: "
        "cómo narrar el proceso, cómo registrar tu trabajo y cómo dejar la mantención agendada.\n"
        "Guárdalo para tu próxima clienta de color.",
        "estilistas",
    ),
    3: (
        "Agenda llena no siempre es buen negocio.\n"
        "Cuatro claves para que cada hora valga más: saber cuánto deja cada servicio, potenciar tus tres fuertes, "
        "armar combos con sentido y subir el estándar antes que el precio.\n"
        "Guárdalo y calcula hoy cuánto te deja tu servicio estrella.",
        "manicuristas",
    ),
    4: (
        "Tu próximo cliente ya te evaluó. Lo hizo mirando tu feed.\n"
        "Cuatro claves para un portafolio que vende solo: misma luz y mismo fondo, el antes y después completo, "
        "pedir permiso siempre y publicar pensando en el cliente, no en los colegas.\n"
        "Guárdalo y elige hoy tu rincón de fotos.",
        "todos",
    ),
    5: (
        "El cliente nuevo decide en la primera visita si habrá una segunda.\n"
        "Cuatro claves para convertirlo en cliente fijo: recordar su nombre, guiarlo con dos opciones claras, "
        "sumar un detalle que no cobras y dejar la próxima cita puesta antes de que pague.\n"
        "Guárdalo y aplícalo con el próximo que llegue.",
        "barberos",
    ),
    6: (
        "La mantención no es un extra. Es tu sueldo fijo.\n"
        "Cuatro claves para que la clienta vuelva con fecha: tratar el retiro como servicio, dar semanas exactas, "
        "recordar con cariño y premiar a la que llega puntual.\n"
        "Guárdalo y define hoy tus plazos por servicio.",
        "manicuristas",
    ),
    7: (
        "Una queja bien atendida fideliza más que un servicio perfecto.\n"
        "Cuatro claves para convertir un reclamo en una clienta de años: escuchar sin defenderte, reparar con buena cara, "
        "anotar la causa real y cerrar el círculo a los días.\n"
        "Guárdalo para el día que llegue un reclamo. Va a llegar.",
        "todos",
    ),
    8: (
        "Recomendar no es vender. Es parte del servicio.\n"
        "Cuatro claves para que el producto se venda solo: indicarlo durante el trabajo y no en la caja, conectarlo con "
        "el problema que te contaron, decirlo una sola vez y ofrecer únicamente lo que tú usarías.\n"
        "Guárdalo y parte por un solo producto.",
        "todos",
    ),
    9: (
        "Tu salón atiende como tú le enseñaste. Nunca mejor que eso.\n"
        "Cuatro claves para que tu equipo sostenga tu estándar: escribirlo en una página, modelarlo tú primero, "
        "corregir en privado y celebrar a quien lo cumple.\n"
        "Guárdalo y escribe tu protocolo esta semana.",
        "duenos",
    ),
    10: (
        "El precio no se justifica. Se comunica.\n"
        "Cuatro claves para hablar de plata con seguridad: lista clara y pareja para todos, el valor antes que la cifra, "
        "el alza anunciada con fecha y motivo, y el precio sostenido sin rebajas de última hora.\n"
        "Guárdalo y revisa hoy cómo está escrita tu lista.",
        "todos",
    ),
}


def caption(set_id):
    cuerpo, publico = CUERPOS[set_id]
    return "%s\n\n%s\n%s" % (cuerpo, CIERRE, HASHTAGS[publico])


def captions():
    """Dict listo para serializar a captions.json."""
    return {"set_%02d" % i: caption(i) for i in sorted(CUERPOS)}


if __name__ == "__main__":
    for k, v in captions().items():
        print("=== %s ===\n%s\n" % (k, v))
