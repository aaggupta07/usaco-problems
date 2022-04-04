with open('balancing.in') as fin:
    lines = [line.strip().split(' ') for line in fin.readlines()]
    n, b = list(map(int, lines.pop(0)))
    cows = [[int(line[0]), int(line[1])] for line in lines]
    min_m = n
    
for cow in cows:
    x = cow[0] + 1
    for cow_2 in cows:
        cnt = [0] * 4
        y = cow_2[1] + 1
        
        for cow_3 in cows:
            
            # check which quadrant
            if cow_3[0] > x and cow_3[1] > y: cnt[0] += 1
            elif cow_3[0] < x and cow_3[1] > y: cnt[1] += 1
            elif cow_3[0] < x and cow_3[1] < y: cnt[2] += 1
            else: cnt[3] += 1
        cnt = max(cnt)
        if cnt < min_m: min_m = cnt
print(min_m, file=open('balancing.out', 'w'))
