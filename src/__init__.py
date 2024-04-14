from flask import Flask

# Routes
from .routes import IndexRoute, ScanImageRoute

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(IndexRoute.index_bp, url_prefix='/')
    app.register_blueprint(ScanImageRoute.pneumonia_bp, url_prefix='/pneumonia')

    return app