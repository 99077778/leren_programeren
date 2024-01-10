
import random


kaarten = ('Klaver', 'Harten', 'Schoppen', 'Ruiten')
waarden = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'Boer', 'Vrouw', 'Heer', 'Joker')


deck = []


for kaart in kaarten:
    for waarde in waarden:
        huidige_kaart = f'{kaart} {waarde}'
        deck.append(huidige_kaart)

        # if kaart == 'Joker':
        #     kaart.split()


random.shuffle(deck)


for _ in range(7):
    print(deck.pop(0))



print(deck)
