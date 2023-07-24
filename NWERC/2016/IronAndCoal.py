
from collections import deque
n,m,k = list(map(int, input().split()))
irons = set(map(int, input().split()))
coals = set(map(int, input().split()))

ALLIRON = int(1e8)
ALLCOAL = int(1e9)


from collections import defaultdict

graph = defaultdict(list)
revgraph = defaultdict(list)

for i in range(n):
    a, *reach = list(map(int, input().split()))
    reach = [(j, 1) for j in reach]
    graph[i+1].extend(reach)
    for r in reach:
        #print("ADDING", r, i+1, "TO REVERSE")
        revgraph[r[0]].append((i+1, 1))

    if i+1 in irons:
        graph[i+1].append((ALLIRON,0))
        revgraph[ALLIRON].append((i+1,0))
    if i+1 in coals:
        graph[i+1].append((ALLCOAL,0))
        revgraph[ALLCOAL].append((i+1,0))

# print(graph)
# print(revgraph)

def bfs(g, start=1):
    MAXDIST = 9999999999
    odists = defaultdict(lambda:MAXDIST)

    q = deque()
    q.append((start,0))

    while q:
        ne,cdist = q.popleft()
        if odists[ne] != MAXDIST:
            continue
        odists[ne] = cdist

        for adj,w in g[ne]:
            if odists[adj] == MAXDIST:
                q.append((adj, cdist+w))
    return odists


odists = bfs(graph)
coaldists = bfs(revgraph, ALLCOAL)
irondists = bfs(revgraph, ALLIRON)

#
# print(odists)
# print(coaldists)
# print(irondists)

MAXDIST = 9999999
best = MAXDIST

for i in range(1, n+1):
    #print(i, odists[i], coaldists[i], irondists[i])
    best = min(best, odists[i]+coaldists[i]+irondists[i])

if best == MAXDIST:
    print("impossible")
else:
    print(best)




