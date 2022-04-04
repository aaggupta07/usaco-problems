with open('backforth.in') as fin:
    farms = [list(map(int, line.strip().split(' '))) for line in fin.readlines()]
    current = farms.copy()
    unique_vals = set()
    tank = 1000

# Complete Search implementation for 4-deep recursion
for i in range(len(farms[0])):
    
    prev_1 = tank
    tank -= current[0][i]
    state_1 = [current[0].copy(), current[1].copy()]
    current[1].append(current[0].pop(i))
    
    for j in range(len(current[1])):
        
        prev_2 = tank
        tank += current[1][j]
        state_2 = [current[0].copy(), current[1].copy()]
        current[0].append(current[1].pop(j))
        
        for k in range(len(current[0])):
            
            prev_3 = tank
            tank -= current[0][k]
            state_3 = [current[0].copy(), current[1].copy()]
            current[1].append(current[0].pop(k))
            
            for l in range(len(current[1])):

                prev_4 = tank
                state_4 = [current[0].copy(), current[1].copy()]
                tank += current[1][l]
                current[0].append(current[1].pop(l))
                
                unique_vals.add(tank)
                
                # Reset all of the values
                tank = prev_4
                current = [state_4[0].copy(), state_4[1].copy()]
            tank = prev_3
            current = [state_3[0].copy(), state_3[1].copy()]
        tank = prev_2
        current = [state_2[0].copy(), state_2[1].copy()]
    tank = prev_1
    current = [state_1[0].copy(), state_1[1].copy()]

with open('backforth.out', 'w') as fout:
    fout.write(str(len(unique_vals)) + '\n')