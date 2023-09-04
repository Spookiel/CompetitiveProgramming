


n,b,r = list(map(int, input().split()))


bb = [list(map(int, input().split())) for i in range(b)]
rb = [list(map(int, input().split())) for i in range(r)]


from math import ceil,sqrt
def dist(p,q):
    return (p[0]-q[0])*(p[0]-q[0]) + (p[1]-q[1])*(p[1]-q[1])

def max_flow(C, s, t):
    n = len(C)  # C is the capacity matrix
    F = [[0] * n for i in range(n)]
    path = bfs(C, F, s, t)
    #  print path
    while path != None:
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))


# find path by using BFS
def bfs(C, F, s, t):
    queue = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v == t:
                    return paths[v]
                queue.append(v)
    return None

def solve(minDist):
    global bb, rb

    sqDist = minDist*minDist
    caps = [[0]*(len(bb)+2+len(rb)) for i in range(len(bb)+len(rb)+2)]
    ## 0 is s, 1 is t, 2...len(bb)+1 is blue len(bb)+2..len(bb)+len(rb)+2 is red
    for bind,b in enumerate(bb):
        caps[0][2+bind] = 1
        #caps[2+bind][0] = 1
        for rind,r in enumerate(rb):
            euclid = dist(b,r)
            #print(b,r, euclid)
            if euclid <= sqDist:
                caps[2+bind][2+len(bb)+rind] = 1
                #caps[2+len(bb)+rind][2+bind] = 1
    for rind,r in enumerate(rb):
        caps[2+len(bb)+rind][1] = 1
        #caps[1][2+len(bb)+rind] = 1
    # for cap in caps:
    #     print(*cap)

    # G = Graph(caps)
    # res = G.FordFulkerson(0,1)
    res = max_flow(caps, 0,1)
    #print("FOUND", res)
    return res





low = 1
high = 30000

EPS = 1e-8
while abs(high-low) > EPS:
    mid = (low+high)/2
    ### Can we solve this where the minimum distance apart is mid
    #print(low, mid, high)
    res = solve(mid)


    if b+r-res >= n:
        ### Can match using this
        low = mid
    else:
        high = mid
print(round(low, 6))