from fruitmand import fruitmand


fruitmand.pop(4)



fruitkleuren = {}

fruitkleuren1 = []


# for fruit in fruitmand:
#     if fruit['color'] not in fruitkleuren:
#        fruitkleuren[fruit['color']] = True

# print(fruitkleuren.keys())



for fruit in fruitmand:
    if fruit['color'] not in fruitkleuren1:
        fruitkleuren1.append(fruit['color'])
print(fruitkleuren1)