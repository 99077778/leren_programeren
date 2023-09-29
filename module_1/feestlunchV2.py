

#CROSANTJES
PRIJS_CROSANT = .39
aantal_crosant = 17

#STOKBROOD
PRIJS_STOKBROOD = 2.78
aantal_stokbrood = 2

#KORTING 50c
KORTINGSBON50C = -.50
aantal_kortingsbon50c = 3


prijs_voor_de_crosantjes = PRIJS_CROSANT * aantal_crosant

prijs_voor_de_stokbrooden = PRIJS_STOKBROOD * aantal_stokbrood

korting = KORTINGSBON50C * aantal_kortingsbon50c


totaal = prijs_voor_de_crosantjes + prijs_voor_de_stokbrooden + korting



print("Je moet" ,totaal, "euro betalen.")



