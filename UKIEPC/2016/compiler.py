from collections import deque, defaultdict
import heapq as hp
t = int(input())

best = defaultdict(lambda: 9999999)
parent = defaultdict(lambda:(-1,0))
START_VAL = 12345
start = (START_VAL,START_VAL,-1)

q = []
hp.heapify(q)
q.append((0, start))
best[start] = 0

def single_transitions(state):

    a,x,s = state
    ### Can set either of the registers to zero or one
    yield 0,(a,0,s)
    yield 1,(0,x,s)
    yield 2,(a,1,s)
    yield 3,(1,x,s)

    if s != -1:
        yield 4, (s, x, -1)
        yield 5, (a, s, -1)
    else:
        if x != START_VAL:
            yield 6,(a,x,x)
        if a != START_VAL:
            yield 7,(a,x,a)
    ### Otherwise can add the register
    ### Handle separately because distance is two
DOUBLE_TRANSITION_CODE = 8
INSTRUCTIONS = ["ZE X", "ZE A", "ST X", "ST A",
                "PL A", "PL X", "PH X", "PH A", "PH A\nAD", "PH X\nAD"]
while q:
    dist, ne = hp.heappop(q)

    if best[ne] != dist:
        continue
    best[ne] = dist

    if t in ne:
        state = tuple(ne)
        ans = []
        while True:
            code, ne = parent[ne]
            if code == -1:
                break
            ans.extend(INSTRUCTIONS[code].split("\n")[::-1])
        ans = list(reversed(ans))
        tot = len(ans)
        for i in ans:
            print(i)
        if t == state[2]:
            print("PL A")
            print("DI A")
            tot += 2
        elif t == state[1]:
            print("DI X")
            tot += 1
        else:
            print("DI A")
            tot += 1
        #print(f"COMPLETED IN {tot} instructions")
        break
    for code,single in single_transitions(ne):
        if dist+1 < best[single]:
            best[single] = dist+1
            #print("MOVING TO", single, dist+1)
            parent[single] = code, ne
            q.append((dist+1, single))
    #input()
    if ne[2] != -1:
        for op in range(2):
            if ne[op] == START_VAL:
                continue

            new_state = (ne[0], ne[1], ne[2]+ne[op])
            if dist+2 < best[new_state]:
                best[new_state] = dist+2
                parent[new_state] = DOUBLE_TRANSITION_CODE+op,ne
                q.append((dist+2, new_state))





