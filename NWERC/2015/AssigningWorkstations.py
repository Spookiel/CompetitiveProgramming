
import heapq

n,m = list(map(int, input().split()))


unlockedUntil = []
using = []
heapq.heapify(using)

rs = [list(map(int, input().split())) for i in range(n)]
rs.sort()
#print(rs)
ctime = 0
got = 0
ind = 0
last = -1
while ind < len(rs):
    a,s = rs[ind]
    if using:
        ctime = min(a, using[0])
        if using[0] <= a:
            ctime = using[0]
        else:
            ctime = a
            ind += 1

    else:
        ctime = a
        ind += 1
    print(ctime, rs, unlockedUntil, using, ind)
    if ind != last:
        if not unlockedUntil:
            ### Must unlock a new machine for them

            using.append(ctime+s)
            got += 1
        else:
            ### Can just take one from the unlocked
            found = False
            while unlockedUntil:
                r = unlockedUntil.pop(0)
                if r <= ctime:
                    continue
                else:
                    found = True
                    break
            if not found:
                got += 1
            else:
                using.append(ctime+s)

        last = ind
    while using:
        leaving = heapq.heappop(using)
        if leaving == ctime:
            unlockedUntil.append(ctime+m)
        else:
            heapq.heappush(using, leaving)
            break
print(got)

