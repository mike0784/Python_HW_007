def writerCSVfile(data, file, fields):
    import csv
    with open(file, 'w', newline = '') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fields)
        writer.writeheader()
        for row in data:
            writer.writerow(data[row])
