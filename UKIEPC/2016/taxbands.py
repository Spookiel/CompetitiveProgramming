







b = int(input())

bands = [list(map(float, input().split())) for i in range(b)]

lastband = float(input())
bands.append((99999999999999999999999999999999999, lastband))

EPS = 1e-7
def compute(income, gift):
    bandscop = list(map(list, bands))
    for ind,(s, p) in enumerate(bandscop):
        taking = min(income, s)
        income -= taking
        bandscop[ind][0] -= taking
        if abs(bandscop[ind][0]) < EPS:
            bandscop[ind][0] = 0

    res = 0
    for ind,(s, p) in enumerate(bandscop):
        taking = min(gift, s)
        res += taking*((100-p)/100)
        gift -= taking

    #print(bandscop)

    return res

def solve(income, target):
   # print(income, target)
    low = 0
    high = 1e12
    while abs(high-low) > EPS:

        mid = (low+high)/2


        got = compute(income, mid)
        #print(low, got, high, income+mid)

        if got < target:
            low = mid

        else:
            high = mid
        if abs(target-got) < EPS:
            break
    return low




f = int(input())

for i in range(f):

    friend = list(map(float,input().split()))
    print(solve(*friend))
    #print(compute(15000, 8624.5))
    #break