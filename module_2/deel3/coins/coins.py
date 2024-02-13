# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # input naar centen omrekenen
paid = int(float(input('Paid amount: ')) * 100) # input naar centen omrekenen
change = paid - toPay # wisselgeld in centen rekenen

if change > 0: # doorgaan als er wisselgeld moet
  coinValue = 500 # met grootste hoveelheid beginnen
  teruggegeven_munten = {}
  
  while change > 0 and coinValue > 0: # door gaan totdat de wisselgeld compleet is
    nrCoins = change // coinValue # de goede aantal centen rekkenen met bedrag

    if nrCoins > 0: # als er centen van deze hoeveelhijd zijn
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #
      teruggegeven_munten[coinValue] = nrCoins

# verander centen value naar de volgende lagere bedrag
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0 # stoppen als het nul is

if change > 0: # als er nog wisselgeld over is
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done') #als alles wisselgeld compleet is
print('de wisselgeld oversicht')
for waarde, aantal in teruggegeven_munten.items():
  print('muntwaarde:' ,waarde ,'cent - aantal:', aantal)





else:
  print('geen wisselgeld')