from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker, declarative_base
import sqlite3

from .main import engine

def create_database() -> None:

    if not database_exists(engine.url):
        create_database(engine.url)
    

if __name__ == "__main__":
    create_database()
    from . import frequencies
    frequencies.populate_recursion()
