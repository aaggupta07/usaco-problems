with open('mowing.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    path = [[line.split(' ')[0], int(line.split(' ')[1])] for line in lines]
    cur_time = 0
    pos = [0, 0]
    past_cells = [[0, 0]]
    times = [0]
    max_time = n * 20
    
    
for line in path:
    direction = line[0]
    if direction == 'N': change, x_or_y = 1, 1
    elif direction == 'E': change, x_or_y = 1, 0
    elif direction == 'S': change, x_or_y = -1, 1
    else: change, x_or_y = -1, 0

    for i in range(line[1]):
        pos[x_or_y] += change
        cur_time += 1
        if pos in past_cells:
            idx = past_cells.index(pos)
            diff_time = cur_time - times[idx]
            if diff_time < max_time: max_time = diff_time
            times[idx] = cur_time
        else:
            past_cells.append(pos.copy())
            times.append(cur_time)
            
if max_time == n * 20: max_time = -1
print(max_time, file=open('mowing.out', 'w'))
