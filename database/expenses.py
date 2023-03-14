from datetime import date
from decimal import Decimal
from sqlalchemy.types import String, Date, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .common import Base

class Expenses(Base):

    __tablename__ = 'expenses'
    Id: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String)
    Amount: Mapped[Decimal] = mapped_column(DECIMAL)
    Recursion: Mapped[str] = mapped_column(ForeignKey("recursion.Name"), nullable=False)
    Description: Mapped[str] = mapped_column(String)
    TransactionDate: Mapped[date] = mapped_column(Date)   

