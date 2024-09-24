"""
Defines the app builder.
"""


from flasgger import Swagger
from flask import Flask
from flask_cors import CORS


from app import constants
from app.controller import (
    control_post_event,
    control_get_events,
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
    app.add_url_rule(methods=['POST'],   rule='/event',  view_func=control_post_event)
    app.add_url_rule(methods=['GET'],    rule='/events', view_func=control_get_events)
    app.add_url_rule(methods=['DELETE'], rule='/event/<string:event_id>',  view_func=control_delete_event)

    return app