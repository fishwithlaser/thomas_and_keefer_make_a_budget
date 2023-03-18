from database.common import engine
from database.transactions import Transactions
from datetime import datetime, date
from json import loads
from sqlalchemy.orm import Session

from decimal import Decimal

# the json from RBC will have this 
def add_rbc_to_database(filename:str ) -> str:
    json_file = open(filename, 'r')
    web_list: dict = loads(json_file.read())
    transaction_list: list[dict] = web_list['transactionList']
    transactions: list[Transactions] = []
    session = Session(engine)
    for entry in transaction_list: 
        date_str:str = entry['bookingDate']
        datetime_: date = datetime.strptime(date_str, '%Y-%m-%d')
        date_ = datetime_.date()
        amount: Decimal = Decimal(entry['amount'])
        transaction = Transactions()
        transaction.Amount =  amount
        transaction.TransactionDate = date_
        transaction.Name = ' '.join(entry['description'])
        transaction.TransactionId = entry['id']
        transaction.Category = "Chequing"
        transactions += [transaction]
    session = Session(engine)
    session.bulk_save_objects(transactions)
    session.commit()

if __name__ == "__main__":
    filename = 'inputs/rbc_chequing.json'
    add_rbc_to_database(filename)