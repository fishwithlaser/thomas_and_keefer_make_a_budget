from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
import sqlite3

Base = declarative_base()
engine = create_engine('sqlite:///budget_database.bd', echo=False)

def create_database() -> None:
    if not database_exists(engine.url):
        create_database(engine.url)
    ##todo create tables here...
    

if __name__ == "__main__":
    create_database()
    frequencies.populate_recursion()
