import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

d = int(input())
l = int(input())
print(d + l * 5)