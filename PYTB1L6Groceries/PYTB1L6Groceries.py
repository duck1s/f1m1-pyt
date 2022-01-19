def compareList(boodschappenlijst, boodschappentas):
   boodschappenlijst.sort()
   boodschappentas.sort()
   if(boodschappentas == boodschappenlijst):
      return "Done Shopping"
   else:
      return "Continue Shopping"

boodschappenlijst = ["Kaas", "Patat"]
boodschappentas = ["Patat", "Kaas"]
print(compareList(boodschappenlijst, boodschappentas))