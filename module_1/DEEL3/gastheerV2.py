mijn_naam = 'oskar'
slb_naam = 'jouke'

gastheer = input('Wie is de gastheer?').lower()
gasten = 0
drank = 0
chips = 0

start_mijnnaam = gastheer == mijn_naam
start_gastenchipsdrank = gasten and chips and drank 
start_gastheerdrank = gastheer and drank
start_slbnaam = gastheer != slb_naam



if (start_mijnnaam or (start_gastenchipsdrank or (start_gastheerdrank)) and start_slbnaam):
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
