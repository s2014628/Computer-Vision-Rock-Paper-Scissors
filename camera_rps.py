import numpy as np
def get_prediction(prediction):

    pred = np.argmax(prediction[0], axis=0)
    if pred == 0:
        return 'Rock'
    elif pred == 1:
        return 'Paper'
    elif pred == 2:
        return 'Scissors'
    else:
        return 'Nothing'


def get_computer_choice(choice_list):
    import random   
    return random.choice(choice_list)

def who_won(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "The match is a draw"
    elif user_choice == 'Rock':
        if computer_choice == 'Scissors':
            return "you win"
        elif computer_choice == 'Paper':
            return "computer wins"
    elif user_choice == 'Scissors':
        if computer_choice == 'Paper':
            return "you win"
        elif computer_choice == 'Rock':
            return "computer wins"
    elif user_choice == 'Paper':
        if computer_choice == 'Scissors':
            return "computer wins"
        elif computer_choice == 'Rock':
            return "you win"









