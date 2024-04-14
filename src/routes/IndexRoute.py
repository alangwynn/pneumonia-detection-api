from flask import Blueprint, request, jsonify
from src.utils.Logger import Logger
import traceback

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    try:
        Logger.add_to_log("info", "{} {}".format(request.method, request.path))
        return "Ok"
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        response = jsonify({'message': 'Internal server error', 'success': False})
        return response, 500
