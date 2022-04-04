with open('crossroad.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    sightings = [list(map(int, line.split(' '))) for line in lines]
    current_side = [0] * 10
    
for cow in range(10):
    for event in sightings:
        if event[0] == cow + 1:
            current_side[cow] = event[1]
            break

count = 0
for event in sightings:
    if current_side[event[0] - 1] != event[1]:
        count += 1
        current_side[event[0] - 1] = event[1]
print(count, file=open('crossroad.out', 'w'))
