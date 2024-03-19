from fruitmand import fruitmand


fruitmand.pop(4)



fruitdict = {}



for fruit in fruitmand:
    if fruit['color'] not in fruitdict:
       fruitdict[fruit['color']] = True

print(fruitdict.keys())



