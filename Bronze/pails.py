with open('pails.in') as fin:
    x, y, m = list(map(int, fin.readline().strip().split(' ')))
    current = 0
    best = 0

for i in range(m//y+1):
    current = m - y * i
    current = m - (current % x)
    if current > best: best = current
print(best, file=open('pails.out', 'w'))
