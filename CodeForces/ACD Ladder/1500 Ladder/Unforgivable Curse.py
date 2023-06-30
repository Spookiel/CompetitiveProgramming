


t = int(input())

from collections import Counter, defaultdict

for i in range(t):
    n,k = list(map(int, input().split()))
    aFreqs = defaultdict(int)
    bFreqs = defaultdict(int)

    s = list(input())
    t = list(input())


    can = True
    for i in range(n):

        if i >= k or i+k < n:
            ### In swap range
            aFreqs[s[i]] += 1
            bFreqs[t[i]] += 1
        else:
            ### Can't swap so must be the same
            can &= s[i] == t[i]
    if aFreqs == bFreqs and can:
        print("Yes")
    else:
        print("No")