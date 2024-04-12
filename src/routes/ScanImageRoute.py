from flask import Flask, request, jsonify

from src.utils.Logger import Logger

app = Flask(__name__)

@app.route('/procesar', methods=['POST'])
def procesar():
    Logger.add_to_log("info", "Se procesa la imagen")
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    if 'imagen' not in request.files or 'documento' not in request.form:
        return jsonify({'mensaje': 'Falta la imagen o el número de documento'}), 400
    
    imagen = request.files['imagen']
    numero_documento = request.form['documento']
    
    return jsonify({'mensaje': f'Número de documento: {numero_documento}, imagen recibida'}), 200

