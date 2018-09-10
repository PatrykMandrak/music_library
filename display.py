
def menu():
    print(' What do you want to do?: ')
    print('1: View all imported albums')
    print('2: Find albums by genre')
    print('3: Find album by the given time range')
    print('4: Find the shortest or longest album')
    print('5: Find albums created by given artis')
    print('6: Find album by album')

def view_all_imported_albums(albums_data):
    albums_in_text=''
    for album in albums_data:
        albums_in_text+=str(album)+'\n'
    return print(albums_in_text)

def find_by_genre_or_artist_or_album(albums_data, input_to_find, choice=2):
    print('inputed genre: ', input_to_find)
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
    return print(albums_with_input_to_find)
