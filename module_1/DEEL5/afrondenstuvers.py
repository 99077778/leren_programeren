
from test_lib import test, report

def afronden_naar_stuiver(prijs):
    STUIVER = 5
    afrondend_getal = round(prijs * 100 / STUIVER) * STUIVER / 100
    return f"{afrondend_getal:.2f}"


bedrag = 2.24
expected = '2.25'
afrondend_bedrag = afronden_naar_stuiver(bedrag)
text = f'{bedrag} afronden naar {afrondend_bedrag}'
test(text, expected, afrondend_bedrag)

bedrag = 13.01
expected = '13.00'
afrondend_bedrag = afronden_naar_stuiver(bedrag)
text = f'{bedrag} afronden naar {afrondend_bedrag}'
test(text, expected, afrondend_bedrag)


bedrag = 69.69
expected = '69.70'
afrondend_bedrag = afronden_naar_stuiver(bedrag)
text = f'{bedrag} afronden naar {afrondend_bedrag}'
test(text, expected, afrondend_bedrag)


bedrag = 41.73
expected = '41.75'
afrondend_bedrag = afronden_naar_stuiver(bedrag)
text = f'{bedrag} afronden naar {afrondend_bedrag}'
test(text, expected, afrondend_bedrag)


bedrag = 0.09
expected = '0.10'
afrondend_bedrag = afronden_naar_stuiver(bedrag)
text = f'{bedrag} afronden naar {afrondend_bedrag}'
test(text, expected, afrondend_bedrag)


bedrag = 0.01
expected = '0.00'
afrondend_bedrag = afronden_naar_stuiver(bedrag)
text = f'{bedrag} afronden naar {afrondend_bedrag}'
test(text, expected, afrondend_bedrag)

report()
