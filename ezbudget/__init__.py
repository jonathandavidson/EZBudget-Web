from flask import Flask
from .api.views import api as api_blueprint
from .ui.views import ui as ui_blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(ui_blueprint)
