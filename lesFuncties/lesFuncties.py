def add(getal01, getal02):
    print(str(getal01)+" keer "+str(getal02)+" is "+str(getal01*getal02))

def lengte(woord):
    print("De lente van de string is "+str(len(woord))+" letters")

lengte("kaasappels")
add(30, 50)
print(" ")

#Volgende opdracht

import random

def roll_dice():
    random_getal = random.randrange(1, 6)
    return random_getal

roll01 = roll_dice()
print(roll01)
roll02 = roll_dice()
print(roll02)