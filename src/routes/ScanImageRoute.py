from flask import Blueprint, request, jsonify
from src.utils.Logger import Logger
from src.services.ScanImagenService import ScanImageService

pneumonia_bp = Blueprint('pneumonia', __name__)

@pneumonia_bp.route('/procesar', methods=['POST'])
def procesar():
    Logger.add_to_log("info", "Se ejecuta el endpoint de /procesar")
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    
    if 'imagen' not in request.files or 'documento' not in request.form:
        return jsonify({'mensaje': 'Falta la imagen o el número de documento'}), 400
    
    imagen = request.files['imagen']
    numero_documento = request.form['documento']
    
    statistic, label, recomendacion = ScanImageService.image_prediction(imagen)
    
    results = {
        'mensaje': f'Imagen procesada correctamente',
        'data': {
            'porcentaje': statistic,
            'mensaje': label,
            'recomendacion': recomendacion,
        }
    }
    
    return jsonify(results), 200
