# CSES 3420 - Különböző értékű résztömbök száma
# Sliding window (csúszó ablak) megoldás:
# minden lépésben annyival bővítjük a résztömbök számát, ahány új egyedi elemet tartalmaz.
# rendezéses

import sys

def main():
    adatok = list(map(int, sys.stdin.read().strip().split()))
    if not adatok:
        return

    n = adatok[0]      # elemek száma
    tomb = adatok[1:]  # maga a lista

    utolso = {}         # elem -> utolsó előfordulás indexe
    bal = 0             # ablak bal széle
    osszeg = 0          # különböző értékű résztömbök száma

    for jobb, ertek in enumerate(tomb):
        # Ha ez az elem már szerepelt az aktuális ablakban, toljuk a bal szélét tovább
        if ertek in utolso and utolso[ertek] >= bal:
            bal = utolso[ertek] + 1

        utolso[ertek] = jobb
        # Minden új pozícióval annyi új egyedi résztömb keletkezik, ahány hosszú az ablak
        osszeg += jobb - bal + 1

    print(osszeg)

if __name__ == "__main__":
    main()
