


n,p = list(map(int, input().split()))

scores = [int(input()) for i in range(n)]
cur = [0]*n
cur[-1] = 0 if scores[-1] == 0 else 1
for i in range(n-2,-1,-1):
    if scores[i+1] < scores[i]:
        cur[i]  = cur[i+1]+1
    else:
        cur[i] = cur[i+1]
if cur[0] != p and sum(scores) > 0:
    print("ambiguous")
else:
    for k in cur:
        print(k)



