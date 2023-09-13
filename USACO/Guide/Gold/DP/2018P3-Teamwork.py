

with open("teamwork.in", "r") as fin:
    n,k = list(map(int, fin.readline().split()))
    nums = [int(fin.readline()) for i in range(n)]
best = [0 for _ in range(n+1)]


for i in range(1,n+1):
    cbest = nums[i-1]
    for j in range(1,min(k+1, i+1)):
        best[i] = max(best[i], best[i-j]+cbest*j)
        cbest = max(cbest, nums[i-j-1])
#print(best)

with open("teamwork.out", "w+") as fout:
    fout.write(str(max(best))+"\n")