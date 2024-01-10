

# def lijstmaken():
#     lijst1 = int(input('Hoeveel voor lijst 1: '))
#     lijst2 = int(input('Hoeveel voor lijst 2: '))
#     lijst3 = int(input('Hoeveel voor lijst 3: '))
#     lijsten = []

#     for i, length in enumerate([lijst1, lijst2, lijst3], start=1):
#         new_list = list(range(i, (i * length) + 1, i))
#         lijsten.append(new_list)

#     print(lijsten)

# lijstmaken()





#todo lijst op lijst altijd vershcil van 5

def lijstmaken():

    num_lijst = int(input('Hoeveel lijsten: '))
    lijsten = []
    
    for i in range(1,num_lijst+1):
        list_length = int(input(f'Hoeveel voor lijst {i}: '))
        nieuwe = list(range(i, i * list_length + 5, i))
        lijsten.append(nieuwe)

    return lijsten

resultaat_lijsten = lijstmaken()
print(resultaat_lijsten)
    
    

