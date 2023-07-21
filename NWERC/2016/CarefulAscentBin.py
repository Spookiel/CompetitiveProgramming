x,y = list(map(int, input().split()))

tot = 0
n = int(input())
shields = [list(map(float, input().split())) for i in range(n)]
shields.sort()



def calc(shields, vhor,y):

    if not shields:
        return vhor*y
    adjShields = [(0, shields[0][0], 1)]+shields+[(shields[-1][1], y, 1)]
    cx = 0
    for l,u,f in adjShields:
        inDist = max(0, min(y, u)-l)
        cx += inDist*f*vhor
    #print("REACHED",cx)
    return cx



low = -10000000000
high = 10000000000

while abs(high-low) > 1e-8:
    mid = (low+high)/2
    dist = calc(shields, mid, y)
    if dist < x:
        low = mid
    else:
        high = mid
print(low)