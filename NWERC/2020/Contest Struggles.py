


### Total is sum(diff) / n = d
### sum(up_to_k) / k = s
### (sum(diff) - sum(up_to_k)) / n-k

n,k = list(map(int, input().split()))
d,s = list(map(int, input().split()))

sdiff = d*n
uptok = s*k

res = (sdiff-uptok) / (n-k)

if res < 0 or res > 100:
    print("impossible")
else:
    print(res)