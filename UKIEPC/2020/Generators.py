


n,m = list(map(int, input().split()))
stations = [list(map(int, input().split())) for i in range(m)]
lines = list(map(int, input().split()))


from collections import defaultdict
import heapq as hp


graph = defaultdict(list)

VIRTUAL_POWER = 9999999999
prioq = []
hp.heapify(prioq)

for loc, cost in stations:
    graph[VIRTUAL_POWER].append((loc, cost))
    graph[loc].append((VIRTUAL_POWER, cost))

for ind in range(1,len(lines)+1):
    targ = ind+1 if ind != n else 1
    graph[ind].append((targ, lines[ind-1]))
    graph[targ].append((ind, lines[ind-1]))
#print(graph)
seen = set()
seen.add(VIRTUAL_POWER)
for t,c in graph[VIRTUAL_POWER]:
    hp.heappush(prioq, (c,t))
#print(prioq)
tot = 0
while prioq and len(seen) < n+1:
    cost,ne = hp.heappop(prioq)
    #print(ne, cost)
    if ne not in seen:
       tot += cost
       #print("ADDING", ne, cost, graph[ne])
       seen.add(ne)
       for t,c in graph[ne]:
           hp.heappush(prioq, (c,t))
print(tot)


