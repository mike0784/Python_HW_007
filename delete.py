def deleteEntry(file, struct):
    from read import readBD
    from view import viewBD
    from writeCSV import writerCSVfile as wrCSVfile
    bd = readBD(file, struct)
    viewBD(bd, struct)
    mode = 'y'
    while(mode == 'y'):
        n = 0
        while(n == 0):
            n = int(input("Какую запись вы хотите удалить: "))
            if not bd.get(n):
                print("Введенное значение отсутствует в списке")
                n = 0
        del bd[n]
        mode = input("Хотете продолжить удаление записей [y/n]: ")
    viewBD(bd, struct)
    wrCSVfile(bd, file, struct)