from fruitmand import fruitmand
import random



hoeveelfruit = int(input('Hoeveel fruit wil je: '))


for fruit in range(hoeveelfruit):
    randmfruit = random.choice(fruitmand)
    print(randmfruit['name'])




