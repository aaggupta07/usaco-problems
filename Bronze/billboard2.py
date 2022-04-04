with open('billboard.in') as fin:
    coordinates = [list(map(int, line.strip().split(' '))) for line in fin.readlines()]
    billboard_1, billboard_2 = [[item[0:2], item[2:]] for item in coordinates]


def length_width(rect):
    return [rect[1][0] - rect[0][0], rect[1][1] - rect[0][1]]
    

def intersection(rect_1, rect_2):
    length = min(rect_1[1][0], rect_2[1][0]) - max(rect_1[0][0], rect_2[0][0])
    width = min(rect_1[1][1], rect_2[1][1]) - max(rect_1[0][1], rect_2[0][1])
    return [length, width]


lw_1 = length_width(billboard_1)
area = lw_1[0] * lw_1[1]

intersection_lw = intersection(billboard_1, billboard_2)

if ((intersection_lw[0] == lw_1[0] or intersection_lw[1] == lw_1[1]) and
    ((billboard_2[0][0] <= billboard_1[0][0]) or (billboard_2[1][0] >= billboard_1[1][0])) and
    ((billboard_2[0][1] <= billboard_1[0][1]) or (billboard_2[1][1] >= billboard_1[1][1]))):
    area -= intersection_lw[0] * intersection_lw[1]
    
with open('billboard.out', 'w') as fout:
    fout.write(str(area) + '\n')
