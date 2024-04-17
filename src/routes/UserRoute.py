from flask import Blueprint, request, jsonify
from src.models.UsuarioModel import UsuarioModel
from src.utils.Logger import Logger

user_bp = Blueprint('user', __name__)

@user_bp.route('/registrar', methods=['POST'])
def registrar():
    Logger.add_to_log("info", "Se ejecuta el endpoint de /registrar")
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))

    data = request.json

    campos_requeridos = ['admin', 'email', 'nombre', 'apellido', 'documento', 'password']
    for campo in campos_requeridos:
        if campo not in data:
            return jsonify({'code': 400, 'mensaje': f'El campo {campo} es requerido'}), 400

    admin = data['admin']
    email = data['email']
    nombre = data['nombre']
    apellido = data['apellido']
    documento = data['documento']
    password = data['password']


@user_bp.route('/usuarios')
def getUsuarios():
    Logger.add_to_log("info", "Se ejecuta el endpoint de /usuarios")
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    try:
        usuario_model = UsuarioModel()
        usuarios = usuario_model.getUsuarios()
        return jsonify({'code': 200, 'mensaje': 'Usuarios obtenidos correctamente', 'data': usuarios})
    except Exception as ex:
        return jsonify({'code': 500, 'message': str(ex)}), 500
    
@user_bp.route('/usuario/<id>')
def getUsuario(id):
    Logger.add_to_log("info", "Se ejecuta el endpoint de /usuario/id")
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    try:
        usuario_model = UsuarioModel()
        usuario = usuario_model.getUsuario(id)
        if usuario == None:
            return jsonify({'code': 404, 'mensaje': f'No se encontró un usuario con el id {id}'})
        
        return jsonify({'code': 200, 'mensaje': 'Usuario obtenido correctamente', 'data': usuario})
    except Exception as ex:
        return jsonify({'code': 500, 'message': str(ex)}), 500
    
@user_bp.route('/login', methods=['POST'])
def login():
    Logger.add_to_log("info", "Se ejecuta el endpoint de /login")
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    
    data = request.json
    
    documento = data['documento']
    password = data['password']