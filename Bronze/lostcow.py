with open('lostcow.in') as fin:
    x, y = list(map(int, fin.readline().split(' ')))
    pos = x
    move = 1
    dist = 0
    if x < y: forward = True
    else: forward = False

while (pos < y and forward) or (pos > y and not forward):
    dist += abs(pos-x) + abs(move)
    pos = x + move
    move *= -2

dist -= abs(pos-y)
print(dist, file=open('lostcow.out', 'w'))
