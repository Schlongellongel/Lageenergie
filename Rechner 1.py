
# Online Python - IDE, Editor, Compiler, Interpreter
Gewicht = float(input("Wie schwer ist dein Gewicht (in kg)"))
Hoehe = float(input("Wie hoch hängt dein Gewicht (in Meter)"))

Erdbeschleunigung = 9.81
Joule = Gewicht*Hoehe*Erdbeschleunigung
WattStunden = Joule/3600
print("")
print("Dieses Gewicht speichert ",Joule, "Joule Energie!")

print("Das währen", WattStunden ,"Watt Stunden (optimal)")

print("Bei einem Strom preis von 40ct währen das", WattStunden*0.04,"ct, bei maximal hoch aufgehängtem Gewicht.")

Infos = input("Willst du mehr Informationen (Ja/Nein)")

while Infos != "Ja" and Infos != "Nein":
    print("Ungültige Antwort")
    Infos = input("Willst du mehr Informationen (Ja/Nein)")

if Infos == "Ja":
    
    
    print("Die Energie würde reichen um...\n")
    
    if WattStunden<6:
         print("...Leider nichts zu betreiben was mir eingefallen ist!")
    
    
    if WattStunden>=6:
        print("...", WattStunden//6 ,"LED Lampe(n) eine Stunde lang zu betreiben")
        
        if WattStunden>=13:
            print("oder...")
            print("...",WattStunden//13 ,"UKW Radio(s) eine Stunde lang zu beteiben")
        
            if WattStunden>= 60:
                print("oder...")
                print("...", WattStunden//60 ,"Glühbirne(n) eine Stunde lang zu betreiben")
        
                if WattStunden>= 70:
                    print("oder...")
                    print("...", WattStunden//70, "LED Fernseher eine Stunde lang zu betreiben")
        
                    if WattStunden>=100:
                        print("oder...")
                        print("...",WattStunden//100,"LCD Fernseher eine Stunde lang zu betreiben")
        
                        if WattStunden>=170:
                            print("oder...")
                            print("...",WattStunden//170,"Plasma Fernseher eine Stunde lang zu betreiben")
        
                            if WattStunden>=300:
                              print("oder..")
                              print("...",WattStunden//300,"Gaming PC(s) eine Stunde lang zu betreiben")
        
# final Version M.J. JuFo 2024
