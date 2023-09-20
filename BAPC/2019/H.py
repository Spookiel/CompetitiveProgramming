
p,v = list(map(int, input().split()))
tests = [(4,3), (2,2), (2,3)]

got = [sorted(map(int, input().split()))+[i+1] for i in range(p)]
vs = list(map(int, input().split()))
vs = list(zip(vs, range(v)))
vs.sort()
from collections import defaultdict

buckets = defaultdict(list)
for a,b,c in got:
    assert a <= b
    buckets[(a,b)].append(c)
can = True
ans = [-1]*v
for i in range(v):
    val, ind = vs[i]
    ### Try to use the equal ones first
    if buckets[(val,val)]:
        ped_ind = buckets[(val,val)].pop()
    elif buckets[(val-1, val)]:
        ped_ind = buckets[(val-1, val)].pop()
    elif buckets[(val, val+1)]:
        ped_ind = buckets[(val, val+1)].pop()
    else:
        can = False
        break

    assert val in got[ped_ind-1]
    assert ans[ind] == -1
    ans[ind] = ped_ind

if not can:
    print("impossible")
else:
    assert -1 not in ans and len(set(ans)) == len(ans)
    for j in ans:
        print(j)