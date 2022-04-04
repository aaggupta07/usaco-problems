with open('traffic.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    highway = []
    
    # designate 0= none, 1= on ramp, and change off to a negative inverted on
    for line in lines:
        mile = line.split(' ')
        traffic = []
        if mile[0] == 'none':
            traffic.append(0)
            traffic.append(int(mile[1]))
            traffic.append(int(mile[-1]))
            
        elif mile[0] == 'on':
            traffic.append(1)
            traffic.append(int(mile[1]))
            traffic.append(int(mile[-1]))
        
        else:
            traffic.append(1)
            traffic.append(int(mile[-1]) * -1)
            traffic.append(int(mile[1]) * -1)
        highway.append(traffic)


def traverse(highway):
    # start at first none
    for i, arr in enumerate(highway):
        if arr[0] == 0: break
    # print(highway, i)
    highway = highway[i:]
    # print(highway)
    current = highway.pop(0)[1:]
    # print(current)
    
    # traverse, finding end values by updating current
    for segment in highway:
        if segment[0] == 0:
            current[0] = max(current[0], segment[1])
            current[1] = min(current[1], segment[2])
        else:
            current[0] += segment[1]
            current[1] += segment[2]
            
            # can't have negative traffic
            if current[0] < 0: current[0] = 0
            if current[1] < 0: current[1] = 0
    return current


end_highway = traverse(highway)

# traverse backwards, reversing on ramps
reversed_highway = []
for mile in highway[::-1]:
    if mile[0] == 1: reversed_mile = [1, mile[-1]*-1, mile[1]*-1]
    else: reversed_mile = mile
    reversed_highway.append(reversed_mile)
    
start_highway = traverse(reversed_highway)

with open('traffic.out', 'w') as fout:
    fout.write(f'{start_highway[0]} {start_highway[1]}\n')
    fout.write(f'{end_highway[0]} {end_highway[1]}\n')