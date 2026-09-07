def opzoeken_persoon(lijst, naam):
    "return het nummer overeenkomstig met de naam."


telefoonboek = [
    ["Jan Jans", "+32 470 998301"],
    ["Piet Joris", "+32 483 313220"],
    ["Kor Neel", "+32 453 231456"],
    ["Piet Dirkx", "+31 269 542463"]
]

# +32 470 998301
print( opzoeken_persoon(telefoonboek, "Jan Jans") )
# +31 269 542463
print( opzoeken_persoon(telefoonboek, "Piet Dirkx") )