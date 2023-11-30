from ValidationException import ValidationException

import csv

def validate_file(file_name):
    row_list = []
    with open(f'{file_name}', 'r') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        next(rows)
        for row in rows:
            try:
                type(int(row[1]))
            except:
                raise ValidationException(f'Invalid Milage {row[1]}')
        




def ex1():
    try:
        
        validate_file("files\input.txt")
    except ValidationException as ve:
        print(ve)

ex1()