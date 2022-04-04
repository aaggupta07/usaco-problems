with open('cbarn.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    rooms = (list(map(int, lines))) * 2
    min_dist = 0

for i in range(n):
    dist = 0
    for j, room in enumerate(rooms[i:i+n]):
        dist += (j) * rooms[i+j]
        
    if dist < min_dist or min_dist == 0: min_dist = dist
print(min_dist, file=open('cbarn.out', 'w'))
