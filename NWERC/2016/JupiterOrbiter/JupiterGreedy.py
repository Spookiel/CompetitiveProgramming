

n,q,s = list(map(int, input().split()))

feeds = [int(i)-1 for i in input().split()]
qcaps = list(map(int, input().split()))
windows = [list(map(int, input().split())) for i in range(n)]


restrictions = []
target = 0
fqs = [0 for i in range(q)]
for wind, (tcap, *data) in enumerate(windows):
    for sensor in range(len(data)):
        fqs[feeds[sensor]] += data[sensor]
        target += data[sensor]
    for qi in range(len(fqs)):
        excess = fqs[qi]-qcaps[qi]
        if excess > 0:
            restrictions.append((wind, excess, qi))
restrictions.sort()
can = True
tm = 0
fqs = [0 for i in range(q)]
for wind, (tcap, *data) in enumerate(windows):
    for sensor in range(len(data)):
        fqs[feeds[sensor]] += data[sensor]
        fqs[feeds[sensor]] = min(qcaps[feeds[sensor]], fqs[feeds[sensor]])

    ### Now need to work out how to remove the data
    left = int(tcap)
    while restrictions and left:
        wlatest, need, qi = restrictions.pop(0)
        if wlatest <= wind:
            can = False
        ### Otherwise still have time to fix this
        if need <= left:
            left -= need
            fqs[qi] -= need
            tm += need
        else:
            ### Going to have to leave this one on the queue
            fqs[qi] -= left
            tm += left
            restrictions.append((wlatest, need-left, qi))
            left = 0
    restrictions.sort()
    #print(left, fqs, tm)
    for qi in range(len(fqs)):
        #print(qi, fqs[qi], left, tm)
        if fqs[qi] <= left:

            left -= fqs[qi]
            tm += fqs[qi]
            fqs[qi] = 0
        else:
            fqs[qi] -= left
            tm += left
            left = 0

#print(tm, target)
if tm >= target and can:
    print("possible")
else:
    print("impossible")
