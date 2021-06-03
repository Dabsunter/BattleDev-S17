import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def can_boom(row,col):
    for c in range(10):
        for r in range(row-3, row+1):
            if game[r][c] == '.' and c != col:
                return False
    return True

game = []

for _ in range(20):
    game.append(input())

for l in game:
    eprint(l)

for col in range(10):
    if game[3][col] == '#':
        continue

    for row in range(3, 20):
        if game[row][col] == '.' and (row == 19 or game[row+1][col] == '#'):
            break

    if can_boom(row,col):
        print("BOOM", col+1)
        exit(0)

print("NOPE")