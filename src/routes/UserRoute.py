from flask import Blueprint, request, jsonify
from src.models.UsuarioModel import UsuarioModel
from src.utils.Logger import Logger

user_bp = Blueprint('user', __name__)

@user_bp.route('/crear', methods=['POST'])
def crear_usuario():
    Logger.add_to_log("info", "Se ejecuta el endpoint de /crear")
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    try:
        data = request.json

        campos_requeridos = ['email', 'nombre', 'apellido', 'documento', 'password']
        for campo in campos_requeridos:
            if campo not in data:
                return jsonify({'code': 400, 'mensaje': f'El campo {campo} es requerido'}), 400

        admin = False
        email = data['email']
        nombre = data['nombre']
        apellido = data['apellido']
        documento = data['documento']
        password = data['password']

        UsuarioModel.crearUsuario(admin, email, nombre, apellido, documento, password)
        
        return jsonify({'code': 200, 'mensaje': 'Usuario creado correctamente'}), 200
    except Exception as ex:
        return jsonify({'code': 500, 'mensaje': 'Error al crear el usuario', 'error': str(ex)}), 500


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

    # Verificar si los campos requeridos están presentes en los datos
    campos_requeridos = ['documento', 'password']
    for campo in campos_requeridos:
        if campo not in data:
            return jsonify({'code': 400, 'mensaje': f'El campo {campo} es requerido'}), 400

    documento = data['documento']
    password = data['password']

    # Buscar el usuario en la base de datos por documento y contraseña
    try:
        usuario = UsuarioModel.loginUsuario(documento, password)
        if usuario:
            return jsonify({'code': 200, 'mensaje': 'Inicio de sesión exitoso', 'data': usuario})
        else:
            return jsonify({'code': 401, 'mensaje': 'Documento o contraseña incorrectos'}), 401
    except Exception as ex:
        return jsonify({'code': 500, 'message': str(ex)}), 500

@user_bp.route('/eliminar/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    Logger.add_to_log("info", "Se ejecuta el endpoint de /eliminar")
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    try:
        UsuarioModel.eliminarUsuario(id)
        return jsonify({'code': 200, 'mensaje': 'Usuario eliminado correctamente'}), 200
    except Exception as ex:
        return jsonify({'code': 500, 'mensaje': 'Error al eliminar el usuario', 'error': str(ex)}), 500