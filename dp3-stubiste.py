def fib3(x):
    dvaiza = 0
    jediza = 1

    for i in range(2, x+1):
        temp = jediza
        jediza = jediza + dvaiza
        dvaiza = temp

    return jediza


n = 3
print(fib3(n+1))





