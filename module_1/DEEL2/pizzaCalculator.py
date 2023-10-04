#Oskar van der Sluis
#opdracht: Pizza calculator



bestellingen = []


#Pizza kiezen
while True:
    try:
        groote = int(input('Welke pizza wil je, kies het nummer: [1] small, [2] medium, [3] large : '))
        if groote < 1 or groote > 3:
            raise ValueError("Ongeldige keuze. Kies een nummer tussen 1 en 3.")
        
        if groote == 1:
            pizza = "small"
            prijs = 7.99
        elif groote == 2:
            pizza = "medium"
            prijs = 9.99
        elif groote == 3:
            pizza = "large"
            prijs = 12.99
        
        bestellingen.append((pizza, prijs))
        
        print(f"De prijs van de gekozen pizza ({pizza}) is: €{prijs:.2f}")
        

        #Nog een pizza bestellen
        bestel_opnieuw = input("Wil je nog een pizza bestellen? (ja/nee): ").strip().lower()
        if bestel_opnieuw != 'ja':
            break
    except ValueError as e:
        print(f"Fout: {e}")


#Bestellijst
if len(bestellingen) > 0:
    print("| Je bestellingen:")
    print('|')
    total_price = 0
    for pizza, price in bestellingen:
        print(f"| {pizza.capitalize()} pizza - €{price:.2f}")
        total_price += price
    print(f"| Totaalprijs: €{total_price:.2f}")



