from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

ENGINE_FILENAME = 'budget_database.bd'

Base = declarative_base()
engine = create_engine(f'sqlite:///{ENGINE_FILENAME}', echo=False)