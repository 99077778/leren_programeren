# dagen = ('Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag')

# omgedraaid = 1


# welke = input('Welke dagen wil je? volle week, werk week, weekend. kies; (1 / 2 / 3): ')


# # volle week
# for dag in dagen:
#     if omgedraaid == 0 and welke == 1:
#         print(dag)
#         if dag == 7:
#             break
        
#     elif omgedraaid == 1 and welke == 1:
#         omgedraaide_dagen = reversed(dagen)
#         for dag in omgedraaide_dagen:
#             print(dag)
#             if dag == 7:
#                 break
    
            
# # werk week
# for dag in dagen:
#     if omgedraaid == 0 and welke == 2:
#         print(dag)
#         if dag == 5:
#             break
        
#     elif omgedraaid == 1 and welke == 2:
#         omgedraaide_dagen = reversed(dagen)
#         for dag in omgedraaide_dagen:
#             print(dag)
#             if dag == 5:
#                 break

# # weekend
# for dag in dagen:
#     if omgedraaid == 0 and welke == 3:
#         print(dag)
#         if dag == 2:
#             break
        
#     elif omgedraaid == 1 and welke == 3:
#         omgedraaide_dagen = reversed(dagen)
#         for dag in omgedraaide_dagen:
#             print(dag)
#             if dag == 2:
#                 break









dagen = ('Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag')

omgedraaid = 1

welke = input('Welke dagen wil je? volle week, werk week, weekend. kies; (1 / 2 / 3): ')
welke = int(welke)

# volle week
if welke == 1:
    if omgedraaid == 0:
        for dag in dagen:
            print(dag)
    elif omgedraaid == 1:
        # omgedraaide_dagen = reversed(dagen)
        print(dagen[7 : : -1])
        # for dag in omgedraaide_dagen:
        #     print(dag)

# werk week
elif welke == 2:
    if omgedraaid == 0:
        for dag in dagen[:5]:
            print(dag)
    elif omgedraaid == 1:
        omgedraaide_dagen = reversed(dagen[:5])
        for dag in omgedraaide_dagen:
            print(dag)

# weekend
elif welke == 3:
    if omgedraaid == 0:
        for dag in dagen[5:]:
            print(dag)
    elif omgedraaid == 1:
        omgedraaide_dagen = reversed(dagen[5:])
        for dag in omgedraaide_dagen:
            print(dag)




