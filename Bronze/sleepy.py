with open('sleepy.in') as fin:
    order = [line.strip() for line in fin.readlines()]
    n = int(order.pop(0))
    order = list(map(int, order[0].split(' ')))

for i, cow_id in enumerate(order[::-1][1:], start=1):
    
    prev = order[::-1][i-1]
    
    if cow_id > prev: break

with open('sleepy.out', 'w') as fout:
    if sorted(order) == order: i += 1
    fout.write(str(n-i) + '\n')
