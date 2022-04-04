with open('whereami.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    houses = lines[0]
    final_val = 0

for i in range(1, n + 1):
    combos = {}
    for j in range(n-i+1):
        c = houses[j:j+i]
        if c in combos: combos[c] += 1
        else:
            combos[c] = 1
    for key in combos:
        if combos[key] != 1: break
    else:
        final_val = i
        break

print(final_val, file=open('whereami.out', 'w'))
