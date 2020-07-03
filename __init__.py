from flask import Flask

from .api.routes import api
from .site.routes import site
from .admin.routes import admin


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(site)
    app.register_blueprint(admin)
    print(app.url_map)
    return app
