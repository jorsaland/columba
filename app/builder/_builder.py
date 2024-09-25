"""
Defines the app builder.
"""


from flasgger import Swagger
from flask import Flask
from flask_cors import CORS


from app import constants
from app.controller import (
    control_get_events,
    control_post_event,
    control_put_event,
    control_delete_event,
)
import switches


def build_app():

    """
    App builder.
    """

    # Flask app definition
    app = Flask(constants.APP_NAME)
    app.config.update({'JSON_AS_ASCII': not switches.UNICODE_RESPONSES})

    # OpenAPI and Swagger configuration 
    if switches.ALLOW_SWAGGER:
        app.config.update(constants.openapi_version)
        Swagger.DEFAULT_CONFIG.update(constants.swagger_schema)
        Swagger(app=app)

    # CORS configuration
    CORS(app, resources=constants.cors_resources)

    # Endpoints configuration
    app.add_url_rule(methods=['GET'],    view_func=control_get_events,   rule='/events')
    app.add_url_rule(methods=['POST'],   view_func=control_post_event,   rule='/event')
    app.add_url_rule(methods=['PUT'],    view_func=control_put_event,    rule='/event/<string:event_id>')
    app.add_url_rule(methods=['DELETE'], view_func=control_delete_event, rule='/event/<string:event_id>')

    return app