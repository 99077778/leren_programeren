lijst = []

for _ in range(5):

    auto = {}
    auto['automerk'] = input('wat is het auto merk: ')
    auto['model'] = input('welk model is de auto: ')
    auto['prijs'] = int(input('wat is de prijs: '))
    
    lijst.append(auto)
 


for auto in lijst:
    print(auto['prijs'])


    
 