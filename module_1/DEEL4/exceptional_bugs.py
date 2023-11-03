
import random


#selecteer 2 nummers
num1 = random.randint(1,10)
num2 = random.randint(5,15)


antwoord = (num1 + num2)

#vraag om een antwoord





#geef reactie op het antwoord
try:
    number = int(input('Weet jij wat '+str(num1)+'+'+str(num2)+' is? '))
except ValueError:
    print('Dat is geen nummer!')

else:
    if number == antwoord:
        print('Dat is juist')
    elif number != antwoord:
        print('Nee dat klopt niet')