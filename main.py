import os
import sys
from functions import *

if __name__ == '__main__':
    did = 1
    while str(did) != str('0'):
        print('Чтобы выйти нажмите 0.\n')
        print('Чтобы сделать все по умолчанию (по порядку) нажмите 1.\n')
        print ()

        print()
        did = input('Введите действие: ')

        if did == "1":
            create_folder('new')
            create_empty_file('new/asdf.ti')
            copy('new')
            remote('new')

            print(view())
            print(view_folders())
            print(view_files())
            # print({1, 2, 3, 4})
            print(system_information())
            creator()
            # victory()
            # bank()
            change_work_catalog('C:\\Users\\user\\PycharmProjects\\console_file_manager\\new_copy')

pass
