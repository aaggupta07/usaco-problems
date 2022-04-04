with open('blist.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    sequence = [list(map(int, cow.split(' '))) for cow in lines]
    milk_times = []
    
    for interval in sequence:
        milk_times.append([interval[0], 0, interval[-1]])
        milk_times.append([interval[1], 1, interval[-1]])
    milk_times = sorted(milk_times)
    
    current_count = 0
    max_count = 0
    
for event in milk_times:
    if event[1] == 0:
        current_count += event[2]
        if current_count > max_count: max_count = current_count
    else: current_count -= event[2]
    
with open('blist.out', 'w') as fout:
    fout.write(str(max_count) + '\n')
