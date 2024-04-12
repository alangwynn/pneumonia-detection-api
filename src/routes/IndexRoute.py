from flask import Flask, jsonify, request

import traceback

app = Flask(__name__)

from src.utils.Logger import Logger

@app.route('/')
def index():
    try:
        Logger.add_to_log("info", "{} {}".format(request.method, request.path))
        return "Ok"
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        response = jsonify({'message': 'Internal server error', 'success': False})
        return response, 500
