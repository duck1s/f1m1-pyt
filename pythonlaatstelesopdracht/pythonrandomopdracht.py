import random

dobbelstenen = random.sample(range(1, 6), 3)

dobbelstenen.sort()

print("Kleinste nummer: " + str(dobbelstenen[0]))

antwoord = dobbelstenen[1] + dobbelstenen[2]
print("De twee hoogste nummers bij elkaar opgeteld is: " + str(antwoord))