import file_handler
import display
import inputs
import music_reports

def master_func():
    data = file_handler.import_data()
    #tuple_of_functions=(display.view_all_imported_albums(data),display.find_by_genre(data,inputs.find_by_genre_input(data)),2,3,4,5)
    while True:
        display.menu()
        decision_made_by_the_user_of_this_program = inputs.menu_input()
        decision_made_by_the_user_of_this_program = int(decision_made_by_the_user_of_this_program)
        if 1 ==  decision_made_by_the_user_of_this_program:
            display.view_all_imported_albums(data)
        elif 2 == decision_made_by_the_user_of_this_program:
            display.find_by_genre(data,inputs.find_by_genre_input(data))
        #elif 3 == decision_made_by_the_user_of_this_program:
        #elif 4 == decision_made_by_the_user_of_this_program:
        #elif 5 == decision_made_by_the_user_of_this_program:
        #elif 6 == decision_made_by_the_user_of_this_program:






















master_func()
