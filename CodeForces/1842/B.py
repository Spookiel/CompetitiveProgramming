t = int(input())


from itertools import permutations



def check(stacks,target):
    know = 0
    for j in range(3):
        for k in stacks[j]:
            if k | target == target:
                know |= k
            else:
                break
    if know == target:
        print("Yes")
    else:
        print("No")




def solve():
    n,x = list(map(int, input().split()))
    stacks = [list(map(int, input().split())) for i in range(3)]

    check(stacks, x)



for i in range(t):
    solve()