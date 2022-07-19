guessed = False
while not guessed:
    guess = input("guess the password\n")
    if guess == "14":
        guessed = True

print("you win")

number_of_leaves = 15
for x in range(0, number_of_leaves):
    print("A leaf fell to the ground " + str(x) + " leaves have fallen.")

print("All the leaves fell. For loop complete.") 