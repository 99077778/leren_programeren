from fruitmand import fruitmand

sorteer_fruitmand = sorted(fruitmand, key=lambda x: x['weight'], reverse=True)




for fruit in sorteer_fruitmand:
    print(f"{fruit['name']}: {fruit['weight'] / 1000} kg")
