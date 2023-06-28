




def solve():
    x = int(input())
    nums = list(map(int, input().split()))
    dp = [999999999 for i in range(len(nums)+1)]
    dp[0] = 0
    bestcols = [9999999 for i in range(len(nums)+1)]

    for i in range(1, len(nums)+1):
        dp[i] = min(dp[i-1]+1,bestcols[nums[i-1]])

        bestcols[nums[i-1]] = min(bestcols[nums[i-1]], dp[i-1])
    #print(dp)
    print(len(nums)-dp[-1])

n = int(input())


for i in range(n):
    solve()