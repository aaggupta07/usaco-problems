with open('lifeguards.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n = int(lines.pop(0))
    times = sorted([list(map(int, line.split(' '))) for line in lines])
    high = 0
    
    
def merge(intervals):
    
    current = intervals[0]
    merged = []
    
    for interval in intervals:
        if interval[0] <= current[1]:
            current[1] = max(interval[1], current[1])
        else:
            merged.append(current.copy())
            current = [interval[0], interval[1]]
    merged.append(current.copy())
    
    return merged


for i in range(n):
    new_intervals = [j.copy() for j in times]
    del new_intervals[i]

    merged = merge(new_intervals)
    time = 0
    for interval in merged: time += interval[1] - interval[0]
    high = max(high, time)
print(high, file=open('lifeguards.out', 'w'))
