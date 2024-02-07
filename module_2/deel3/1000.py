

# Opdracht
# Maak een programma dat de getallen vanaf 50 (dus 50, 51, 53, 54 enzovoort) optelt totdat hun gezamelijke som groter is dan 1000.

# Print elk cijfer en de totale som per iteratie, zoals dit:

# 1. 50 + 51 = 101
# 2. 50 + 51 + 52 = 153
# 3. 50 + 51 + 52 + 53 = 206
# 4. 50 + 51 + 52 + 53 + 54 = 260



waarde = 50

totaal = 0

iritaite = 1

som = 50

while totaal < 1000:
    waarde = waarde +1 #elke keer een erbij
    som = f'{som} + {waarde}' #som uitrekenen
    totaal = totaal + waarde
    print(f"{iritaite}. {som} = {totaal}")
    iritaite += 1

