# -*- coding: utf-8 -*-
"""
Libreria de ilustraciones SVG propias para las laminas de La Fiore Academy.

Sistema:
  - Todo se dibuja dentro de un viewBox de 240 x 180.
  - Trazo 5-7px, esquinas y puntas redondeadas, sin relleno salvo pelo y textos.
  - Color base TINTA #1A1D1B, acentos VERDE #32614D.
  - Los textos cortos dentro del SVG van en Bebas Neue.

Se construye por composicion: primitivas reutilizables + iconos compuestos.
"""

import math

TINTA = "#1A1D1B"
VERDE = "#32614D"

W, H = 240, 180


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def g(body, x=0.0, y=0.0, s=1.0):
    """Envuelve markup en un grupo trasladado/escalado."""
    return '<g transform="translate(%g,%g) scale(%g)">%s</g>' % (x, y, s, body)


def texto(t, x, y, size=30, color=TINTA, anchor="middle"):
    return (
        '<text x="%g" y="%g" text-anchor="%s" font-family="Bebas Neue" font-weight="700" '
        'font-size="%g" fill="%s" stroke="none" letter-spacing="0.04em">%s</text>'
        % (x, y, anchor, size, color, t)
    )


def linea(x1, y1, x2, y2, color=TINTA, w=6):
    return '<path d="M%g,%g L%g,%g" stroke="%s" stroke-width="%g"/>' % (x1, y1, x2, y2, color, w)


def circulo(cx, cy, r, color=TINTA, w=6, fill="none"):
    return '<circle cx="%g" cy="%g" r="%g" stroke="%s" stroke-width="%g" fill="%s"/>' % (
        cx, cy, r, color, w, fill)


def rect(x, y, w_, h_, r=8, color=TINTA, w=6, fill="none"):
    return ('<rect x="%g" y="%g" width="%g" height="%g" rx="%g" stroke="%s" '
            'stroke-width="%g" fill="%s"/>' % (x, y, w_, h_, r, color, w, fill))


def path(d, color=TINTA, w=6, fill="none"):
    return '<path d="%s" stroke="%s" stroke-width="%g" fill="%s"/>' % (d, color, w, fill)


# --------------------------------------------------------------------------
# primitivas
# --------------------------------------------------------------------------

def persona(color=TINTA, pelo=TINTA, hombros=True):
    """Cabeza con pelo solido + hombros. Caja local: 0,0 -> 62,76."""
    p = []
    p.append('<path d="M9,26 C9,7 22,-2 31,-2 C40,-2 53,7 53,26 '
             'C50,20 44,14 31,14 C18,14 12,20 9,26 Z" fill="%s" stroke="none"/>' % pelo)
    p.append(circulo(31, 26, 20, color))
    if hombros:
        p.append(path("M0,76 C0,55 13,45 31,45 C49,45 62,55 62,76", color))
    return "".join(p)


def telefono(color=TINTA, pantalla=None):
    """Telefono vertical. Caja local: 0,0 -> 52,92."""
    p = [rect(0, 0, 52, 92, 10, color)]
    p.append(linea(17, 10, 35, 10, color, 5))
    if pantalla:
        p.append(pantalla)
    return "".join(p)


def bocadillo(t="", w_=104, h_=64, color=TINTA, size=30, color_texto=None, cola="izq"):
    """Bocadillo con cola. Caja local: 0,0 -> w_, h_+22."""
    p = [rect(0, 0, w_, h_, 14, color)]
    if cola == "izq":
        p.append(path("M22,%g L22,%g L52,%g" % (h_, h_ + 22, h_), color))
    else:
        p.append(path("M%g,%g L%g,%g L%g,%g" % (w_ - 22, h_, w_ - 22, h_ + 22, w_ - 52, h_), color))
    if t:
        p.append(texto(t, w_ / 2.0, h_ / 2.0 + size * 0.34, size, color_texto or color))
    return "".join(p)


