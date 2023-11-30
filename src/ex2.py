import csv 
import numpy as np
def find_total_visits():
    total = 0
    files_to_read = ["week-1.csv","week-2.csv","week-3.csv"]
    for week in files_to_read:
        with open(f'files/{week}', 'r') as csv_file:
            rows = csv.reader(csv_file, delimiter=',')
            next(rows)
            for row in rows:
                npArray = np.array(row[1:], dtype='int8')
                total += np.sum(npArray)
                
    return total



def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()