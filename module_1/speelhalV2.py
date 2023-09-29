
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



print("Het totaal bedrag =" ,eindtotaal, "euro.")


