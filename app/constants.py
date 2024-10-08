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
    FIELD_NAME_EVENT_ID := 'event_id',
    FIELD_NAME_STATE := 'state',
    FIELD_NAME_FIRST_RUNTIME := 'first_runtime',
    FIELD_NAME_NEXT_RUNTIME := 'next_runtime',
    FIELD_NAME_MESSAGE := 'message',
    FIELD_NAME_PERIOD := 'period',
]


# Request constants

IO_FIELD_EVENT_ID = 'event_id'
IO_FIELD_MESSAGE = 'message'
IO_FIELD_STATE = 'state'
IO_FIELD_PERIOD = 'period'
IO_FIELD_RUNTIME = 'runtime'
IO_FIELD_FIRST_RUNTIME = 'first_runtime'
IO_FIELD_NEXT_RUNTIME = 'next_runtime'

valid_query_params = [
    IO_FIELD_EVENT_ID,
    IO_FIELD_STATE,
    IO_FIELD_FIRST_RUNTIME,
    IO_FIELD_NEXT_RUNTIME,
    IO_FIELD_PERIOD,
]

creation_request_valid_fields = [
    IO_FIELD_MESSAGE,
    IO_FIELD_STATE,
    IO_FIELD_PERIOD,
    IO_FIELD_RUNTIME,
]

creation_request_mandatory_fields = [
    IO_FIELD_MESSAGE,
    IO_FIELD_RUNTIME,
]

update_request_valid_fields = [
    IO_FIELD_MESSAGE,
    IO_FIELD_STATE,
    IO_FIELD_PERIOD,
    IO_FIELD_NEXT_RUNTIME,
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