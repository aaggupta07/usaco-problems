with open('measurement.in') as fin:
    lines = [item.strip() for item in fin.readlines()]
    n = int(lines.pop(0))
    lines = [line.split(' ') for line in lines]
    log = sorted([[int(item[0]), item[1], int(item[2])] for item in lines])
    current_standings = [7] * 3

count = 0
old_board = [0, 1, 2]
    
for event in log:
    if event[1] == 'Bessie':
        current_standings[0] += event[2]
    elif event[1] == 'Elsie':
        current_standings[1] += event[2]
    else:
        current_standings[2] += event[2]
    
    # print(current_standings)
    
    past = 0
    
    maxes = []
    
    for i, item in enumerate(current_standings):
        if item > past:
            maxes = [i]
            past = item
        elif item == past:
            maxes.append(i)
    # print(maxes)
    if maxes != old_board: count += 1
    
    old_board = maxes
    
with open('measurement.out', 'w') as fout:
    fout.write(str(count) + '\n')
