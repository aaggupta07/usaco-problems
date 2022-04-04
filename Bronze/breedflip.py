with open('breedflip.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    a = lines[0]
    b = lines[1]
    pairs = list(zip(a, b))

# prune front and end
for i in range(n):
    x, y = pairs[i]
    if x != y:
        pairs = pairs[i:]
        break
else: pairs = []

pairs = pairs[::-1]
for i in range(len(pairs)):
    x, y = pairs[i]
    if x != y:
        pairs = pairs[i:]
        pairs = pairs[::-1]
        break
if len(pairs) == 0: cnt = 0
else: cnt = 1


prev = False
for x, y in pairs:
    if x == y and not prev:
        cnt += 1
        prev = True
    elif x != y:
        prev = False
print(cnt, file=open('breedflip.out', 'w'))
