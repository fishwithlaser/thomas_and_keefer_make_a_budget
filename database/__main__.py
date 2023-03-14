from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import IntegrityError
from .main import engine, Base

def create_database() -> None:

    if not database_exists(engine.url):
        create_database(engine.url)
    

if __name__ == "__main__":
    create_database()
    from . import frequencies
    from . import expenses
    
    expenses.Expenses
    Base.metadata.create_all(engine)

    #dear thomas (thomas); i should check to see if one exists not try and fail
    try:
        frequencies.populate_recursion()
    except IntegrityError:
        pass