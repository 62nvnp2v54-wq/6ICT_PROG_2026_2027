# Voorbeeld woord als 'lijst'.
woord = "hallo!"
for index, letter in enumerate(woord):
    print(f"Karakter {index+1}: {letter}")

# Voorbeeld lijst van woorden als 'geneste lijst'.
namen = ["Jan", "Piet"]
for i, naam in enumerate(namen):
    for j, letter in enumerate(naam):
        print(f"{i},{j}: {letter}")

# Niveau 1
namen = ["jan", "piet", "joris", "korneel"]


# Niveau 2
namen = ["jan", "piet", "joris", "korneel"]


