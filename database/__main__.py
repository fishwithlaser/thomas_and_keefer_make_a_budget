from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import IntegrityError
from .common import engine, Base, ENGINE_FILENAME


def init_database() -> None:
    if not database_exists(engine.url):
        create_database(engine.url)

def remove_db_exists() -> None:
    try:
        remove(ENGINE_FILENAME)
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    import sys
    from os import remove

    if 'replace' in sys.argv:
        remove_db_exists()

    init_database()
    from . import frequencies
    from . import expenses
    from . import transactions

    expenses.Expenses
    transactions.Transactions
    Base.metadata.create_all(engine)

    #dear thomas (thomas); i should check to see if one exists not try and fail
    try:
        frequencies.populate_recursion()
    except IntegrityError:
        pass