with open('tttt.in') as fin:
    board = [line.strip() for line in fin.readlines()]
    individuals = set()
    teams = set()


def check(board):
    for row in board:
        for char in row:
            if row.count(char) == 3:
                individuals.add(char)
            elif row.count(char) == 2:
                for char_2 in row:
                    if char_2 != char:
                        l = sorted([char, char_2])
                        team = ''
                        for c in l: team += c
                        teams.add(team)

check(board)

vertical = []
for i in range(3):
    temp = ''
    for row in board: temp += row[i]
    vertical.append(temp)
check(vertical)

check([board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]])

with open('tttt.out', 'w') as fout:
    fout.write(f'{len(individuals)}\n{len(teams)}\n')
