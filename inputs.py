import os

def bulletproof_release_year():
    while True:
        try:
            release = int(input('Enter release date (only year): '))
            return str(release)
        except:
            print(' Invalid input, enter only years')

def bulletproof_length():
    while True:
        length = input('Enter album\'s length in format (mm:ss): ')
        if ':' in length:
            length = length.split(':')
            try:
                int(length[0]) + (int(length[1])/100)
                float(length[0]) + (float(length[1])/100)
            except:
                print('Invalid format')
            try:
                if int(length[1]) >=60:
                    length[1] = '59'
                length = str(length[0]) +':' + str(length[1])[:2]
                return length
            except:
                print(' Enter valid data')
        else:
            print('Invalid format')


def valid_input_to_change(what_to_edit):
    if what_to_edit==0:
        input_to_edit=input(' Edit artist name for this album: ')
        return input_to_edit
    elif what_to_edit==1:
        input_to_edit=input(' Edit album name for this album: ')
        return input_to_edit
    elif what_to_edit==2:
        input_to_edit=bulletproof_release_year() # to bulletproof
        return input_to_edit
    elif what_to_edit==3:
        input_to_edit=input(' Edit album\'s genre: ')
        return input_to_edit
    elif what_to_edit==4:
        input_to_edit=bulletproof_length() # to bulletproof
        return input_to_edit

def get_valid_index(index_length, deleteprint = False):
    while True:
        try:
            edit_or_delete = 'edit'
            if deleteprint == True:
                edit_or_delete = 'delete'
            choosen_album = int(input(' Enter a number of an album u want to {0} '.format(edit_or_delete)))-1
            print('Remember, you must enter a number.')
            if 0 <= choosen_album <= index_length-1:
                return choosen_album
            else:
                print('There is no such number in data.')
        except:
            print('Remember, you must enter a number.')

def valid_input_to_edit(index_length):
    choosen_album = get_valid_index(index_length)
    print('\nWhich element you want to edit? Choose from following options:')
    print('Artist, Album, Released, Genre, Length')
    options = ['artist', 'album', 'released', 'genre', 'length']
    while True:
        choosen_element = input(' Enter the element: ').lower()
        if choosen_element in options:
            for i in range(len(options)):
                if choosen_element == options[i]:
                    choosen_element = i
                    return [choosen_album, choosen_element]
        print(' There is no such element')

def bulletproof_add_album_input():
    print(' Adding new album...')
    artist = input('Enter artist name: ')
    album_name = input('Enter album name: ')
    release = bulletproof_release_year()
    genre = input('Enter a genre: ')
    length = bulletproof_length()
    new_album_list_done = [artist, album_name, release, genre, length]
    return new_album_list_done

def valid_input(number_of_options):
    while True:
        possible_choices = [i+1 for i in range(number_of_options)]
        question = input('\n Enter Your choice: ')
        try:
            question = int(question)
        except:
            print(" You must input a number! ")
        if question in possible_choices:
            os.system('clear')
            return str(question)
        print(" Choose only displayed options! ")

def valid_genre_or_artist_or_album_input(albums_data, choice=2):
    while True:
        artist_or_genre=''
        if choice == 0:
            artist_or_genre='Genre'
            possible_genres_setup = [albums_data[i][3] for i in range(len(albums_data))]
        elif choice ==1:
            artist_or_genre='Artist'
            possible_genres_setup = [albums_data[i][0] for i in range(len(albums_data))]
        else:
            artist_or_genre='Album'
            possible_genres_setup = [albums_data[i][1] for i in range(len(albums_data))]
        possible_genres = []
        for i in range(len(possible_genres_setup)):
            if possible_genres_setup[i] not in possible_genres:
                possible_genres.append(possible_genres_setup[i])
        print(' Possible choices:\n',str(possible_genres)[1:-1])
        check_if_exists = input(" " + artist_or_genre + " you want to find: ")
        if check_if_exists in possible_genres:
            os.system('clear')
            return check_if_exists
        print("This " + artist_or_genre + " doesn't exist")

def valid_time_range_format():
    while True:
        time_format_check = input(' Enter time range in format from year to year (yyyy-yyyy): ')
        if '-' in time_format_check:
            time_format_check=time_format_check.split('-')
            try:
                time_format_check[0]=int(time_format_check[0])
                time_format_check[1]=int(time_format_check[1])
                os.system('clear')
                return time_format_check
            except:
                print('Invalid format, u need to input numbers as years')
        else:
            print('Invalid format')

def valid_short_or_long_format_XD():
    while True:
        short_or_long_check = input(" Enter \'shortest\' to find the shortest, or enter \'longest\' to find the longest: ").upper()
        if short_or_long_check=='SHORTEST':
            os.system('clear')
            return False
        elif short_or_long_check=='LONGEST':
            os.system('clear')
            return True
        else:
            print('Invalid format, input only \'shortest\' or \'longest\' ')


def menu_input():
    user_choice = valid_input(10)
    return user_choice

def find_by_choice_input(albums_data, choice=2):
    user_choice = valid_genre_or_artist_or_album_input(albums_data, choice)
    return user_choice

def find_by_time_range_input():
    user_choice_time_range = valid_time_range_format()
    return user_choice_time_range

def find_the_shortest_or_longest_input():
    user_choice_short_or_long = valid_short_or_long_format_XD()
    return user_choice_short_or_long
