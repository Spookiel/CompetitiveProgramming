


t = int(input())


for i in range(t):
    n = int(input())

    nums = list(map(int, input().split()))
    pos = [-1 for _ in range(len(nums)+1)]

    for j in range(len(nums)):
        pos[nums[j]] = j

    low = (n+1)//2
    high = (n+2)//2

    while low > 0 and (low == high or pos[low] < pos[low+1] and pos[high-1] < pos[high]):
        low -= 1
        high += 1
    print(low)
