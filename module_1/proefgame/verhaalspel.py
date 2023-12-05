import time

gebroken = 0
zaklamp = 1
touw = 0
stabiel_toren = 1
wapen = 0

start = 0
radio = 0
huisje = 0
berg1 = 0
berg2 = 0
helikopter1 = 0
helikopter2 = 0
terug = 0


print('VERHAALSPEL')
time.sleep(.8)
print('''
Elke keuze die je maakt, beïnvloedt je overleving in het bos en bepaalt of je erin slaagt om uiteindelijk 
terug te keren naar de beschaving. Kies verstandig en overleef het avontuur in Greenwood Forest!
---------------------------------------------------------------------------------------------------
''')
time.sleep(2)
print('VERHAAL..')
time.sleep(.8)
print('''
Je bent een ervaren amateurpiloot en je vliegt met je zelfgebouwde helikopter over een uitgestrekt bosgebied genaamd Greenwood Forest. 
Tijdens je vlucht ervaar je motorproblemen en maak je een noodlanding die je in het hart van het dichte bos plaatst.
Je realiseert je al snel dat je mobiele telefoon geen signaal heeft en dat je enige hoop op redding is om contact te maken met de buitenwereld 
via een nabijgelegen radiozendantenne.

''')
time.sleep(2.8)
input('Begin het spel (Ja/Nee): ')


start = int(input('''

|   Je helikopter is zojuist neergestort, je telefoon heeft geen signaal maar doet het nog wel als zaklamp.
|   Je zet de zaklamp aan en kijkt om je heen, het is heel donker maar je ziet 2 opties...
|                 
|   [1] Ga door het dichte bosgebied..
|   [2] Ga door de donkere grot..
  ------------------------------>> '''))




if start == 1:
    radio = int(input('''
              
|   Je gaat door het dichte bosgebied en na een tijdje zie je ver weg een radiozendantenne.. maar je hoort rare geluiden...
|
|   [1] Ga door in de richting van de radiozendantenne..
|   [2] Keer om en probeer een andere route te vinden..
  ---------------------------------------------------->> '''))
    
    


elif start == 2:
    gebroken = 1
    zaklamp = 0
    radio = int(input('''

|   Je betreedt de donkere grot en loopt verder, na een tijdje is je telefoon leeg en zie je niks meer..
|   je gaat blind verder en je maakt een harde val.. je been is gebroken... Na nog een lange tijd blind
|   erdoorheen te lopen zie je eindelijk licht, je bent buiten en ziet ver weg een
|   radiozendantenne.. maar je hoort rare geluiden...
|
|   [1] Ga door in de richting van de radiozendantenne..
|   [2] Keer om en probeer een andere route te vinden..
  ---------------------------------------------------->> '''))
    
else:
    pass





#--------




if radio == 1 and gebroken == 1:
    print('''

|   Je gaat door richting de radiozendantenne.. het rare geluid word steeds harder en het lijkt nu heel dichtbij..
|   opeens komt er een boze beer en je rent weg.. je been is gebroken en je kunt niet meer rennen...
|   De beer pakt je en je overleeft het niet....
  ------------------------------------------------''')
    time.sleep(3)
    print('....Game Over...')


elif radio == 1 and gebroken == 0:
    huisje = int(input('''

|   Je gaat door richting de radiozendantenne.. het rare geluid word steeds harder en het lijkt nu heel dichtbij..
|   opeens komt er een boze beer en je rent weg.. na een lange tijd rennen ben je de beer kwijtgeraakt...
|   Na een tijdje kom je bij een huisje...
|
|   [1] Ga het huisje in en zoek voor spullen..
|   [2] Klim over een hek en ga verder richting de radiotoren.. 
  ------------------------------------------------------------>> '''))
    
elif radio == 2:
    huisje = int(input('''

|   Je neemt een andere route.. na een lange tijd kom je bij een huisje...
|
|   [1] Ga het huisje in en zoek voor spullen..
|   [2] Klim over een hek en ga verder richting de radiotoren..
  ------------------------------------------------------------>> '''))
    

else:
    pass




#--------



if huisje == 1 and zaklamp == 1:
    touw = 1
    wapen = 1
    berg1 = int(input('''
                     
|   Je betreedt het huisje en na een tijdje zoeken vind je een touw, en een pistool.
|   Je gaat verder in de richting van de radiozendantenne, en je ziet twee routes..
|
|   [1] Gebruik het touw om de berg te beklimmen naar de radiozendantenne..
|   [2] Neem een omweg..
  --------------------->> '''))
    

elif huisje == 1 and zaklamp == 0:
    gebroken = 0
    berg1 = int(input('''
                     
|   Je betreedt het huisje en na een tijdje zoeken vind je niets... Je rust uit in het huisje en je
|   been is volledig genezen!!                      
|   Je gaat verder in de richting van de radiozendantenne, en je ziet twee routes..
|
|   [1] Beklim een berg over naar de radiozendantenne..
|   [2] Neem een omweg..
  --------------------->> '''))
    


elif huisje == 2:
    print('''

|   Je klimt over een hek heen en gaat verder richting de radiotoren.
|   Opeens sta je in een berenval!!
|          
|   Je overleeft het niet....
  -----------------------------''')
    time.sleep(3)
    print('....Game Over...')

    

else:
    pass





#--------




