
cijfer = int(input('Welke tafel wil je weergeven: '))

for tafel in range(1,11):
    uitkomst = tafel * cijfer
    print(f'{tafel} x {cijfer} = {uitkomst}')

