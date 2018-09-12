def import_data():
    with open('text_albums_data.txt') as file:
        text_to_convert_to_list= file
        text_to_convert_to_list=[]
        for line in file.readlines():
            line=line.split(",")
            line[4]=line[4][:-1]
            text_to_convert_to_list.append(line)
    return text_to_convert_to_list

def add_album():
    albums_data = import_data()
    print(' Adding new album...')
    artist = input('Enter artist name: ')
    album_name = input('Enter album name: ')
    release = input('Enter release date (only year): ')
    genre = input('Enter a genre: ')
    length = input('Enter album\'s length in format (mm:ss): ')
    albums_data.append([str(artist), str(album_name), str(release), str(genre), str(length)])
    with open('text_albums_data.txt', "w") as file:
        for album in albums_data:
            file.write(album[0]+','+album[1]+','+album[2]+','+album[3]+','+album[4]+'\n')
    print('')
