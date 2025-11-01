# CSES 1624 - Chessboard and Queens
# Feladat: 8×8-as táblán ('.' = üres, '*' = tiltott) helyezzünk el 8 királynőt úgy,
# hogy ne üssék egymást, és ne kerüljön tiltott mezőre. Adjuk meg a megoldások számát.
# rekurzió

import sys

def main():
    tabla = [sys.stdin.readline().strip() for _ in range(8)]

    # Foglalt oszlopok és átlók (azonosítók: főátló = sor+oszlop, mellékátló = sor-oszlop)
    foglalt_oszlopok = set()
    foglalt_foatlo   = set()  # sor + oszlop
    foglalt_mellekat = set()  # sor - oszlop

    megoldasok = 0

    def rekurzio(sor: int):
        nonlocal megoldasok
        # Ha mind a 8 sort sikeresen feltöltöttük, találtunk egy elrendezést
        if sor == 8:
            megoldasok += 1
            return

        # Próbáljuk végig a lehetséges oszlopokat az aktuális sorban
        for oszlop in range(8):
            if tabla[sor][oszlop] == '*':
                continue  # tiltott mező

            fo = sor + oszlop
            m  = sor - oszlop

            if (oszlop in foglalt_oszlopok) or (fo in foglalt_foatlo) or (m in foglalt_mellekat):
                continue  # ütközne egy korábbi királynővel

            # Helyezzük el a királynőt
            foglalt_oszlopok.add(oszlop)
            foglalt_foatlo.add(fo)
            foglalt_mellekat.add(m)

            rekurzio(sor + 1)

            # Visszalépés (backtracking)
            foglalt_oszlopok.remove(oszlop)
            foglalt_foatlo.remove(fo)
            foglalt_mellekat.remove(m)

    rekurzio(0)
    print(megoldasok)

if __name__ == "__main__":
    main()
