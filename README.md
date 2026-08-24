# La Fiore Academy · carruseles + publicación automática

Genera 10 sets de 6 láminas (1080×1350, JPG calidad 95) con la plantilla de
**La Fiore Academy** y los publica en Instagram, uno por día, sin que tengas
que tocar nada.

---

## 1. Qué hay en cada carpeta

```
lafiore-academy/
├── assets/              logos (logo_verde.png, logo_blanco.png) + fuentes
│   └── fonts/           Bebas Neue Bold, Lora, Poppins
├── plantilla/
│   ├── iconos.py        librería de ilustraciones SVG propias
│   ├── plantilla.py     HTML/CSS de las láminas
│   └── render.py        render con Chromium + control de calidad
├── contenido/
│   ├── sets.py          el copy de los 10 sets
│   └── captions.py      los textos de Instagram
├── salida/
│   ├── set_01/ … set_10/    6 JPG por carpeta
│   └── captions.json
├── publicar.py          publica un carrusel vía Graph API
├── estado.json          qué set se publicó y cuándo
└── .github/workflows/publicar.yml   el cron diario
```

---

## 2. Generar las imágenes

Solo hace falta la primera vez:

```bash
pip install playwright pillow && python -m playwright install chromium
```

Y para renderizar:

```bash
python plantilla/render.py
```

Opciones:

```bash
python plantilla/render.py 1        # solo el set 01
python plantilla/render.py 1 3 7    # sets sueltos
```

El render revisa cada lámina por su cuenta: que nada invada el pie, que ningún
texto se salga de su caja, que las frases quepan en un renglón y que las
ilustraciones no pasen de su columna. Si algo no cabe, lo avisa por pantalla y
termina con error. **La regla es acortar el texto, nunca achicar la tipografía.**

### Cambiar los logos

Los logos que vienen ahora son un provisorio hecho con el sello de La Fiore
Studio. Cuando tengas el sello de **Academy**, guárdalo en `assets/` con estos
nombres exactos y vuelve a renderizar:

- `logo_verde.png` — sello en verde sobre fondo transparente (va en los pies)
- `logo_blanco.png` — el mismo sello en blanco sobre transparente (va en portadas)

PNG con transparencia real, cuadrado o casi, mínimo 600 px de lado.

---

## 3. Publicar en Instagram

### 3.1 Lo que necesitas tener (una sola vez)

**a) Cuenta profesional vinculada a una página de Facebook**

1. En Instagram: *Configuración → Cuenta → Cambiar a cuenta profesional*.
2. Crea o elige una página de Facebook y vincúlala:
   *Configuración → Centro de cuentas → Cuentas → Añadir la página*.

Sin este vínculo la API no funciona. Es el paso que más se olvida.

**b) Una app en developers.facebook.com**

1. Entra a <https://developers.facebook.com> con la cuenta de Facebook dueña de
   la página, y haz *Mis apps → Crear app*.
2. Tipo de app: **Empresa (Business)**.
3. Añade el producto **Instagram Graph API**.
4. Permisos que hay que pedir:
   `instagram_basic`, `instagram_content_publish`, `pages_show_list`,
   `business_management`.

**c) El token y el `ig_user_id`**

1. Ve al **Explorador de la API Graph**
   (<https://developers.facebook.com/tools/explorer/>).
2. Arriba, elige tu app y pulsa *Generar token de acceso*. Marca los cuatro
   permisos de arriba y acepta.
3. Ese token dura 1 hora. Para conseguir el de 60 días, ejecuta:

   ```bash
   curl -s "https://graph.facebook.com/v23.0/oauth/access_token?grant_type=fb_exchange_token&client_id=TU_APP_ID&client_secret=TU_APP_SECRET&fb_exchange_token=EL_TOKEN_CORTO"
   ```

   El `access_token` que devuelve es el bueno: **guárdalo**.
4. Con ese token, saca el id de la cuenta de Instagram:

   ```bash
   curl -s "https://graph.facebook.com/v23.0/me/accounts?access_token=EL_TOKEN_LARGO"
   ```

   Copia el `id` de tu página y pídele su cuenta de Instagram:

   ```bash
   curl -s "https://graph.facebook.com/v23.0/ID_DE_LA_PAGINA?fields=instagram_business_account&access_token=EL_TOKEN_LARGO"
   ```

   El número que sale en `instagram_business_account` es tu **`IG_USER_ID`**.

**d) Las imágenes en una URL pública**

