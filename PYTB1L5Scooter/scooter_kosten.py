def bereken_maandkosten(km_per_maand):
    verzekering_per_maand = 23
    benzine_kosten_per_liter = 1.54
    liter_per_kilometer = 0.2

    maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter + verzekering_per_maand)
    return maandkosten

def main():
    kmamount = ""
    while not isinstance(kmamount, float):
        try:
            kmamount = input("Hoeveel kilometer rijd jij per maand?: ")
            kmamount = float(kmamount)
            bedrag = bereken_maandkosten(int(kmamount))
            print("Het bedrag dat jij per maand aan je scooter uitgeeft is €" + str(bedrag))
        except ValueError:
            print("Dat is geen getal. Probeer opnieuw")
            main()

main()