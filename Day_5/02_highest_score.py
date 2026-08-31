scores=[90,99,55,73,55,67,88,77,87,89,67,89]

print(sum(scores))

print(max(scores))

# using for loops
total_score=0

for score in scores:
    total_score+=score

print(total_score)

highest_score=0
for score in scores:
    if score>highest_score:
        highest_score=score
print(highest_score)