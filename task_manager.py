
ukoly = []

def pridat_ukol():
    global ukoly
    ukol_nazev = str(input("\nZadej název úkolu: "))
    ukol_popis = str(input("Zadej popis úkolu: "))
    ukoly.append({"nazev": ukol_nazev, "popis": ukol_popis})
    print(f"Úkol '{ukol_nazev}' byl přidán.")

def zobrazit_ukoly():
    if not ukoly:
        print("\nSeznam úkolu je prázdný.")
        return
    
    print("\nSeznam úkolů:")

    for i, ukol in enumerate(ukoly, 1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukoly():
        if not ukoly:
            print("\nSeznam úkolu je prázdný.")
            return

        zobrazit_ukoly()
        try:
                cislo_ukolu = int(input("\nZadejte číslo úkolu, který chcete odstranit: "))

                if 1 <= cislo_ukolu <= len(ukoly):
                     odstraneny = ukoly.pop(cislo_ukolu - 1)
                     print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
                else:
                     print("Neplatné číslo úkolu.")

        except ValueError:
              print("Musíš zadat číslo.")

def hlavni_menu():
    while True:
        volba = int(input(  " \n"
                "Správce úkolů - Hlavní menu\n"
                "1. Přidat nový úkol\n"
                "2. Zobrazit všechny úkoly\n"
                "3. Odstranit úkol\n"
                "4. Konec programu\n"
                f"Vyberte možnost (1-4): "
                ))

        match volba:
            case 1:
                pridat_ukol()
            case 2:
                zobrazit_ukoly()
            case 3:
                odstranit_ukoly()
            case 4:
                print("\nKonec programu.")
                break
            case _:
                print("Neplatná volba.")


hlavni_menu()
