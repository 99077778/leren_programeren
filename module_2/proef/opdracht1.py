import random

namenlijst = []

hoveelnamen = 0


stoppen = ''
while stoppen != 'nee':
    naam = input('voer een naam in: ').lower()
    if naam in namenlijst:
        print('deze naam is al toegevoegd')
    elif naam not in namenlijst:
        namenlijst.append(naam)
        print(f'{naam} is toegevoegd')
        hoveelnamen += 1
        if hoveelnamen >= 3:
            stoppen = input('wil je nog een naam toevoegen? (ja/nee): ').lower()




lootjes = list(namenlijst)
random.shuffle(lootjes)

# #lootjes opnieuw shuffelen als iemand zijn eigen lootje heeft
# for i in range(len(namenlijst)):
#     while lootjes[i] == namenlijst[i]:
#         random.shuffle(lootjes)


# #lootjes onder elkaar printen
# for i in range(len(namenlijst)):
#     print(f'{namenlijst[i]} heeft {lootjes[i]}.')





while True:
    match = True
    for x in range(len(namenlijst)):
        print(x)
        if lootjes[x] == namenlijst[x]:
            match = False
            random.shuffle(lootjes)
            break
    if match:
        break

for i in range(len(namenlijst)):
    print(f'{namenlijst[i]} heeft {lootjes[i]}.')