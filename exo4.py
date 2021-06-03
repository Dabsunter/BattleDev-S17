import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

n = int(input())
n2 = n//2
orbite = input()
trashset = set(orbite)

sonde1 = dict()
sonde2 = dict()

def is_valid():
    for t in trashset:
        if sonde1[t] != sonde2[t]:
            return False
    return True

for t in trashset:
    sonde1[t] = 0
    sonde2[t] = 0

for i in range(n2):
    sonde1[orbite[i]] += 1
    sonde2[orbite[i+n2]] += 1

nbsol = 0

for i in range(n2):
    if is_valid():
        nbsol += 1

    # rotate
    a = orbite[n2+i]
    b = orbite[i]
    sonde1[a] += 1
    sonde2[a] -= 1
    sonde1[b] -= 1
    sonde2[b] += 1

print(2 * nbsol)
