import csv
import os
from create import *
from settings import *
from read import readBD
from view import viewBD
from update import readerBD
from delete import deleteEntry
from append import appendEntry

mode = -1
file = "d:\Mike\Proba\HW_07\BD.csv"
a = input("Введите БД: ")
if len(a) != 0:
    if os.path.exists(a):
        file = a
    else:
        print("Файл " + a + " не существует")
    print("Вы выбрали " + file)
while(mode != 0):
    f = open('d:\Mike\Proba\HW_07\menu.txt', 'r', encoding='utf-8')
    buf = f.read()
    f.close()
    print("-----------------------------------------------------------------")
    print(buf)
    mode = int(input("Введите режим работы: "))
    if mode == 1:
        createBD(file, struct)
    elif mode == 2:
        bd = readBD(file, struct)
        viewBD(bd, struct)
        input()
    elif mode == 3:
        readerBD(file, struct)
    elif mode == 4:
        deleteEntry(file, struct)
    elif mode == 5:
        appendEntry(file, struct)