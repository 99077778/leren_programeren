dagen = ('Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag')



for dag in dagen:
    print(dag)

print(dagen[1])

for x in range(5, 7):
    print(dagen[x])


for n in range(4, -1, -1):
    print(dagen[n])


for m in dagen[5 : : -1]: #
    print(m)


print(dagen[2]) #aleen element
print(type(dagen[2 : 3]))# een lijst met een element







