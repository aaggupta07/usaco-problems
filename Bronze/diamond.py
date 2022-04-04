with open('diamond.in') as fin:
    diamonds = [line.strip() for line in fin.readlines()]
    n, k = list(map(int, diamonds.pop(0).split(' ')))
    diamonds = [int(item) for item in diamonds]
    high = 0
    
for i in diamonds:
    count = 0
    for j in diamonds:
        if j >= i and j-i <= k: count += 1
    if count > high: high = count
print(high, file=open('diamond.out', 'w'))