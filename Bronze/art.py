with open('art.in') as fin:
    canvas = [line.strip() for line in fin.readlines()]
    n = int(canvas.pop(0))
    colors = []
    for i in range(1, 10):
        for row in canvas:
            if str(i) in row:
                colors.append(str(i))
                break
    later_colors = set()


def offending_colors(canvas, color):
    closest_x = len(canvas) + 1
    closest_y = len(canvas) + 1
    farthest_x = 0
    farthest_y = 0
    
    # find the smallest rectangle
    for i, row in enumerate(canvas):
        for j, spot in enumerate(row):
            # print(j, spot)
            if spot == color:
                closest_x, closest_y = min(closest_x, j), min(closest_y, i)
                farthest_x, farthest_y = max(farthest_x, j), max(farthest_y, i)
    
    # find out any colors painted after this rectangle:
    for row in canvas[closest_y:farthest_y+1]:
        for spot in row[closest_x:farthest_x+1]:
            if spot != color:
                later_colors.add(spot)
    return [[closest_x, closest_y], [farthest_x, farthest_y]] 


# make sure that there is at least one square that other colors could have gone on
rectangles = [offending_colors(canvas, color) for color in colors]
count = 0

for i, color in enumerate(colors):
    if not color in later_colors:
        rect = rectangles[i]
        
        for j, row in enumerate(canvas):
            for k, spot in enumerate(canvas):
                if spot != '0':
                    if (k < rect[0][0] or k > rect[1][0]) or (j > rect[0][1] or j < rect[1][1]):
                        count += 1
                        break
            else: continue
            break            

print(count, file=open('art.out', 'w'))
