t = int(input())
nums = list(map(int, input().split()))

from random import randint
from collections import deque
def check(seq):

    for i in range(1, len(seq)-1):
        tdiff = abs(seq[i-1] - seq[i])
        idiff = abs(seq[i]-seq[i+1])
        if tdiff > idiff:
            return False

    return True


def brute_check():
    for j in range(100):
        nums = [randint(-100, 100) for _ in range(400)]
        ans = solve(nums)
        if not check(ans):
            print(nums)
            print("ANSWER WAS: ", ans)
            print("SORTED IS ", sorted(nums,key = lambda x: abs(x)))
            input()


def solve(nums):
    nums.sort()
    res = []
    nums = deque(nums)
    while len(nums) >= 2:
        a = nums.pop()
        b = nums.popleft()
        #print(a,b)
        res.append((a,b))

    res.sort(key = lambda x: abs(x[0]-x[1]))


    for j in res:
       nums.append(j[0])
       nums.append(j[1])
    return nums


ans = solve(nums)
#assert check(ans)
print(*ans)



