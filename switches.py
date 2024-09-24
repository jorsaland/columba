"""
Define los interruptores (valores booleanos) para encender o apagar funcionalidades.
"""


DEFAULT_ACTIVE = True
# True  --> Events are created active by default
# False --> Events are created paused by default

REJECT_INVALID_QUERY_PARAMS = True
# True  --> Respond with error if there are invalid query params in a GET request 
# False --> Just leave a log if there are invalid query params in a GET request

UNICODE_RESPONSES = True
# True  --> All Unicode characters are used in Flask responses
# False --> Only ASCII characters are used in Flask responses

EXPLICIT_ERROR_RESPONSES = True
# True  --> The API error responses are explicit
# False --> The same standard error message is shown in API responses

ALLOW_SWAGGER = True
# True  --> Enable Swagger API
# False --> Disable Swagger API