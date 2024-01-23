import math
# GewuenschteEnergie = 50, MaxGewicht = 1000
GewuenschteEnergie = float(input("Wie viele Wattstunden sind gewuenscht?"))

print("")

MaxHoehe = input("Gibt es eine Maximal Höhe (Ja/Nein)")
while MaxHoehe != "Ja" and MaxHoehe != "Nein":
    print("Ungueltige Antwort")
    MaxHoehe = input("Gibt es eine Maximal Höhe (Ja/Nein)")

 
if MaxHoehe == "Ja":
    MaxHoehe = float(input("Welche Maximal Höhe in Metern?"))

if MaxHoehe == "Nein":
    MaxHoehe = math.inf

print("")

MaxGewicht = input("Gibt es ein Maximal Gewicht?(Ja/Nein)")
while MaxGewicht!= "Ja" and MaxGewicht != "Nein":
    print("Ungueltige Antwort")
    MaxGewicht = input("Gibt es ein Maximal Gewicht? (Ja/Nein)")
    
if MaxGewicht == "Ja":
    MaxGewicht = float(input("Welches Maximal Gewicht in Kilo?"))
    
if MaxGewicht == "Nein":
    MaxGewicht = math.inf

print("")

GewuenschteEnergie = GewuenschteEnergie*3600
moeglich = 1
hoehe = 0
gewicht = 0
erdbeschleunigung = 9.81
eigentlicheEinergie = 0
while hoehe*gewicht*erdbeschleunigung < GewuenschteEnergie:
    if hoehe < MaxHoehe -0.1 :
        hoehe = hoehe + 0.1
    if gewicht < MaxGewicht -0.1 :
        gewicht = gewicht+ 0.1
    else:
        eigentlicheEinergie = hoehe*gewicht*erdbeschleunigung
        print("Die Bedingung kann nicht erfüllt werden!")
        print("Dieses Gewicht kann nur ", eigentlicheEinergie/3600 ,"Wattstunden Energie Speichern!")
        print("Du bräuchtest ca. ", round(GewuenschteEnergie/eigentlicheEinergie) ,"von diesen Gewichten um ", GewuenschteEnergie/3600 ,"Wattstunden zu Speichern")
        moeglich = 0
        break

if moeglich == 1:  
    print ("Das Gewicht muss in einer Höhe von ", round(hoehe) ,"Metern aufgehangen werden...")
    print ("und ", round(gewicht) ,"Kilo schwer sein!")

print("Der Wirkungsgrad ist in diesen Werten nicht berücksichtigt!")

# final Version M.J. JuFo 2024
