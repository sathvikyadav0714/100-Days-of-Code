import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

print("Welcome to password generator")
nr_letters=int(input("How may letters would you like to be in your password:\n"))
nr_numbers=int(input("How may numbers would you like to be in your password:\n"))
nr_symbols=int(input("How may symbols would you like to be in your password:\n"))


# easy way
password=""

for ch in range(1,nr_letters+1):
    password+=random.choice(letters)
for ch in range(1,nr_numbers+1):
    password+=random.choice(numbers)
for ch in range(1,nr_symbols+1):
    password+=random.choice(symbols)

print(password)


# hard wayyy
password_list=[]

for ch in range(0,nr_letters):
    password_list.append(random.choice(letters))
for ch in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
for ch in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
print(password_list)

password_shuffled=""
for ch in password_list:
    password_shuffled+=ch

print(password_shuffled)