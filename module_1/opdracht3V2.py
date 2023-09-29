

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



print(f"De feestlunch kost je bij de bakker {totaal} voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")








#ENTREE
PRIJS_ENTREE = 7.45
aantal_entree = 4


#GAMESEAT
PRIJS_VIPVR_5MIN = .37
aantal_vipvr_minuten = 45
VIPVR_DELENDOOR5MIN = 5
aantal_vipvr_personen = 4



totaal_entree = PRIJS_ENTREE * aantal_entree

totaal_gameseat = PRIJS_VIPVR_5MIN * aantal_vipvr_minuten / VIPVR_DELENDOOR5MIN * aantal_vipvr_personen


eindtotaal = totaal_entree + totaal_gameseat



print(f"Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {eindtotaal} euro")


