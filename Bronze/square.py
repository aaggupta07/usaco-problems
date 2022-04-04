with open('square.in') as fin:
    coordinates = [list(map(int, line.strip().split(' '))) for line in fin.readlines()]
    p_1, p_2 = [[[item[0], item[1]], [item[2], item[3]]] for item in coordinates]

with open('square.out', 'w') as fout:
    fout.write(str(max(max(p_1[1][0],p_2[1][0])-min(p_1[0][0],p_2[0][0]), max(p_1[1][1],p_2[1][1])-min(p_1[0][1],p_2[0][1]))**2))
