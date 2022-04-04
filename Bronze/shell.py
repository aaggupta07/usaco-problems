with open('shell.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    swaps = [list(map(int, line.split(' '))) for line in lines]
    max_cnt = 0
    
for pos in range(3):
    shells = [0, 0, 0]
    shells[pos] = 1
    cnt = 0
    
    for swap in swaps:
        shells[swap[0] - 1], shells[swap[1] - 1] = shells[swap[1] - 1], shells[swap[0] - 1]
        if shells[swap[2] - 1] == 1: cnt += 1
    max_cnt = max(max_cnt, cnt)
    
with open('shell.out', 'w') as fout:
    fout.write(str(max_cnt) + '\n')