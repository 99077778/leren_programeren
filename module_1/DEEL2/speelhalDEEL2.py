
#ENTREE
PRIJS_ENTREE = 745
aantal_entree = int(input("Hoeveel entreekaartjes wil je bestellen? "))


#GAMESEAT
PRIJS_VIPVR_5MIN = 37
aantal_vipvr_minuten = int(input("Hoeveel minuten wil je op de VIP VR-gamestoel zitten? "))
VIPVR_DELENDOOR5MIN = 5
aantal_vipvr_personen = int(input("Met hoeveel personen wil je gebruik maken van de VIP VR-gamestoel? "))



totaal_entree = PRIJS_ENTREE * aantal_entree

totaal_gameseat = (PRIJS_VIPVR_5MIN * aantal_vipvr_minuten * aantal_vipvr_personen) // VIPVR_DELENDOOR5MIN


eindtotaal = (totaal_entree + totaal_gameseat) / 100



print("Het totaalbedrag =", eindtotaal, "euro.")


