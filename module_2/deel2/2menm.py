
import random


menm = ('oranje', 'blauw', 'groen', 'bruin')
menms = []


hoeveel = int(input('Hoeveel MenM wil je: '))


for _ in range(hoeveel):
    menms.append(random.choice(menm))
    #menms.append('oranje')


hoeveeloranje = menms.count('oranje')
hoeveelblauw = menms.count('blauw')
hoeveelgroen = menms.count('groen')
hoeveelbruin = menms.count('bruin')

totaal = hoeveeloranje + hoeveelblauw + hoeveelgroen + hoeveelbruin

#print(menms)


print(f'oranje: {hoeveeloranje}')
print(f'blauw: {hoeveelblauw}')
print(f'groen: {hoeveelgroen}')
print(f'bruin: {hoeveelbruin}')


print(f'totaal: {totaal}')



