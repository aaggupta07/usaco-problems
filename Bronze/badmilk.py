with open('badmilk.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n, m, d, s = list(map(int, lines.pop(0).split(' ')))
    events = [list(map(int, item.split(' '))) for item in lines[:d]]
    sick = [list(map(int, item.split(' '))) for item in lines[d:]]

events = [sorted([[j[2], j[1]] for j in events if j[0] == i+1]) for i in range(n)]
bad_milks = [i+1 for i in range(m)]

for person in sick:
    potential = []
    
    for time_milk in events[person[0] - 1]:
        if time_milk[0] < person[1] and time_milk[1] in bad_milks: potential.append(time_milk[1])
        elif time_milk[1] >= person[1]: break
    bad_milks = potential.copy()

max_cnt = 0

for milk in bad_milks:
    cnt = 0
    
    for person in events:
        for time_milk in person:
            if time_milk[1] == milk:
                cnt += 1
                break
    if cnt > max_cnt: max_cnt = cnt

with open('badmilk.out', 'w') as fout:
    fout.write(str(max_cnt) + '\n')