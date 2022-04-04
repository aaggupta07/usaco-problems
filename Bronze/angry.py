with open('angry.in') as fin:
    positions = [int(line.strip()) for line in fin.readlines()]
    n = positions.pop(0)
    positions = sorted(positions)
    # print(positions)
    max_cnt = 0

    
def blow_up(bale, rng):
    new_bale = []
    remove_bales = []
    cnt = 0
    
    # detonate current bales and find next in the chain
    for x in positions:
        # print(x)
        for y in bale:
            if abs(y-x) <= rng and not x in bale:
                # print(f'Range: {rng}')
                new_bale.append(x)
                cnt += 1
                break
    if cnt == 0:
        return 0
    
    # remove current bales that blew up
    original = positions.copy()
    positions[:] = [x for x in positions if x not in bale]
    
    # recurse
    # print(bale, cnt)
    cnt += blow_up(new_bale, rng+1)
    positions[:] = original
    return cnt
    
    
for i, bale in enumerate(positions):
    rng = 1
    # print(bale)
    amt = blow_up([bale], rng) + 1
    # print(amt)
    if amt > max_cnt: max_cnt = amt
print(max_cnt, file=open('angry.out', 'w'))
