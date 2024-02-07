# waarde = 50
# totaal = 0
# iteratie = 1
# som = str(waarde)

# while totaal < 1000:
#     totaal += waarde # Voeg de waarde toe aan de totaal
#     print(f"{iteratie}. {som} = {totaal}") # Print de huidige iteratie en de som van alle getallen
#     iteratie += 1 # Verhoog de itiratie met 1
#     waarde += 1 # verhoog de waarde met 1
#     som += f" + {waarde}" #  Maak een string van de som

#     print("De som van alle getallen is 1000.")





totaal = 50
links_som = '50'
next_getal = 51


while totaal < 1000:
    totaal += next_getal
    links_som += f" + {next_getal}"
    next_getal +=1
    print(f'{links_som} = {totaal}')






# totaal = 750
# links_som = '750'
# next_getal = 753


# while totaal < 15000:
#     totaal += next_getal
#     links_som += f" + {next_getal}"
#     next_getal +=1
#     print(f'{links_som} = {totaal}')