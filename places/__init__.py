from os.path import dirname

from flask import url_for
from flask.ext.swagger_ui import SwaggerUI
from flask_api_app import FlaskApiApp
from flask_config_helper import Config

from places.blueprint import api
from places.extensions import swagger_ui
from places.swagger import get_swagger_spec

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

    swagger_ui.init_app(app, spec=get_swagger_spec(), params={
        'OAUTH_CLIENT_ID': 'swagger',
        'OAUTH_CLIENT_SECRET': 'secret'
    })

    @api.before_app_first_request
    def api_before_app_first_request():
        SwaggerUI().spec["securityDefinitions"]["oauth"]["authorizationUrl"] = url_for('api.user_authorize', _external=True)
        SwaggerUI().spec['info']['description'] = SwaggerUI().spec['info']['description'].replace(
            '{{OAUTH_AUTHORIZE_URL}}',
            url_for('api.user_access_token', _external=True)
        )

    # register api routes
    import places.modules.places.api

    # register admin routes
    import places.modules.places.admin

    app.register_core_blueprint(api=api, api_url_prefix='/api/v1.0')

    return app
