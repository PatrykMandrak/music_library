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

def menu_input():
    user_choice = valid_input(6)
    return user_choice

def find_by_choice_input(albums_data, choice=2):
    user_choice = valid_genre_or_artist_or_album_input(albums_data, choice)
    return user_choice
