"""
Defines the error that catches invalid requests.
"""


from app.internal_messages import response_message_undefined_error


class ValidationError(Exception):

    """
    Catches invalid requests. It takes a HTTP status code and a message as input.
    """

    def __init__(self, *, code=500, message=response_message_undefined_error):
        self.args: tuple[int, str]
        super().__init__(code, message)