

from collections import defaultdict
n,m = list(map(int, input().split()))

stations = [list(map(int, input().split())) for i in range(m)]


ngraph = defaultdict(list)
dgraph = defaultdict(list)
firsts = []

for x,s,t,l in stations:
    ngraph[x].append((s,t))
    dgraph[x].append((s+l, t+l))
    if x == 1:
        firsts.append((s,t,l))
for i in ngraph:
    ngraph[i] = sorted(ngraph[i])
    dgraph[i] = sorted(dgraph[i])
# print(ngraph)
# print(dgraph)

import heapq as hp
def traverse(graph, first_train=None, delay=False):
    ### First train is (start, end) including delay if necessary

    best = [99999999 for i in range(n+1)]
    parents = [0 for i in range(n+1)]
    q = []
    hp.heapify(q)

    if first_train is not None and not delay:
        best[2] = first_train[1]
        ### Put objects on in terms of (time, node)
        hp.heappush(q, (first_train[1],2))
    if delay:
        best[1] = first_train[0]
        hp.heappush(q, (first_train[0],1))
    # print(q)
    # print(graph, delay)
    while q:
        cur_time, cur_node = hp.heappop(q)
        if cur_time != best[cur_node]:
            continue
        #print(cur_time, cur_node, delay)
        ### See which trains I can get from here

        for start, end in graph[cur_node]:
            if start >= cur_time:
                ### can take this train
                ### Would arrive at end
                if end < best[cur_node+1]:
                    ### Should take this train
                    best[cur_node+1] = end
                    parents[cur_node+1] = start
                    hp.heappush(q, (end, cur_node+1))
    # print(best)
    # print(parents)
    return best, parents



best = 999999999
for s,t,l in firsts:

    nd, ndp = traverse(ngraph, (s,t))
    d,dp = traverse(dgraph, (s,t), delay=True)
    # print(nd)
    # print(d)
    if d[-1]-nd[-1] >= 1800:
        ### Compensation possible
        best = min(best, s)
if best == 999999999:
    print("impossible")
else:
    print(best)


