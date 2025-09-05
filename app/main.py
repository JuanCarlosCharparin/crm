from pydoc import text
from flask import Flask, redirect, request, jsonify, render_template, url_for
import mysql.connector

app = Flask(__name__)

conection_string = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Juanki3031$$",
    database="crm"
)

cursor = conection_string.cursor()

LOCAL_ID = 1

@app.route("/")
def index():
    return render_template("index.html")

#index productos
@app.route("/productos")
def productos():
    cursor = conection_string.cursor()
    cursor.execute(
        """SELECT 
            p.producto_id, 
            p.nombre, 
            c.nombre as categoria, 
            p.precio, 
            p.stock, 
            p.codigo_barras 
        FROM productos p
        inner join categorias c on p.categoria_id = c.categoria_id 
        WHERE p.local_id = %s""", (LOCAL_ID,))
    rows = cursor.fetchall()
    print(rows)
    return render_template("productos.html", productos=rows)

#alta productos
@app.route("/productos/nuevo", methods=["GET", "POST"])
def nuevo_producto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        categoria_id = request.form["categoria_id"]
        precio = request.form["precio"]
        stock = request.form["stock"]
        codigo_barras = request.form["codigo_barras"]
        

        cursor.execute(
            "INSERT INTO productos (local_id, nombre, descripcion, categoria_id, precio, stock, codigo_barras) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (LOCAL_ID, nombre, descripcion, categoria_id, precio, stock, codigo_barras)
        )
        conection_string.commit()
        return redirect(url_for("productos"))
    return render_template("producto_crear.html", producto=None)



if __name__ == "__main__":
    app.run(debug=True, port=2000)