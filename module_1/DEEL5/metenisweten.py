from test_lib import test, report



def nummers(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return'Allebij de getallen zijn even groot'
    elif nr1 > nr2:
        return f'Maximum = {nr1}, minimum = {nr2}'
    else:
        return f'Maximum = {nr2}, minimum = {nr1}'



nr1 = input('Vul een nummer in: ')
nr2 = input('Vul een 2de nummer in: ')




resultaat = nummers(nr1, nr2)
#print(resultaat)



if nr1 == nr2:
    expected = 'Allebij de getallen zijn even groot'
    text = 'Allebij de getallen zijn even groot'
    test(text, resultaat, expected)
elif nr1 > nr2:
    expected = f'Maximum = {nr1}, minimum = {nr2}'
    text = f'Maximum = {nr1}, minimum = {nr2}'
    test(text, resultaat, expected)
else:
    expected = f'Maximum = {nr2}, minimum = {nr1}'
    text = f'Maximum = {nr2}, minimum = {nr1}'
    test(text, resultaat, expected)




report()

