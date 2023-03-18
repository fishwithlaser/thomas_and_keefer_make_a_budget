from sqlalchemy.orm import Session
from typing import Iterator
from datetime import datetime
from database.transactions import Transactions
from database.common import engine



def add_ctfs_to_database(csv_iterator: Iterator) -> None:
    #gotta make sure i'm only adding unique
    _map = {
        'ref': 0,
        'date': 1,
        'type': 2,
        'description': 4,
        'category': 5,
        'amount': 6
    }
    csv_iterator.__next__()
    csv_iterator.__next__()
    csv_iterator.__next__()
    transactions: list[Transactions] = []
    while True:
        try:
            row = csv_iterator.__next__()
            transactions += [
                Transactions(
                    Amount = row[_map['amount']],
                    Category = row[_map['category']],
                    Name = row[_map['description']],
                    TransactionDate = datetime.strptime(row[_map['date']], '%Y-%m-%d'),
                    TransactionId = row[_map['ref']],
                )
            ]
        except StopIteration:
            break

    session = Session(engine)
    session.bulk_save_objects(transactions)
    session.commit()
