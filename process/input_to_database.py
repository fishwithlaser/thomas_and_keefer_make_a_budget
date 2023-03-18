from typing import Iterator
from os import path, listdir
import csv

from common.stupid import fstr
from process.ctfs import add_ctfs_to_database
from process.rbc import add_rbc_to_database

INPUT_FILE: str = 'inputs'


def guess_account_source(csv_iterator:Iterator ) -> str:
    headers = csv_iterator.__next__()

    if headers[0] == 'MY ACCOUNT TRANSACTIONS':
        return 'ctfs'
    
    return 'none.'

def files_in_the_import_folder_to_database():
    filenames: list[str] = listdir(INPUT_FILE)
    for filename in filenames:
        if filename[-3:].lower() == 'csv':
            with open(path.join(INPUT_FILE, filename)) as csv_file:
                csv_reader = csv.reader(csv_file)
                csv_iterator = csv_reader.__iter__()
                match guess_account_source(csv_iterator):
                    case 'ctfs': #Canadian Tire Financial Services
                        add_ctfs_to_database(csv_iterator)
                        print(fstr(f'SUCCESSFULLY UPLOADED {filename}'))

                    case 'bmo': #bank of montreal
                        continue
                        raise NotImplementedError

                    case _:
                        continue
                        raise NotImplementedError
        if filename[-4:].lower() == 'json':
            add_rbc_to_database(path.join(INPUT_FILE, filename))
            print(fstr(f'SUCCESSFULLY UPLOADED {filename}'))


        if filename[:-3].lower() == 'pdf':
            continue