# Popeyes Brand Kit — Sistema de Pedidos (CS2032)
## Mantiene el Integrante 4 · lo consumen Integrante 1 (app Cliente) e Integrante 2 (app Trabajadores)

Kit compartido para que las dos web apps se vean consistentes y parecidas
a la referencia (popeyes.com.pe), como pide la rúbrica.

## Archivos
- `tokens.css` — variables de color, tipografía, espaciado (cárgalo primero).
- `tokens.json` — los mismos tokens para apps JS (React/Vue).
- `popeyes-kit.css` — componentes: botones, header, cards, pills de estado, tabla.
- `catalogo.json` — productos con precios referenciales y keys de imágenes en S3.
- `demo.html` — guía viva: ábrela en el navegador para ver todo aplicado.

## Cómo usar
En el `<head>` de cada app:
```html
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="popeyes-kit.css">
```
Y en el `<body>`:
```html
<body class="pp-app"> ... </body>
```
Las fuentes (Fredoka + Nunito Sans) ya se importan desde `tokens.css`.
Para componentes, usa las clases con prefijo `pp-` (ver `demo.html`).
En React/Vue, importa `tokens.json` si prefieres tokens en JS.

## Estados del pedido → pills (úsenlos los 2 frontends + dashboard)
Para que el estado se vea IGUAL en toda la app, usen estas clases según el
estado que viene del backend (`estadosPedido` del shared-config):

| Estado backend | Clase de pill            | Texto         |
|----------------|--------------------------|---------------|
| `RECIBIDO`     | `pp-pill pp-pill--recibido`  | Recibido  |
| `EN_COCINA`    | `pp-pill pp-pill--cocina`    | En cocina |
| `EN_DESPACHO`  | `pp-pill pp-pill--despacho`  | En despacho |
| `EN_REPARTO`   | `pp-pill pp-pill--reparto`   | En reparto |
| `ENTREGADO`    | `pp-pill pp-pill--entregado` | Entregado |

## Imágenes y logo en S3
1. Crear un bucket de assets, ej. `pp-assets-<cuenta>`.
2. Subir bajo `productos/` las imágenes que referencia `catalogo.json`
   (mismos nombres de key) y el logo bajo `marca/`.
3. Servirlas públicas (o vía CloudFront). En la app, la URL queda:
   `https://<bucket>.s3.amazonaws.com/productos/combo-2-presas.jpg`
4. Pon la URL base del bucket en la config de cada frontend (variable de
   entorno), no hardcodeada.

## Nota de marca (importante)
- La paleta usa los colores oficiales de Popeyes (son datos públicos).
- Este kit trae un **logo placeholder** (el círculo naranja con 🍗). No incluye
  el logo ni las fotos oficiales por ser material con derechos. Para el trabajo
  académico, suban ustedes los assets oficiales a S3 desde la referencia y
  reemplacen el placeholder; úsenlos solo con fines educativos del curso.
- Los nombres y precios del catálogo son **referenciales**.

## Previsualizar
Abre `demo.html` en el navegador (doble clic). Verás header, hero, catálogo,
pills de estado, vista de trabajadores y botones, todo con la marca aplicada.
