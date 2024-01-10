#eisen pasword lengte moet tusen 10 en 20'
#start met hoofletre en eindiged met kleine letter
# vanaf kartakter drie kompt er een random 4 getallen met tussendoor random hoofd of kleine letter

# ww10: Aa1f3G4j7x


import string
from random import randint, choice

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)



# print(randint(0, 9))
# print(choice(string.ascii_uppercase))
# print(choice(string.ascii_lowercase))



password = ''

lengte = int(input('Hoelang moet het wachtwoord; tussen (10, 20): '))


print(f'Uw wachtwoord is: {password}')




for x in lengte:
    password += choice(string.ascii_uppercase)
    password += choice(string.ascii_lowercase)
