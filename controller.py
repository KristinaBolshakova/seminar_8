import view
import model

def run():
    num = 1
    while num > 0:
        view.input_data()
        num = int(input('Выберете действие: '))
        if num == 1:
            model.show_dict()
        elif num == 2:
            model.enter_cont()
        elif num == 3:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass