with open('mixmilk.in') as fin:
    lines = [line.strip().split(' ') for line in fin.readlines()]
    capacities = [int(item[0]) for item in lines] + [int(lines[0][0])]
    current = [int(item[1]) for item in lines] + [int(lines[0][1])]
    # print(current)
    
for pour in range(33):
    for i in range(3):
        # print(current, i)
        if current[i] + current[i+1] > capacities[i+1]:
            current[i] -= capacities[i+1] - current[i+1]
            current[i+1] = capacities[i+1]
        else:
            current[i+1] += current[i]
            current[i] = 0
        
        # dynamically update the additional first bucket (last) so that it loops
        if i == 0:
            current[-1] = current[i]
        elif i == 2:
            current[0] = current[-1]
            
# last pour
if current[0] + current[1] > capacities[1]:
    current[0] -= capacities[1] - current[1]
    current[1] = capacities[1]
else:
    current[1] += current[0]
    current[0] = 0
            
with open('mixmilk.out', 'w') as fout:
    for milk in current[:3]:
        fout.write(str(milk) + '\n')
