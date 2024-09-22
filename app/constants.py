"""
Defines the app constants.
"""


DATABASE_SKETCH_PATH = 'local_database.csv'
LOGGER_SKETCH_PATH = 'local_events.log'

valid_time_units = [
    MINUTES := 'm',
    HOURS := 'h',
    DAYS := 'd',
]

ordered_fields = [
    FIELD_NAME_FIRST_RUNTIME := 'first_runtime',
    FIELD_NAME_NEXT_RUNTIME := 'next_runtime',
    FIELD_NAME_MESSAGE := 'message',
    FIELD_NAME_PERIOD := 'period',
]