import texttable as tt
import display

def print_logo():
    with open('logo_graphics.txt') as file:
        logo = file.read()
    return print(logo)

def menu():
    print(' What do you want to do?: ')
    print('1: View all imported albums')
    print('2: Find albums by genre')
    print('3: Find album by the given time range')
    print('4: Find the shortest or longest album')
    print('5: Find albums created by given artis')
    print('6: Find album by album')

def make_a_table(table_data):
    tab = tt.Texttable()
    tab.header(['Artist:','Album','Released:','Genre:','Length:'])
    tlist=table_data # ustaw liste danych
    artists = [i[0] for i in tlist]
    albums = [i[1] for i in tlist]
    releases = [i[2] for i in tlist]
    genres = [i[3] for i in tlist]
    lengths = [i[4] for i in tlist]
    for row in zip(artists, albums, releases, genres, lengths):
        tab.add_row(row)
    s = tab.draw()
    return print(s)

def view_all_imported_albums(albums_data):
    return make_a_table(albums_data)

def find_by_genre_or_artist_or_album(albums_data, input_to_find, choice=2):
    #print('inputed genre: ', input_to_find)
    #print('data', albums_data)
    if choice==0:
        options=3
    elif choice==1:
        options=0
    else:
        options=1
    albums_with_input_to_find = []
    for album in albums_data:
        if album[options]==input_to_find:
            albums_with_input_to_find.append(album)
    display.print_logo()
    return make_a_table(albums_with_input_to_find)

def find_by_time_range(albums_data, input_to_find):
    albums_by_time_range = []
    for album in albums_data:
        if input_to_find[0] <= int(album[2]) <= input_to_find[1]:
            albums_by_time_range.append(album)
    display.print_logo()
    return make_a_table(albums_by_time_range)

def find_the_shortest_or_longest(albums_data, shortest_or_longest):
    shortest = 99999.0
    longest = 0.0
    shortest_album = []
    longest_album = []
    for album in albums_data:
        time_to_float = album[4].split(':')
        time_to_float = float(time_to_float[0]) + (float(time_to_float[1])/100)
        if time_to_float < shortest:
            shortest = time_to_float
            shortest_album = album
        if time_to_float > longest:
            longest = time_to_float
            longest_album = album
    if shortest_or_longest==True:
        display.print_logo()
        return make_a_table([longest_album])
    else:
        display.print_logo()
        return make_a_table([shortest_album])
