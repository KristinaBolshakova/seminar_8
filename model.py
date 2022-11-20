from os.path import exists

head = ['id', 'Фамилия', 'Имя', 'Отчество', 'Класс', 'Дата_рождения', 'Домашний_адрес']
table = []
# print(table[1][0])

# Отсутствует справочник
def none_file():
    print('''Справочник не существует\n
Создать справочник?''')
    var = input('Введите "Y" или любую для выхода: ')
    if var == 'Y' or var == 'y':
        creat_head_txt()
    else:
        exit()

# Создание заголовка таблицы
def creat_head_txt():
    with open('student.txt', 'w', encoding= 'utf-8') as file:
        file.write(f'{head}\n')
        table.append(head)
    print(f'Добавили заголовок таблицы: {head}\n')

# Показать справочник(1)
def show_dict_txt():
    try:
        with open('student.txt', 'r', encoding= 'utf-8') as file:
            file_content = file.read()
            print(file_content)
    except IOError:
        none_file()

# Создание и запись
def enter_stud_data():
    if not exists('student.txt'):
        none_file()
    else:
        input_data_stud()

# Ввод данных и запись в файл (2)
def input_data_stud():
    id = input('Введите id ученика: ')
    last_name = input('Введите фамилию ученика: ')
    first_name = input('Введите имя ученика: ')
    second_name = input('Введите отчество ученика: ')
    class_room = input('Введите класс ученика: ')
    birth_day = input('Введите день рождения ученика: ')
    adress = input('Введите адрес ученика: ')
    stud_data = [id, last_name, first_name, second_name, class_room, birth_day, adress]
    table.append(stud_data)
    print(table)
    with open('student.txt', 'a+', encoding= 'utf-8') as file:
        file.write(f'{stud_data}\n')
    print(f'\nДобавили запись {stud_data}\n')






