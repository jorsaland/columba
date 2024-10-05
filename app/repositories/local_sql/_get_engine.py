"""
Defines the function that gets the SQL engine. 
"""


from sqlalchemy import create_engine


def get_engine():

    """
    Gets the SQL engine.
    """

    return create_engine('sqlite:///local_database.db')