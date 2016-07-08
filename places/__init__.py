from os.path import dirname

from flask_api_app import FlaskApiApp
from flask_config_helper import Config

from places.blueprint import api

config = Config()


def create_app_min(config_name):
    app = FlaskApiApp(__name__)
    config.init_app(app)
    app.config.from_yaml(
        config_name=config_name,
        file_name='app.yml',
        search_paths=[dirname(app.root_path)]
    )

    return app


def create_app(config_name):
    app = create_app_min(config_name)
    app.init_extensions()

    # register api routes
    import places.modules.places.api

    # register admin routes
    import places.modules.places.admin

    app.register_core_blueprint(api=api, api_url_prefix='/api/v1.0')

    return app
