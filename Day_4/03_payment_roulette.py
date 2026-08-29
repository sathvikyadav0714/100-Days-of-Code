import random
friends=["allen","bob","charlie","jeff","john"]

# who will pay hem bill

print(random.choice(friends))

# option2

random_index=random.randint(0,4)
print(friends[random_index])