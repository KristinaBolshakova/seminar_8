table = ['id', 'last_name', 'first_name', 'class_room', 'birth_day', 'adress']

print(table[1][0])

def show_dict():
    try:
        with open('student.txt', 'r', encoding= 'utf-8') as file:
            file_contetnt = file.read()
            if len(file_contetnt) == 0:
                print('Контактов нет')
            else:
                print(file_contetnt)
    except IOError:
        print('Справочник не существует')

def enter_cont():
    id = input('Введите id контакта: ')
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    class_room = input('Введите класс: ')
    birth_day = input('Введите день рождения: ')
    adress = input('Введите адрес: ')
    table.append(id)
    table.append(first_name)
    table.append(last_name)
    table.append(class_room)
    table.append(birth_day)
    table.append(adress)
   
    with open('student.txt', 'a+', encoding= 'utf-8') as file:
        file.write(f'{table}\n')
    print(f'Добавили запись {table}')


