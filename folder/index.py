from user_input import *



def get_position() -> str:
    position = 0
    while position < 11 or position > 33: 
        position = get_integer('Kies een vakje tussen 11 en 33: ')
        #print('kies een waarde tussen 11 en 33: ')

    return str(position)


rij1 = ['U', 'U', 'U']
rij2 = ['U', 'U', 'U']
rij3 = ['U', 'U', 'U']



print(rij1)
print(rij2)
print(rij3)



move = get_position() 
print(move[0])




