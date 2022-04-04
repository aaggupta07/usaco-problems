from itertools import combinations

with open('gymnastics.in') as fin:
    rankings = [line.strip() for line in fin.readlines()]
    n, k = list(map(int, rankings.pop(0).split(' ')))
    rankings = [list(map(int, line.split(' '))) for line in rankings]
    
combos = combinations(rankings[0], 2)
count = 0


for combo in combos:
    for ranking in rankings:
        consistent = False
        
        for cow in ranking:
            if cow == combo[0]: consistent = True
            elif cow == combo[1] and not consistent:
                break
        else: continue
        break
    else: count += 1
print(count, file=open('gymnastics.out', 'w'))
