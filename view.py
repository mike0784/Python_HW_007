

def viewBD(data, struct):
    for row in data:
        print(f'{row} : {struct[0]}: {data[row][struct[0]]}  {struct[1]}: {data[row][struct[1]]}  {struct[2]}: {data[row][struct[2]]}  {struct[3]}: {data[row][struct[3]]}')