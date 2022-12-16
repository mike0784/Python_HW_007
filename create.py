def createBD(file, struct):
    from writeCSV import writerCSVfile as wrCSVfile
    mode = 'y'
    while(mode == 'y'):
        lst = {}
        for item in struct:
            lst[item] = input("Введите " + item + ": ")
        bd[len(bd) + 1] = lst
        mode = input("Продолжить ввод [y/n]")
    wrCSVfile(bd, file, struct)