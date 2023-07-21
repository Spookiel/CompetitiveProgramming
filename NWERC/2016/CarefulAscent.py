
from fractions import Fraction

x,y = list(map(int, input().split()))

tot = 0
n = int(input())
shields = [list(map(float, input().split())) for i in range(n)]
shields.sort()
if shields:
    shields = [(0, shields[0][0], 1)]+shields+[(shields[-1][1], y, 1)]
    adjShields = []
    for l, u, f in shields:
        if u > y:
            adjShields.append((l, y, f))
            break
        else:
            adjShields.append((l,u,f))
else:
    adjShields = [(0, y, 1)]
#print(adjShields)
for ind, (l, u, f) in enumerate(adjShields):
    if ind != 0:
        tot += (l-adjShields[ind-1][1])
        #print("ADDING EXTRA",(l-adjShields[ind-1][1]) )
    tot += (u-l)*f
if tot == 0:
    print(0)
else:
    print(x/tot)
