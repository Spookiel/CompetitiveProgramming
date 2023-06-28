


t = int(input())
for i in range(t):
    n,k = list(map(int, input().split()))
    ans = [-1]*n

    while k >= n and k > 0:
        #print(n, k)
        ans[n-1] = 1000
        k -= n
        n -= 1

    if k == 0:
        print(*ans)
    else:
        k -= 1
        ans[k] = 200
        ans[k+1] = -400
        print(*ans)