


a = int(input('voer een getal in voor A: '))
b = int(input('voer een getal in voor B: '))

minimaal = 0
maximaal = 0


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



if a > b or a < b:
    print(f'Het minimum is: {minimaal}')
    print(f'Het maximum is: {maximaal}')
else:
    print('allebij de getallen zijn gelijk')




# if a > b:
#     print(f'Het minimum is: {min}')
# elif a < b:
#     print(f'Het maximum is: {max}')


 