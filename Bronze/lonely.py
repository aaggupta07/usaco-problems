n = int(input())
seq = input()
count = 0

for i in range(n):
    
    left = 0
    if i > 0 and seq[i-1] != seq[i]:
        char = seq[i-1]
        
        left += 1
        
        for j in seq[:i-1][::-1]:
            if j == char: left += 1
            else: break
    
    right = 0
    if i+1 < n and seq[i+1] != seq[i]:
        char = seq[i+1]
        
        right += 1
        
        for j in seq[i+2:]:
            if j == char: right += 1
            else: break
    count += left * right + max(left-1, 0) + max(right-1, 0)      
print(count)