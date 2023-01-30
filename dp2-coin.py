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
