with open('shuffle.in') as fin:
    lines = [item.strip() for item in fin.readlines()]
    n = int(lines.pop(0))
    shuffle = list(map(int, lines[0].split(' ')))
    ids = lines[1].split(' ')
    
    
for i in range(3):
    current_pos = [0] * n
    
    for i, cow_id in enumerate(ids, start=1):
        for j, place in enumerate(shuffle):
            if place == i:
                break
        current_pos[j] = cow_id
        
    ids = current_pos
    
with open('shuffle.out', 'w') as fout:
    for cow_id in ids:
        fout.write(cow_id + '\n')
