# AND
# Both must be True

print(True and True)      # True
print(True and False)     # False
print(False and True)     # False
print(False and False)    # False


# or
# At least one must be True

print(True or True)       # True
print(True or False)      # True
print(False or True)      # True
print(False or False)     # False


# not
# Reverses True/False

print(not True)           # False
print(not False)          # True



# example
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
# age >= 18 → True
# has_id → True
# True AND True → True




# example
print("Welcome to the rollercoaster!")
height=float(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("Enter your age: "))

    if age<12:
        bill=5
        print("You need to pay $7")
    elif age>=12 and age<=18:
        bill=7
        print("You need to pay $5")
    elif 45<=age<=55:
        print("everything is going to be ok. You can take a ride on us")
    else:
        bill=12
        print("You need to pay $12")

    wants_photo=input("do you want a photo y for YES n for NO: ")
    if wants_photo=="y":
        bill+=3
        print(f"Your final bill is ${bill}")

else:
    print("Sorry, you can't ride.")