with open('cowqueue.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    cows = sorted([list(map(int, line.split(' '))) for line in lines])
    current_time = 0
    
for cow in cows:
    if cow[0] > current_time:
        current_time = cow[0] + cow[1]
    elif cow[0] <= current_time:
        current_time += cow[1]
print(current_time, file=open('cowqueue.out', 'w'))
