from fruitmand import fruitmand

fruitgewicht = sum(fruit['weight'] for fruit in fruitmand)




print(fruitgewicht)


fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 1300,
    'color' : 'green',
    'round' : True
})

fruitgewich2 = sum(fruit['weight'] for fruit in fruitmand)
print(fruitgewich2)