def calendario(t="", color=TINTA, color_texto=None):
    """Calendario. Caja local: 0,0 -> 88,84."""
    p = [rect(0, 8, 88, 76, 10, color)]
    p.append(linea(0, 30, 88, 30, color, 6))
    p.append(linea(22, 0, 22, 16, color, 6))
    p.append(linea(66, 0, 66, 16, color, 6))
    if t:
        p.append(texto(t, 44, 66, 30, color_texto or color))
    return "".join(p)


def etiqueta_precio(t="$", color=TINTA, color_texto=None):
    """Etiqueta con perforacion. Caja local: 0,0 -> 94,92."""
    p = [path("M52,2 L90,40 C94,44 94,50 90,54 L56,88 C52,92 46,92 42,88 "
              "L4,50 L4,10 C4,6 8,2 12,2 Z", color)]
    p.append(circulo(22, 22, 7, color, 5))
    if t:
        p.append(texto(t, 56, 62, 32, color_texto or color))
    return "".join(p)


def reloj(color=TINTA):
    """Reloj. Caja local: 0,0 -> 72,72."""
    p = [circulo(36, 36, 32, color)]
    p.append(path("M36,18 L36,38 L52,46", color))
    return "".join(p)


def check_circulo(color=VERDE, r=32):
    p = [circulo(r, r, r - 3, color)]
    p.append(path("M%g,%g L%g,%g L%g,%g" % (r * 0.52, r, r * 0.88, r * 1.36, r * 1.5, r * 0.62), color))
    return "".join(p)


def equis_circulo(color=TINTA, r=32):
    p = [circulo(r, r, r - 3, color)]
    d = r * 0.42
    p.append(path("M%g,%g L%g,%g M%g,%g L%g,%g" % (r - d, r - d, r + d, r + d, r + d, r - d, r - d, r + d), color))
    return "".join(p)


def estrella_destello(color=VERDE, escala=1.0, destellos=True):
    """Estrella de 5 puntas con destellos. Caja local aprox 0,0 -> 96,92."""
    p = [path("M48,4 L60,36 L94,38 L67,59 L77,92 L48,72 L19,92 L29,59 L2,38 L36,36 Z", color)]
    if destellos:
        p.append(linea(108, 12, 122, 12, color, 5))
        p.append(linea(115, 5, 115, 19, color, 5))
        p.append(linea(-24, 62, -12, 62, color, 5))
        p.append(linea(-18, 56, -18, 68, color, 5))
    return g("".join(p), 0, 0, escala)


def documento_checks(n=3, color=TINTA, acento=VERDE, marcas=True):
    """Hoja con esquina doblada y n filas. Caja local: 0,0 -> 84,104."""
    p = [path("M0,8 C0,4 4,0 8,0 L56,0 L84,28 L84,96 C84,100 80,104 76,104 "
              "L8,104 C4,104 0,100 0,96 Z", color)]
    p.append(path("M56,0 L56,28 L84,28", color, 6))
    for i in range(n):
        y = 50 + i * 20
        if marcas:
            p.append(path("M14,%g L20,%g L30,%g" % (y, y + 6, y - 6), acento, 5))
            p.append(linea(40, y, 70, y, color, 5))
        else:
            p.append(linea(14, y, 70, y, color, 5))
    return "".join(p)


def sol(color=TINTA, r=18, rayos=8):
    """Sol / luz. Centrado en 0,0."""
    p = [circulo(0, 0, r, color)]
    for i in range(rayos):
        a = 2 * math.pi * i / rayos
        p.append(linea(math.cos(a) * (r + 9), math.sin(a) * (r + 9),
                       math.cos(a) * (r + 20), math.sin(a) * (r + 20), color, 5))
    return "".join(p)


