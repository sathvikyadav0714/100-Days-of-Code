height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kg: "))
bmi=weight/(height**2)
print("your bmi is ",bmi)
if bmi<18.5:
    print("you are underweight")
elif bmi>=18.5 and bmi<25:
    print("you have a normal weight")
elif bmi>=25 and bmi<30:
    print("you are overweight")
else:
    print("you are obese")