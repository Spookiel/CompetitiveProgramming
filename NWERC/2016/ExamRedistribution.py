


n = int(input())

nums = list(map(int, input().split()))

tot = sum(nums)

can = True
for j in nums:
    if j > tot/2:
        can = False

if can:
    r = list(range(len(nums)))
    r.remove(nums.index(max(nums)))

    print(nums.index(max(nums))+1, *[a+1 for a in r])
else:
    print("impossible")