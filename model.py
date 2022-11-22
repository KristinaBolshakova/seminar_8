from os.path import exists
from logger import LOG
from variables import *
from csv import reader
from prettytable import PrettyTable

id_number = 1
table_students = []


@LOG
def increase_id():
    '''Увеличение id'''
    global id_number
    id_number += 1


@LOG
def show_dict_txt():
    '''Показать спарвочник если существует'''
    try:
        read_file()
        print_table()
    except IOError:
        print(f'Справочник {file_name} не существует, можно добавить данные пункт 2 меню')


def print_table():
    '''Вывод в виде таблицы'''
    t = PrettyTable(field_names)
    t.add_rows(list_of_rows)
    print(t)


@LOG
def enter_stud_data():
    '''Создание новой записи'''
    student = {}
    student[field_names[0]] = id_number
    for key in field_names[1:]:
        student[key] = input(f'{key}: ')
    table_students.append(student)
    increase_id()


@LOG
def save_data():
    '''Запись в файл'''
    with open(file_name, 'a+', encoding='utf-8') as file:
        for student in table_students:
            file.writelines(' '.join(map(str, student.values())))
            file.write('\n')


def read_file(file_name='student.csv'):
    global list_of_rows
    with open(file_name, 'r', encoding='UTF-8') as file:
        list_of_rows = list(reader(file, delimiter=' '))


@LOG
def delete_data(file_name='student.csv'):
    '''Удаление записи'''
    show_dict_txt()
    delete_id = input('Введите ИД строки, которую хотите удалить: ')
    with open(file_name, 'w', encoding='UTF-8') as file:
        for line in list_of_rows:
            if line[0] != delete_id:
                lst = ' '.join(str(item) for item in line)
                file.write(lst + '\n')
        print(f'Запись с id = {delete_id} удалена')


@LOG
def correction_data(file_name='student.csv'):
    show_dict_txt()
    corr_line = input('Введите id строки для редактирования: ')
    corr_item = input('Введите номер столбца для редактирования \n'
                      '1 - Фамилия, 2 - Имя, 3 - Отчество, 4-Класс, 5-Дата рождения, 6- Домашний адрес: ')
    # print(list_of_rows[1][4])
    corr_new_item = input('Введите новые данные: ')
    with open(file_name, 'w', encoding='UTF-8') as file:
        for line in list_of_rows:
            if line[0] == corr_line:
                line[int(corr_item)] = corr_new_item
            lst = ' '.join(str(item) for item in line)
            file.write(lst + '\n')
        print(f'Запись с id {corr_line} изменена ')
    print_table()
