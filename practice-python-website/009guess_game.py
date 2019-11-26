import random

print('''
    This is a game where you have to guess the secret number from 0 to 100
    The game will tell you if you\'re higher or lower to the secret number
    You can quit the game at any time typing the word 'EXIT'
    ''')

secret_number = random.randint(0, 100)
game_won = False
tries = 0

while game_won == False:
    guessed_number = int(input('Type a number to guess... '))
    if guessed_number == secret_number:
        tries += 1 
        print("Congratulations, the secret number is " + str(secret_number) + " and it took you " + str(tries) + " tries")
        game_won = True
    elif guessed_number < secret_number:
        tries += 1
        print("Too low...")
    elif guessed_number > secret_number:
        tries += 1
        print("Too high...")
    elif guessed_number == 'EXIT':
        print("You quit the game :(")