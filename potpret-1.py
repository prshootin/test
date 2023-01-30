import itertools

niz = [0, 1, 2]

for x in range(len(niz) + 1):
    permutacije = itertools.combinations(niz, x)
    for el in permutacije:
        print(el)



