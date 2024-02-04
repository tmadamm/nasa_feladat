def beolvas():
    elofordulasok = [0]*12
    with open('astronauts.csv') as bemenet:
        for sor in bemenet.readlines()[1:]:
            sor = sor.strip().split(",")
            elofordulasok[int(sor[4].split("/")[0])-1] += 1
    return elofordulasok


def leggyakoribb_ho():
    eloford = beolvas()
    osszeg = sum(eloford)
    return [max_kereses(eloford, osszeg) for _ in range(3)]


def max_kereses(elofordulasok, osszeg):
    max_honap = 0
    jelenlegi_max = 0
    for i in range(len(elofordulasok)):
        if elofordulasok[i] > jelenlegi_max:
            jelenlegi_max = elofordulasok[i]
            max_honap = i
    elofordulasok[max_honap] = 0
    return {max_honap+1: (jelenlegi_max/osszeg)*100}


def main():
    leggyakoribbak = leggyakoribb_ho()
    for ertekek in leggyakoribbak:
        for honap in ertekek:
            print(f"{honap}. hónap: {ertekek[honap]:.1f}%")


main()
