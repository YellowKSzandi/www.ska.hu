# CSES 1202 - Investigation
# Feladat: legrövidebb utak hossza, darabszáma (mod 1e9+7),
# valamint a legrövidebb utak minimum és maximum él-száma.

# Megoldás: Dijkstra algoritmus kiegészítve útszámlálással.
# gráf

import sys
import heapq

def main():
    adatok = sys.stdin.read().strip().split()
    it = iter(adatok)
    n = int(next(it))  # csúcsok száma
    m = int(next(it))  # élek száma

    # Szomszédsági lista: (szomszéd, súly)
    szomszedok = [[] for _ in range(n + 1)]
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        suly = int(next(it))
        szomszedok[a].append((b, suly))

    VEGTELEN = 10**19
    MOD = 10**9 + 7

    tav = [VEGTELEN] * (n + 1)  # legrövidebb távolság
    utak_szama = [0] * (n + 1)  # hány legrövidebb út vezet ide
    min_el = [10**18] * (n + 1)  # legrövidebb úton minimum él-szám
    max_el = [-10**18] * (n + 1) # legrövidebb úton maximum él-szám

    # Kiindulópont: 1. csúcs
    tav[1] = 0
    utak_szama[1] = 1
    min_el[1] = 0
    max_el[1] = 0

    # Prioritási sor (min-heap)
    sor = [(0, 1)]  # (aktuális_távolság, csúcs)

    while sor:
        akt_tav, u = heapq.heappop(sor)
        if akt_tav != tav[u]:
            continue  # már jobb értéket találtunk korábban

        for v, suly in szomszedok[u]:
            uj_tav = akt_tav + suly

            # Jobb (rövidebb) út találtunk
            if uj_tav < tav[v]:
                tav[v] = uj_tav
                utak_szama[v] = utak_szama[u]
                min_el[v] = min_el[u] + 1
                max_el[v] = max_el[u] + 1
                heapq.heappush(sor, (uj_tav, v))

            # Ugyanilyen hosszú út — bővítjük a kombinációkat
            elif uj_tav == tav[v]:
                utak_szama[v] = (utak_szama[v] + utak_szama[u]) % MOD
                min_el[v] = min(min_el[v], min_el[u] + 1)
                max_el[v] = max(max_el[v], max_el[u] + 1)

    # Eredmény: a célcsúcs (n) értékei
    print(tav[n], utak_szama[n] % MOD, min_el[n], max_el[n])

if __name__ == "__main__":
    main()
