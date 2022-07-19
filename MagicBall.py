import random
roll = input("say \"roll\" when ready\n")
ran = random.randint(1, 8)
print(ran)
if roll == "roll":
    if ran == 1:
        print("you will die sometime in your life")
    elif ran == 2:
        print("you are not #1")
    elif ran == 3:
        print("not amazing")
    elif ran == 4:
        print("ok")
    elif ran == 5:
        print("yay!")
    elif ran == 6:
        print("you win")
    elif ran == 7:
        print("feel good about yourself")
    elif ran == 8:
        print("you won the lottery")