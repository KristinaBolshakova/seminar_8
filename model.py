from os.path import exists
from logger import LOG
from variables import *
from csv import reader

id_number = 0
table_students = []


@LOG
def increase_id():
    '''Увеличение id'''
    global id_number
    id_number += 1


# Показать справочник(1)
@LOG
def show_dict_txt():
    '''Показать спарвочник если существует'''
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()
            print(file_content)

    except IOError:
        print(f'Справочник {file_name} не существует, можно добавить данные пункт 2 меню')


# Создание и запись
@LOG
def enter_stud_data():
    '''Создание новой записи'''
    student = {}
    student[field_names[0]] = id_number
    for key in field_names[1:]:
        student[key] = input(f'{key}: ')
    # add_student(student)
    table_students.append(student)
    increase_id()


@LOG
def save_data():
    '''Запись в файл'''
    with open(file_name, 'a+', encoding='utf-8') as file:
        for student in table_students:
            file.writelines(' '.join(map(str, student.values())))
            file.write('\n')

@LOG
def delete_data(file_name='student.csv'):
    '''Удаление записи'''
    show_dict_txt()
    with open(file_name, 'r', encoding='UTF-8') as file:
        list_of_rows = list(reader(file, delimiter=' '))
    delete_id = input('Введите ИД строки, которую хотите удалить: ')
    with open(file_name, 'w', encoding='UTF-8') as file:
        for line in list_of_rows:
            if line[0] != delete_id:
                lst = ' '.join(str(item) for item in line)
                file.write(lst + '\n')
        print(f'Запись с id = {delete_id} удалена')

