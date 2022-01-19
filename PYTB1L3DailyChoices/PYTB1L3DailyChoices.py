print("1 + 1 =")
antwoord1 = input("Antwoord: ")
if antwoord1 == "2":
    print("2 + 2 =")
    antwoord2 = input("Antwoord: ")
    if antwoord2 == "4":
        print("4 + 4 =")
        antwoord3 = input("Antwoord: ")
        if antwoord3 == "8":
            print("5 + 5 =")
            antwoord4 = input("Antwoord: ")
            if antwoord4 == "10":
                print("10 + 10 =")
                antwoord5 = input("Antwoord: ")
                if antwoord5 == "20":
                    print("Goed")
                else:
                    print("Fout")
            else:
                print("Fout")
        else:
            print("Fout")
    else:
        print("Fout")
else:
    print("Fout")