with open('cowsignal.in') as fin:
    signal = [item.strip() for item in fin.readlines()]
    n, m, k = [int(item) for item in signal.pop(0).split(' ')]

amplified_msg = [] 


for line in signal:
    past = line[0]
    cnt = 0
    current_line = ''
    
    for char in line:
        if char != line:
            current_line += past * cnt * k
            past = char
            cnt = 0
        cnt += 1
    
    current_line += past * cnt * k
    
    for i in range(k): amplified_msg.append(current_line)

with open('cowsignal.out', 'w') as fout:
    for line in amplified_msg: fout.write(line + '\n')
