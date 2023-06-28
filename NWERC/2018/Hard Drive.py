


n,b,c = list(map(int, input().split()))




broken = set([int(i)-1 for i in input().split()])
ans = [0 for i in range(n)]

ans[0] = 1 if b%2 == 1 else 0
for j in range(1,n):
    #print(b, j, ans)

    if b == 0:
        break

    if j not in broken:
        b -= 1
        if ans[j-1] == 1:
            continue

        ans[j] = 1
    else:
        if ans[j-1] == 1:
            b -= 1





print("".join(list(map(str, ans))))