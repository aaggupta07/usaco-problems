with open('cownomics.in') as fin:
    sequences = [line.strip() for line in fin.readlines()]
    n, k = list(map(int, sequences.pop(0).split(' ')))
    spotty, not_spotty = sequences[:n], sequences[n:]
    spotty, not_spotty = list(zip(*spotty)), list(zip(*not_spotty))
    count = 0
    
for i, pos in enumerate(spotty):
    for genome in pos:
        if genome in not_spotty[i]: break
    else: count += 1
print(count, file=open('cownomics.out', 'w'))
