import random
def game(n):
    print('Get ready!')
    computer_choice = ['rock', 'paper', 'scissors']
    beats = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
    player_choice = input('(Type Rock, Paper, Scissors)').lower()
    computer_choice = random.choice(computer_choice)
    if computer_choice == player_choice:
        print('Computer chose ' + computer_choice + '. You tie!')
    elif beats[player_choice] == computer_choice:
        print(player_choice + ' beats '+ computer_choice)
        print('Computer chose ' + computer_choice + '. You win!')
        ##pp = pp + 1
    elif beats[computer_choice] == player_choice:
        print('Computer chose ' + computer_choice + '. You lose!')
        print(computer_choice + ' beats ' + player_choice)
       ## cp = cp + 1
    else:
        print('error')
    play_again = input('Press enter to play again or X to end the game')
    if play_again == "":
        game()
    else:
        print('Thank you for playing')
        ##print('Player points', pp)
        ##print('Computer points', cp)


game()
