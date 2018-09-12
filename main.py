#python module imports
import os
#file module imports
import file_handler
import display
import inputs
import music_reports

def setup_menu_get_input():
    display.menu()
    decision_made_by_the_user_of_this_program = int(inputs.menu_input())
    os.system('clear')
    return decision_made_by_the_user_of_this_program

def master_func():
    data = file_handler.import_data()
    os.system('clear')
    display.print_logo()
    user_choice = setup_menu_get_input()
    while True:
        display.print_logo()
        if 1 ==  user_choice:
            display.view_all_imported_albums(data)
            user_choice = setup_menu_get_input()
        elif 2 == user_choice:
            display.find_by_genre_or_artist_or_album(data,inputs.find_by_choice_input(data,0), 0)
            user_choice = setup_menu_get_input()
        elif 3 == user_choice:
            display.find_by_time_range(data, inputs.find_by_time_range_input())
            user_choice = setup_menu_get_input()
        elif 4 == user_choice:
            display.find_the_shortest_or_longest(data, inputs.find_the_shortest_or_longest_input())
            user_choice = setup_menu_get_input()
        elif 5 == user_choice:
            display.find_by_genre_or_artist_or_album(data,inputs.find_by_choice_input(data,1), 1)
            user_choice = setup_menu_get_input()
        elif 6 == user_choice:
            display.find_by_genre_or_artist_or_album(data,inputs.find_by_choice_input(data))
            user_choice = setup_menu_get_input()

master_func()






















master_func()
