


def afronden_naar_stuiver(prijs):
    STUIVER = 5
    afrondend_getal = round(prijs * 100 / STUIVER) * STUIVER / 100
    return f'{afrondend_getal:.2f}'




bedrag = 2.24
afrondend_bedrag = afronden_naar_stuiver(bedrag)
print(afrondend_bedrag)


bedrag = 13.01
afrondend_bedrag = afronden_naar_stuiver(bedrag)
print(afrondend_bedrag)


bedrag = 69.69
afrondend_bedrag = afronden_naar_stuiver(bedrag)
print(afrondend_bedrag)


bedrag = 41.73
afrondend_bedrag = afronden_naar_stuiver(bedrag)
print(afrondend_bedrag)


bedrag = 0.09
afrondend_bedrag = afronden_naar_stuiver(bedrag)
print(afrondend_bedrag)


bedrag = 0.01
afrondend_bedrag = afronden_naar_stuiver(bedrag)
print(afrondend_bedrag)


