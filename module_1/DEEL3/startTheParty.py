gastheer = True
gasten = True
drank = True
chips = True

if (not chips) or ((chips and not drank) or (not gasten and not gastheer)):
    print('No Party')
else:
    print('Start the Party')
