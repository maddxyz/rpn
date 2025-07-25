from flask import Flask, jsonify
from flasgger import Swagger
from routes import register_blueprints
from config.swagger_config import SWAGGER_CONFIG

def create_app():
    app = Flask(__name__)

    # Configure Flasgger for Swagger
    app.config['SWAGGER'] = SWAGGER_CONFIG

    Swagger(app)

    @app.route('/ping')
    def ping():
        return jsonify({'message': 'pong'})

    # Register blueprints
    register_blueprints(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)