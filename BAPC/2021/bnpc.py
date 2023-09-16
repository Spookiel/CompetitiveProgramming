from collections import defaultdict
n,k = list(map(int, input().split()))


scores = {}
for i in range(n):
    attri, score = input().split()
    scores[attri] = int(score)

l = int(input())

events = []
for i in range(l):
    event, needed = input().split()
    needed = int(needed)
    events.append((event, needed))

    if scores[event] < needed:
        k -= needed-scores[event]
        scores[event] = needed
        ### Definitely need to spend this many points

if k < 0:
    print(0)
    ### No way to get over the threshold for every event
else:
    ### Need to allocate the remaining points somehow
    ### Try allocating the remaining points to a single attribute

    ans = 0
    cnt = defaultdict(int)
    at_bdn = defaultdict(int)
    lt_bdn = defaultdict(int)
    #print(events)
    tot = 0
    for name, score in events:
        cnt[name] += 1
        if score == scores[name]:
            at_bdn[name] += 1
        else:
            lt_bdn[name] += 1
            tot += scores[name]
    #print("DEFINITELY GETS", tot)
    ### (one turn value, can repeat
    moves = []
    for name in cnt:
        moves.append((at_bdn[name]*(scores[name]+1)+lt_bdn[name], False))
        moves.append((cnt[name], True))

    moves.sort()
    #print(moves)

    while k:
        score_per_point, repeat = moves.pop(-1)
        if not repeat:
           tot += score_per_point
           k -= 1
        else:
            tot += score_per_point*k
            k = 0
    print(tot)
