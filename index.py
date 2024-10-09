from config import config
from flask_cors import CORS
from src import init_app

configuration = config['development']
app = init_app(configuration)

CORS(app)

def pageNotFound(error):
    return "<h1>Page not found</h1>", 404

if __name__ == '__main__':    
    app.register_error_handler(404, pageNotFound)
    app.run(host='0.0.0.0', port=5000)