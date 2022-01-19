from datetime import datetime
datumtijd = datetime.now()

def mainscript():
    print("Hello You, Ik ben Joeri")
    print ("Wie ben jij?")
    naam = input ("")
    print ("Hello "+naam)
    print ("De datum en tijd is " + str(datumtijd))
    print(naam + " wil jij dit programma nog een keer doen?")

def restartscript():
    restart = input("Type Y / N: ")
    if restart == "Y" or restart == "y" or restart == "yes" or restart == "Yes" or restart == "YES":
        mainscript()
    elif restart == "N" or restart == "No" or restart == "NO" or restart == "no" or restart == "n":
        exit()
    else:
        print("Dat is niet Y / N, probeer opnieuw")
        restartscript()

mainscript()
restartscript()