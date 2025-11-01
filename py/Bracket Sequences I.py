# CSES 2064 - Helyes zárójelezések száma
# A feladat: hány különböző helyes zárójelezést alkothatunk n zárójellel.
# Ez a híres Catalan-szám: C_k = (1 / (k + 1)) * (2k alatt k)
# Csak páros n esetén értelmezett (n = 2 * k).
# dinamikus programozás

MOD = 10**9 + 7

def main():
    n = int(input())

    # Ha n páratlan, nem alkotható helyes zárójelezés
    if n % 2 == 1:
        print(0)
        return

    k = n // 2
    max_ertek = 2 * k

    # Faktoriálisok és inverzek előállítása 1..max_ertek tartományban
    faktorialis = [1] * (max_ertek + 1)
    inverz = [0] * (max_ertek + 1)
    inverz[1] = 1  # 1 inverze mindig 1

    # Inverzek kiszámítása lineárisan (Fermat-tétel nélkül)
    for i in range(2, max_ertek + 1):
        inverz[i] = MOD - (MOD // i) * inverz[MOD % i] % MOD

    # Inverz faktoriálisok előállítása
    inverz_faktorialis = [1] * (max_ertek + 1)
    for i in range(1, max_ertek + 1):
        faktorialis[i] = faktorialis[i - 1] * i % MOD
        inverz_faktorialis[i] = inverz_faktorialis[i - 1] * inverz[i] % MOD

    # Binomiális együttható: (2k alatt k)
    kombinacio = (
        faktorialis[2 * k] *
        inverz_faktorialis[k] % MOD *
        inverz_faktorialis[k] % MOD
    )

    # Catalan-szám: (kombinacio / (k + 1))
    catalan = kombinacio * inverz[k + 1] % MOD

    print(catalan)

if __name__ == "__main__":
    main()
