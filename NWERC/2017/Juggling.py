

def brute_sim(nums,debug=False):

    steps = 0
    while True:
        res = [nums[i] for i in range(len(nums))]
        cont = False
        for i in range(1,len(nums)-1):
            if nums[i] > 1:
                res[i-1] += 1
                res[i+1] += 1
                res[i] -= 2
        if len(nums) > 1:

            if nums[0] > 1:
                res[1] += 1
                res[0] -= 2
            if nums[-1] > 1:
                res[-2] += 1
                res[-1] -= 2
        else:
            res[0] = 0
        for j in res:
            if j > 1:
                cont = True
        if debug:
            print(f"DEBUG: {res}")
        if not cont:
            break
        steps += 1

        nums = res
    #print(f"Finished in {steps} steps")
    print("".join(list(map(str, res))))
    return steps
nums = [int(i) for i in input()]
brute_sim(nums, debug=True)
from random import shuffle
from collections import Counter
def brute_check():

    for j in range(2,20,2):
        ordered = [1,2]*(j//2)
        rand = list(ordered)
        shuffle(rand)
        print("Length:", j)

        res = brute_sim(rand)
        res2 = brute_sim(ordered)
        print(f"Shuffled: {res}")
        print(f"Ordered: {res2}")
        print(f"Counts: S - {Counter(ordered)}, US - {Counter(rand)}")
        print("-"*40)

#brute_check()

def move_one_check():


    for x in range(19,20):
        c = [1]*x +[2] + [2]*x
        #print(c)
        print(f"Steps: {brute_sim(c, debug=True)}")
#move_one_check()
