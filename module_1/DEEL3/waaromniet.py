

MAX_GEWICHT = 120
MIN_GEWICHT = 90
MAX_LANGTE = 220
MIN_LANGTE = 150

print('sollicitatieformulier Circusdirecteur')
print('')
print('Er worden u een aantal relevante vragen gesteld...')
print('Gelieve die naar eer en geweten in te vullen')
print('Als blijkt dat u aan de criteria voldoet, dan komt u in aanmerking voor een serieus sollicitatiegesprek!')
print('Ontspan maar blijf wakker, hier komen de vragen')
print('')

# Sollicitatie eisen
vrachtwagen_rijbewijs = input('Ben je in bezit van een geldige vrachtwagen rijbewijs (ja/nee): ')
hoed = input('Ben je in bezit van een hoge hoed? (ja/nee): ')
gewicht = float(input('Wat is jouw gewicht? (in KG): '))
langte = int(input('Hoe lang ben je? (in CM): '))
certificaat = input('Heb je een certificaat "Overleven met gevaarlijk personeel" (ja/nee): ')
dieren_dressuur = int(input('Hoeveel jaar ervaring heb je met dieren-dressuur (voer een cijfer in): '))
jongleren = int(input('Hoeveel jaar ervaring heb je met jongleren (voer een cijfer in): '))
acrobatiek = int(input('Hoeveel jaar ervaring heb je met acrobatiek (voer een cijfer in): '))
geslacht = input('Wat is jouw geslacht (man/vrouw/anders): ')

# extra eisen
if geslacht == 'man':
    snor = input('Heb je een snor? (ja/nee): ')
    snor_voldoet = snor == 'ja'
elif geslacht == 'vrouw':
    haar = input('Heb je rood krulhaar? (ja/nee): ')
    haar_voldoet = haar == 'ja'
else:
    brede_glimlach = input('Heb je een brede glimlach? (ja/nee): ')
    brede_glimlach_voldoet = brede_glimlach == 'ja'

criteria_niet_voldaan = []

if (vrachtwagen_rijbewijs != 'ja'):
    criteria_niet_voldaan.append('Je hebt geen geldig vrachtwagen rijbewijs.')

if (hoed != 'ja'):
    criteria_niet_voldaan.append('Je hebt geen hoge hoed.')

if not (MIN_GEWICHT <= gewicht <= MAX_GEWICHT):
    criteria_niet_voldaan.append('Je voldoet niet aan de eisen voor gewicht.')

if not (MIN_LANGTE <= langte <= MAX_LANGTE):
    criteria_niet_voldaan.append('Je voldoet niet aan de eisen voor lengte.')

if (certificaat != 'ja'):
    criteria_niet_voldaan.append('Je hebt geen certificaat "Overleven met gevaarlijk personeel".')

if (dieren_dressuur < 4 and jongleren < 5 and acrobatiek < 3):
    criteria_niet_voldaan.append('Je hebt niet voldoende ervaring met dieren-dressuur, jongleren en acrobatiek.')

if (geslacht == 'man' and not snor_voldoet):
    criteria_niet_voldaan.append('Je voldoet niet aan het bizarre eis van een snor.')

if (geslacht == 'vrouw' and not haar_voldoet):
    criteria_niet_voldaan.append('Je voldoet niet aan het bizarre eis van rood krulhaar.')

if (geslacht == 'anders' and not brede_glimlach_voldoet):
    criteria_niet_voldaan.append('Je voldoet niet aan het bizarre eis van een brede glimlach.')


if not criteria_niet_voldaan:
    print('Gefeliciteerd je komt in aanmerking voor deze functie')
else:
    print('je voldoet niet aan onze strenge eisen voor de functie circusdirecteur. Reden voor afwijzing:')
    for reden in criteria_niet_voldaan:
        print(reden)
