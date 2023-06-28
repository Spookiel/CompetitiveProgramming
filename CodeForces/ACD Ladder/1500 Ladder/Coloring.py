from math import ceil

t = int(input())

for i in range(t):
    n,m,k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    r = ceil(n/k)
    cnt = 0
    flag = True
    for i in nums:
        if  i == r:
            cnt += 1
        elif i > r:
            flag = False
            break
    #print(cnt, n%k)
    if not flag:
        print("NO")
    else:
        if cnt <= (n %k) or n%k == 0:
            print("YES")
        else:
            print("NO")