n = str(input())
b = int(n, 2)

r = 0

while(b):
    r += b%2
    b = b >> 1

print(r)

    