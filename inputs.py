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

def valid_genre_input(albums_data):
    while True:
        possible_genres_setup = [albums_data[i][3] for i in range(len(albums_data))]
        possible_genres = []
        for i in range(len(possible_genres_setup)):
            if possible_genres_setup[i] not in possible_genres:
                possible_genres.append(possible_genres_setup[i])
        print(' Possible choices:',possible_genres)
        check_if_exists = input(" Genre You want to find: ")
        if check_if_exists in possible_genres:
            return check_if_exists
        print("This genre doesn't exist")

def menu_input():
    user_choice = valid_input(6)
    return user_choice

def find_by_genre_input(albums_data):
    genre_choice = valid_genre_input(albums_data)
    return genre_choice
