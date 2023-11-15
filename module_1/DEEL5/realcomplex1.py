
def get_value(data: str, separator: str, position: int) ->str:
    splitted_string = data.split(separator)
 
    if position >=1 and position <= len(splitted_string):
        value = splitted_string[position -1]
    else:
        value = None
   
    return value


toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
position = int(input('welke nummer: '))
 
 
result = get_value(toets_data, separator, position)
print(result)

