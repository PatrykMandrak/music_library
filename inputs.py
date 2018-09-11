def valid_input(number_of_options):
    while True:
        possible_choices = [i+1 for i in range(number_of_options)]
        question = input(' Enter Your choice: ')
        try:
            question = int(question)
        except:
            print(" You must input a number! ")
        if question in possible_choices:
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
        print(' Possible choices:',possible_genres)
        check_if_exists = input(" " + artist_or_genre + " you want to find: ")
        if check_if_exists in possible_genres:
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
                return time_format_check
            except:
                print('Invalid format, u need to input numbers as years')
        else:
            print('Invalid format')

def valid_short_or_long_format_XD():
    while True:
        short_or_long_check = input(" Enter \'shortest\' to find the shortest, or enter \'longest\' to find the longest: ").upper()
        if short_or_long_check=='SHORTEST':
            return False
        elif short_or_long_check=='LONGEST':
            return True
        else:
            print('Invalid format, input only \'shortest\' or \'longest\' ')


def menu_input():
    user_choice = valid_input(6)
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
