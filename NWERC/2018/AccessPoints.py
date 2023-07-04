
from collections import deque
n = int(input())

points = [list(map(int, input().split())) for i in range(n)]


def solve(coords):

    groups = deque() ## (tot, size)
    groups.append((coords[0], 1))

    for i in range(1, len(coords)):
        groups.append((coords[i], 1))


        while len(groups) > 1:
            a,b = groups.pop()
            c,d = groups.pop()

            if a * d< c * b:
                groups.append((a+c, b+d))
            else:
                groups.append((c,d))
                groups.append((a,b))
                break




    score = 0
    cind = 0

    for a,b in groups:
        for k in range(b):
            r = a/b-coords[cind]
            score += r*r
            cind += 1

        #print(score,a,b)
    return score

a = solve([a[0] for a in points])
b = solve([a[1] for a in points])

print(a+b)
