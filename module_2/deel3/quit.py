teller = 0

vraag = 0

while vraag != 'quit':
    vraag = input('Voer text in: ').lower()
    teller += 1
    if vraag == 'quit':
        break


print(f'je hebt {teller} iritaties gedaan')

