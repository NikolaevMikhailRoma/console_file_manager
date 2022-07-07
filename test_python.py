import shutil
from math import pi, sqrt, pow, hypot
import functions
import os

def test_filter():
    list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
    assert filter(str.isdigit, list_of_strings), ['100', '1', '50']


def test_map():
    def double(num):
        return num * 2

    assert map(double([1, 2, 3]), [2, 4, 6])


def test_sorted():
    assert sorted([1, 5, 2, 3]), [1, 2, 3, 5]


def test_pi():
    assert pi, pi


def test_sqrt():
    assert sqrt(4), 2


def test_pow():
    assert pow(2, 2), 4


def test_hypot():
    assert hypot(2, 3), 4


def test_file_manager_create_folder():
    path = 'asdf'
    functions.create_folder(path)
    assert os.path.exists(path), True
    os.rmdir(path)

def test_file_manager_create_empty_file():
    path = 'asdf.py'
    functions.create_empty_file(path)
    assert os.path.exists(path), True
    os.remove(path)

def test_file_manager_copy():


    path = 'asdfasdfadfadfadfasdfasdfafd'

    functions.create_folder(path)
    shutil.copytree(path, path + '_copy')
    assert os.path.exists(path + "_copy"), True
    shutil.rmtree(path + "_copy")
    shutil.rmtree(path)

    path = 'asdfasdfadfadfadfasdfasdfafd.py'
    functions.create_empty_file(path)
    shutil.copy(path, path + '_copy')
    assert os.path.exists(path + "_copy"), True
    os.remove(path)
    os.remove(path + "_copy")

def test_file_manager_view():
    path = 'test_view'
    functions.create_folder(path)
    assert 'test_view' in functions.view(), True
    shutil.rmtree(path)

def test_file_manager_view_folders():
    assert 'venv' in functions.view_folders(), True

def test_file_manager_view_files():
    assert 'main.py' in functions.view_files(), True

def test_file_manager_system_information():
    assert type(functions.system_information()), str

def test_file_manager_creator():
    assert True, True

# больше чистых функций нет