

MAX_GEWICHT = 120
MIN_GEWICHT = 90
MAX_LANGTE = 220
MIN_LANGTE = 150

print('sollicitatieformulier Circusdirecteur')
print('')
print('er wordt u een antal relevante vragen gesteld...')
print('Gelive die naar eer en geweten in te vullen')
print('Als blijkt dat u aan de criteria voldoet dan komt u in aanmerking voor een serieus sollicitatiegesprek!')
print('Ontspan maar blijf wakker , hier komen de vragen')
print('')


#sollicitati eisen
vrachtwagen_rijbewijs = input('Ben je in bezit van een geldige vrachtwagen rijbewijs (ja/nee): ')
hoed = input('Ben je in bezit van een hoge hoed? (ja/nee): ')
gewicht = float(input('Wat is jou gewicht? (in KG): '))
langte = int(input('Hoe lang ben je? (in CM): '))
certificaat = input('Heeft Certificaat Overleven met gevaarlijk personeel (ja/nee): ')
dieren_dressuur = int(input('hoe veel jaar/jaren heb je ervaring met praktijkervaring met dieren-dressuur (voer cijfer in): '))
jongleren = int(input('hoe veel jaar ervaring heb je met jongleren (voer cijfer in): '))
acrobatiek = int(input('hoe veel jaar ervaring heb je met acrobatiek (voer cijfer in): '))


geschikt = vrachtwagen_rijbewijs == 'ja' and hoed == 'ja' and gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT and langte >= MIN_LANGTE and langte <= MAX_LANGTE and certificaat == 'ja' and (dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3)


if geschikt:
    print('Gefeliciteerd je komt in aanmerking voor deze functie ')
    
else:
    print('u voldoet niet aan onze strenge eizen voor de functie Circusdirecteur, Helaas het spijt ons ')








