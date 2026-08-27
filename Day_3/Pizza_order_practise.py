print("welcome to pizza deliveries!")
size=input("what size you would like to order s or m or l: ")
pepperoni=input("do you want pepperoni y or n: ")
cheese=input("do you want extra cheese y or n: ")

if size=="s":
    bill=15
elif size=="m":
    bill=20
elif size=="l":
    bill=25

else:
    print("you typed wrong input")

if pepperoni=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3
        
if cheese=="y":
    bill+=1

print(f"Your final bill is ${bill}")