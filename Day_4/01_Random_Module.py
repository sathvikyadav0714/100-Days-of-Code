import random
import my_module    

# # Generate a random integer between 1 and 20
# random_number=random.randint(1,20)
# print(random_number)

# print(my_module.favourite_number)

# # Generate a random float between 0 and 1
# random_number_1to10=random.random() 
# print(random_number_1to10)

# random_float_number=random.uniform(10,20)
# print(random_float_number)



# generate heads and tails based on random numbers
random_number=random.random()
print(random_number)
if random_number<0.5 :
    print("heads")
else:
    print("tails")

# or

random_heads_or_tails=random.randint(0,1)
print(random_heads_or_tails)
if random_heads_or_tails==0:
    print("heads")
else:
    print("Tails")
    