#This program is a 2-player rock-paper-scissors game
#Variables definition
weapons = ['Rock', 'Paper', 'Scissors']
player_one_choice = ''
player_two_choice = ''
valid_answer = False

#Data input
print("This is a 2-player Rock-Paper-Scissors game")
print('''Choice your weapon:\n
        1. Rock\n
        2. Paper\n
        3. Scissors
      ''')

#Data input for player one
while valid_answer == False:
    player_one_choice = int(input("Player one choice: "))
    if player_one_choice == 1 or player_one_choice == 2 or player_one_choice== 3:
        valid_answer= True
        break
    else:
        valid_answer = False

#Re-initializing the conditional variable
valid_answer = False        

#Data input for player 2
while valid_answer == False:
    player_two_choice = int(input("Player two choice: "))
    if player_two_choice == 1 or player_two_choice == 2 or player_two_choice== 3:
        valid_answer = True
        break
    else:
        valid_answer = False

#Result output
if player_one_choice == player_two_choice:
    print('It\'s a DRAW!')
elif player_one_choice == 1 and player_two_choice == 2:
    print("Player two WINS and Player one LOSES!!")
elif player_one_choice == 1 and player_two_choice == 3:
    print("Player one WINS and Player two LOSES!!")
elif player_one_choice == 2 and player_two_choice == 1:
    print("Player one WINS and Player two LOSES!!")
elif player_one_choice == 2 and player_two_choice == 3:
    print("Player two WINS and Player one LOSES!!")
elif player_one_choice == 3 and player_two_choice == 1:
    print("Player two WINS and Player one LOSES!!")
elif player_one_choice == 3 and player_two_choice == 2:
    print("Player one WINS and Player two LOSES!!")