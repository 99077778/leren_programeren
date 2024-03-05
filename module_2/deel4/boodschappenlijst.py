# boodschappenlijst = []


# keuze = ''

# while keuze != 'nee':
#     artikel = input('Welk artikel wilt u toevoegen?: ').lower()
#     hoveel = input(f'Hoveel {artikel} wilt u toevoegen?: ')
#     boodschappenlijst.append ((artikel, hoveel))
    
#     keuze = input('Wilt u nog meer boodshappen toevoegen? (ja/nee): ').lower()


# #print(boodschappenlijst)

# print('''
# -- BOODSCHAPPENLIJST --''')

# for item, hoveel in boodschappenlijst:
#     print(f"{hoveel} x {item}")







boodschappenlijst = {}
keuze = ''

while keuze != 'nee':
    artikel = input('Welk artikel wilt u toevoegen?: ').lower()
    hoeveel = int(input(f'Hoeveel {artikel} wilt u toevoegen?: '))
    
    if artikel in boodschappenlijst:
        boodschappenlijst[artikel] += hoeveel
    else:
        boodschappenlijst[artikel] = hoeveel
    
    keuze = input('Wilt u nog meer boodshappen toevoegen? (ja/nee): ').lower()

print('''
-- BOODSCHAPPENLIJST --''')

for item, hoeveelheid in boodschappenlijst.items():
    print(f"{hoeveelheid} x {item}")
