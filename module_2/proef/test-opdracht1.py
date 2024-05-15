import random
import string

namenlijst = []

hoveelnamen = 0

aantalnamen = random.randint(3000,8000)





def generate_random_name():
    name_length = random.randint(3, 10)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(name_length))



stoppen = 0
while stoppen != 1:
    naam = generate_random_name()
    if naam in namenlijst:
        print('deze naam is al toegevoegd')
    elif naam not in namenlijst:
        namenlijst.append(naam)
        print(f'{naam} is toegevoegd')
        hoveelnamen += 1
        if hoveelnamen >= aantalnamen:
            stoppen = 1




lootjes = list(namenlijst)
random.shuffle(lootjes)

# #lootjes opnieuw shuffelen als iemand zijn eigen lootje heeft
# for i in range(len(namenlijst)):
#     while lootjes[i] == namenlijst[i]:
#         random.shuffle(lootjes)




# #lootjes onder elkaar printen
# for i in range(len(namenlijst)):
#     if namenlijst[i] == lootjes[i]:
#         print(f'{namenlijst[i]} heeft {lootjes[i]}.')




while True:
    match = True
    for x in range(len(namenlijst)):
        if lootjes[x] == namenlijst[x]:
            match = False
            random.shuffle(lootjes)
            break
    if match:
        break

for i in range(len(namenlijst)):
    if namenlijst[i] == lootjes[i]:
        print(f'{namenlijst[i]} heeft {lootjes[i]}.')