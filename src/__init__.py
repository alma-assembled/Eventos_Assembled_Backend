from flask import Flask
from flask_cors import CORS
#from flask_socketio import SocketIO

# Routes
from .routes import IndexRoutes, EventosRoutes

app = Flask(__name__) 
#CORS(app, resources={r"/eventos/*": {"origins": "http://172.29.224.1:3000"}})
#CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://172.29.224.1:3000"]}})
CORS(app)
#socketio = SocketIO(app)

def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(EventosRoutes.main, url_prefix='/eventos')
    app.run(host='0.0.0.0', port=5000, debug=True)
    # Iniciar la app con SocketIO
#    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    return app