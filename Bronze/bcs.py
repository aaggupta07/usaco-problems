with open('bcs.in') as fin:
    lines = [line.strip() for line in fin.readlines()]
    n, k = list(map(int, lines.pop(0).split(' ')))
    figure = lines[:n]
    pieces = []
    for i in range(k):
        pieces.append(lines[i*n+n:i*n+n+n])
        
def vertical(grid):
    new_grid = []
    for i in range(len(grid)):
        temp = ''
        for row in grid:
            temp += row[i]
        new_grid.append(temp)
    return new_grid
        

def shifts(grid, n):
    new_shifts = []
    
    # empty indivudual rows on top
    for i, row in enumerate(grid):
        if row == '.' * n:
            new_shifts.append(grid[i+1:] + grid[:i+1])
        else: break
    
    # empty individual rows on bottom
    length = len(grid)
    for i, row in enumerate(grid[::-1]):
        if row == '.' * n:
            new_shifts.append(grid[length-i-1:] + grid[:length-i-1])
        else: break
            
    # empty columns on left
    rotated = vertical(grid)
    for i, row in enumerate(rotated):
        if row == '.' * n:
            updated_grid = rotated[i+1:] + rotated[:i+1]
            updated_grid = vertical(updated_grid)
            new_shifts.append(updated_grid.copy())
            
            # empty rows on top for each left column
            for i, row in enumerate(updated_grid):
                if row == '.' * n:
                    new_shifts.append(updated_grid[i+1:] + updated_grid[:i+1])
                else: break

            # empty rows on bottom for each left column
            for i, row in enumerate(updated_grid[::-1]):
                if row == '.' * n:
                    new_shifts.append(updated_grid[length-i-1:] + updated_grid[:length-i-1])
                else: break
        else: break
    # empty columns on right
    for i, row in enumerate(rotated[::-1]):
        if row == '.' * n:
            updated_grid = rotated[length-i-1:] + rotated[:length-i-1]
            updated_grid = vertical(updated_grid)
            new_shifts.append(updated_grid.copy())
            
            # empty rows on top for each right column
            for i, row in enumerate(updated_grid):
                if row == '.' * n:
                    new_shifts.append(updated_grid[i+1:] + updated_grid[:i+1])
                else: break

            # empty rows on bottom for each right column
            for i, row in enumerate(updated_grid[::-1]):
                if row == '.' * n:
                    new_shifts.append(updated_grid[length-i-1:] + updated_grid[:length-i-1])
                else: break
        else: break
    return new_shifts

all_shifts = []

for piece in pieces:
    x = shifts(piece, n)
    x.append(piece)
    all_shifts.append(x)

for i, piece in enumerate(all_shifts):
    for shift in piece:
        for j, piece_2 in enumerate(all_shifts[i+1:], start=i+1):
            for shift_2 in piece_2:
                flag = False
                new_piece = shift.copy()

                for k, line in enumerate(shift_2):
                    row = ''
                    for l, char in enumerate(line):
                        if char == '#':
                            if new_piece[k][l] == '#':
                                flag = True
                                break
                            else: row += '#'
                        elif new_piece[k][l] == '#': row += '#'
                        else: row += '.'
                    if flag: break
                    new_piece[k] = row
                
                if new_piece == figure and not flag:
                    answer = sorted([i+1, j+1])
                    break

print(f'{answer[0]} {answer[1]}', file=open('bcs.out', 'w'))