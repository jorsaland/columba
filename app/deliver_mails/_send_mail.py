"""
Defines the function that sends an email.
"""


import smtplib
import ssl


from app.utils.env_variables import EnvVars


from ._build_multipart import build_multipart


def send_mail(
    *,
    sender_name: (str|None) = None,
    subject: (str|None) = None,
    message: (str|None) = None,
    is_html: (bool|None) = None,
):

    """
    Sends an email.
    """

    multipart = build_multipart(
        sender_name = sender_name,
        subject = subject,
        is_html = is_html,
        message = message,
    )

    context = ssl.create_default_context()
    host = EnvVars.SMTP_HOST
    port = int(EnvVars.SMTP_PORT)

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(EnvVars.SENDER, EnvVars.PASSWORD)
        server.sendmail(EnvVars.SENDER, EnvVars.SENDER, multipart)