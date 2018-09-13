def update_data(updated_albums_data):
    with open('text_albums_data.txt', "w") as file:
        for album in updated_albums_data:
            file.write(album[0]+','+album[1]+','+album[2]+','+album[3]+','+album[4]+'\n')

def import_data():
    with open('text_albums_data.txt') as file:
        text_to_convert_to_list= file
        text_to_convert_to_list=[]
        for line in file.readlines():
            line=line.split(",")
            line[4]=line[4][:-1]
            text_to_convert_to_list.append(line)
    return text_to_convert_to_list

def add_album(bulletproof_input):
    albums_data = import_data()
    new_album_list = bulletproof_input
    albums_data.append(new_album_list)
    update_data(albums_data)

def edit_album(input_what_to_edit , new_change):
    albums_data = import_data()
    albums_data[input_what_to_edit[0]][input_what_to_edit[1]] = new_change
    update_data(albums_data)

def del_album(index_to_delete):
    albums_data = import_data()
    del albums_data[index_to_delete]
    update_data(albums_data)
