koder = {
    "A" : "00",
    "B" : "01",
    "C" : "10",
    "D" : "11"
}

izlaz = ""
ulaz = "AABACDACA"

for el in ulaz:
    izlaz += koder[el]

print(izlaz)