from . import Base
from datetime import date
from decimal import Decimal
from sqlalchemy import Column
from sqlalchemy.types import Float, String, Date, Decimal

class Expenses(Base):

    __tablename__ = 'expenses'

    Id: mapped_column[int] = Mapped(primary_key=True)
    Amount: mapped_column[Decimal] = Mapped(Decimal)
    Recursion: mapped_column[str] = Mapped(ForeignKey("recursion.name"), nullable=False)
    Description: mapped_column[str] = Mapped(String)
    TransactionDate: mapped_column[date] = Mapped(Date)   

