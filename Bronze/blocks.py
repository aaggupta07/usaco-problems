with open('blocks.in') as fin:
    words = list(map(lambda x: x.strip(), fin.readlines()))
    n = int(words.pop(0))
    words = [item.split(' ') for item in words]
    
values = [0] * 26
alphabet = 'abcdefghijklmnopqrstuvwxyz'


for i, block in enumerate(words):
    current_count = [0] * 26
    
    for letter in block[0]:
        idx = alphabet.index(letter)
        current_count[idx] += 1
        
    for i in range(26):
        cnt = block[1].count(alphabet[i])
        if current_count[i] < cnt: current_count[i] = cnt
    # print(current_count)
            
    for i, val in enumerate(current_count): values[i] += val

with open('blocks.out', 'w') as fout:
    for i in values:
        fout.write(str(i) + '\n')
