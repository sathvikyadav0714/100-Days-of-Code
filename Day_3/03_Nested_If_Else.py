print("Welcome to the rollercoaster!")
height=float(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("Enter your age: "))

    if age<218:
        print("You need to pay $7")
    elif age>=12 and age<=18:
        print("You need to pay $5")
    else:
        print("You need to pay $12")
else:
    print("Sorry, you can't ride.")