def frasco(t="", color=TINTA, color_texto=None):
    """Frasco de producto. Caja local: 0,0 -> 62,100."""
    p = [rect(19, 0, 24, 16, 4, color, 5)]
    p.append(path("M4,30 C4,22 12,16 20,16 L42,16 C50,16 58,22 58,30 L58,92 "
                  "C58,96 54,100 50,100 L12,100 C8,100 4,96 4,92 Z", color))
    p.append(linea(4, 44, 58, 44, color, 5))
    if t:
        p.append(texto(t, 31, 78, 26, color_texto or color))
    return "".join(p)


def mano_unas(color=TINTA, acento=VERDE):
    """Mano estilizada con unas pintadas. Caja local: 0,0 -> 104,96."""
    p = [path("M12,96 L12,52 C12,44 20,38 28,38", color)]
    for x, top in [(28, 20), (50, 8), (72, 14), (92, 30)]:
        p.append(path("M%g,%g L%g,%g" % (x, top + 16, x, 54), color))
        p.append(path("M%g,%g C%g,%g %g,%g %g,%g" % (x - 9, top + 16, x - 9, top, x + 9, top, x + 9, top + 16),
                      acento, 6))
    p.append(path("M12,60 C4,60 0,68 6,74 L20,86", color))
    return "".join(p)


def grafico_barras(alturas=(30, 52, 76), color=TINTA, acento=VERDE):
    """Barras ascendentes. Caja local: 0,0 -> 108,88."""
    p = [linea(0, 88, 108, 88, color)]
    for i, h_ in enumerate(alturas):
        c = acento if i == len(alturas) - 1 else color
        p.append(rect(8 + i * 34, 88 - h_, 26, h_, 4, c, 6))
    return "".join(p)


def flecha(x1, y1, x2, y2, color=TINTA, w=6, punta=14):
    """Flecha recta con punta."""
    a = math.atan2(y2 - y1, x2 - x1)
    p = [linea(x1, y1, x2, y2, color, w)]
    for s in (2.6, -2.6):
        p.append(linea(x2, y2, x2 + math.cos(a + s) * punta, y2 + math.sin(a + s) * punta, color, w))
    return "".join(p)


def camara(color=TINTA):
    """Camara de fotos. Caja local: 0,0 -> 104,76."""
    p = [path("M0,26 C0,20 5,14 12,14 L26,14 L34,2 L70,2 L78,14 L92,14 "
              "C99,14 104,20 104,26 L104,64 C104,70 99,76 92,76 L12,76 "
              "C5,76 0,70 0,64 Z", color)]
    p.append(circulo(52, 44, 19, color))
    return "".join(p)


def cuadro_foto(t="", color=TINTA, w_=76, h_=88, color_texto=None):
    """Marco de foto: con texto o con paisaje. Caja local: 0,0 -> w_,h_."""
    p = [rect(0, 0, w_, h_, 8, color)]
    if t:
        p.append(texto(t, w_ / 2.0, h_ / 2.0 + 11, 30, color_texto or color))
    else:
        p.append(path("M10,%g L%g,%g L%g,%g L%g,%g" % (h_ - 16, w_ * 0.34, h_ * 0.46,
                                                       w_ * 0.56, h_ - 30, w_ - 10, h_ * 0.40), color, 5))
        p.append(circulo(w_ * 0.28, 24, 8, color, 5))
    return "".join(p)


def tijera(color=TINTA):
    """Tijera de barberia. Caja local: 0,0 -> 76,104."""
    p = [circulo(16, 88, 14, color), circulo(60, 88, 14, color)]
    p.append(path("M60,76 L20,10", color))
    p.append(path("M16,76 L56,10", color))
    p.append(circulo(38, 46, 4, color, 5, color))
    return "".join(p)


# --------------------------------------------------------------------------
# iconos compuestos
# --------------------------------------------------------------------------

ICONOS = {}


def _reg(nombre):
    def deco(fn):
        ICONOS[nombre] = fn
        return fn
    return deco


@_reg("tijera_prisa")
def _tijera_prisa():
    return (g(tijera(), 108, 34, 1.05) +
            linea(14, 66, 62, 66) + linea(30, 96, 68, 96) + linea(22, 126, 58, 126))


