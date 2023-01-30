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
