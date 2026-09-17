versie = 0
while versie == 0:
    Telefoonnummers = ["+31601234567","+32610592015","+31630201050"]
    Presonen =        ["Jan","Piet","Klaas"]
    naam = input("naam: ")
    if naam in Presonen:
        print("naam:", naam)
        print("Telefoonnummer:", Telefoonnummers[Presonen.index(naam)])

#dictionary-variant van bovenstaande code:
while versie == 1:
    telefoonboek = {
        "Jan": "+31601234567",   #element 1
        "Piet": "+32610592015",  #element 2
        "Klaas": "+31630201050"  #element 3
    }
    naam = input("naam: ")
    if naam in telefoonboek:
        print("naam:", naam)
        print("Telefoonnummer:", telefoonboek[naam])

# #nieuwe waarde toevoegen aan de dictionary:
# telefoonboek["Henk"] = "+31612345678"  #element 4

# #een waarde wijzigen in de dictionary:
# telefoonboek["Jan"] = "+31698765432"  #wijzigt element 1

# #een waarde verwijderen uit de dictionary:
# del telefoonboek["Piet"]  #verwijdert element 2

# #element opzoeken in de dictionary:
# if "jan" in telefoonboek:
#     print("Jan is aanwezig in het telefoonboek.")

# if "fioejfimz" in telefoonboek:
#     print("jan is aanwezig in het telefoonboek.")

#opgave: vraag de gebruiker voor de naam en print het nummer dat bij de naam hoort:
naam = input("naam: ")
if naam in telefoonboek:
    print("naam:", naam)
    print(f"element nummer {list(telefoonboek.keys()).index(naam) + 1} in telefoonboek.")