

t = int(input())

for i in range(t):
    n,k = list(map(int, input().split()))

    nums = [int(i) for i in input().split()]
    res = []
    tot = 0
    for j in nums:
        tot += j//k
        res.append(j%k)
    res.sort()

    low = 0
    high = n-1
    while low < high:
        r = (res[low]+res[high])
        if r >= k:
            #print("PAIRED", res[low], res[high], r//k)
            tot += r//k
            high -= 1
        low += 1
    print(tot)






