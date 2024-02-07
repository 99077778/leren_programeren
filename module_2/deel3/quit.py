teller = 0

vraag = ''

print(type(vraag))


while vraag != 'quit':
    vraag = input('Voer text in: ').lower()
    teller += 1


print(f'je hebt {teller} iritaties gedaan')

