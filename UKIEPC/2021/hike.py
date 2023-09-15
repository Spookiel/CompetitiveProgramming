import sys

sys.setrecursionlimit(100000000)
from collections import defaultdict
n,m = list(map(int, input().split()))

graph = [[] for i in range(n+1)]

seen = [0 for i in range(n+1)]


def rec(node,first=1):
    seen[node] =1
    if first:
        print(node, end=" ")

    for child in graph[node]:
        if not seen[child]:
            ### Traverse this

            rec(child,1-first)
    ### Otherwise add to the order when unwinding

    if not first:
        print(node, end=" ")









for i in range(m):
    x,y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)


rec(1)

