with open('milkorder.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n, m, k = list(map(int, lines.pop(0).split(' ')))
    sequence = list(map(int, lines.pop(0).split(' ')))
    order = [0] * n

final_pos = 0

# fill in insertions
for cow in lines:
    pos = list(map(int, cow.split(' ')))
    order[pos[1] - 1] = pos[0]

# check if cow 1 is inserted
for i, cow in enumerate(order):
    if cow == 1: final_pos = i + 1 

# if 1 is in sequence, then prioritize sequence:
if 1 in sequence and not 1 in order:
    past = -1
    for cow in sequence:
        if cow in order: past = order.index(cow)
        else:
            for i, pos in enumerate(order[past + 1:], start=past+1):
                if pos == 0:
                    order[i] = cow
                    break
            past = i
        if cow == 1: final_pos = past + 1
        
else:
    # fill in sequence
    prev_cows = []

    for cow in sequence:
        if cow in order:
            if len(prev_cows) > 0:
                length = order.index(cow)

                for i, space in enumerate(order[:length][::-1]):
                    if space == 0:
                        order[length - i - 1] = prev_cows[-1]
                        del prev_cows[-1]
                        if len(prev_cows) == 0: break

        else: prev_cows.append(cow)

    # any remaining cows in sequence
    if len(prev_cows) > 0:

        for i, space in enumerate(order[::-1]):
            if space == 0:
                order[n - i - 1] = prev_cows[-1]
                del prev_cows[-1]
                if len(prev_cows) == 0: break

# find first available spot
for i in range(n):
    if order[i] == 0: break
if final_pos == 0:
    final_pos = i + 1

with open('milkorder.out', 'w') as fout:
    fout.write(str(final_pos) + '\n')