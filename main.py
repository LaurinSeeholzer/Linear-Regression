xwerte = [1,2,3]
ywerte = [2,4,6]
xvorgabe = 200
yprediction = 0

xdurchschnitt = (sum(xwerte))/(len(xwerte))
ydurchschnitt = (sum(ywerte))/(len(ywerte))

#Zähler von b bestimmen
Zählerb = 0
z = 0
for i in xwerte:
    x = xwerte[z]
    y = ywerte[z]

    zwischenerg1 = (x - xdurchschnitt)
    zwischenerg2 = (y - ydurchschnitt)
    erg = (zwischenerg1 * zwischenerg2)

    Zählerb = Zählerb + erg
    z = z+1

#Nenner von b bestimmen
Nennerb = 0
z = 0
for i in xwerte:
    x = xwerte[z]

    zwischenerg1 = (x - xdurchschnitt)
    erg = (zwischenerg1 * zwischenerg1)

    Nennerb = Nennerb + erg
    z = z+1


b = Zählerb / Nennerb
#a berechnen
a = ydurchschnitt - (b * xdurchschnitt)

#Endberechnung
yprediction = a + (b * xvorgabe)

#Ausgaben
z = 0
for i in xwerte:
    x = xwerte[z]
    y = ywerte[z]
    z = z+1
    print(x,y)

print("")
print("prediction:")
print(xvorgabe, yprediction)
print("")
