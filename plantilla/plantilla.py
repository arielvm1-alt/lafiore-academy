# -*- coding: utf-8 -*-
"""
Generador del HTML/CSS de las laminas de La Fiore Academy.

Cada lamina es un documento HTML autocontenido de 1080 x 1350 px:
fuentes y logos van embebidos en base64 para que el render sea
reproducible y no dependa de rutas relativas.
"""

import base64
import os
import re

import iconos

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(RAIZ, "assets")
FUENTES = os.path.join(ASSETS, "fonts")

ANCHO, ALTO = 1080, 1350

# ---- identidad -----------------------------------------------------------
VERDE_OSCURO = "#1E3A2E"
VERDE_CLARO = "#32614D"
CREMA = "#F4EFE3"
DORADO = "#C2A15B"
TINTA = "#1A1D1B"

ANO = "2026"
HANDLE = "@La_Fiore_Academy"


# --------------------------------------------------------------------------
# assets embebidos
# --------------------------------------------------------------------------

def _b64(ruta):
    with open(ruta, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def _fuente(archivo):
    return "data:font/ttf;base64," + _b64(os.path.join(FUENTES, archivo))


def _imagen(archivo):
    return "data:image/png;base64," + _b64(os.path.join(ASSETS, archivo))


_CACHE = {}


def assets():
    if not _CACHE:
        _CACHE.update({
            "bebas": _fuente("BebasNeue-Bold.ttf"),
            "lora": _fuente("LoraVF.ttf"),
            "poppins_medium": _fuente("Poppins-Medium.ttf"),
            "poppins_semibold": _fuente("Poppins-SemiBold.ttf"),
            "poppins_bold": _fuente("Poppins-Bold.ttf"),
            "logo_verde": _imagen("logo_verde.png"),
            "logo_blanco": _imagen("logo_blanco.png"),
        })
    return _CACHE


# --------------------------------------------------------------------------
# marcado del copy
# --------------------------------------------------------------------------

def _escapar(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def marcar(texto, simple="em", doble="b"):
    """Convierte **negrita** y *resalte* en etiquetas HTML."""
    t = _escapar(texto)
    t = re.sub(r"\*\*(.+?)\*\*", r"<%s>\1</%s>" % (doble, doble), t)
    t = re.sub(r"\*(.+?)\*", r"<%s>\1</%s>" % (simple, simple), t)
    return t


def sin_marcas(texto):
    return texto.replace("*", "")


# --------------------------------------------------------------------------
# CSS
# --------------------------------------------------------------------------

GRANO = (
    "data:image/svg+xml;utf8,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E"
    "%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' "
    "numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E"
    "%3Crect width='300' height='300' filter='url(%23g)'/%3E%3C/svg%3E"
)


def css():
    a = assets()
    return """
@font-face { font-family:'Bebas Neue'; src:url('%(bebas)s') format('truetype'); font-weight:700; }
@font-face { font-family:'Lora'; src:url('%(lora)s') format('truetype'); font-weight:400 700; }
@font-face { font-family:'Poppins'; src:url('%(poppins_medium)s') format('truetype'); font-weight:500; }
@font-face { font-family:'Poppins'; src:url('%(poppins_semibold)s') format('truetype'); font-weight:600; }
@font-face { font-family:'Poppins'; src:url('%(poppins_bold)s') format('truetype'); font-weight:700; }

*, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
html, body { width:%(ancho)dpx; height:%(alto)dpx; }
body { -webkit-font-smoothing:antialiased; text-rendering:geometricPrecision; }

.lamina {
  position:relative; width:%(ancho)dpx; height:%(alto)dpx; overflow:hidden;
  display:flex; flex-direction:column;
}
.grano {
  position:absolute; inset:0; z-index:5; pointer-events:none;
  background-image:url("%(grano)s"); background-size:300px 300px;
  opacity:.22; mix-blend-mode:multiply;
}
.capa { position:relative; z-index:1; display:flex; flex-direction:column; height:100%%; }

/* ------------------------------------------------------------ PORTADA */
.portada { background:%(verde_oscuro)s; padding:70px 66px; }
.kicker {
  font-family:Poppins; font-weight:600; font-size:23px; letter-spacing:.30em;
  color:%(dorado)s; text-transform:uppercase;
}
.regla-dorada { width:100px; height:4px; background:%(dorado)s; margin-top:28px; }
.portada-centro { flex:1; display:flex; flex-direction:column; justify-content:center; }
.portada-titulo {
  font-family:Lora; font-weight:700; font-size:88px; line-height:1.12; color:%(crema)s;
}
.portada-titulo em { font-style:normal; color:%(dorado)s; }
.portada-sub {
  font-family:Poppins; font-weight:500; font-size:31px; line-height:1.44;
  color:#BFCCC1; margin-top:42px; max-width:880px;
}
.portada-sub b { color:%(dorado)s; font-weight:700; }
.portada-pie { display:flex; align-items:flex-end; justify-content:space-between; }
.desliza { display:flex; align-items:center; gap:24px; }
.desliza .circulo {
  width:62px; height:62px; border-radius:50%%; background:%(dorado)s;
  display:flex; align-items:center; justify-content:center;
  color:%(verde_oscuro)s; font-family:Poppins; font-weight:600; font-size:32px; line-height:1;
}
.desliza .txt {
  font-family:Poppins; font-weight:600; font-size:24px; letter-spacing:.24em; color:%(dorado)s;
}
.logo-portada { height:110px; width:auto; display:block; }

/* ----------------------------------------------------------- INTERIOR */
.interior { background:%(crema)s; padding:50px 54px; color:%(tinta)s; }

.barra-sup {
  display:flex; justify-content:space-between; align-items:baseline;
  font-family:Poppins; font-weight:500; font-size:14px; letter-spacing:.13em;
  color:#5A5F5B; text-transform:uppercase;
}
.masthead { position:relative; margin-top:20px; text-align:center; }
.masthead .marca {
  font-family:Lora; font-weight:700; font-size:52px; letter-spacing:.12em;
  line-height:1.06; color:%(tinta)s;
}
.masthead .bajada {
  font-family:Poppins; font-weight:500; font-size:14px; letter-spacing:.24em;
  color:#5A5F5B; margin-top:10px; text-transform:uppercase;
}
.folio {
  position:absolute; left:0; top:50%%; transform:translateY(-50%%);
  width:56px; height:56px; background:%(verde_claro)s; color:#FFFFFF;
  display:flex; align-items:center; justify-content:center;
  font-family:'Bebas Neue'; font-weight:700; font-size:42px; line-height:1;
}
.doble-regla { margin-top:20px; }
.doble-regla i { display:block; background:%(tinta)s; }
.doble-regla i:first-child { height:3px; }
.doble-regla i:last-child { height:2px; margin-top:6px; }

.antetitulo {
  font-family:'Bebas Neue'; font-weight:700; font-size:40px; letter-spacing:.10em;
  color:%(tinta)s; margin-top:26px; line-height:1;
}
.titulo {
  font-family:'Bebas Neue'; font-weight:700; font-size:100px; line-height:.90;
  letter-spacing:.005em; color:%(tinta)s; margin-top:12px;
}
.titulo em { font-style:normal; color:%(verde_claro)s; }

.filas { flex:1; display:flex; flex-direction:column; justify-content:space-between; margin-top:4px; }
.fila { display:flex; align-items:center; gap:26px; padding:36px 0; }
.fila + .fila { border-top:2px solid rgba(26,29,27,.22); }
.disco {
  flex:0 0 68px; width:68px; height:68px; border-radius:50%%;
  display:flex; align-items:center; justify-content:center;
  font-family:Poppins; font-weight:600; font-size:30px; line-height:1;
}
.disco.no { background:%(tinta)s; color:#FFFFFF; }
.disco.si { background:%(verde_claro)s; color:#FFFFFF; }
.disco.frase { border:5px solid %(verde_claro)s; color:%(verde_claro)s; font-size:32px; }
.etiqueta {
  flex:0 0 auto; font-family:'Bebas Neue'; font-weight:700; font-size:54px;
  line-height:1; letter-spacing:.05em;
}
.etiqueta.no { color:%(tinta)s; }
.etiqueta.si { color:%(verde_claro)s; }
.etiqueta.frase { font-size:44px; color:%(verde_claro)s; letter-spacing:.10em; }
.fila.frase-fila { display:block; }
.frase-kicker { display:flex; align-items:center; gap:26px; }
.cuerpo {
  flex:1 1 auto; min-width:0;
  font-family:Poppins; font-weight:500; font-size:41px; line-height:1.22; color:#2B2F31;
}
.frase-lineas { margin:16px 0 0 94px; font-family:Poppins; font-weight:700; font-size:47px; line-height:1.18; }
.frase-lineas .a { color:%(tinta)s; }
.frase-lineas .b { color:%(verde_claro)s; }
.ilu-col { flex:0 0 226px; height:172px; display:flex; align-items:center; justify-content:center; }
.ilu { width:100%%; height:100%%; display:block; }

/* ------------------------------------------------------------- CIERRE */
.cierre-centro { flex:1; display:flex; align-items:center; justify-content:center; }
.cierre-centro .ilu { width:620px; height:465px; }
.banda {
  background:%(verde_claro)s; margin:0 -54px; padding:40px 54px 44px;
  display:flex; flex-direction:column; gap:12px;
}
.banda .guarda {
  font-family:'Bebas Neue'; font-weight:700; font-size:70px; line-height:1;
  letter-spacing:.04em; color:%(crema)s;
}
.banda .cta { font-family:Poppins; font-weight:500; font-size:23px; line-height:1.42; color:#DCE6DD; }

/* ---------------------------------------------------------------- PIE */
.pie { margin-top:26px; border-top:3px solid %(tinta)s; padding-top:22px;
       display:flex; align-items:center; justify-content:space-between; }
.pie-izq { display:flex; align-items:center; gap:22px; }
.logo-pie { height:104px; width:auto; display:block; }
.pie-txt { font-family:Poppins; font-weight:500; font-size:19px; letter-spacing:.13em;
           line-height:1.5; color:%(tinta)s; text-transform:uppercase; }
.pie-txt .handle { text-transform:none; letter-spacing:.05em; }
.pie-der { font-family:Poppins; font-weight:500; font-size:19px; letter-spacing:.13em;
           color:%(tinta)s; text-transform:uppercase; text-align:right; }
""" % {
        "bebas": a["bebas"], "lora": a["lora"],
        "poppins_medium": a["poppins_medium"], "poppins_semibold": a["poppins_semibold"],
        "poppins_bold": a["poppins_bold"],
        "grano": GRANO, "ancho": ANCHO, "alto": ALTO,
        "verde_oscuro": VERDE_OSCURO, "verde_claro": VERDE_CLARO,
        "crema": CREMA, "dorado": DORADO, "tinta": TINTA,
    }


# --------------------------------------------------------------------------
# bloques
# --------------------------------------------------------------------------

def _documento(clase, contenido):
    return (
        "<!doctype html><html lang='es'><head><meta charset='utf-8'>"
        "<style>%s</style></head><body>"
        "<div class='lamina %s'><div class='capa'>%s</div><div class='grano'></div></div>"
        "</body></html>" % (css(), clase, contenido)
    )


def _cabecera(vol, pagina):
    return (
        "<div class='barra-sup'><span>Edición especial</span>"
        "<span>Formación continua</span><span>Vol. %s · %s</span></div>"
        "<div class='masthead'><div class='folio'>%d</div>"
        "<div class='marca'>LA FIORE ACADEMY</div>"
        "<div class='bajada'>Barberos · Estilistas · Manicuristas</div></div>"
        "<div class='doble-regla'><i></i><i></i></div>"
        % (vol, ANO, pagina)
    )


def _pie(pagina, derecha=None):
    a = assets()
    der = derecha if derecha is not None else "Página %d de 6" % pagina
    return (
        "<div class='pie'><div class='pie-izq'>"
        "<img class='logo-pie' src='%s' alt=''>"
        "<div class='pie-txt'>La Fiore Academy /<br><span class='handle'>%s</span></div>"
        "</div><div class='pie-der'>%s</div></div>"
        % (a["logo_verde"], HANDLE, der)
    )


def _fila(tipo, etiqueta, simbolo, texto, icono):
    return (
        "<div class='fila'><div class='disco %s'>%s</div>"
        "<div class='etiqueta %s'>%s</div>"
        "<div class='cuerpo'>%s</div>"
        "<div class='ilu-col'>%s</div></div>"
        % (tipo, simbolo, tipo, etiqueta, _escapar(texto), iconos.svg(icono))
    )


def _fila_frase(a_txt, b_txt):
    return (
        "<div class='fila frase-fila'>"
        "<div class='frase-kicker'><div class='disco frase'>★</div>"
        "<div class='etiqueta frase'>FRASE</div></div>"
        "<div class='frase-lineas'><div class='a'>%s</div><div class='b'>%s</div></div></div>"
        % (_escapar(a_txt), _escapar(b_txt))
    )


# --------------------------------------------------------------------------
# laminas
# --------------------------------------------------------------------------

def portada(s):
    a = assets()
    contenido = (
        "<div><div class='kicker'>La Fiore Academy · Formación profesional</div>"
        "<div class='regla-dorada'></div></div>"
        "<div class='portada-centro'>"
        "<h1 class='portada-titulo'>%s</h1>"
        "<p class='portada-sub'>%s</p></div>"
        "<div class='portada-pie'>"
        "<div class='desliza'><div class='circulo'>&#8594;</div><div class='txt'>DESLIZA</div></div>"
        "<img class='logo-portada' src='%s' alt=''></div>"
        % (marcar(s["portada"]["titulo"]), marcar(s["portada"]["sub"]), a["logo_blanco"])
    )
    return _documento("portada", contenido)


def interior(s, indice):
    """indice 0..3 -> paginas 2..5."""
    p = s["paginas"][indice]
    n = indice + 2
    contenido = (
        _cabecera(s["vol"], n)
        + "<div class='antetitulo'>%s</div>" % _escapar(p["ante"])
        + "<h2 class='titulo'>%s</h2>" % marcar(p["titulo"])
        + "<div class='filas'>%s%s%s</div>" % (
            _fila("no", "NO", "&#10005;", p["no"], p["no_icono"]),
            _fila("si", "SÍ", "&#10003;", p["si"], p["si_icono"]),
            _fila_frase(p["frase_a"], p["frase_b"]),
        )
        + _pie(n)
    )
    return _documento("interior", contenido)


def cierre(s):
    c = s["cierre"]
    contenido = (
        _cabecera(s["vol"], 6)
        + "<div class='antetitulo'>%s</div>" % _escapar(c["ante"])
        + "<h2 class='titulo'>%s</h2>" % marcar(c["titulo"])
        + "<div class='cierre-centro'>%s</div>" % iconos.svg(c["icono"])
        + "<div class='banda'><div class='guarda'>GUÁRDALO.</div>"
          "<div class='cta'>%s</div></div>" % _escapar(c["cta"])
        + _pie(6, "Talagante · Chile")
    )
    return _documento("interior cierre", contenido)


def laminas(s):
    """Devuelve las 6 laminas del set como lista de (nombre, html)."""
    out = [("01_portada", portada(s))]
    for i in range(4):
        out.append(("%02d_pagina" % (i + 2), interior(s, i)))
    out.append(("06_cierre", cierre(s)))
    return out
