"""
Defines the function that validates no env variables are missing.
"""


from app.internal_messages import admin_message_missing_env_vars
from app.utils.exceptions import DevelopmentError


from ._env_variables import EnvVars


def check_env_vars():

    """
    Validates no env variables are missing.
    """

    missing_env_vars: list[str] = []
    for var, value in vars(EnvVars).items():
        if var.startswith('_'):
            continue
        if value is None:
            missing_env_vars.append(var)

    if missing_env_vars:
        error_message = admin_message_missing_env_vars.format(env_vars=', '.join(missing_env_vars))
        raise DevelopmentError(error_message)