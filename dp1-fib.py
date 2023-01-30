def fib2(x):
    fibbrojevi = []
    fibbrojevi.append(0)
    fibbrojevi.append(1)

    for i in range(2, x+1):
        fibbrojevi.append(fibbrojevi[i-2] + fibbrojevi[i-1])
    
    return fibbrojevi[-1]


def fib3(x):
    dvaiza = 0
    jediza = 1

    for i in range(2, x+1):
        temp = jediza
        jediza = jediza + dvaiza
        dvaiza = temp

    return jediza


print(fib3(40))