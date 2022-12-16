from settings import *
def readCSVfile(file, struct):
    import csv
    result = {}
    # with open(file, 'r', newline='', encoding='cp1251') as csv_file:
    #     reader = csv.DictReader(csv_file, delimiter=';', quotechar='|')
    #     for row in reader:
    #         print(f' {row[struct[0]]} {row[struct[1]]} {row[struct[2]]} : {row[struct[3]]}')

    csv_file = open(file, 'r', newline='', encoding='cp1251')
    reader = csv.DictReader(csv_file, delimiter=';', quotechar='|')
    buf = reader

    for row in reader:
        #print(f' {row[struct[0]]} {row[struct[1]]} {row[struct[2]]} : {row[struct[3]]}')
        result[len(result) + 1] = row
    csv_file.close()
    return result