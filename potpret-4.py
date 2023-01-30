import itertools

ulaz = [2, 4, 5, 9]
trazise = 15
a = ulaz[:len(ulaz)//2]
b = ulaz[len(ulaz)//2:]

def suma(niz):
    sume = []
    for x in range(len(niz) + 1):
        permutacije = itertools.combinations(niz, x)
        for el in permutacije:
            print(el)
            sume.append(sum(el))
    return sume

Sa = suma(a)
Sb = suma(b)

moguce=False
for i in Sa:
    for j in Sb:
        if i + j == trazise:
            moguce=True

if moguce:
    print("YES")
else:
    print("no")
