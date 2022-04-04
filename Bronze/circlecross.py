import itertools

with open('circlecross.in') as fin:
    crossings = fin.readline().strip()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

combos = itertools.combinations(alphabet, 2)
count = 0

for pair in combos:
    index_1 = []
    index_2 = []
    
    for i, point in enumerate(crossings):
        if point == pair[0]:
            index_1.append(i)
        elif point == pair[1]:
            index_2.append(i)
    if ((index_1[0] < index_2[0] and index_1[1] < index_2[1] and index_1[1] > index_2[0]) or
        (index_1[0] > index_2[0] and index_1[1] > index_2[1] and index_1[0] < index_2[1])):
        count += 1
print(count, file=open('circlecross.out', 'w'))
