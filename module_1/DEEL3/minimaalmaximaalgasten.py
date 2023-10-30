mijn_naam = 'oskar'
slb_naam = 'jouke'

gastheer = input('Wie is de gastheer: ').lower()

gasten = int(input('Hoeveel gasten: '))

drank = 1
chips = 0


start_mijnnaam = gastheer == mijn_naam
start_gastnchipsdrank = gasten and chips and drank
start_gastheerdrank = gastheer and drank
start_gastheerSLB = gastheer != slb_naam
start_aantalgasten = 20 >= gasten >=4



if (start_mijnnaam) or ((start_gastnchipsdrank) or (start_gastheerdrank)) and (start_gastheerSLB and start_aantalgasten):
    print('Start the Party')
else:
    print('No party')




