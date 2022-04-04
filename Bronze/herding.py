with open('herding.in') as fin:
    positions = sorted(list(map(int, fin.readline().strip().split(' '))))
    
# find minimum moves
diff_2, diff_1 = positions[2] - positions[1], positions[1] - positions[0]

if diff_1 == 1 and diff_2 == 1: min_moves = 0
elif diff_1 == 2 or diff_2 == 2: min_moves = 1
elif diff_1 == 1 or diff_2 == 1: min_moves = 2
else: min_moves = 2
    
# find max_moves
max_moves = max(diff_1, diff_2) - 1

with open('herding.out', 'w') as fout:
    fout.write(f'{min_moves}\n{max_moves}\n')
