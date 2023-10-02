

#CROSANTJES
PRIJS_CROSANT = 39
aantal_crosant = int(input("Hoeveel croissantjes wil je bestellen? "))

#STOKBROOD
PRIJS_STOKBROOD = 278
aantal_stokbrood = int(input("Hoeveel stokbroden wil je bestellen? "))

#KORTING 50c
KORTINGSBON50C = -50 
aantal_kortingsbon50c = int(input("Hoeveel kortingsbonnen van 50 cent heb je? "))


prijs_voor_de_croissantjes = PRIJS_CROSANT * aantal_crosant

prijs_voor_de_stokbroden = PRIJS_STOKBROOD * aantal_stokbrood

korting = KORTINGSBON50C * aantal_kortingsbon50c


totaal = prijs_voor_de_croissantjes + prijs_voor_de_stokbroden + korting



print("Je moet", totaal / 100, "euro betalen.")


