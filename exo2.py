import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

n = int(input())

boutons = dict()

for _ in range(n):
    b = input()
    if b in boutons:
        boutons[b] += 1
    else:
        boutons[b] = 1

for item in boutons.items():
    if item[1] == 2:
        print(item[0])
        break