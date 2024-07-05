from flask import Flask
from flask_cors import CORS

# Routes
from .routes import IndexRoutes, EventosRoutes

app = Flask(__name__) 
CORS(app, resources={r"/eventos/*": {"origins": "http://localhost:3000"}})

def init_app(config):
    # Configuration
    app.config.from_object(config)
    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(EventosRoutes.main, url_prefix='/eventos')

    return app