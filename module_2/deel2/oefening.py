lijst = ['c', 2, 4, 4, 'b', 1, 1, 6, 'c', 2, 6, 5, 'c', 7, 9, 8, 'b', 1, 1, 4, 'a', 3, 9, 4, 'c', 2, 7, 7, 'b', 1, 9, 2, 'b', 3, 5, 9, 'c', 8, 3, 3, 'c', 5, 3, 4, 'a', 8, 8, 2, 'a', 3, 1, 8, 'c', 2, 7, 9, 'b', 8, 1, 3, 'a', 7, 8, 7, 'a', 4, 7, 1, 'b', 1, 4, 2, 'a', 8, 7, 5, 'c', 6, 6, 9, 'c', 1, 2, 7, 'b', 3, 5, 5, 'b', 2, 9, 5, 'b', 1, 5, 4, 'a', 3, 4, 3, 'b', 4, 4, 6, 'b', 2, 1, 5, 'c', 4, 4, 3, 'b', 3, 5, 9, 'b', 9, 8, 5, 'a', 2, 7, 5, 'a', 4, 1, 6, 'a', 5, 7, 2, 'a', 9, 5, 2, 'c', 1, 7, 4, 'c', 1, 8, 4, 'c', 7, 2, 9, 'c', 8, 2, 2, 'c', 1, 5, 9, 'c', 6, 1, 4, 'a', 5, 1, 4, 'b', 7, 8, 9, 'b', 8, 5, 3, 'a', 3, 6, 8, 'c', 1, 6, 2, 'c', 9, 6, 5, 'c', 2, 7, 4, 'b', 8, 1, 8, 'b', 7, 7, 5, 'b', 5, 8, 3, 'b', 4, 3, 7, 'b', 8, 8, 2, 'a', 6, 1, 4, 'b', 9, 4, 1, 'b', 2, 5, 6]

lege_lijst = []

# for n in range('a', 3, 1):
#     print(lijst[n])



# for m in lijst['a' : 3 : 1]: 
#     print(m)



# if lijst in lijst(['a']):
#     print('test')


# print(lijst(['a']))




print(lijst.count('a'))


while len(lijst) >0:
    element = lijst.pop(0)
    if element == 'a':
        #print(lijst[0:3])
        lege_lijst += lijst[0:3]
        lijst = lijst[3:]


print(lege_lijst)

print(len(lege_lijst))
