def voeg_toe(index, getal, lijst):
    """ return een gewijzigde lijst 
    
        Deze lijst is hetzelfde als de oude,
        maar variabele getal is toegevoegd op index.
    """


# [8, 3]
print( voeg_toe(-1, 8, [3]) )    
# [0, 1, 2, 3, 4, 5]           
print( voeg_toe( 0, 0, [1, 2, 3, 4, 5]) )   
# [7, 6, 8, 10, 12, 2]
print( voeg_toe( 3, 10, [7, 6, 8, 12, 2]) )  
