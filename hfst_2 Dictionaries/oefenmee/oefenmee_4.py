# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
sleutelnummer = input("Geef een sleutelnummer: ")
if sleutelnummer in fruitmand:
    print(f"aantal {sleutelnummer}(en) in fruitmand: {fruitmand[sleutelnummer]}")