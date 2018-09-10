import file_handler
import display
import inputs
import music_reports

def master_func():
    tuple_of_functions=(display.view_all_imported_albums(file_handler.import_data()),1,2,3,4,5)
    while True:
        display.menu()
        decision_made_by_the_user_of_this_program = inputs.menu_input()
        for i in range(6):
            if i ==  int(decision_made_by_the_user_of_this_program)-1:
                print(tuple_of_functions[i])
                break

master_func()
