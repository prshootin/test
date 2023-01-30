niz = input().split()
niz = [int(x) for x in niz]


def nedostaje(niz):
    """
    U program se unosi lista 
 koja sadrži 
 cjelobrojnih vrijednosti koje su u rasponu od 
 do 
, u unesenoj listi nedostaje jedan broj iz intervala od 
 do 
. Program zatim ispisuje broj koji nedostaje u unesenoj listi.
    """
    pocetak = min(niz)
    kraj = max(niz)
    rez = 0

    for el in niz:
        rez = rez ^ el

    for i in range(pocetak, kraj + 1):
        rez = rez ^ i

    return rez


print(nedostaje(niz))