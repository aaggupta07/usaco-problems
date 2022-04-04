from itertools import permutations

with open('lineup.in') as fin:
    constraints = [line.strip() for line in fin.readlines()]
    n = int(constraints.pop(0))
    constraints = [[line.split(' ')[0], line.split(' ')[-1]] for line in constraints]
    cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
    works = []

orders = permutations(cows, 8)

for order in orders:
    for constraint in constraints:
        i = order.index(constraint[0])
        j = order.index(constraint[1])
        if abs(i-j) > 1: break
    else:
        works.append(order)

works = sorted(works)[0]

with open('lineup.out', 'w') as fout:
    for cow in works:
        fout.write(cow + '\n')
