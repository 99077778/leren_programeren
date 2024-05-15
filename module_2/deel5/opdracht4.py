from fruitmand import fruitmand
import random



hoeveelfruit = int(input('Hoeveel fruit wil je: '))








for fruit in range(hoeveelfruit):
    randomgetal = random.randint(0, len(fruitmand) -1)
    randomfruit1 = fruitmand[randomgetal] ['name']
    print(randomfruit1)


# for fruit in range(hoeveelfruit):
#     randmfruit = random.choice(fruitmand)
#     print(randmfruit['name'])


