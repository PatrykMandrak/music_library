
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

def find_by_genre(albums_data, inputed_genre):
    print('inputed genre: ', inputed_genre)
    #print('data', albums_data)
    albums_with_inputed_genre = []
    for album in albums_data:
        if album[3]==inputed_genre:
            albums_with_inputed_genre.append(album)
    return print(albums_with_inputed_genre)
