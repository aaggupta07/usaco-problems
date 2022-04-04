# Not Last (USACO)

with open('notlast.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    lines = [[line.split(' ')[0], int(line.split(' ')[1])] for line in lines]

production = {'Bessie': 0, 'Elsie': 0, 'Daisy': 0, 'Gertie': 0, 'Annabelle': 0, 'Maggie': 0, 'Henrietta': 0}
for event in lines: production[event[0]] += event[1]

minimal_amt = min(production.values())
remove = []

for cow, val in production.items():
    if val == minimal_amt: remove.append(cow)
for cow in remove: del production[cow]
    
# Repeat above for next minimal
second_worst_cows = []
if len(production) > 0:
    second_min = min(production.values())
    second_worst_cows = [cow for cow, val in production.items() if val == second_min]
     
with open('notlast.out', 'w') as fout:
    if len(second_worst_cows) > 1 or len(second_worst_cows) == 0: fout.write('Tie\n')
    else: fout.write(second_worst_cows[0] + '\n')