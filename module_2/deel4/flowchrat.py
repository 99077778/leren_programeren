
import random

punten = 0

rondes = 0
pogingen = 10


while rondes <20:
    spelen = input('Wil je opneiuw spelen (ja/nee): ').lower()
    if spelen != 'nee':
        pogingen = 10
        rondes  += 1
        nummer = random.randint(1,1000)
        print(nummer)

        while pogingen >0:
            raden = int(input('Raad het getal tussen 1-1000: '))
            verschilraden = abs(raden-nummer)
            if raden == nummer:
                print("geraden")
                punten +=1
                break

            elif verschilraden < 20:
                pogingen -=1
                print('je bent heel warm')
                print(f'je hebt nog {pogingen} pogingen over')

            elif verschilraden < 50:
                pogingen -=1
                print('je bent  warm')
                print(f'je hebt nog {pogingen} pogingen over')
                

            else:
                pogingen -=1
                print('die is niet in de buurt, opnieuw randen')
                print(f'je hebt nog {pogingen} pogingen over')


    else:
        print(f'de score is {punten} punten')
        print(f'totaal heb je {rondes} rondes gespeeld')
        exit()