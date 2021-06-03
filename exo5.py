import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

line = input().split()
N = int(line[0])
A = int(line[1])
C = int(line[2])
AC = A + C

nbsteroid = [int(i) for i in input().split()]

# cumsteroid = nbsteroid[:]
# for i in range(1, N):
#     cumsteroid[i] += cumsteroid[i-1]

best = float("inf")

for shift in range(AC):
    score = 0

    for i in range(N):
        modpos = i % AC
        if modpos >= shift - C + 1 and (modpos < shift or modpos >= A + shift):
            score += nbsteroid[i]
    
    best = min(score, best)

print(best)