@_reg("persona_preguntas")
def _persona_preguntas():
    return g(persona(), 14, 66) + g(bocadillo("? ? ?", 118, 62, TINTA, 34, VERDE), 96, 26)


@_reg("bocadillo_repetir")
def _bocadillo_repetir():
    return g(bocadillo("LO MISMO", 172, 74, TINTA, 34), 34, 30) + texto("...", 120, 172, 40)


@_reg("persona_escucha")
def _persona_escucha():
    return g(persona(), 8, 66) + g(bocadillo("¿CÓMO TE FUE?", 156, 62, VERDE, 26, VERDE, "der"), 78, 26)


@_reg("persona_obedece")
def _persona_obedece():
    return g(persona(), 16, 66) + g(bocadillo("TAL CUAL", 138, 62, TINTA, 30), 92, 26)


@_reg("persona_propone")
def _persona_propone():
    return (g(persona(), 6, 66) + g(bocadillo("MEJOR ASÍ", 142, 62, VERDE, 30, VERDE), 82, 24) +
            g(estrella_destello(VERDE, 0.42, False), 178, 116))


@_reg("bocadillo_mudo")
def _bocadillo_mudo():
    return g(bocadillo("", 136, 74, TINTA), 52, 34) + linea(78, 122, 176, 44, TINTA, 6)


@_reg("bocadillo_explica")
def _bocadillo_explica():
    return (g(bocadillo("", 128, 74, VERDE), 8, 34) +
            linea(30, 60, 116, 60, VERDE, 5) + linea(30, 82, 98, 82, VERDE, 5) +
            g(documento_checks(2), 152, 40, 0.86))


@_reg("etiqueta_sube")
def _etiqueta_sube():
    return g(etiqueta_precio("$"), 22, 40, 1.20) + g(flecha(0, 70, 0, 0, VERDE, 8, 17), 186, 58)


@_reg("reloj")
def _reloj():
    return g(reloj(), 84, 54, 1.1)


@_reg("reloj_moneda")
def _reloj_moneda():
    return g(reloj(), 22, 50) + g(circulo(0, 0, 30, VERDE) + texto("$", 0, 12, 36, VERDE), 172, 92)


@_reg("documento_checks")
def _documento_checks():
    return g(documento_checks(3), 78, 38)


@_reg("documento_lineas")
def _documento_lineas():
    return g(documento_checks(3, marcas=False), 78, 38)


@_reg("documento_equis")
def _documento_equis():
    return g(documento_checks(2, marcas=False), 30, 38, 0.94) + g(equis_circulo(TINTA, 28), 150, 92)


@_reg("persona_muda")
def _persona_muda():
    return (g(persona(), 40, 62, 1.15) + g(bocadillo("", 92, 52, TINTA), 138, 30) +
            linea(150, 96, 224, 42, TINTA, 6))


@_reg("bocadillo_simple")
def _bocadillo_simple():
    return g(persona(), 8, 66) + g(bocadillo("EN SIMPLE", 150, 62, VERDE, 30, VERDE), 80, 26)


@_reg("camara_tachada")
def _camara_tachada():
    return g(camara(), 62, 52) + linea(52, 148, 196, 34, TINTA, 7)


@_reg("antes_despues")
def _antes_despues():
    return (g(cuadro_foto("ANTES", TINTA, 96, 104), 6, 38) +
            g(cuadro_foto("DESPUÉS", VERDE, 96, 104, VERDE), 138, 38) +
            g(flecha(0, 0, 24, 0, VERDE, 6, 11), 106, 90))


@_reg("calendario_duda")
def _calendario_duda():
    return g(calendario("?"), 74, 44, 1.15)


@_reg("calendario_fecha")
def _calendario_fecha():
    return g(calendario("4 SEM", VERDE, VERDE), 74, 44, 1.15)


@_reg("calendario_tres_sem")
def _calendario_tres_sem():
    return g(calendario("3 SEM", VERDE, VERDE), 74, 44, 1.15)


