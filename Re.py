a=3
b=6
if a>b:
    print("a is > b")

x=2
if x>3:
    x+=2
print(x)

has_key = True
if has_key == True:
    print("you won unlock the door")

player_age = 12

if player_age >= 18:
    print("You could be in college.")
elif player_age >= 13:
    print("You can also attend iD Academies!")
elif player_age >= 7:
    print("You can attend iD Tech Camps!")
else:
    print("You're young.")

player_has_item = True
score = 101
won = False

if player_has_item and score > 100:
    won = True

if not won:
    print("You haven't beaten the game yet.")
elif won:
    print("You won the game!")

player_has_item = False
score = 201
won = False

if player_has_item or score > 200:
    won = True

if not won:
    print("You haven't beaten the game yet.")
elif won:
    print("You won the game!")

import random

computer_number = random.randrange(0, 101)

guessed = False

while True:
    if not guessed:
        answer = input("Guess the number ")
        if int(answer) == computer_number:
            guessed = True
            print("You got it!")
            break
        elif int(answer) > computer_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

    else:
        break