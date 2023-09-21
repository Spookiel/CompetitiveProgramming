from math import ceil, log2
a,b = list(map(int, input().split()))
c,d = list(map(int, input().split()))

depth = ceil(log2(c+d))

processing = [(c,-1),(d,-2), (pow(2, depth)-c-d,0)]
processing.sort(reverse=True)

ans = [None for i in range(400)]

def wire_one_one(ind, out1, out2):
    ans[ind] = (ind+1, ind+2)
    ans[ind+1] = (ind, out1)
    ans[ind+2] = (out2, ind)

def solve_fewer(cur_val, ind=0):
    global processing
    if all([i[0] == 0 for i in processing]) or cur_val ==0:
        return 0
    ne,target = processing.pop(0)
    left = ind+3
    right = None
    if cur_val//2 <= ne:
        ### Should pipe left output to target
        processing.append((ne-cur_val//2, target))
        processing.sort(reverse=True)
        left = target
        right = ind+3
        ### Only way you can have this would be at the last layer
        ne, target = processing.pop(0)
        if cur_val//2 <= ne:
            right = target
            processing.append((ne-cur_val//2, target))
            processing.sort(reverse=True)
            wire_one_one(ind, left, right)
            return 3
        else:
            ### Still need to process right tree
            processing.append((ne, target))
            wire_one_one(ind, left, right)
            return solve_fewer(cur_val//2, ind+3)+3

    ### Can't use this node as too big
    processing.append((ne, target))
    processing.sort(reverse=True)

    left_size = solve_fewer(cur_val//2, ind+3)
    right_size = solve_fewer(cur_val//2, ind+left_size+3)
    wire_one_one(ind, left, ind+left_size+3)
    return left_size+right_size+3


solve_fewer(pow(2, depth))
alen = ans.index(None)
ans = ans[:alen]
print(len(ans))
DEBUG = 0
assert len(ans) <= 200
for ind,x in enumerate(ans):
    if DEBUG == 1:
        print(ind,":", *x)
    elif DEBUG == 2:
        print(f"Splitter{x[0], x[1], 0 if ind != 0 else 1},", end=" ")
    else:
        print(*x)