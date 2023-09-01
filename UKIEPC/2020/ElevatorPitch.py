



h,w = list(map(int, input().split()))


grid = [list(map(int, input().split())) for i in range(h)]


from collections import deque

lst = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        lst.append((grid[i][j], j, i))
lst.sort(reverse=True)

q = deque(lst)

reachable = set()
elevators = set()

def level_search(x,y):
    global reachable
    ### Flood fill on the same level as x,y

    q = deque()
    q.append((x,y))

    while q:
        nx, ny = q.popleft()
        if (nx, ny) in reachable:
            continue
        reachable.add((nx, ny))
        ### Check all the adj nodes
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ax,ay = dx+nx, dy+ny
            if 0 <= ax < w and 0 <= ay < h:

                if grid[ay][ax] <= grid[ny][nx]:
                    q.append((ax,ay))


ans = 0
while q:
    height, x, y = q.popleft()
    if height <= 1:
        continue

    if (x,y) in reachable:
        continue
        ### We definitely don't need an elevator here
    #print(height, x,y, "HERE")
    ans += 1
    ### Place one of the elevators

    for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        ax, ay = dx + x, dy + y
        if 0 <= ax < w and 0 <= ay < h and grid[ay][ax] != 0:
            level_search(ax,ay)
#print(len(reachable), h*w, reachable)
print(ans)


