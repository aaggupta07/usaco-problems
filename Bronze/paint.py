with open('paint.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    a, b = map(int, lines[0].split(' '))
    c, d = map(int, lines[1].split(' '))
    
overlap = min(b, d) - max(a, c)
length = (b-a) + (d-c)

with open('paint.out', 'w') as fout:
    if overlap > 0:
        fout.write(str(length - overlap) + '\n')
    else:
        fout.write(str(length) + '\n')
