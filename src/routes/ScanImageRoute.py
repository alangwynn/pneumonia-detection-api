from flask import Blueprint, request, jsonify
from src.utils.Logger import Logger
from src.services.ScanImagenService import ScanImageService
from src.models.RadiografiaModel import Radiografia

pneumonia_bp = Blueprint('pneumonia', __name__)

@pneumonia_bp.route('/procesar', methods=['POST'])
def procesar():
    Logger.add_to_log("info", "Se ejecuta el endpoint de /procesar")
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    
    if 'imagen' not in request.files or 'documento' not in request.form:
        return jsonify({'mensaje': 'Falta la imagen o el número de documento'}), 400
    
    imagen = request.files['imagen']
    numero_documento = request.form['documento']
    userId = request.form['userId']
    
    statistic, label, recomendacion = ScanImageService.image_prediction(imagen)
    
    statistic_string = "{:.2f}".format(statistic)
    statistic_string = str(round(statistic, 2))
    
    response = Radiografia.loadRadiography(numero_documento, True if label == 'Paciente con neumonía' else False, userId)
    print(response)

    results = {
        'code': 200,
        'mensaje': f'Imagen procesada correctamente',
        'data': {
            'porcentaje': statistic_string,
            'mensaje': label,
            'recomendacion': recomendacion,
        }
    }
    
    return jsonify(results), 200
