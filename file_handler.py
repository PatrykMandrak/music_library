def import_data():
    with open('text_albums_data.txt') as file:
        text_to_convert_to_list= file
        text_to_convert_to_list=[]
        for line in file.readlines():
            line=line.split(",")
            line[4]=line[4][:-1]
            text_to_convert_to_list.append(line)
    return text_to_convert_to_list