@_reg("calendario_vacio")
def _calendario_vacio():
    return g(calendario("", TINTA), 74, 44, 1.15)


@_reg("calendario_lleno")
def _calendario_lleno():
    marcas = "".join(linea(14 + c * 22, 46 + f * 18, 26 + c * 22, 46 + f * 18, TINTA, 5)
                     for f in range(2) for c in range(3))
    return g(calendario("", TINTA) + marcas, 74, 44, 1.15)


@_reg("calendario_checks")
def _calendario_checks():
    marcas = "".join(
        path("M%g,%g L%g,%g L%g,%g" % (12 + c * 25, 48 + f * 20, 18 + c * 25, 54 + f * 20,
                                       28 + c * 25, 42 + f * 20), VERDE, 5)
        for f in range(2) for c in range(3))
    return g(calendario("", VERDE) + marcas, 74, 44, 1.15)


@_reg("calendario_aviso")
def _calendario_aviso():
    return g(calendario("1 MES", VERDE, VERDE), 74, 44, 1.15)


@_reg("estrella_destello")
def _estrella_destello():
    return g(estrella_destello(VERDE, 1.15), 82, 40)


@_reg("carta_larga")
def _carta_larga():
    return g(documento_checks(4, marcas=False), 78, 30, 1.05)


@_reg("grafico_barras")
def _grafico_barras():
    return g(grafico_barras(), 66, 46)


@_reg("etiqueta_descuento")
def _etiqueta_descuento():
    return g(etiqueta_precio("30%"), 74, 44, 1.05) + linea(64, 150, 192, 38, TINTA, 7)


@_reg("combo_suma")
def _combo_suma():
    return (g(etiqueta_precio("", VERDE), 4, 52, 0.86) + texto("+", 120, 118, 54, VERDE) +
            g(etiqueta_precio("", VERDE), 154, 52, 0.86))


@_reg("etiqueta_estrella")
def _etiqueta_estrella():
    return g(etiqueta_precio("", VERDE), 22, 46) + g(estrella_destello(VERDE, 0.5, False), 148, 82)


@_reg("nivel_sube")
def _nivel_sube():
    return g(grafico_barras((28, 50, 74)), 10, 54, 0.9) + g(estrella_destello(VERDE, 0.44, False), 154, 46)


@_reg("reloj_espera")
def _reloj_espera():
    return g(reloj(), 40, 52) + texto("...", 180, 120, 44)


@_reg("luces_dispares")
def _luces_dispares():
    return g(sol(TINTA, 16, 8), 62, 66) + g(sol(TINTA, 9, 6), 178, 110) + linea(112, 90, 142, 102, TINTA, 5)


@_reg("rincon_luz")
def _rincon_luz():
    return g(camara(), 16, 66, 0.92) + g(sol(VERDE, 15, 8), 188, 56)


@_reg("foto_una")
def _foto_una():
    return g(cuadro_foto("", TINTA, 96, 108), 72, 36)


@_reg("telefono_publica")
def _telefono_publica():
    return g(telefono(), 62, 44) + g(equis_circulo(TINTA, 26), 148, 100)


@_reg("bocadillo_permiso")
def _bocadillo_permiso():
    return g(persona(), 8, 66) + g(bocadillo("¿PUEDO?", 132, 62, VERDE, 30, VERDE), 94, 26)


@_reg("dos_personas")
def _dos_personas():
    return g(persona(), 20, 66, 0.94) + g(persona(), 122, 66, 0.94) + g(bocadillo("", 74, 40, TINTA), 84, 14)


@_reg("telefono_cliente")
def _telefono_cliente():
    return (g(telefono(), 22, 44) + g(persona(), 128, 64, 0.92) +
            g(estrella_destello(VERDE, 0.3, False), 202, 38))


@_reg("telefono_grid")
def _telefono_grid():
    celdas = "".join(rect(9 + c * 22, 24 + f * 22, 18, 18, 3, VERDE, 4)
                     for f in range(3) for c in range(2))
    return g(telefono(VERDE, celdas), 94, 44)