La API de Meta no acepta archivos: solo URLs que pueda descargar. Lo más simple
es dejar que las sirva el propio repositorio de GitHub. Si el repo es público,
la base es:

```
https://raw.githubusercontent.com/TU_USUARIO/lafiore-academy/main/salida
```

Comprueba que funciona abriendo en el navegador:
`…/salida/set_01/01_portada.jpg`. Si ves la imagen, está listo.

Si prefieres no tener el repo público, sirve la carpeta `salida/` desde
Cloudinary (plan gratuito), S3 o GitHub Pages y usa esa base en su lugar.

### 3.2 Los tres secretos

En el repositorio: *Settings → Secrets and variables → Actions → New repository secret*.

| Nombre | Qué va | Ejemplo |
|---|---|---|
| `IG_USER_ID` | el id de la cuenta de Instagram | `178414…` |
| `IG_ACCESS_TOKEN` | el token de 60 días | `EAAG…` |
| `IG_BASE_URL` | la URL pública de `salida/`, sin barra final | `https://raw.githubusercontent.com/tu-usuario/lafiore-academy/main/salida` |

**Nunca escribas el token dentro de un archivo del repositorio.** Solo en
Secrets.

### 3.3 Probar antes de publicar de verdad

En tu computador, con las variables puestas:

```bash
python publicar.py --verificar
```

Debe responder con el nombre de la cuenta y la cuota usada. Después:

```bash
python publicar.py --dry-run
```

Muestra exactamente qué imágenes y qué caption se enviarían, sin publicar nada.

### 3.4 Publicar

```bash
python publicar.py            # el siguiente set pendiente
python publicar.py --set 3    # forzar el set 03
python publicar.py --estado   # ver qué se publicó y qué falta
```

---

## 4. El cron diario

`.github/workflows/publicar.yml` publica **un set por día a las 12:00 de Chile**.

Como Chile cambia de hora dos veces al año, el cron se lanza a las 15:00 y a
las 16:00 UTC, y el script comprueba la hora real en Santiago: publica en la
ejecución correcta e ignora la otra. No hay que tocar nada en marzo ni en
septiembre.

Al terminar, guarda el resultado en `estado.json` y lo sube al repositorio.
Si algo falla, reintenta con esperas crecientes y, si aun así no lo consigue,
abre un **issue** en el repositorio contando qué pasó.

También puedes lanzarlo a mano desde la pestaña *Actions → Publicar carrusel
del día → Run workflow*, indicando un set concreto o marcando *dry run*.

---

## 5. Mantención

### Renovar el token antes de los 60 días

Ponte un recordatorio para el día 50. El token largo se renueva a partir de
sí mismo:

```bash
curl -s "https://graph.facebook.com/v23.0/oauth/access_token?grant_type=fb_exchange_token&client_id=TU_APP_ID&client_secret=TU_APP_SECRET&fb_exchange_token=EL_TOKEN_ACTUAL"
```

Pega el nuevo valor en el secreto `IG_ACCESS_TOKEN`. Nada más.

### Cambiar o añadir contenido

Todo el copy está en `contenido/sets.py` y los textos de Instagram en
`contenido/captions.py`. Reglas que el propio código verifica:

- La palabra **«oficio» está prohibida** en cualquier lámina.
- Los textos de NO y SÍ: máximo 50 caracteres.
- Cada línea de FRASE: máximo 34 caracteres.

Y la regla que no verifica ningún programa, pero manda: **el contenido hace
crecer al profesional. Nunca se critica a clientas, clientes ni colegas.** Los
«NO» describen prácticas mejorables del profesional, jamás defectos de otras
personas.

Después de editar, vuelve a renderizar y sube los JPG:

```bash
python plantilla/render.py
```

### Límites de Meta

- Máximo **25 publicaciones por API cada 24 horas**. Publicando una al día,
  sobra de lejos; el script igual consulta la cuota antes de subir.
- Un contenedor de carrusel caduca a las 24 horas si no se publica.
- Máximo 10 imágenes por carrusel (aquí van 6).
