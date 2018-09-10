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


def menu_input():
    user_choice = valid_input(6)
    return user_choice
