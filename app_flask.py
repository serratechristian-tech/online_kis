from flask import Flask

app = Flask(__name__)

productos = [
    {
        "nombre": "Remera taller L",
        "precio": "$12.500",
        "descripcion": "Remera 100% algodón premium."
    },
    {
        "nombre": "Buzo KIS MANDA",
        "precio": "$28.000",
        "descripcion": "Buzo frizado de invierno."
    },
    {
        "nombre": "Gorra KIS MANDA",
        "precio": "$9.500",
        "descripcion": "Gorra urbana edición limitada."
    }
]

@app.route("/")
def inicio():

    html = f"""
<!DOCTYPE html>
<html>

<head>

<title>TiendaEquis</title>

<style>

/* ========================= */
/* ESTILO GENERAL            */
/* ========================= */

body{{
    margin:0;
    font-family:Arial;
    background:#e6e6e6;
    display:flex;
}}

/* ========================= */
/* MENU CONFIGURADOR         */
/* ========================= */

.sidebar{{
    width:260px;
    background:#111;
    color:white;
    min-height:100vh;
    padding:20px;
}}

.sidebar h2{{
    text-align:center;
    border-bottom:1px solid #444;
    padding-bottom:10px;
}}

.sidebar ul{{
    list-style:none;
    padding:0;
}}

.sidebar li{{
    background:#1f1f1f;
    margin-bottom:8px;
    padding:12px;
    border-radius:8px;
    cursor:pointer;
}}

.sidebar li:hover{{
    background:#333;
}}

/* ========================= */
/* CONTENIDO PRINCIPAL       */
/* ========================= */

.contenido{{
    flex:1;
}}

/* ========================= */
/* BARRA SUPERIOR            */
/* ========================= */

header{{
    background:white;
    padding:15px 25px;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
}}

.marca{{
    font-size:14px;
    font-weight:bold;
    color:#777;
}}

/* ========================= */
/* PORTADA                   */
/* ========================= */

.hero{{
    background:#222;
    color:white;
    text-align:center;
    padding:50px;
}}

.hero h1{{
    font-size:40px;
    margin-bottom:10px;
}}

.hero p{{
    color:#ccc;
}}

/* ========================= */
/* PRODUCTOS                 */
/* ========================= */

.productos{{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    padding:20px;
}}

.card{{
    background:white;
    width:280px;
    margin:15px;
    padding:15px;
    border-radius:12px;
    box-shadow:0 0 15px rgba(0,0,0,0.15);

    transition:0.3s;
}}

.card:hover{{
    transform:translateY(-5px);
}}

.foto{{
    height:180px;
    background:#d9d9d9;
    border-radius:10px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:60px;
}}

.precio{{
    color:#008000;
    font-size:24px;
    font-weight:bold;
}}

button{{
    width:100%;
    padding:12px;
    background:black;
    color:white;
    border:none;
    border-radius:8px;
    cursor:pointer;
}}

button:hover{{
    background:#333;
}}

</style>

</head>

<body>

<!-- ========================= -->
<!-- MENU LATERAL CONFIGURADOR -->
<!-- ========================= -->

<div class="sidebar">

<h2>⚙ CONFIGURADOR</h2>

<ul>

<li>🏪 Agregar nombre de tienda</li>

<li>🖼 Cambiar logo</li>

<li>➕ Agregar artículo</li>

<li>✏ Editar artículo</li>

<li>🗑 Eliminar artículo</li>

<li>📂 Categorías</li>

<li>💳 Opciones de pago</li>

<li>🚚 Métodos de envío</li>

<li>📱 Redes sociales</li>

<li>📞 Contactenos</li>

<li>⭐ Productos destacados</li>

<li>🎨 Colores de la tienda</li>

<li>🧾 Cupones de descuento</li>

<li>📊 Ver pedidos</li>

<li>👤 Usuarios</li>

<li>⚙ Configuración general</li>

</ul>

</div>

<!-- ========================= -->
<!-- CONTENIDO PRINCIPAL       -->
<!-- ========================= -->

<div class="contenido">

<header>

<span class="marca">
TIENDAEQUIS | Constructor de Tiendas Online
</span>

</header>

<!-- ========================= -->
<!-- PORTADA PRINCIPAL         -->
<!-- ========================= -->

<section class="hero">

<h1>Mi Tienda</h1>

<p>
Creada con TiendaEquis
</p>

</section>

<!-- ========================= -->
<!-- PRODUCTOS                -->
<!-- ========================= -->

<div class="productos">
"""

    # =========================
    # PRODUCTOS AUTOMATICOS
    # =========================

    for p in productos:

        html += f"""
        <div class="card">

            <div class="foto">
            📦
            </div>

            <h2>{p['nombre']}</h2>

            <p>{p['descripcion']}</p>

            <p class="precio">{p['precio']}</p>

            <button>Comprar</button>

        </div>
        """

    html += """

</div>

</div>

</body>

</html>

"""

    return html







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)