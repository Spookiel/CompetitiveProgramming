
from collections import defaultdict
import random
from math import sin, cos, pi, dist, degrees
tree = defaultdict(list)
n = int(input())



DEBUG = False
BANS = False

for i in range(n-1):
    a,b = list(map(int, input().split()))

    tree[a].append(b)
    tree[b].append(a)


size = dict()


def count_size(node, par=-1):
    tsize = 1
    for child in tree[node]:
        if child != par:
            tsize += count_size(child, node)
    size[node] = tsize
    return tsize




def solve(node, startrad, endrad, par=-1):
    #print("SOLVING", node, par)
    x,y = coords[node]
    if not tree[node]:
        return

    startarc = float(startrad)
    for ind, child in enumerate(tree[node], start=1):
        if child == par:
            continue
        angchange = (size[child]/(size[node]))*(endrad-startrad)

        dx = sin(startarc+(angchange/2))
        dy = cos(startarc+(angchange/2))
        coords[child] = (x+dx, y+dy)
        #print("PLACING PAR", node, "CHILD", child, coords[child], degrees(angchange), size[child], size[node], degrees(startrad), degrees(endrad))


        solve(child, startarc, startarc+angchange, node)
        startarc += angchange

coords = [None]*(n+1)

def check(node, par=-1):
    for child in tree[node]:
        assert abs(dist(coords[node], coords[child])-1) <= (1e-6)

        #print("CHECKED", node, child, abs(dist(coords[node], coords[child])-1))
        if child != par:
            check(child, node)
def check_pairs_dist():
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            #print(i, j, coords[i], coords[j], dist(coords[i], coords[j]))
            #assert dist(coords[i], coords[j]) >= 1e-4
            if dist(coords[i], coords[j]) <= 1e-4:
                return False
    return True
### Choose node with the most children as the root?
#check(root)

root = 1
count_size(root)
coords[root] = (0,0)
solve(root, 0, 2*pi)

check(1)
check_pairs_dist()

for node in coords[1:]:
    #node = coords[ind]
    if BANS:
        print(f"({node[0]:.10f},{node[1]:.10f})")
    else:
        print(f"{node[0]:.10f} {node[1]:.10f}")

#print("TRIES:", tries, root)
