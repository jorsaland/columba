"""
Defines the function that sends a mail.
"""


import smtplib
import ssl


from app.utils.env_variables import EnvVars


def send_mail(message: str):

    """
    Sends a mail.
    """

    context = ssl.create_default_context()
    host = EnvVars.SMTP_HOST
    port = int(EnvVars.SMTP_PORT)

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(EnvVars.SENDER, EnvVars.PASSWORD)
        server.sendmail(EnvVars.SENDER, EnvVars.SENDER, message)
