def get_user_choice():
    '''
    This is the 
    '''
    
    user_choice = input("what is you choice? Please enter r for (rock), p for (papper) or s for (scissors)")

    if user_choice == "r":
        return "rock"
    elif user_choice == "p":
        return "paper"
    elif user_choice =="s":
        return "scissors"

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
def play():
    choice_list = ['rock', 'paper', 'scissors']
    computer_choice = get_computer_choice(choice_list)
    user_choice = get_user_choice()

    print("Your choice is", user_choice)
    print("The computer choice is", computer_choice)
    print(who_won(user_choice, computer_choice))
play()
