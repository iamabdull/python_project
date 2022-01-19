print("Welcome to Treasure island Your vission is to field")

lr = str(input("Where do you want to go left or right"))
if lr == "right":
    sw = str(input("will you swim or wait"))
    if sw == "wait":
        br = str(input("Which color blue or red or yellow"))
        if br == "yellow":
            print("You win")
        else:
            print("game over")
    else:
        print("game over")
else :
    print("game over")
    