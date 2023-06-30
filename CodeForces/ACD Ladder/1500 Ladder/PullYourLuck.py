




#print(can)
t = int(input())
for i in range(t):
    n,x,p = list(map(int, input().split()))


    for px in range(1, min(p, 2*n)+1):
        res = (x+0.5*px*(px+1)) % n
        if res == 0:
            print("yes")
            break
    else:
        print("No")



