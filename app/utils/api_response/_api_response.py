"""
Defines the class that represents app responses.
"""


from flask import jsonify


import json
from typing import Any


from app.response_messages import admin_message_not_jsonifyable_response
from app.utils.exceptions import DevelopmentError


class APIResponse:


    """
    Represents app responses.
    """


    def __init__(self, *, code: int, message = '', data: Any = None):

        # Validate data

        try:
            json.dumps(data)
        except TypeError:
            raise DevelopmentError(admin_message_not_jsonifyable_response)
        
        # Asignaciones

        self._code = code
        self._message = message
        self._data = data


    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message

    @property
    def data(self):
        return self._data
    
    @property
    def response_dict(self):
        return {
            'data': self.data,
            'message': self.message,
        }


    def get_flask_response(self):
        
        """
        Converts the API response to the format required by Flask.
        """
        
        return jsonify(self.response_dict), self.code