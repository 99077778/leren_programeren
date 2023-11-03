ALTIJD = 0
VAAK = 1
REGELMATIG = 2
SOMS = 3
NOOIT = 4
GEMIDDELD = 3
from studieadviestextt import *

print(STUDIEDOKTER_TITEL)

print(OPTIES)


aantal_weken_vraag = int(input(AANTAL_WEKEN_VRAAG))


if aantal_weken_vraag >= 10:
    competentie_stelling_6 = int(input(COMPETENTIE_STELLING_6))
    competentie_stelling_7 = int(input(COMPETENTIE_STELLING_7))
else:
    competentie_stelling_6 = competentie_stelling_7 = NOOIT  \


competentie_stelling_1 = int(input(COMPETENTIE_STELLING_1))
competentie_stelling_2 = int(input(COMPETENTIE_STELLING_2))
competentie_stelling_3 = int(input(COMPETENTIE_STELLING_3))
competentie_stelling_4 = int(input(COMPETENTIE_STELLING_4))
competentie_stelling_5 = int(input(COMPETENTIE_STELLING_5))



antwoorden = [competentie_stelling_1, competentie_stelling_2, competentie_stelling_3, competentie_stelling_4, competentie_stelling_5, competentie_stelling_6, competentie_stelling_7]



aantal_altijd = antwoorden.count(ALTIJD)
aantal_vaak = antwoorden.count(VAAK)
aantal_regelmatig = antwoorden.count(REGELMATIG)



gemiddelde_score = (
    competentie_stelling_1 + competentie_stelling_2 + competentie_stelling_3 +
    competentie_stelling_4 + competentie_stelling_5 + competentie_stelling_6 + competentie_stelling_7
) / GEMIDDELD


if gemiddelde_score <= 2 or aantal_altijd + aantal_vaak > 3:
    advies = COMPETENTIE_ADVIES_ZORGELIJK
elif gemiddelde_score <= 3 or aantal_altijd + aantal_vaak + aantal_regelmatig > 3:
    advies = COMPETENTIE_ADVIES_TWIJFELACHTIG
else:
    advies = COMPETENTIE_ADVIES_GERUSTSTELLEND


print(f'\nVerbeterd Advies: {advies}\n')



