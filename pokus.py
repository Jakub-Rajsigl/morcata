def zpracuj_morcata(nazev_souboru):
    with open(nazev_souboru, "r") as soubor:
        for radek in soubor:
            radek = radek.strip()

            casti = radek.split(";")

            jmeno = casti[0]
            hmotnost = int(casti[1])
            datum_narození = casti[2]
            cena = float(casti[3])
            pohlavi = casti[4]

            cena_se_slevou = cena * 0.9

            if pohlavi.lower() == "m":
                druh = "samec"
            else:
                druh = "samice"

            print(f"jmeno: {jmeno}, pohlavi {druh}")
            print(f"hmotnost: {hmotnost} g")
            print(f"datum narození: {datum_narození}")
            print(f"cena: {cena}Kč, cena se slevou: {cena_se_slevou}Kč")

zpracuj_morcata("morcata.txt")