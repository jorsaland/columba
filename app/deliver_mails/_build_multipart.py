"""
Defines the function that builds the MIME multipart.
"""


from email import header
from email.mime import multipart, text


from app.utils.env_variables import EnvVars


def build_multipart(
    *,
    sender_name: (str|None) = None,
    subject: (str|None) = None,
    is_html: (bool|None) = None,
    message: (str|None) = None,
):

    """
    Builds the MIME multipart.
    """

    # Mode

    if is_html is None:
        is_html = False

    if is_html:
        mode = 'html'
    else:
        mode = 'plain'

    # Main part

    main_part = multipart.MIMEMultipart('mixed')

    main_part.add_header('To', EnvVars.SENDER)
    if sender_name is not None:
        main_part.add_header('From', header.Header(sender_name, 'utf-8').encode())
    if subject:
        main_part.add_header('Subject', subject)

    # Body part

    if message is not None:
        text_part = text.MIMEText(message, mode, 'utf-8')
        body_part = multipart.MIMEMultipart('alternative')
        body_part.attach(text_part)
        main_part.attach(body_part)

    return main_part.as_string()