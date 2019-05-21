from app_factory import create_app
from flask import g
import os

app = create_app()

rest_model_mapping = {}

from routes import *
from lumavate_service_util import icon_blueprint, lumavate_blueprint
app.register_blueprint(lumavate_blueprint)
app.register_blueprint(icon_blueprint)

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")
