import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

i = len(people)
while i > 0:
    i -= 1
    if (people[i]) == "Waldo":
        print("Waldo zit op stoel nummer " + str(i))