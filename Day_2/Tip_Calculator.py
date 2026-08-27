print("Welcome to the Tip Calculator!")

bill = float(input("Enter the bill amount: "))
tip = int(input("Enter the tip percentage (10, 12, or 15): "))
people = int(input("Enter the number of people to split the bill: "))

total_bill = bill + (bill * tip / 100)
each_person = total_bill / people

print("Each person should pay:", round(each_person, 2))