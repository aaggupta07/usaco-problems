with open('tracing.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n, t = list(map(int, lines.pop(0).split(' ')))
    state = list(map(int, lines.pop(0)))
    events = sorted([list(map(int, item.split(' '))) for item in lines])
    patients, min_k, max_k = 0, float('inf'), 0
        

for cow in range(n):
    if state[cow] == '0': continue
    works = False
    for k in range(251):
        cows = [0] * n
        hoof_counter = [0] * n
        cows[cow] = 1
        
        for i in events:
            if cows[i[1] - 1] == 1 and cows[i[2] - 1] == 1:
                hoof_counter[i[1] - 1] += 1
                hoof_counter[i[2] - 1] += 1
                continue
            elif cows[i[1] - 1] == 1 or cows[i[2] - 1] == 1:
                if cows[i[1] - 1] == 1:
                    infected = i[1] - 1
                    safe = i[2] - 1
                else:
                    infected = i[2] - 1
                    safe = i[1] - 1
                
                if hoof_counter[infected] < k:
                    cows[safe] = 1
                    hoof_counter[infected] += 1
                    
        # update values
        # print(cows, state)
        if cows == state and not works:
            min_k = min(min_k, k)
            max_k = max(max_k, k)
            patients += 1
            works = True
        elif cows == state:
            max_k = max(max_k, k)
            continue
        elif works:
            break
        
with open('tracing.out', 'w') as fout:
    if max_k == 250: max_k = 'Infinity'
    fout.write(f'{patients} {min_k} {max_k}\n')
        