


import time

time.sleep(0.8)


from collections import deque, defaultdict

t = int(input())


best = defaultdict(lambda: 9999999)
parent = defaultdict(lambda:(-1,0))
START_VAL = 12345
start = (START_VAL,START_VAL,None)


q = deque()

q.append((start, 0))

best[start] = 0


def single_transitions(state):

    a,x,s = state
    ### Can set either of the registers to zero or one
    yield 0,(a,0,s)
    yield 1,(0,x,s)
    yield 2,(a,1,s)
    yield 3,(1,x,s)

    if x != START_VAL and a != START_VAL:
        ### Can pull the stack into one of the registers
        if s is not None:
            yield 4,(s,x, None)
            yield 5,(a, s, None)
        else:
            yield 6,(a,x,x)
            yield 7,(a,x,a)
    ### Otherwise can add the register
    ### Handle separately because distance is two
DOUBLE_TRANSITION_CODE = 8
INSTRUCTIONS = ["ZE X", "ZE A", "ST X", "ST A",
                "PL A", "PL X", "PH X", "PH A", "PH A\nAD", "PH X\nAD"]

while q:
    ne, dist = q.popleft()

    if t in ne:
        state = tuple(ne)
        ans = []
        while True:
            #print(ne, parent[ne][1], parent[ne][0])
            code, ne = parent[ne]
            if code == -1:
                break
            ans.extend(INSTRUCTIONS[code].split("\n")[::-1])
        ans = list(reversed(ans))
        #print(len(ans))
        for i in ans:
            print(i)
        if t == state[2]:
            print("PL A")
            print("DI A")
        elif t == state[1]:
            print("DI X")
        else:
            print("DI A")

        break
    for code,single in single_transitions(ne):
        if dist+1 < best[single]:
            best[single] = dist+1
            parent[single] = code, ne
            q.append((single, dist+1))

    if ne[2] is not None:
        for op in range(2):
            new_state = list(ne)

            new_state[2] = new_state[2]+new_state[op]
            new_state = tuple(new_state)

            if dist+2 < best[new_state]:
                best[new_state] = dist+2
                parent[new_state] = DOUBLE_TRANSITION_CODE+op,ne
                q.append((new_state, dist+2))





