
from itertools import product

key = [58018, 419817, 467405, 76676, 168542, 130899, 112855, 109529, 105539, 321104, 81539, 143665, 486822, 366448, 445912, 111388]

MOD = int(1e9+7)
def evaluate(seq, nums):
    assert len(nums) == len(seq)+1, f"{len(nums)}, {len(seq)}"
    ### 0 for add and 1 for multiply

    first = nums[0]
    for j in range(1, len(nums)):
        if seq[j-1] == 0:
            first += nums[j]
        else:
            first *= nums[j]
        first %= MOD
    return first

def build_master(nums):
    seen = dict()
    for seq in product([0,1], repeat=len(nums)):
        seen[evaluate(seq, [0]+nums)] = tuple(seq)
        #print(seq,evaluate(seq, nums))

    if len(seen) == pow(2,len(nums)):
        return seen
    return None


look = build_master(key)
#print(look)
BSIZE = 16
n = int(input())
blocks = [0 for i in range(n+1)]
divs = [blocks[i:i+BSIZE] for i in range(0, len(blocks), BSIZE)][::-1]
### Divides into blocks of 16 with small block at the front

cur_ind = len(divs)-1
found = []

#print([i for i in look if look[i] == (0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)])
#+xx+x+xx+x+xx+x+xx+x
#print(evaluate((0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1), [0,0,0,0,0]+key))

def query(ind):
    divs[ind] = key
    after = list(map(str, key))+list(map(str, found))
    print("?", "0 "*(n+1-len(after))+" ".join(after))
while cur_ind > 0 and len(divs[cur_ind]) == BSIZE:
    query(cur_ind)

    res = int(input())

    func = look[res]
    found = list(func)+found
    cur_ind -= 1

def query_small():
    global found
    for i in range(n%BSIZE):
        if len(found) == n:
            break
        q = list(map(str, [0]*(n-len(found))+[1]+found))
        #print(len(q))
        print("? ", " ".join(q))
        ans = int(input())
        found = [1-ans]+found

query_small()

print("! "+"".join(["x" if i else "+" for i in found]))
