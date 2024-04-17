from config import config
from src import init_app

configuration = config['development']
app = init_app(configuration)

def pageNotFound(error):
    return "<h1>Page not found</h1>", 404

if __name__ == '__main__':    
    app.register_error_handler(404, pageNotFound)
    app.run(host='0.0.0.0')