@_reg("documento_numeros")
def _documento_numeros():
    filas = "".join(texto("#", 18, 54 + i * 20, 22, TINTA, "start") +
                    linea(38, 48 + i * 20, 70, 48 + i * 20, TINTA, 5) for i in range(3))
    return g(documento_checks(0, marcas=False) + filas, 78, 38)


@_reg("ficha_persona")
def _ficha_persona():
    return g(documento_checks(2), 10, 40, 0.92) + g(persona(), 144, 66)


@_reg("bocadillo_seco")
def _bocadillo_seco():
    return g(bocadillo("¿QUÉ TE HAGO?", 204, 76, TINTA, 32), 18, 34)


@_reg("dos_opciones")
def _dos_opciones():
    return (g(cuadro_foto("A", VERDE, 88, 96, VERDE), 12, 42) +
            g(cuadro_foto("B", VERDE, 88, 96, VERDE), 140, 42))


@_reg("check_simple")
def _check_simple():
    return g(check_circulo(TINTA, 42), 78, 48)


@_reg("persona_estrella")
def _persona_estrella():
    return g(persona(), 40, 62, 1.2) + g(estrella_destello(VERDE, 0.46, False), 148, 44)


@_reg("mano_apurada")
def _mano_apurada():
    return (g(mano_unas(TINTA, TINTA), 52, 44, 1.15) +
            linea(12, 154, 58, 154, TINTA, 5) + linea(30, 172, 70, 172, TINTA, 5))


@_reg("mano_cuidado")
def _mano_cuidado():
    return g(mano_unas(TINTA, VERDE), 36, 44, 1.2) + g(estrella_destello(VERDE, 0.3, False), 196, 34)


@_reg("telefono_mensaje")
def _telefono_mensaje():
    return (g(telefono(), 16, 44) + g(bocadillo("", 96, 54, VERDE), 114, 40) +
            linea(134, 62, 196, 62, VERDE, 5) + linea(134, 80, 178, 80, VERDE, 5))


@_reg("bocadillos_choque")
def _bocadillos_choque():
    return g(bocadillo("", 104, 56, TINTA, cola="der"), 6, 20) + g(bocadillo("", 104, 56, TINTA), 130, 82)


@_reg("bocadillo_favor")
def _bocadillo_favor():
    return g(bocadillo("FAVOR", 170, 76, TINTA, 36), 36, 34)


@_reg("reparacion_ok")
def _reparacion_ok():
    return g(check_circulo(VERDE, 40), 30, 50) + g(estrella_destello(VERDE, 0.42, False), 148, 46)


@_reg("interrogacion_circulo")
def _interrogacion_circulo():
    return g(circulo(0, 0, 44, TINTA) + texto("?", 0, 18, 56, TINTA), 120, 90)


@_reg("bocadillo_caja")
def _bocadillo_caja():
    return g(bocadillo("¿TE LLEVAS ALGO?", 220, 70, TINTA, 30), 10, 20) + g(etiqueta_precio("", TINTA), 150, 112, 0.6)


@_reg("frasco_aplica")
def _frasco_aplica():
    return g(frasco("", VERDE), 30, 40) + g(mano_unas(TINTA, TINTA), 116, 60, 0.86)


@_reg("frasco_texto")
def _frasco_texto():
    lineas = "".join(linea(12, 58 + i * 14, 50, 58 + i * 14, TINTA, 4) for i in range(3))
    return g(frasco("", TINTA) + lineas, 90, 38, 1.15)


@_reg("frasco_conecta")
def _frasco_conecta():
    return (g(persona(), 4, 66, 0.94) + g(bocadillo("", 94, 52, VERDE), 82, 28) +
            g(frasco("", VERDE), 190, 70, 0.72))


@_reg("bocadillos_insiste")
def _bocadillos_insiste():
    return (g(bocadillo("", 86, 42, TINTA), 6, 10) + g(bocadillo("", 86, 42, TINTA), 76, 62) +
            g(bocadillo("", 86, 42, TINTA), 146, 114))


