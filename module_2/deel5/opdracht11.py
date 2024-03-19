from fruitmand import fruitmand



fruitkleuren = []

for fruit in fruitmand:
    if fruit['color'] not in fruitkleuren:
        fruitkleuren.append(fruit['color'])
print(fruitkleuren)


while True:
    fruitvraag = input(f'welke kleur fruit wil je, kies uit {fruitkleuren}: ')
    if fruitvraag in fruitkleuren:
        break
    else:
        print(f'de kleur {fruitvraag} is niet in de lijst')




rondefruit = 0
niet_rondefruit = 0


for fruit in fruitmand:
    if fruit['color'] == fruitvraag:
        if fruit['round']:
            rondefruit +=1
        else:
            niet_rondefruit +=1

verschil = (rondefruit - niet_rondefruit)

if verschil > 0:
    print(f'er is {abs(verschil)} meer ronde fruit in deze kleur {fruitvraag}')
elif verschil < 0:
    print(f'er is {abs(verschil)} minder ronde fruit in deze kleur {fruitvraag}')
else:
    print(f'er zijn evenveel ronde als niet ronde fruit in deze kleur {fruitvraag}')


