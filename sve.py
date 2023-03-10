#Vremenska slozenost

#vrsloz1
#Zadan je niz od n brojeva, naš zadatak je izračunati najveći zbroj podniza, tj. najveći mogući zbroj niza uzastopnih vrijednosti u nizu.
ulaz = [-1, 2, 4, -3, 5, 2, -5, 2]
najv = 0
for i in range(0, len(ulaz)):
    for j in range(i, len(ulaz)):
        suma = 0
        for k in range(i, j):
            suma += ulaz[k]
        if suma > najv:
            najv = suma

print(najv)

#Potpuno pretrazivanje

#Zadatak 1: Generiranje podskupova
import itertools

niz = [0, 1, 2]

for x in range(len(niz) + 1):
    permutacije = itertools.combinations(niz, x)
    for el in permutacije:
        print(el)

#Zadatak 4 K-sum Meet in the middle
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


#Pohlepni algoritmi

#Zadatak 1 - Problem s kovanicama, kovanice
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

#Zadatak 3 - upis predmeta, raspored

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


#Dinamicko programiranje

#Zadatak 1 - Fibonacci

def fib1(n):
   if n <= 1:
       return n
   else:
       return(fib1(n-1) + fib1(n-2))


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



#Zadatak 2: Problem s kovanicama
kovanice = [5, 9]
def solve(x):
    if x==0:
        return 0
    if x<0:
        return float("inf")
    best = float("inf")
    for el in kovanice:
        best = min(best, solve(x-el) + 1)
    
    return best

print(solve(4))

#Zadatak 3 - Stubiste, stepenice

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

#Bit manipulation

#Zadatak 1 - Element bez ponavljanja

l = [2, 2, 1]

rez = 0

for el in l:
    rez = rez ^ el

print(rez)

#Zadatak 2 - Hammingova tezina - broj bitova 1
n = str(input())
b = int(n, 2)

r = 0

while(b):
    r += b%2
    b = b >> 1

print(r)

#Zadatak 3 - Broj koji nedostaje u listi
niz = input().split()
niz = [int(x) for x in niz]

def nedostaje(niz):
    pocetak = min(niz)
    kraj = max(niz)
    rez = 0

    for el in niz:
        rez = rez ^ el

    for i in range(pocetak, kraj + 1):
        rez = rez ^ i

    return rez

print(nedostaje(niz))


# ALGORITMI

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend([i for i in graph[vertex] if i not in visited])
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend([i for i in graph[vertex] if i not in list(visited)])

    return visited


def get_Susjed(m, node):
    susjedi = []
    
    for ix, dist in enumerate(m[node]):
        if dist != 0:
            susjedi.append(ix)
    
    return susjedi

def dijkstra(matrica, pocetniCvor):
    not_visited = [x for x in range(0, len(matrica))]
    shortest_paths = {}
    prev_nodes = {}
    for node in not_visited:
        shortest_paths[node] = float("inf")
    shortest_paths[pocetniCvor] = 0
    while not_visited:
        curr_node = None
        for node in not_visited:
            if curr_node == None:
                curr_node = node
            elif shortest_paths[node] < shortest_paths[curr_node]:
                curr_node = node

        susjedi = get_Susjed(matrica, curr_node)

        for h in susjedi:
            temp = shortest_paths[curr_node] + matrica[curr_node][h]
            if temp < shortest_paths[h]:
                shortest_paths[h] = temp
        not_visited.remove(curr_node)

    return shortest_paths


def top_sort(g):
    visited = set()
    stack = []
    for vertex in g:
        if vertex not in visited:
            dfs(g, vertex, visited, stack)
    print(stack[::-1])


def floyd_warshall(G):
    udaljenost = list(map(lambda i: list(map(lambda j: j, i)), G))


    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                udaljenost[i][j] = min(udaljenost[i][j], udaljenost[i][k] + udaljenost[k][j])


