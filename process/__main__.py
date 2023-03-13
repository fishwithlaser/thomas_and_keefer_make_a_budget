
INPUT_FILE: str = 'inputs'

if __name__ == "__main__":
    from os import listdir, path
    from process 
    import csv

    files: list[str] = listdir(INPUT_FILE)
    for file in files:
        print(path.join(INPUT_FILE, file))
        with open(path.join(INPUT_FILE, file)) as csv_file:
            csv_reader = csv.reader(csv_file)
            match guess_account_source(row[0])
                case 'rbc': #Royal Bank of Canada
                    raise NotImplementedError

                case 'ctfs': #Canadian Tire Financial Services
                    raise NotImplementedError

                case 'bmo': #bank of montreal
                    raise NotImplementedError

                case _:
                    raise NotImplementedError
            for row in csv_reader:
                match guess_account_source(row)