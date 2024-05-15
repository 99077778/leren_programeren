import random

namenlijst = []

hoveelnamen = 0


stoppen = ''
while stoppen != 'nee':
    naam = input('voer een naam in: ').lower()
    if naam in namenlijst:
        print('deze naam is al toegevoegd')
    elif naam == 'stop':
        print('deze naam mag niet in de lijst')
        
    elif naam not in namenlijst:
        namenlijst.append(naam)

        print(f'{naam} is toegevoegd')
        hoveelnamen += 1
        if hoveelnamen >= 3:
            stoppen = input('wil je nog een naam toevoegen? (ja/nee): ').lower()

lootjes = list(namenlijst)
print(lootjes)
random.shuffle(lootjes)



while True:
    match = False
    for x in range(len(namenlijst)):
        if lootjes[x] == namenlijst[x]:
            match = True
            random.shuffle(lootjes)
            break
    if not match:
        break


naam_vragen = ''

while naam_vragen != 'stop':
    naam_vragen = input('wiens lootje wil je kijken? of typ stop: ')
    if naam_vragen in namenlijst:
        positie = namenlijst.index(naam_vragen)
        print(f'{naam_vragen} heeft lootje van {lootjes[positie]}')
    else:
        if naam_vragen != 'stop':
            print('deze naam is niet toegevoegd')