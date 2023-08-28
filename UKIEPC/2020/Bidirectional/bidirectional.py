
from random import random

n = int(input())

def process_end(num):
    return 1

ans = []
def reduce(num):
    global ans
    if len(str(num)) <= 2:
        #print("LEFT",  num)
        for j in range(9,-1,-1):
            if (c := int(10*j+j)) <= num and c != 0:
                ans.append(c)
                num -= c
        if len(str(num)) == 1 and num != 0:
            ans.append(num)
        elif num != 0:
            ans.append(1)
            ans.append(9)
        return


    minus = num-max(int(50*random()), int(0.001*int(num)))
    print(minus,int(50*random()), int(0.001*int(num)), num)
    res = ["0" for i in range(len(str(minus)))]
    for dig in range((len(str(minus)))//2):
        res[dig] = str(minus)[dig]
        res[-dig-1] = str(minus)[dig]

    if len(str(minus))%2 == 0:
        mid = len(str(minus))//2
        res[mid] = "0"
        res[mid+1] = "0"


    res = "".join(res)

    ans.append(res)

    print(num, res, "HERE")
    return reduce(num-int(res))



its = 0
best = 99999
while True:
    reduce(n)
    if len(ans) < best:
        best = len(ans)
        #print(best)
    if sum(map(int, ans)) != n or len(ans) > 10:
        #print(sum(map(int, ans)), n)
        #print(ans)
        ans = []
        its += 1
        continue
    print(len(ans))
    for k in ans:
        print(k)
    break
