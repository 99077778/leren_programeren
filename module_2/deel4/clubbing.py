PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

import time

leeftijd = int(input('Hoe oud ben je?: '))
naam = ''
bandje = ''
stempel = 0


probeerlater = f'Probeer het in {18 - leeftijd} jaar nog eens'

complimenten = 'Alstublieft, complimenten van het huis'

jecola = f'Alsjeblieft je cola, dat is dan {PRIJS_COLA} euro'
jebier = f'Alsjeblieft je bier, dat is dan {PRIJS_BIER} euro'
jechampagne = f'Alsjeblieft je champagne, dat is dan {PRIJS_CHAMPAGNE} euro'

geenalchol = 'Sorry, je mag geen alcohol bestellen onder de 21'

time.sleep(.5)

if leeftijd < 18:
    print('Sorry je mag niet naar binnen')
    print(probeerlater)
    exit()
else:
    naam = input('Wat is je naam?: ').lower()

if naam in VIP_LIST:
    if leeftijd >= 21:
        bandje = 'blauw'
    else:
        bandje = 'rood'
    print(f'Je krijgt van mij een {bandje} bandje')
else:
    if leeftijd >= 21:
        print('Je krijgt van mij een stempel')
        stempel = 1

drinken = input('wat wil je drinken?: ').lower()

if drinken == 'cola':
    if bandje == 'blauw' or bandje == 'rood':
        print(complimenten)
    else:
        print(jecola)
elif drinken == 'bier':
    if stempel == 1 or bandje == 'blauw' or bandje == 'rood':
        if bandje == 'blauw' or bandje == 'rood':
            print(complimenten)
        else:
            print(jebier)
    else:
        print(geenalchol)
        print(probeerlater)
elif drinken == 'champagne':
    if bandje == 'blauw':
        print(jechampagne)
    elif bandje == 'rood':
        print(geenalchol)
        print(probeerlater)
    else:
        print('Sorry, alleen vips mogen champagne bestellen')
else:
    print('Sorry, geen idee wat je bedoeld, hier een glaasje water')
