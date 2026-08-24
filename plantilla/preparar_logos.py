# -*- coding: utf-8 -*-
"""
Prepara los dos logos que usa la plantilla a partir del sello corporativo.

Entrada:  assets/Logo Verde corporativo.webp  (disco verde, texto crema, fondo blanco)
Salida:   assets/logo_verde.png   -> tal cual, con el fondo recortado.
                                     Va en los pies, sobre crema.
          assets/logo_blanco.png  -> colores invertidos: disco crema, arte verde.
                                     Va en las portadas, sobre verde oscuro.

Un disco verde sobre el verde oscuro de portada no se leeria, por eso la
version invertida en vez de un simple recoloreado.

Uso:  python plantilla/preparar_logos.py
"""

import os
import sys

from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(RAIZ, "assets")
ORIGEN = os.path.join(ASSETS, "Logo Verde corporativo.webp")

CREMA = (244, 239, 227)
VERDE_OSCURO = (30, 58, 46)

BLANCO_FONDO = 246          # por encima de esto y fuera del sello: es fondo
MARGEN = 2                  # px de holgura al recortar


def cargar():
    if not os.path.exists(ORIGEN):
        raise SystemExit("No encuentro %s" % ORIGEN)
    return Image.open(ORIGEN).convert("RGB")


def mascara_circular(im):
    """Alpha: opaco dentro del sello, transparente en el fondo blanco."""
    w, h = im.size
    px = im.load()

    # el sello es circular y esta centrado: busco su radio desde el centro
    cx, cy = w / 2.0, h / 2.0
    radio = 0
    for x in range(int(cx), w):
        r, g, b = px[x, int(cy)]
        if r >= BLANCO_FONDO and g >= BLANCO_FONDO and b >= BLANCO_FONDO:
            radio = x - cx
            break
    if radio <= 0:
        radio = min(cx, cy)

    alpha = Image.new("L", (w, h), 0)
    ap = alpha.load()
    r2 = (radio - MARGEN) ** 2
    borde = (radio + 1.5) ** 2
    for y in range(h):
        dy2 = (y - cy) ** 2
        for x in range(w):
            d2 = (x - cx) ** 2 + dy2
            if d2 <= r2:
                ap[x, y] = 255
            elif d2 <= borde:                      # antialias del borde
                ap[x, y] = 140
    return alpha, radio


def _muestrear_colores(im, radio):
    """Los dos colores reales del sello: el verde del disco y el crema del arte."""
    px = im.load()
    w, h = im.size
    cx, cy = w // 2, h // 2
    claros, oscuros = [], []
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            if (x - cx) ** 2 + (y - cy) ** 2 > (radio * 0.86) ** 2:
                continue
            r, g, b = px[x, y]
            (claros if (r + g + b) > 450 else oscuros).append((r, g, b))
    prom = lambda L: tuple(sum(c[i] for c in L) // len(L) for i in range(3))
    return prom(oscuros), prom(claros)          # verde, crema


def invertir(im, verde_src, crema_src):
    """Intercambia verde y crema conservando el suavizado de los bordes."""
    px = im.load()
    w, h = im.size
    salida = Image.new("RGB", (w, h))
    sp = salida.load()

    dx = tuple(verde_src[i] - crema_src[i] for i in range(3))
    den = float(sum(c * c for c in dx)) or 1.0

    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            t = ((r - crema_src[0]) * dx[0] +
                 (g - crema_src[1]) * dx[1] +
                 (b - crema_src[2]) * dx[2]) / den
            t = 0.0 if t < 0 else (1.0 if t > 1 else t)
            # t=1 (era verde) -> crema ; t=0 (era crema) -> verde oscuro
            sp[x, y] = tuple(
                int(round(VERDE_OSCURO[i] + (CREMA[i] - VERDE_OSCURO[i]) * t))
                for i in range(3))
    return salida


def main():
    im = cargar()
    alpha, radio = mascara_circular(im)
    print("Sello detectado: radio %d px sobre %dx%d" % (radio, im.size[0], im.size[1]))

    verde_src, crema_src = _muestrear_colores(im, radio)
    print("Colores del sello: verde %s  crema %s" % (verde_src, crema_src))

    # 1. version para interiores: el sello tal cual, sin fondo
    verde = im.copy()
    verde.putalpha(alpha)
    verde = verde.crop(verde.getbbox())
    verde.save(os.path.join(ASSETS, "logo_verde.png"))
    print("logo_verde.png   %s  (pies, sobre crema)" % (verde.size,))

    # 2. version para portadas: invertida
    blanco = invertir(im, verde_src, crema_src)
    blanco.putalpha(alpha)
    blanco = blanco.crop(blanco.getbbox())
    blanco.save(os.path.join(ASSETS, "logo_blanco.png"))
    print("logo_blanco.png  %s  (portadas, sobre verde oscuro)" % (blanco.size,))


if __name__ == "__main__":
    sys.exit(main())
