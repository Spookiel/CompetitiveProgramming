

r,c,k = list(map(int, input().split()))

grid = [[i for i in input()] for j in range(r)]

fungs = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            fungs.append((j,i))


def make_rectangle(centre, time):

    return sorted([(centre[0]+time, centre[1]+time), (centre[0]+time, centre[1]-time), (centre[0]-time, centre[1]-time), (centre[0]-time, centre[1]+time)])
def lrud(rect):
    xs = [i[0] for i in rect]
    ys = [i[1] for i in rect]
    return min(xs), max(xs), min(ys), max(ys)
rects = [make_rectangle(i, k) for i in fungs]

from collections import defaultdict, deque

grid = defaultdict(int)

if k <= 22:
    for cs in rects:
        xs = [i[0] for i in cs]
        ys = [i[1] for i in cs]

        for xcoord in range(min(xs), max(xs)+1):
            for y in range(min(ys), max(ys)+1):
                grid[(xcoord, y)] += 1
    tot = 0

    for j in grid:
        #print(j, grid[j])
        if grid[j] >= 1:
            tot += 1
    print(tot)
else:
    ### Time to do the big thing with the connected ones

    q = deque()

    rects.sort()


    lines = [lrud(i) for i in rects]
    lines.sort()
    events = []

    for ind, (l,r,d,u) in enumerate(lines):
        events.append((l, 0, ind))
        events.append((r+1, 1, ind))
    events.sort(reverse=True)
    if not events:
        print(0)
        exit()
    currects = set()
    curx = events[-1][0]

    tot = 0
    while events:
        sq = []
        nx = events[-1][0]
        #print(curx, nx, currects, events)
        high = -1e9
        low = 1e9
        for j in currects:
            high = max(high, lines[j][3])
            low = min(low, lines[j][2])
        if currects:
            #assert curx <= nx and high >= low
            tot += (nx-curx)*(high-low+1)

        while events and events[-1][0] == curx:
            x, etype, ind = events.pop()
            sq.append((x, etype, ind))

        for x, etype, ind in sq:
            if etype == 0:
                currects.add(ind)
            else:
                currects.remove(ind)
            if not nx:
                nx = x
        # Now time to do the adding
        curx = nx

    print(tot)










