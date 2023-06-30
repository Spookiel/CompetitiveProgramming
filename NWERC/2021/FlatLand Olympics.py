

from math import atan2, degrees
sx,sy,ex,ey = list(map(int, input().split()))
s,e = sorted([(sx,sy), (ex,ey)]) ### Make sure start is down and to the left of end
sx,sy = s
ex,ey = e
n = int(input())

coords = [list(map(int, input().split())) for i in range(n)]


def f(a,x, y):
    return atan2(*[a[1] - y, a[0] - x])


def sort_around(lst, x, y):


    return sorted(lst, key = lambda a:( f(a,x,y), a[0], a[1]))


r1 = sort_around(coords, sx, sy)

mp = {}
for i in range(len(r1)):
    mp[tuple(r1[i])] = i
    print(degrees(f(r1[i], sx, sy)), r1[i])

res = []
r2 = sort_around(coords, ex, ey)

print("AROUND SECOND")
for k in r2:
    res.append(mp[tuple(k)])
    print(degrees(f(k, ex, ey)), k)

### Now need to count the inversions in res

gswaps = 0

def merge(left, mid, right):
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
    #print(swaps, "SWAPS FOR", left, right, "BEFORE REST")
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
    #print("SWAPS FOR ", left, right, "IS", swaps)
    gswaps += swaps
def mergesort(left, right):
    ###  [left, right)
    if right-left == 1:
        return
        ### Just one element

    mid = (left+right)//2
    ##print(left, mid, right)
    #print(f"SPLITS {res[left:mid]} AND {res[mid:right]}")
    mergesort(left, mid)
    mergesort(mid, right)
    #print(res, left, mid, right, "HERE")
    merge(left, mid, right)
#res = [5,1,4,2,3,6,7,9,8]
#print(res, "BEFORE")
mergesort(0, len(res))
print(gswaps)


