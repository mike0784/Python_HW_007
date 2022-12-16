def readerBD(file, struct):
    from read import readBD
    from view import viewBD
    from writeCSV import writerCSVfile as wrCSVfile
    bd = readBD(file, struct)
    viewBD(bd, struct)
    mode = 'y'
    while(mode == 'y'):
        n = 0
        while(n == 0):
            n = int(input("Какую запись вы хотите редактировать: "))
            if not bd.get(n):
                print("Введенное значение отсутствует в списке")
                n = 0
        lst = {}
        for item in struct:
            lst[item] = input("Введите новое значение для поля '" + item + "': ")
        bd[n] = lst
        mode = input("Хотете продолжить редактирование [y/n]: ")
    viewBD(bd, struct)
    wrCSVfile(bd, file, struct)

