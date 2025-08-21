from datetime import datetime


from flask import Flask, request, jsonify, render_template


app = Flask(__name__)



#Ruta verificar funcionamiento correcto de la API
@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'API en funcionamiento'}), 200



@app.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True, port=2000)