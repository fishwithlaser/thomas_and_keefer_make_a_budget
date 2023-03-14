from sqlalchemy.types import String, REAL
from sqlalchemy.orm import mapped_column, Mapped, Session

from .common import Base

class Recursion(Base):

    __tablename__ = 'recursion'

    Name: Mapped[str] = mapped_column(String, primary_key=True)
    FrequencyMonthly: Mapped[float] = mapped_column(REAL)


RECURSION_FREQUENCIES: tuple[str, float] = [
    ('daily', 30),
    ('monthly', 1),
    ('semi-monthly', 2),
    ('biweekly', 26 / 12 ),
]

def populate_recursion() -> None:
    from database.main import engine
    session = Session(engine)
    for name_frequency_tuple in RECURSION_FREQUENCIES:
        name, frequency = name_frequency_tuple
        session.add(Recursion(Name = name, FrequencyMonthly = frequency))
    session.commit()
    session.close()

if __name__ == "__main__":
    print('started')
    populate_recursion()
    print('finished')