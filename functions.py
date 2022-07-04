import os
import sys
import shutil
import random


def create_folder(path):
    # checking for folder existence
    if not os.path.exists(path):
        # print(path)
        # create folder
        os.mkdir(path)


def create_empty_file(path):
    open(path, 'a').close()


def remote(path):
    # check
    if os.path.exists(path):
        if '.' in path:
            if os.path.exists(path):
                # remote
                print('asdf')
                os.remove(path)
        elif len(os.listdir(path)) == 0:
            os.rmdir(path)
        elif len(os.listdir(path)) != 0:
            shutil.rmtree(path)


def copy(path):
    if not os.path.exists(path):
        # если существует path то не копируем
        if '.' in path:
            shutil.copy(path, path + '_copy')
        else:
            shutil.copytree(path, path + '_copy')


def view(*args):
    if not args:
        return os.listdir()
    else:
        return os.listdir(*args)


def view_folders(*args):
    if args:
        return list(filter(lambda x: '.' not in x, os.listdir(*args)))
    else:
        return list(filter(lambda x: '.' not in x, os.listdir()))


def view_files(*args):
    if args:
        return list(filter(lambda x: '.' in x, os.listdir(*args)))
    else:
        return list(filter(lambda x: '.' in x, os.listdir()))


def system_information():
    return str('My OS is, {}, ({})'.format(sys.platform, os.name))


def creator():
    print('****MIKHAIL****')


def victory():
    answers = {'Хендрикс': '18.09.1970',
               'Армстронг': '4.08.1901',
               'Бальзак': '20.05.1799',
               'Пастернак': '10.02.1890',
               'first': '01.01.1901',
               'second': '02.02.1902',
               'third': '03.03.1903',
               'fourth': '04.04.1904',
               'fifth': '05.05.1905',
               'sixth': '06.06.1906'}

    def get_date(date):
        day_list = ['первое', 'второе', 'третье', 'четвёртое',
                    'пятое', 'шестое', 'седьмое', 'восьмое',
                    'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                    'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                    'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                    'двадцать первое', 'двадцать второе', 'двадцать третье',
                    'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                    'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                    'тридцатое', 'тридцать первое']
        month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                      'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        date_list = date.split('.')
        return (day_list[int(date_list[0]) - 1] + ' ' +
                month_list[int(date_list[1]) - 1] + ' ' +
                date_list[2] + ' года')

    chetchic = 0
    repeat = 'y'
    while repeat == 'y':
        for i in range(0, 5):
            name = random.choice(list(answers.keys()))
            date = answers.pop(name)

            ansver = input("Введите дату раждения {}:".format(name))

            if ansver == date:
                print('Верно\n')
                chetchic += 1
            else:
                print('Неверно. Правильный ответ: {} \n'.format(get_date(date)))

        print("Кол-во правильных ответов {}".format(chetchic))
        repeat = 'n'
        repeat = input('Для повтора теста введите "y"\n')

    print('Выход из цикла')


def bank():
    S = 0.
    history = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            var1 = float(input('Введите сумму пополнения'))
            S += var1

        elif choice == '2':
            var1 = float(input('Введите сумму покупки'))
            if var1 < S:
                S -= var1
                var2 = str(input('Введите название покупки'))
                history.append({var2: var1})
            else:
                print("Недостаточно средств")
            pass
        elif choice == '3':
            print(history)
            pass
        elif choice == '4':
            print('Выход')
            break
        else:
            print('Неверный пункт меню')


def change_work_catalog(path):
    # проблемы с os.join, использовать только абсолютный путь
    os.chdir(path)
    print(os.getcwd())

    # Печать текущего рабочего каталога
    print("Текущий рабочий каталог: {0}".format(os.getcwd()))
