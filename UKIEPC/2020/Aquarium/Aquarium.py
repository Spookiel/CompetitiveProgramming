

n,k = list(map(int, input().split()))

start = list(map(int, input().split()))
end = list(map(int, input().split()))



def step(positions):
    positions = list(positions)
    last = -1
    got = []
    for ind, p in enumerate(positions):
        diff = p-last

        if diff >= 4:
            ### Then can move both of these fish
            if last < 0:
                ### This is the first fish
                got.append([p-1]+list(positions[1:]))
            elif ind == n-1:
                ### THis is the last fish
                got.append(list(positions[:-1])+[p+1])
            else:
                #### Has fish to both sides

                got.append(list(positions[:ind-1])+[positions[ind-1]+1, p-1]+list(positions[ind+1:]))
        last = p
    #print(got)
    if n-positions[-1] >= 2:
        got.append(list(positions[:-1])+[positions[-1]+1])
    for i in got:
        assert len(i) == len(positions)
    return list(map(tuple, got))


#print(step((1, 4, 7, 10, 15, 18)))

#exit()
from collections import deque

q = deque()

seen = set()
seen.add(tuple(start))

q.append((tuple(start),0))

ans = -1
while q:
    cur, dist = q.popleft()
    print(cur, dist)
    if cur == tuple(end):
        ans = dist
        break


    for adj in step(cur):
        if adj not in seen:
            seen.add(adj)
            q.append((adj, dist+1))
if ans == -1:
    print("impossible")
else:
    print(ans)




