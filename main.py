"""
Columba 0.4
https://github.com/jorsaland/columba

A back-end Web app capable of scheduling emails.

In version 0.4, an email delivery system is implemented.

----------------------------------------------------------------------

Please, run both this script and messenger.py
"""


from app.builder import build_app
from app.repositories.local_sql import configure_database


def main():

    """
    Runs the events scheduler.
    """

    configure_database()
    app = build_app()
    app.run(use_reloader=True)


if __name__ == '__main__':
    main()