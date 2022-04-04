with open('hoofball.in') as fin:
    positions = [line.strip() for line in fin.readlines()]
    n = int(positions.pop(0))
    positions = sorted(list(map(int, positions[0].split(' '))))
    passes = []


for i, pos in enumerate(positions):
    diff_1, diff_2 = float('inf'), float('inf')
    pass_to, idx = pos, i
    passed_to = []
    
    while not pass_to in passed_to:
        passed_to.append(pass_to)
        if idx > 0:
            left = positions[idx-1]
            diff_1 = pos - left
        if idx < n-1:
            right = positions[idx+1]
            diff_2 = right - pos
        if diff_1 < diff_2 or diff_1 == diff_2:
            pass_to = left
            idx -= 1
            pos = positions[idx]
        else:
            pass_to = right
            idx += 1
            pos = positions[idx]
    passes.append(passed_to)

longest_passes = sorted(passes, key=lambda x: len(x))
discarded = []
count = n
# print(passes)
for i, pass_1 in enumerate(longest_passes):
    for j, pass_2 in enumerate(longest_passes):
        if i == j: continue
        elif pass_2 in discarded: continue
        for element in pass_1:
            if not element in pass_2:
                break
        else:
            # print(pass_1)
            count -= 1
            discarded.append(pass_1)
            break
print(count, file=open('hoofball.out', 'w'))
# print(count) 