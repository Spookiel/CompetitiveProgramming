

from math import ceil, sqrt
t = int(input())
for j in range(t):
    x,y = list(map(int, input().split()))


    best = 99999999999
    for stepsize in range(1, 2*ceil(sqrt(max(x,y)))+5):
        res = ceil(x/stepsize)+ceil(y/stepsize)+stepsize-1

        #if res < best:

            #print(res, stepsize)
        best = min(best, res)
    print(best)
