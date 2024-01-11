
vertaal_dictonary = {
    'hart': 'ingang',
    'schubben': 'teennagels',
    'vurige': 'waterende',
    'draak': 'geit',
    'vlammenzee': 'golf',
    'schild': 'zwemvliezen',
    'magie': 'plastic'
}


orginele_tekst = input("Voer stukje text in: ")

woorden = orginele_tekst.split() 
vertaalde_text = []

for woord in woorden:
    if woord in vertaal_dictonary:
        vertaalde_text.append(vertaal_dictonary[woord])
    else:
        vertaalde_text.append(woord)

print("vertaalde zin: ")
for vertaalde_woord in vertaalde_text:
    print(vertaalde_woord, end=" ")

#print(" ".join(vertaalde_text))


