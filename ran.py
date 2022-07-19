import random
print("rolling")
print(random.randint(1, 12))

guess = False
limit = input("set an upper limit\n")
ran = random.randint(1,int(limit))
death = random.randint(1, int(limit))
if death == ran:
    death+=1
tries = 0
while not guess:
    tries+=1
    num = int(input("Guess a number 1-" + limit + "\n"))
    if num == death:
        print("you guessed the death number\nGAME OVER")
    if num == ran:
        print("you win\nit took you " + str(tries) + " tries")
        break
    elif ran > num:
        print("higher")
    else:
        print("lower")