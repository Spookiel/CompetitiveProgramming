
from collections import deque

def solve():
    n,MAXX,MAXY = list(map(int, input().split()))


    sx,sy,ex,ey = list(map(int, input().split()))

    bases = [list(map(int, input().split())) for i in range(n)]

    def inside(cx, cy, rad, tx, ty):
        return abs(cx-tx)+abs(cy-ty) < rad

    def check(max_rad):
        if max_rad <= 0:
            return abs(ex-sx)+abs(ey-sy)
        banned = set()
        for bx,by in bases:
            ### Mark out a max_rad zone around the box

            bot = by-max_rad+1
            top = by+max_rad-1

            for dx in range(max_rad):
                banned.add((bx-dx, bot+dx))
                banned.add((bx+dx, bot+dx))
                banned.add((bx+dx, top-dx))
                banned.add((bx-dx, top-dx))
            ### Check if the start or end point is inside the box

            if inside(bx, by, max_rad, sx, sy) or inside(bx, by, max_rad, ex, ey):
                return -1

        q = deque()
        banned.add((sx, sy))
        q.append((sx, sy,0))
        #print(banned)
        while q:
            x, y,dist = q.popleft()
            #print("CHECKING", x, y, dist)
            if x == ex and y == ey:
                return dist

            for dx in [1,-1]:
                nx, ny = x+dx, y

                if (nx, ny) not in banned and 0 <= nx < MAXX and 0 <= ny < MAXY:
                    banned.add((nx, ny))
                    q.append((nx, ny, dist+1))
            for dy in [1, -1]:
                nx, ny = x, y+dy

                if (nx, ny) not in banned and 0 <= nx < MAXX and 0 <= ny < MAXY:
                    banned.add((nx, ny))
                    q.append((nx, ny, dist+1))
        return -1

    from math import ceil
    low = 0
    high = 10000
    ans = check(0)
    while low < high:
        mid = low+ceil((high-low)/2)
        #print(low, mid, high)
        best = check(mid)
        #print(low, mid, high, "SCORE", best)
        if best != -1:
            ans = best
            low = mid
        else:
            high = mid-1
    print(low, ans)


runs = 1

for i in range(runs):
    solve()