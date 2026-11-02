from flask import Flask

app = Flask(__name__)

productos = [
    {
        "nombre": "Remera KIS MANDA",
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

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>KIS MANDA</title>

        <style>

        body{
            font-family:Arial;
            background:#f5f5f5;
            margin:0;
        }

        header{
            background:black;
            color:white;
            text-align:center;
            padding:25px;
        }

        .productos{
            display:flex;
            flex-wrap:wrap;
            justify-content:center;
        }

        .card{
            background:white;
            width:300px;
            margin:20px;
            padding:15px;
            border-radius:10px;
            box-shadow:0 0 10px gray;
        }

        .foto{
            height:200px;
            background:#ddd;
            border-radius:10px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:40px;
        }

        .precio{
            color:green;
            font-size:24px;
            font-weight:bold;
        }

        button{
            width:100%;
            padding:12px;
            background:black;
            color:white;
            border:none;
            border-radius:8px;
            cursor:pointer;
        }

        </style>
    </head>

    <body>

    <header>
        <h1>KIS MANDA</h1>
        <p>Moda urbana</p>
    </header>

    <div class="productos">
    """

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

    </body>
    </html>
    """

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)