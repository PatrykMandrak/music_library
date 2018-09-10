
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
    return albums_in_text
