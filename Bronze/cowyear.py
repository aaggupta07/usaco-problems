n = int(input())
statements = [input().split(' ') for i in range(n)]
years = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']

prev = 0
relationships = {'Bessie': [0, 'Ox']}
for i, statement in enumerate(statements):
    prev = years.index(relationships[statement[-1]][-1])
    idx = years.index(statement[4])
    if statement[3] == 'previous':
        if idx > prev:
            diff = (12 - (idx - prev))*-1
        elif idx < prev:
            diff = (prev - idx)*-1
        else:
            diff = -12
    else:
        if idx > prev:
            diff = idx - prev
        elif idx < prev:
            diff = 12 - (prev - idx)
        else:
            diff = 12
    prev = idx       
    relationships[statement[0]] = [statement[-1], diff, statement[4]]
del relationships['Bessie']

related_cow = 'Elsie'
ttl = 0

while related_cow != 'Bessie':
    vals = relationships[related_cow]
    related_cow = vals[0]
    ttl += vals[1]
print(abs(ttl))