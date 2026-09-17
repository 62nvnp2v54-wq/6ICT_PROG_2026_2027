# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
while True:
    naam = input("naam: ")
    if naam in gasten:
        print(f"welkom, {gasten[naam]} {naam}.")
        gasten.pop(naam)
    elif naam.upper() == "STOP":
        print("programma gestopt.")
        break
    else:
        print(f"Sorry, {naam} staat niet in de gastenlijst.")