MIJN_NAAM = 'oskar'
SLB_NAAM = 'jouke'

gastheer = input('Wie is de gastheer?')
gasten = 0
drank = 1
chips = 0

start1 = gastheer == MIJN_NAAM
start2 = gasten and chips and drank
start3 = gastheer != SLB_NAAM

if (start1 or (start2 or (gastheer and drank)) and start3):
    print('Start the Party')
else:
    print('No Party')








# MIJN_NAAM = 'oskar'
# SLB_NAAM = 'jouke'

# gastheer = input('wie is de gastheer')
# gasten = 0
# drank = 1
# chips = 0


# start1 = gastheer == MIJN_NAAM
# start2 = gasten and chips and drank = true
# start3 = gastheer !
