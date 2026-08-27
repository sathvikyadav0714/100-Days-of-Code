print("Welcome to Treasure Island.")

direction=input("enter in which direction you want to go left or right: ").lower
if direction=="right":
    print("you fall in hole and game over")
elif direction=="left":
    swim_or_wait=input("enter swim or wait: ").lower()
    if swim_or_wait=="swim":
        print("you are attacked by trout and game over")
    elif swim_or_wait=="wait":
        door=input("which door you want to enter red, blue or yellow: ").lower()
        if door=="red":
            print("you are burned by fire and game over")
        elif door=="blue":
            print("you are eaten by beasts and game over")
        elif door=="yellow":
            print("you win the treasure")
        else:
            print("invalid door")
    else:
        print("invalid option")
else:
    print("invalid direction")


