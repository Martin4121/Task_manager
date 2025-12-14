
ukoly = []

def pridat_ukol():
    #Funkce pridat_ukol přidá nový úkol do seznamu úkolů s názvem a popisem.

    global ukoly
    ukol_nazev = input("\nZadej název úkolu: ").strip()
    if ukol_nazev == "":
       print("Název úkolu nemůže být prázdný.")
       return

    ukol_popis = input("Zadej popis úkolu: ").strip()
    if ukol_popis == "":
       print("Popis úkolu nemůže být prázdný.")
       return

    ukoly.append({"nazev": ukol_nazev, "popis": ukol_popis})
    print(f"Úkol '{ukol_nazev}' byl přidán.")

def zobrazit_ukoly():
    #Funkce zobrazit_ukoly zobrazí všechny úkoly v seznamu s jejich názvy a popisy.

    if not ukoly:
        print("\nSeznam úkolu je prázdný.")
        return
    
    print("\nSeznam úkolů:")

    for i, ukol in enumerate(ukoly, 1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukoly():
    #Funkce odstranit_ukoly odstraní úkol ze seznamu na základě zadaného čísla úkolu.

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
    #Funkce hlavni_menu zobrazí hlavní menu a umožní uživateli vybrat akce pro správu úkolů.

    while True:
       try:

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

       except ValueError:
              print("\nMusíš zadat číslo.")


hlavni_menu()
