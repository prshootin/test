import random

#random.seed(1337)

n = int(input())
out = []

for i in range(n):
    out.append(random.choice(range(-10, 10)))

print(out)