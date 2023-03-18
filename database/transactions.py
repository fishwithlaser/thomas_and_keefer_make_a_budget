from datetime import date
from decimal import Decimal
from sqlalchemy.types import String, Date, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .frequencies import Recursion 
from .common import Base
from common.stupid import lstr

class Transactions(Base):

    def __repr__(self) -> str:
        return f'{lstr(self.Name, 10)} - {lstr(self.Amount)} - {lstr(self.Category)}'

    __tablename__ = 'transactions'
    Id: Mapped[int] = mapped_column(primary_key=True)
    TransactionId: Mapped[str] = mapped_column(String)
    Name: Mapped[str] = mapped_column(String)
    Amount: Mapped[Decimal] = mapped_column(DECIMAL)
    Recursion: Mapped[str] = mapped_column(ForeignKey(Recursion.Name), nullable=True, default=None)
    Description: Mapped[str] = mapped_column(String, nullable=True)
    TransactionDate: Mapped[date] = mapped_column(Date)
    Category: Mapped[str or None] = mapped_column(String, nullable=True)

