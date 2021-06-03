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

class ShieldSession:
    def __init__(self, next = None) -> None:
        self.next = next
        self.time = 0
        self.shift = 0

    def is_expired(self):
        return self.shift == AC

    def reset(self):
        self.time = 0

    def tick(self):
        if self.next != None:
            self.next.tick()
            if self.next.is_expired():
                self.next.reset()
                self.shift += 1

        else:
            self.shift += 1

    def protect(self):
        if self.time == AC + self.shift:
            return self.next.protect()
        result = (self, self.time < self.shift or self.time >= self.shift + A)
        self.time += 1
        return result

best = float("inf")

shield = None
for _ in range(N):
    shield = ShieldSession(shield)

while not shield.is_expired():
    score = 0
    s = shield

    for i in range(N):
        eprint("arrivé", i)
        s, unprotected = s.protect()
        if unprotected:
            score += nbsteroid[i]
    
    best = min(score, best)
    shield.tick()

print(best)