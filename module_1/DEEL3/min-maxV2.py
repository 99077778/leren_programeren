

a = int(input('voer een getal in voor A: '))
b = int(input('voer een getal in voor B: '))



if a > b:
    print(f'A is het grootste getal')
    maximaal = a
    minimaal = b
elif a < b:
    print(f'A is het kleinste getal')
    minimaal = a
    maximaal = b
else:
    print(f'A en B zijn even groot')
    minimaal = a
    maximaal = b



if a > b or a < b:
    print(f'Het minimum is: {minimaal}')
    print(f'Het maximum is: {maximaal}')
else:
    print(f'allebij de getallen zijn gelijk: {minimaal}, {maximaal}')






 