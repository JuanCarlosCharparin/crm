from pydoc import text
from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

conection_string = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Juanki3031$$",
    database="crm"
)

cursor = conection_string.cursor()





@app.route("/")
def index():
    cursor.execute("SELECT * FROM locales")
    rows = cursor.fetchall()
    return render_template("index.html", rows=rows)

@app.route("/ping")
def ping():
    try:
        cursor.execute("SELECT * FROM locales")
        rows = cursor.fetchall()
        return '<br>'.join(str(row) for row in rows)
    except Exception as e:
        return f"Error: {str(e)}"



if __name__ == "__main__":
    app.run(debug=True, port=2000)