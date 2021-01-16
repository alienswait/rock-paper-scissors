import random

def game():
    player = input("Please choose .. 'r' for rock, 'p' for paper, 's' for scissors, 'q' for exit ")
    computer = random.choice(['r','p','s'])

    if player == 'q':
        print("Signing out.. Have a nice day")
        exit()


    if player == computer:
        return "It's draw.."

    if win(computer,player):
        return "you won :)"

    return "You lost :( "

def win(player,computer):

    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True



print(game())
