"""
Defines the app constants.
"""


# Flask constants

APP_NAME = 'columba'


# Logic constants

LOGGER_SKETCH_PATH = 'local_events.log'


# Database constants

TABLE_NAME_EVENTS = 'Events'

ordered_fields = [

    FIELD_EVENT_ID := 'event_id',
    FIELD_STATE := 'state',
    FIELD_COUNTS := 'counts',

    FIELD_RUNTIME := 'runtime',
    FIELD_PERIOD := 'period',

    FIELD_SENDER_NAME := 'sender_name',
    FIELD_SUBJECT := 'subject',
    FIELD_IS_HTML := 'is_html',
    FIELD_MESSAGE := 'message',
]


# Request constants

valid_query_params = [
    FIELD_EVENT_ID,
    FIELD_STATE,
    FIELD_RUNTIME,
    FIELD_PERIOD,
    FIELD_SENDER_NAME,
    FIELD_SUBJECT,
]

creation_request_valid_fields = [
    FIELD_STATE,
    FIELD_RUNTIME,
    FIELD_PERIOD,
    FIELD_SENDER_NAME,
    FIELD_SUBJECT,
    FIELD_IS_HTML,
    FIELD_MESSAGE,
]

creation_request_mandatory_fields = [
    FIELD_RUNTIME,
]

update_request_valid_fields = [
    FIELD_STATE,
    FIELD_RUNTIME,
    FIELD_PERIOD,
    FIELD_SENDER_NAME,
    FIELD_SUBJECT,
    FIELD_IS_HTML,
    FIELD_MESSAGE,
]

valid_states = [
    ACTIVE := 'active',
    PAUSED := 'paused',
]

valid_period_units = [
    MINUTES := 'm',
    HOURS := 'h',
    DAYS := 'd',
]

json_valid_types: tuple[type, ...] = (str, int, float, bool, list, dict, type(None))


# OpenAPI and Swagger constants

SWAGGER_FILENAME = 'swag.yaml'

openapi_version = {'SWAGGER': {'openapi': '3.0.3'}}
swagger_schema = {'components': {'securitySchemes': {'Bearer': {
    'type': 'http',
    'scheme': 'bearer',
    'bearerFormat': 'JWT'
}}}}


# CORS constants

cors_resources = {'/*': {'origins': '*'}}


# Environment variables

ENV_SENDER = 'COLUMBA_SENDER'
ENV_PASSWORD = 'COLUMBA_PASSWORD'
ENV_SMTP_HOST = 'COLUMBA_SMTP_HOST'
ENV_SMTP_PORT = 'COLUMBA_SMTP_PORT'


# Logger constants

LOGGER_NAME = 'COLUMBA'
LOGGER_LEVEL = 'DEBUG'
LOGGER_FORMAT = '{asctime} {name} {levelname}: {message}'
LOG_FILE_NAME = 'messenger.log'