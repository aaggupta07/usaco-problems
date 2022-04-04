with open('billboard.in') as fin:
    lines = [item.strip() for item in fin.readlines()]
    lines = [list(map(int, item.split(' '))) for item in lines]
    rect_1, rect_2, truck = [[item[:2], item[2:]] for item in lines]
    

def intersection_area(rect_1, rect_2):
    length = min(rect_1[1][0], rect_2[1][0]) - max(rect_1[0][0], rect_2[0][0])
    width = min(rect_1[1][1], rect_2[1][1]) - max(rect_1[0][1], rect_2[0][1])
    
    if length <= 0 or width <= 0:
        return 0
    return length * width


def area(rect):
    return (rect[1][0] - rect[0][0]) * (rect[1][1] - rect[0][1])
    

ttl_area = area(rect_1) + area(rect_2)
ttl_area = ttl_area - intersection_area(rect_1, truck) - intersection_area(rect_2, truck)

with open('billboard.out', 'w') as fout:
    fout.write(str(ttl_area) + '\n')
