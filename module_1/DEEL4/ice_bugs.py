

def convertToEuroText (amount):
    prijsformat = "€{:.2f}".format(float(amount)).replace(".", ",")
    return prijsformat



SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10



amount = int(input("Hoeveel ijsjes van {} wil je bestellen?".format(SMALL_PRICE)))
totalSmallPrice = amount * SMALL_PRICE
amount = int(input("En hoeveel ijsjes van {} wil je bestellen?".format(MEDIUM_PRICE)))
totalMediumPrice = amount * MEDIUM_PRICE

totalPrice = totalSmallPrice + totalMediumPrice


print('Dat is dan {} totaal'.format(convertToEuroText(totalPrice)))

