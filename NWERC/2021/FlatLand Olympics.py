
from functools import cmp_to_key
from math import atan2, degrees, gcd,dist
sx,sy,ex,ey = list(map(int, input().split()))
s,e = sorted([(sx,sy), (ex,ey)]) ### Make sure start is down and to the left of end
sx,sy = s
ex,ey = e
n = int(input())

coords = [list(map(int, input().split())) for i in range(n)]


def f(a,x, y):
    return atan2(*[a[1] - y, a[0] - x])

def det(p, q, r): return (p[0] - r[0]) * (q[1] - r[1]) - (p[1] - r[1]) * (q[0] - r[0])
def make_cmp(s, t, reverse=1):
    def cmp(p1, p2):
        a = det(p1, p2, s)
        if a != 0: return a * reverse
        a = det(p1, p2, t)
        return -a * reverse

    return cmp

def sort_around(lst, rev = False):
    if not rev:
        return sorted(lst, key=cmp_to_key(make_cmp(s,e)))
    else:
        return sorted(lst, key=cmp_to_key(make_cmp(e, s, reverse=-1)), reverse=True)
    # if rev:
    #     return sorted(lst, key = lambda a:( f(a,sx,sy), -f(a,ex,ey)))
    # else:
    #     return sorted(lst, key=lambda a: (f(a, ex, ey), -f(a, sx, sy)))


#### Need to get rid of the co-linear points first
#### Just check the gradient of the point to the start



def grad_to(p1, p2):
    a,b = p1
    c,d = p2
    dy = d-b
    dx = c-a
    gc = gcd(dx,dy)
    dy //= gc
    dx //= gc
    if dx == 0:
        return float("inf")
    return float(dy)/float(dx)

rest = []
left = []

leftup = []
leftdown = []
rightup = []
rightdown = []

right = []

linegrad = grad_to(s, e)
##print(linegrad, "HERE")
for j in coords:
    gs = grad_to(j,s)
    if gs == linegrad:
        if tuple(j) <= s:
            left.append(j)
        else:
            right.append(j)
    else:
        rest.append(j)


#print(rest, "HERE")
coords = rest
gswaps = 0


### Deal with the ones co-linear to the ends

for lst in [left, right]:
    #print(lst)
    if lst:
        gswaps += 0.5*len(lst)*(len(lst)-1)




def solve(loc_coords):
    # print("\n\n\n")
    # for k in loc_coords:
    #     print(k, "START ANGLE", degrees(f(k, sx,sy)), "END ANGLE", degrees(f(k, ex,ey)))
    #
    # print("\n\n\n")


    r1 = sort_around(loc_coords)
    #print("SOLVING", loc_coords)
    #print(r1)
    mp = {}
    for i in range(len(r1)):
        mp[tuple(r1[i])] = i

    res = []
    r2 = sort_around(loc_coords,True)
    #print(r2)
    ##print("AROUND SECOND")
    for k in r2:
        res.append(mp[tuple(k)])
    ##print(degrees(f(k, ex, ey)), k)
    #print(res, "MERGING")
    mergesort(0, len(res),res)

### Now need to count the inversions in res

def merge(left, mid, right, res):
    global gswaps
    merged = []
    swaps = 0
    rpointer = int(mid)
    lpointer = int(left)
    while lpointer < mid and rpointer < right:
        ### Need to compare these two elements
        a = res[lpointer]
        b = res[rpointer]
        if b < a:
            swaps += mid-lpointer
            merged.append(b)
            rpointer += 1
        else:
            merged.append(a)
            lpointer += 1
    ##print(swaps, "SWAPS FOR", left, right, "BEFORE REST")
    if lpointer < mid:
        ### Need to add the rest of the left ones
        ### So these ones are bigger than all of the ones on the right

        #swaps += (right-rpointer)*(mid-lpointer)
        for j in range(lpointer, mid):
            merged.append(res[j])
    else:
        ### All the ones to the right are bigger
        ### BUt that's fine because there's no inversions here then
        for j in range(rpointer, right):
            merged.append(res[j])
    ### Now need to replace the merged
    for j in range(left, right):
        res[j] = merged[j-left]
    ##print("SWAPS FOR ", left, right, "IS", swaps)
    gswaps += swaps
def mergesort(left, right,res):
    ###  [left, right)
    if right-left <= 1:
        return
        ### Just one element

    mid = (left+right)//2
    mergesort(left, mid,res)
    mergesort(mid, right,res)
    merge(left, mid, right,res)
def cross(a,b):
    return a[0]*b[1] - a[1]*b[0]
def vto(a,b):
    return b[0]-a[0], b[1]-a[1]


def is_above(ls, le, point):

    det = cross(vto(ls,le), vto(ls, point))
    assert det != 0
    return det < 0


above = []
below = []
for i in coords:
    if is_above(s, e, i):
        above.append(i)
    else:
        below.append(i)

solve(below)
solve(above)
print(int(gswaps))



