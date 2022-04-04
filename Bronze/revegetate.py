with open('revegetate.in') as fin:
    favorites = [list(map(int, line.strip().split(' '))) for line in fin.readlines()]
    n, m = favorites.pop(0)
    favorites = sorted([sorted(pair) for pair in favorites])
    farm = [1] * n

# remove duplicates
pairs = []
for pair in favorites:
    if not pair in pairs: pairs.append(pair)

# generate minimum num
for pair in pairs:
    if farm[pair[0] - 1] == farm[pair[1] - 1]:
        farm[pair[1] - 1] += 1
min_num = ''
for n in farm:
    min_num += str(n)

with open('revegetate.out', 'w') as fout:
    fout.write(min_num + '\n')
