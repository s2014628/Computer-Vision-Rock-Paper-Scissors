def get_prediction(prediction):
    if prediction[0][0]>0.5:
        return'Rock'
    elif prediction[0][1]>0.5:
        return'Papper'
    elif prediction[0][2]>0.5:
        return'Scissors'
    elif prediction[0][3]>0.5:
        return'Nothing'

def get_computer_choice(choice_list):
    import random   
    return random.choice(choice_list)

def who_won(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "The match is a draw"
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            return "you win"
        elif computer_choice == 'paper':
            return "computer wins"
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            return " you win"
        elif computer_choice == 'rock':
            return " computer wins"

    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return " computer wins"
        elif computer_choice == 'rock':
            return " you win"
