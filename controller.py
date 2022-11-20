import view
import model

def run():
    num = 1
    while num > 0:
        view.input_data()
        num = int(input('Выберете действие: '))
        if num == 1:
            model.show_dict_txt()
        elif num == 2:
            model.enter_stud_data()
        elif num == 3:
            pass
        elif num == 4:
            pass