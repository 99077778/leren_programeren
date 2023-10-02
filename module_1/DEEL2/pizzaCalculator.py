#Oskar van der Sluis
#opdracht: Pizza calculator



while True:
    try:
        groote = int(input('Welke pizza wil je, kies het nummer: [1] small, [2] medium, [3] large : '))
        if groote < 1 or groote > 3:
            raise ValueError("Ongeldige keuze. Kies een nummer tussen 1 en 3.")
        break
    except ValueError as e:
        print(f"Fout: {e}")




price_small = '7,99'
price_medium = '9,99'
price_large = '12,99'




