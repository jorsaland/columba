"""
Defines the function that generates a unique ID.
"""


from uuid import uuid1


def generate_id():

    """
    Generates a unique ID.
    """

    return str(uuid1())