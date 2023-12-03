"""ezbudget Flask application package initializer"""
from flask import Flask
from .api.views import api as api_blueprint
from .ui.views import ui as ui_blueprint

def create_app(config_filename):
    """Create ezbudget app instance"""
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(ui_blueprint)

    return app
