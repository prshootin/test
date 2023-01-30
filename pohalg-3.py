vremena = [[8, 9], [11, 13], [9, 10], [8, 14], [15, 17], [10, 12], [8, 10]]

def zavrsetak(x):
    return x[1]

vremena.sort(key=zavrsetak)
raspored = []
#print(vremena)

trenutniZavrsetak = 0
for el in vremena:
    if el[0] >= trenutniZavrsetak:
        trenutniZavrsetak = el[1]
        raspored.append(el)

for el in raspored:
    print(el)
