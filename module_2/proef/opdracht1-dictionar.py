import random

namenlijstmetlootjes = {}

hoveelnamen = 0


stoppen = ''
while stoppen != 'nee':
    naam = input('voer een naam in: ').lower()
    if naam in namenlijstmetlootjes:
        print('deze naam is al toegevoegd')
    elif naam == 'stop':
        print('deze naam mag niet in de lijst')
        
    elif naam not in namenlijstmetlootjes:
        namenlijstmetlootjes.append(naam)

        print(f'{naam} is toegevoegd')
        hoveelnamen += 1
        if hoveelnamen >= 3:
            stoppen = input('wil je nog een naam toevoegen? (ja/nee): ').lower()

namenlijst = list(namenlijstmetlootjes.keys())
lootjes = list(namenlijstmetlootjes.values())
random.shuffle(lootjes)

while True:
    match = False
    for naam, lootje in namenlijstmetlootjes.items():
        if lootje == naam:
            match = True
            random.shuffle(list(namenlijstmetlootjes.values()))
            break
    if not match:
        break

naam_vragen = ''

while naam_vragen != 'stop':
    naam_vragen = input('wiens lootje wil je kijken? of typ stop: ')
    if naam_vragen in namenlijstmetlootjes:
        print(f'{naam_vragen} heeft lootje van {namenlijstmetlootjes[naam_vragen]}')
    else:
        if naam_vragen != 'stop':
            print('deze naam is niet toegevoegd')
