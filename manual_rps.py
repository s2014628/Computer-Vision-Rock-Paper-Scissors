def get_user_choice():
    user_choice = input("Please enter rock (r), paper (p) or scissors (s)")

    if user_choice == "r":
        return "rock"
    elif user_choice == "p":
        return "paper"
    elif user_choice =="s":
        return "scissors"
    else:
        return "invalid"

def get_computer_choice(choice_list):
    import random   
    return random.choice(choice_list)

def who_won(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "The result is a draw"
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            return "Rock sharpens scissors: you win"
        elif computer_choice == 'paper':
            return "Paper wraps rock: computer wins"
        else:
            return "The computer's selection could not be processed"
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            return "Scissors cut paper=: you win"
        elif computer_choice == 'rock':
            return "Rock sharpens scissors: computer wins"
        else:
            return "The computer's selection could not be processed"
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return "Scissors cut paper=: computer wins"
        elif computer_choice == 'rock':
            return "Rock sharpens scissors: you win"
        else:
            return "The computer's selection could not be processed"
    else:
        return "Your selection could not be processed"
        
def play_rps():
    rps_list = ['rock', 'paper', 'scissors']
    computer_choice = get_computer_choice(rps_list)
    user_choice = get_user_choice()

    print("You chose", user_choice)
    print("The computer chose", computer_choice)
    print(who_won(user_choice, computer_choice))