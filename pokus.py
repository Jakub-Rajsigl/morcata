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
                druh = "Sameček"
            else :
                druh = "Samice"

            print(f"- Pohlaví zvířete: {pohlavi}, jméno {jmeno}")
            print(f"- Váží: {hmotnost} g")
            print(f"- Datum narození: {datum_narození}")
            print(f"- Cena se slevou: {cena_se_slevou}Kč, 90% z ceny {cena} Kč")

zpracuj_morcata("morcata.txt")