print("Welcome to the rollercoaster!")
height=float(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("Enter your age: "))

    if age<=12:
        bill=5
        print("You need to pay $7")
    elif age>12 and age<=18:
        bill=7
        print("You need to pay $5")
    else:
        bill=12
        print("You need to pay $12")

    wants_photo=input("do you want a photo y for YES n for NO: ")
    if wants_photo=="y":
        bill+=3
        print(f"Your final bill is ${bill}")

else:
    print("Sorry, you can't ride.")