n = int(input())
preferred = list(map(int, input().split(' ')))
start = list(map(int, input().split(' ')))
diff = [i-j for i, j in zip(preferred, start)]

ttl = (sum([abs(i-j) for i, j in zip([0] + diff, diff + [0])]))//2
print(ttl)
