import itertools

with open('guess.in') as fin:
    animals = [line.strip().split(' ')[2:] for line in fin.readlines()[1:]]
    
combos = itertools.combinations(animals, 2)
max_cnt = 0

for combo in combos:
    cnt = 0
    for prop in combo[1]:
        if prop in combo[0]: cnt += 1
    max_cnt = max(cnt, max_cnt)
    
with open('guess.out', 'w') as fout:
    fout.write(str(max_cnt + 1) + '\n')
