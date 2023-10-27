

geelkaas = input('Is de kaas geel? (ja/nee): ').lower()

if geelkaas == 'ja':
    gaten = input('Zitten er gaten in? (ja/nee): ').lower()
    if gaten == 'ja':
        duur = input('Is de kaas belachelijk duur? (ja/nee): ').lower()
        if duur == 'ja':
            print('Emmenthaler')
        elif duur == 'nee':
            print('Leerdammer')
        else:
            print('Ongeldige invoer voor duur')
    elif gaten == 'nee':
        steen = input('Is de kaas hard als steen? (ja/nee): ').lower()
        if steen == 'ja':
            print('Parmigiano Reggiano')
        elif steen == 'nee':
            print('Goudse kaas')
        else:
            print('Ongeldige invoer voor steen')
    else:
        print('Ongeldige invoer voor gaten')
elif geelkaas == 'nee':
    schimmel = input('Heeft de kaas blauwe schimmel (ja/nee): ').lower()
    if schimmel == 'ja':
        korst = input('Heeft de kaas korst? (ja/nee): ').lower()
        if korst == 'ja':
            print('Blue de Rochbaron')
        elif korst == 'nee':
            print('Foume dambert')
        else:
            print('Ongeldige invoer voor korst')
    elif schimmel == 'nee':
        korst2 = input('Heeft de kaas korst? (ja/nee): ').lower()
        if korst2 == 'ja':
            print('Camembert')
        elif korst2 == 'nee':
            print('Mozzarella')
        else:
            print('Ongeldige invoer voor korst2')
    else:
        print('Ongeldige invoer voor schimmel')
else:
    print('Ongeldige invoer voor geelkaas')




