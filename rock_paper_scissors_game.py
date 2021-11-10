import random


def game():
    choice = input('Choose rock, paper, or scissors to play: ')
    options = ['rock', 'paper', 'scissors']
    bot = random.choice(options)

    if choice == bot:
        print('It is a Tie!')

    elif choice == 'rock' and bot == 'paper':
        print(f'You Loose! {bot} beats {choice}')

    elif choice == 'rock' and bot == 'scissors':
        print(f'You Win!!! {choice} beats {bot}')

    elif choice == 'paper' and bot == 'rock':
        print(f'You Win!!! {choice} beats {bot}')

    elif choice == 'paper' and bot == 'scissors':
        print(f'You Loose! {bot} beats {choice}')

    elif choice == 'scissors' and bot == 'paper':
        print(f'You Win!! {choice} beats {bot}')

    elif choice == 'scissors' and bot == 'rock:':
        print(f'You Loose! {bot} beats {choice}')


game()
