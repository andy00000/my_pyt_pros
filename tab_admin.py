# SQL table admin module

# First version - just for primary filling of SQL\pcs

import MySQLdb
import sys

base = MySQLdb.connect(host="localhost", user="Andy", passwd="Hfcnfafhf2010", db="pcs")
cursor = base.cursor()


def action(case):
    if case == 1:
        cursor.execute('SELECT * FROM in_pc')
        data = cursor.fetchall()
        for row in data:
            index = row[0]
            name = row[1]
            date = row[2]
            im_ver = row[3]
            win_ver = row[4]
            in_flag = row[5]
            print('{0}. PC: {1}, install date: {2}, image version: {3}, Windows version: {4}, installation flag: {5}'
                  .format(index, name, date, im_ver, win_ver, in_flag))
        return (False)
    elif case == 2:
        cursor.execute('SELECT MAX(id_in_pc) AS id_in_pc FROM in_pc;')
        data = cursor.fetchall()
        max_index = int(data[0][0])
        values = inp_values()
        comma = "'" + str(max_index + 1) + "'," + values + ",'0'"  # флаг установки по умолчанию False
        cursor.execute('INSERT INTO in_pc VALUES (' + comma + ');')
        print('Line inserted!')
        return (False)

    elif case == 3:
        cursor.execute('SELECT MAX(id_in_pc) AS id_in_pc FROM in_pc;')
        data = cursor.fetchall()
        max_index = int(data[0][0])
        print('Select line from 1 to {0}.'.format(max_index))
        insline = int(input('Line: '))
        if insline not in range(1, max_index + 1):
            print('Error! Wrong line number!')
            return (False)
            # дописать сюда goto

        print('Are you sure? The line {0} will be permanently deleted! (Y/N): ')
        char = sys.stdin.read(1)
        if char == 'y' or char == 'Y':
            cursor.execute('DELETE FROM in_pc WHERE id_in_pc=' + str(insline) + ';')
            print('Line deleted!')
            return (False)



    elif case == 5:
        return (True)


def inp_values():
    print('Insert values:\n')
    name = input('PC name: ')  # Пока без проверки, её сделаю потом
    date = input('Install date: ')
    im_ver = input('Image version: ')
    win_ver = input('Windows version: ')
    return ("'" + name + "','" + date + "','" + im_ver + "','" + win_ver + "'")


selected = False

while not selected:
    print('\n---------------------------\nFilling SQL DB "PCs" module\n')
    print('Select operation:')
    print('1 - Show table')
    print('2 - Insert new line(s)')
    print('3 - Delete line(s)')
    print('4 - Edit line(s)')
    print('5 - Quit\n')
    case = int(input('Your choise: '))
    if case < 1 or case > 5:
        print('Incorrect value, try again!')
        continue
    else:
        selected = action(case)
        continue
