with open('triangles.in') as fin:
    pairs = [line.strip() for line in fin.readlines()]
    n = int(pairs.pop(0))
    pairs = [list(map(int, line.split(' '))) for line in pairs]
    high = 0
    
for point_1 in pairs:
    for point_2 in pairs:
        if point_1[0] == point_2[0]:
            for point_3 in pairs:
                if point_1[1] == point_3[1]:
                    area = abs(point_1[1] - point_2[1]) * abs(point_1[0] - point_3[0])
                    high = max(area, high)
print(high, file=open('triangles.out', 'w'))
