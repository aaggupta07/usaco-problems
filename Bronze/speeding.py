with open('speeding.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n, m = list(map(int, lines.pop(0).split(' ')))
    limit = [list(map(int, item.split(' '))) for item in lines[:n]]
    speed = [list(map(int, item.split(' '))) for item in lines[n:]]

limit = [seg[1] for seg in limit for i in range(seg[0])]
speed = [seg[1] for seg in speed for i in range(seg[0])]

infringement = 0

for i in range(len(speed)):
    diff = speed[i] - limit[i]
    if diff > infringement: infringement = diff
        
with open('speeding.out', 'w') as fout:
    fout.write(str(infringement) + '\n')
