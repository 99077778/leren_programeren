PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')



import time

#bouw hieronder de floowchart na

leeftijd = int(input('Hoe oud ben je?: '))
bandje = 'rood'
naam = ''
verder = 'nee'

time.sleep(.5)

if leeftijd < 18:
    print('Sorry je mag niet naar binnen')
    print(f'Probeer het in {18 - leeftijd} jaar nog eens')

else:
    naam = input('Wat is je naam?: ').lower()


if naam in VIP_LIST:
    if leeftijd >=21:
        bandje = 'blauw'
    print(f'Je krijgt van mij een {bandje} bandje')
    verder = 'ja'
else:
    if leeftijd >=21:
        print('Je krijgt van mij een stempel')
    verder = 'ja'

if verder == 'ja': 
    print('wat wil je drinken')