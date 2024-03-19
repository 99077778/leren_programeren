from fruitmand import fruitmand
 
kleuren = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'brown': 'bruin'
}
 
lengtenaam = [len(fruit['name']) for fruit in fruitmand]
 
lastenaam = lengtenaam.index(max(lengtenaam))
print(lastenaam)


langstefruitnaam = fruitmand[lastenaam]

kleur = langstefruitnaam['color']
if langstefruitnaam['color'] in kleuren:
    kleur = kleuren[langstefruitnaam['color']]
 
print(f"de {langstefruitnaam['name']} heeft {len(langstefruitnaam['name'])} aantal letters en {kleur} van kleur en een gewicht van {langstefruitnaam['weight'] / 1000} kg.")
 