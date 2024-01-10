


import random

menm = ('oranje', 'blauw', 'groen', 'bruin')
#menms = []

hoeveel_totaal = int(input('Hoeveel MenM wil je: '))


aantal_perkleur = {kleur: random.randint(1, hoeveel_totaal) for kleur in menm}
totaal = sum(aantal_perkleur.values())


factor = hoeveel_totaal / totaal
aantal_perkleur = {kleur: int(aantal * factor) for kleur, aantal in aantal_perkleur.items()}


verschil = hoeveel_totaal - sum(aantal_perkleur.values())
aantal_perkleur[menm[-1]] += verschil

for kleur, aantal in aantal_perkleur.items():
    print(f'{kleur} = {aantal}')

print(f'totaal = {sum(aantal_perkleur.values())}')