from sqlalchemy_utils import database_exists, create_database
from .common import engine, Base

def create_database() -> None:
    if not database_exists(engine.url):
        create_database(engine.url)
    ##todo create tables here..


if __name__ == "__main__":
    create_database()
    from .expenses import Expenses
    Base.metadata.create_all(engine)
    #frequencies.populate_recursion()