if berg1 == 1 and touw == 0:
    gebroken = 1
    berg2 = int(input('''
                      
|   Je gaat de berg over beklimmen, maar je hebt koude vingers...
|   Je valt een paar meter naar beneden en je breekt je been.. alweer...
|
|   [2] Neem een omweg..
  --------------------->> '''))
    


elif berg1 == 1 and touw == 1:
    helikopter1 = int(input('''
                            
|   Je gaat de berg over beklimmen met het touw, na een lange tijd ben je eroverheen..
|   de radiotoren is nu heel dichtbij, maar hij staat in brand!
|   Je hoop is nu verloren maar je komt langs een schuurtje met onderdelen voor je helikopter..
|              
|   [1] Neem de helikopteronderdelen mee en ga terug naar je helikopter..
|   [2] Laat die helikopter, die is total loss, zoek een andere manier voor contact..
|   [3] Ga naar de brandende radiotoren en hoop dat daar hulp komt..
  ----------------------------------------------------------------->> '''))
    


elif berg1 == 2 and gebroken == 0:
    helikopter1 = int(input('''
                            
|   Je neemt een omweg door het dichte bos heen.. na een lange tijd hoor je brommende geluiden...
|   Je kijkt achter je en ziet een horde van beren.. je rent hard weg.
|   
|   Na een tijd rennen zie je de radiotoren nu heel dichtbij, maar hij staat in brand!
|   Je hoop is nu verloren maar je komt langs een schuurtje met onderdelen voor je helikopter..
|              
|   [1] Neem de helikopteronderdelen mee en ga terug naar je helikopter..
|   [2] Laat die helikopter, die is total loss, zoek een andere manier voor contact..
|   [3] Ga naar de brandende radiotoren en hoop dat daar hulp komt..
  ----------------------------------------------------------------->> '''))
    


else:
    pass




#--------





if berg2 == 2 and gebroken == 1:
    print('''

|   Je neemt een omweg door het dichte bos heen.. na een lange tijd hoor je brommende geluiden...
|   Je kijkt achter je en ziet een horde van beren.. je rent hard weg, maar je been is gebroken...
|   Je valt hard op de grond en de beren hebben je te pakken.... 
|   Je overleefd het niet....
  ------------------------------''')
    time.sleep(3)
    print('....Game Over...')



    


else:
    pass


#-------


if helikopter1 == 1:
    wapen = 1
    helikopter2 = int(input('''

|   Je doorzoekt het schuurtje en vind een geweer met een aantal kogels, die neem je mee.
|   Ook neem je de helikopteronderdelen mee in een karretje en gaat hed pad terug naar de
|   Helikopter, het is heel ver weg en het karretje is heel zwaar.. je kan het opgeven..
|
|   [1] Ga door naar de helikopter en probeer het te repareren.
|   [2] Geef het op en loop terug.
  ------------------------------->> '''))




elif helikopter1 == 3:
    print('''

|   Je bent bij de radiotoren en het gaat ineens hard regenen, het vuur is geblust en de
|   appratuur in de toren is verwoest, alle hoop is verloren en je blijft voor altijd
|   vast in het bos. Maar je hebt het overleefd... 
  --------------------------------------------------''')
    time.sleep(4)
    print('Einde 2; Slechte einde.')


else:
    pass


#=========


if helikopter2 == 1:
    print('''

|   Je gaat door en neemt het zware karretje mee.. na een hele lange tijd ben je eindelijk
|   bij de helikopter, je bent het aan het repareren, en na een tijd gaat die weer aan!
|   je stapt in de helikopter en vliegt omhoog... Opeens valt alles uitelkaar en stort je
|   vele meters neer....
|   Je overleefd het niet....
  ------------------------------''')
    time.sleep(3)
    print('....Game Over...')




elif helikopter2 == 2:
    stabiel_toren = 0
    terug = int(input('''

|   Je besluit terug te gaan, er zat toch geen hoop meer in die helikopter.
|   
|   Na het teruglopen zie je de radiotoren nu weer dichtbij, hij staat nogsteeds in brand en
|   ziet er niet stabiel uit.. Je ziet 2 opties..
|              
|   [1] Laat de helikopter en zoek een andere manier voor contact..
|   [2] Ga naar de brandende radiotoren en hoop dat daar hulp komt..
  ----------------------------------------------------------------->> '''))



else:
    pass

#---------------------

if terug == 2:
    print('''
          
|   Je loopt naar de brandende radiotoren en het is daar heel warm, opeens begint de 
|   toren te kraken en valt die om, bovenop je hoofd.. 
|   je overleefd het niet...
  ----------------------------''')
    time.sleep(3)
    print('....Game Over...')


elif (wapen == 0 and terug == 1) or (helikopter1 == 2 and wapen == 0):
    print('''
          
|   Je besluit de helikopter en de radiotoren achter te laten, je loopt kilometers verder.
|   Opeens komt er een hele grote beer, de beer stormt op je af en heeft je te pakken..
|   je overleefd het niet...
  ----------------------------''')
    time.sleep(3)
    print('....Game Over...')




elif (wapen == 1 and terug == 1) or (helikopter1 == 2 and wapen == 1):
    print('''
          
|   Je besluit de helikopter en de radiotoren achter te laten, je loopt kilometers verder.
|   Opeens komt er een hele grote beer, de beer stormt op je gebruikt het wapen en schiet de beer dood.
|   Na een tijd komen er mensen aan in autos, ze komen je helpen en je rijdt uit het bos.
  -------------------------------------------------------------------------------------------''')
    time.sleep(4)
    print('Einde 1; Goede einde.')


else:
    pass


