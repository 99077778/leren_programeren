
import random

MAX_AANTAL_RONDEN = 20
MAX_AANTAL_POGINGEN = 10
VERSCHIL_HEEL_WARM = 20
punten = 0

rondes = 1
#pogingen = 10

spelen = 'ja'

while rondes < MAX_AANTAL_RONDEN:
    if rondes > 1:
        spelen = input('Wil je opneiuw spelen (ja/nee): ').lower()

    if spelen != 'nee':
        print(f'dit is je {rondes}e ronde')
        
        pogingen = MAX_AANTAL_POGINGEN
        rondes  += 1
        nummer = random.randint(1,1000)
        print(nummer)

        while pogingen >0:
            try:
                raden = int(input('Raad het getal tussen 1-1000: '))
            
                verschilraden = abs(raden - nummer)
                if raden == nummer:
                    print("geraden")
                    punten +=1
                    break

                elif verschilraden < VERSCHIL_HEEL_WARM:
                    pogingen -=1
                    print('je bent heel warm')
                    if raden < nummer:
                        print('hoger')
                    else:
                        print('lager')
                    print(f'je hebt nog {pogingen} pogingen over')

                elif verschilraden < 50:
                    pogingen -=1
                    print('je bent  warm')
                    if raden < nummer:
                        print('hoger')
                    else:
                        print('lager')
                    print(f'je hebt nog {pogingen} pogingen over')
                    

                else:
                    pogingen -=1
                    print('die is niet in de buurt, opnieuw randen')
                    print(f'je hebt nog {pogingen} pogingen over')
            except ValueError:
                print("Dat is geen geldig getal")
        print(f'de score is nu {punten}')

    else:
        print(f'de score is {punten} punten')
        print(f'totaal heb je {rondes} rondes gespeeld')
        exit()