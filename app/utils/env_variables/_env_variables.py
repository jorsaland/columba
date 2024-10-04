"""
Defines the class that contains all env variables
"""


import os


from app.constants import (
    ENV_PASSWORD,
    ENV_SENDER,
    ENV_SMTP_HOST,
    ENV_SMTP_PORT,
)


class EnvVars:

    """
    Contains all env variables.
    """

    SENDER = os.environ.get(ENV_SENDER)
    PASSWORD = os.environ.get(ENV_PASSWORD)
    SMTP_HOST = os.environ.get(ENV_SMTP_HOST)
    SMTP_PORT = os.environ.get(ENV_SMTP_PORT)