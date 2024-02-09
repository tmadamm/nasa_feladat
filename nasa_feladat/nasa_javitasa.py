def beolvas():
    honapok_gyakorisaga = [0]*12
    with open('astronauts.csv') as bemenet:
        for sor in bemenet.readlines()[1:]:
            sor = sor.strip().split(",")
            honapok_gyakorisaga[int(sor[4].split("/")[0])-1] += 1
    return honapok_gyakorisaga


def leggyakoribb_honapok(honapok_gyak):
    leggyakoribbak = []
    szamlalo = 0
    honapok_gyak_rendezett = sorted(honapok_gyak, reverse=True)
    for _ in range(3):
        kereso = honapok_gyak.index(honapok_gyak_rendezett[szamlalo])+1
        leggyakoribbak.append(kereso)
        szamlalo += 1
    return leggyakoribbak


def szazalekos_kiiratas(leggyakoribbak, honappok_gyak):
    szamlalo = 0
    osszeg = sum(honappok_gyak)
    for _ in range(3):
        legyakoribbak_szazalek = honappok_gyak[leggyakoribbak[szamlalo]-1] / osszeg * 100
        print(f"{leggyakoribbak[szamlalo]} . hónap: {legyakoribbak_szazalek:.1f}%")
        szamlalo += 1


def main():
    honapok_gyakorisaga = beolvas()
    leggyakoribbak = leggyakoribb_honapok(honapok_gyakorisaga)
    szazalekos_kiiratas(leggyakoribbak, honapok_gyakorisaga)


main()
