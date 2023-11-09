

def nummers(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return'Allebij de getallen zijn even groot'
    elif nr1 > nr2:
        return f'Maximum = {nr1}, minimum = {nr2}'
    else:
        return f'Maximum = {nr2}, minimum = {nr1}'
 
 
  
nr1 = int(input("Voer een nummer voor getal 1 in: "))
nr2 = int(input("Voer een nummer voor getal 2 in: "))
 

MIN = 0
MAX = 0
 

 
resultaat = nummers(nr1, nr2)
print(resultaat)
 
 
 
 
 