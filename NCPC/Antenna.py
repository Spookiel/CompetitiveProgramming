n,c = list(map(int, input().split()))



nums = list(map(int, input().split()))


low = 0
high = 0

for i in range(len(nums)):
    if nums[high]-nums[i] - (i-high)*c < 0:
        high = i

    if nums[i]-nums[low] - (i-low)*c < 0:
        low = i

    score = max(abs(nums[low] - nums[i]) - c * (i - low), abs(nums[high] - nums[i]) - c * (i - high))
    print(score, end=" ")
