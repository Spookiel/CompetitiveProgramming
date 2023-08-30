from collections import deque
from random import shuffle
import random

n = int(input())
nums = list(map(int, input().split()))




def part_sort(nums):
    #### First calculate the positions of everything

    pos = [0]*(len(nums)+1)

    for i in range(len(nums)):
        pos[nums[i]] = i+1

    to_sort = deque()
    for i in range(1, len(nums)+1):
        if pos[i] != i:
            to_sort.append(i)
            ### Need to sort this position

    early = 1
    ans = set()
    while len(ans) < len(nums)//2:
        if not to_sort:
            #### Everything is sorted but we still need to pad until it's n/2 long
            ans.add(early)
            early += 1
        else:
            ne = to_sort.popleft()
            ans.add(ne)
            if len(ans) < len(nums)//2:
                ans.add(pos[ne])
    #### Now make the changes
    print(*ans)
    #print(len(ans))
    assert len(ans) == len(nums)//2
    inds = sorted(ans)
    so = sorted([nums[i-1] for i in ans])

    for mind, ind in enumerate(inds):
        nums[ind-1] = so[mind]
    return nums

def solve(nums, SUBMIT=True):
    orig = list(nums)
    if SUBMIT:
        print(3)
    for p in range(3):
        nums = part_sort(nums)
    if SUBMIT:
        pass
        #print(nums)
    if nums != [i+1 for i in range(len(nums))]:
        print("ORIGINAL", orig)
        print("FAILED", nums)
        input()


solve(nums)
assert nums == sorted(nums)
# for i in range(10000):
#     size = random.randint(1, 10)
#     ra = [i+1 for i in range(size*4)]
#     shuffle(ra)
#     solve(ra, SUBMIT=False)


