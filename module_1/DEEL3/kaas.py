
geelkaas = input('Is de kaas geel? (ja/nee): ')

if geelkaas == 'ja':
    gaten = input('Zitten er gaten in? (ja/nee): ')
elif geelkaas == 'nee':
    schimmel = input('Heeft de kaas blauwe schimmel (ja/nee): ')



if gaten == 'ja':
    duur = input('Is de kaas belachelijk duur? (ja/nee): ')
elif gaten == 'nee':
    steen = input('Is de kaas hard als steen? (ja/nee): ')

if duur == 'ja':
    print('Emmenthaler')
elif duur == 'nee':
    print('Leerdammer')

if steen == 'ja':
    print('Parmigiano Reggiano')
elif steen  == 'nee':
    print('Goudse kaas')



if schimmel == 'ja':
    korst = input('Heeft de kaas korst? (ja/nee): ')
elif schimmel == 'nee':
    korst2 = input('Heeft de kaas korst? (ja/nee): ')

if korst == 'ja':
    print('Blue de Rochbaron')
elif korst == 'nee':
    print('Foume dambert')

if korst2 == 'ja':
    print('Camembert')
elif korst2 == 'nee':
    print('Mozzerella')