@_reg("bocadillo_una_vez")
def _bocadillo_una_vez():
    return g(bocadillo("", 118, 60, VERDE), 12, 40) + g(check_circulo(VERDE, 30), 160, 58)


@_reg("frasco_duda")
def _frasco_duda():
    return g(frasco("", TINTA), 40, 40) + g(circulo(0, 0, 30, TINTA) + texto("?", 0, 12, 38, TINTA), 178, 92)


@_reg("frasco_estrella")
def _frasco_estrella():
    return g(frasco("", VERDE), 32, 40) + g(estrella_destello(VERDE, 0.46, False), 138, 58)


@_reg("frasco_check")
def _frasco_check():
    return g(frasco("", VERDE), 36, 40) + g(check_circulo(VERDE, 32), 148, 74)


@_reg("cabeza_reglas")
def _cabeza_reglas():
    return (g(persona(), 18, 66) + g(bocadillo("", 110, 62, TINTA), 106, 24) +
            linea(126, 44, 198, 44, TINTA, 5) + linea(126, 64, 176, 64, TINTA, 5))


@_reg("persona_modelo")
def _persona_modelo():
    return (g(persona(), 14, 64, 1.05) + g(flecha(0, 0, 42, 0, VERDE, 6, 12), 98, 102) +
            g(persona(VERDE, VERDE), 158, 64, 1.05))


@_reg("correccion_publica")
def _correccion_publica():
    return (g(persona(), 6, 70, 0.88) + g(persona(), 90, 70, 0.88) + g(persona(), 174, 70, 0.88) +
            g(bocadillo("", 90, 40, TINTA), 74, 12))


@_reg("correccion_privada")
def _correccion_privada():
    return (g(persona(), 24, 70, 0.98) + g(persona(VERDE, VERDE), 132, 70, 0.98) +
            g(bocadillo("", 64, 34, VERDE), 98, 22))


@_reg("equipo_sello")
def _equipo_sello():
    return (g(persona(), 6, 74, 0.86) + g(persona(VERDE, VERDE), 86, 62, 0.98) +
            g(persona(), 176, 74, 0.86) + g(estrella_destello(VERDE, 0.3, False), 98, 16))


@_reg("bocadillo_depende")
def _bocadillo_depende():
    return g(bocadillo("DEPENDE...", 200, 78, TINTA, 38), 20, 32)


@_reg("lista_precios")
def _lista_precios():
    filas = "".join(linea(14, 50 + i * 18, 50, 50 + i * 18, VERDE, 5) +
                    texto("$", 70, 56 + i * 18, 20, VERDE) for i in range(3))
    return g(documento_checks(0, VERDE, VERDE, False) + filas, 78, 38)


@_reg("etiqueta_sola")
def _etiqueta_sola():
    return g(etiqueta_precio("$", TINTA), 72, 44, 1.15)


@_reg("valor_y_precio")
def _valor_y_precio():
    return g(documento_checks(3, VERDE, VERDE), 8, 40, 0.9) + g(etiqueta_precio("$", VERDE), 132, 56, 0.92)


@_reg("bocadillo_disculpa")
def _bocadillo_disculpa():
    return g(bocadillo("ES QUE...", 180, 78, TINTA, 38), 30, 32)


@_reg("etiqueta_firme")
def _etiqueta_firme():
    return g(etiqueta_precio("$", VERDE), 26, 44, 1.1) + g(check_circulo(VERDE, 28), 158, 96)


# --------------------------------------------------------------------------

def svg(nombre):
    """Devuelve el SVG completo de un icono."""
    if nombre not in ICONOS:
        raise KeyError("icono desconocido: %s" % nombre)
    return (
        '<svg class="ilu" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
        'fill="none" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
        % (W, H, ICONOS[nombre]())
    )


def disponibles():
    return sorted(ICONOS)
