import view
import model

def run():
    while True:
        view.input_data()
        num = input('Выберите действие: ')
        match num:
            case '1':
                model.show_dict_txt()
            case '2':
                model.enter_stud_data()
            case '3':
                model.save_data()
            case '4':
                pass
            case '5':
                model.delete_data()
            case '6':
                exit()
