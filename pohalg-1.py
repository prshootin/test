kovanice = [1, 2, 5, 10, 20, 50, 100, 200]

trazeniIznos = 530

while not trazeniIznos==0:
    izlaz = False
    temp = len(kovanice) - 1
    while not izlaz:
        if trazeniIznos >= kovanice[temp]:
            trazeniIznos -= kovanice[temp]
            izlaz = True
            print(kovanice[temp])
        else:
            temp -= 1
