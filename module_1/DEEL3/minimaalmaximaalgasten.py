MIJN_NAAM = 'oskar'
SLB_NAAM = "jouke"

gastheer = input('Wie is de gastheer: ').lower()

gasten = int(input('Hoeveel gasten: '))

drank = 0
chips = 0


start1 = gastheer == MIJN_NAAM
start2 = gasten and chips and drank
start3 = gastheer and drank
start4 = gastheer != SLB_NAAM or 20 >= gasten >=4



if (start1) or ((start2) or (start3)) and start4:
    print('Start the Party')
else:

    print('No party')




