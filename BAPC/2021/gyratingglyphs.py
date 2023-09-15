

from itertools import combinations, product
from random import randint


MOD = int(1e9+7)


def evaluate(seq, nums):
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
    for seq in product([0,1], repeat=len(nums)-1):
        seen[evaluate(seq, nums)] = tuple(seq)

    if len(seen) == pow(2,len(nums)-1):
        return seen
    return None

assert evaluate([1,1,0,0], [2,4,3,1,1]) == 26

#print(build_master([58018, 419817, 467405, 76676, 168542, 130899, 112855, 109529, 105539, 321104, 81539, 143665, 486822, 366448, 445912, 111388]))

all_keys = [[0],[0], [3300, 4433], [7110, 3350, 9060], [9798, 1436, 4822, 5379], [8981, 6714, 4881, 2614, 5329], [8789, 7860, 4420, 158, 5871, 4080], [6937, 2437, 4729, 8537, 1227, 4281, 5154], [6845, 3584, 4093, 8526, 3403, 1376, 3207, 170], [9856, 8543, 527, 2300, 9966, 6950, 4880, 2250, 5164], [7684, 8129, 1152, 8414, 5327, 5975, 1326, 1548, 9769, 9836], [2983, 8897, 2405, 1913, 5478, 1976, 628, 7437, 1439, 9520, 24], [6784, 8320, 9569, 5209, 9693, 930, 6398, 3312, 3928, 36, 4207, 5441], [1471, 3130, 9659, 802, 2720, 5447, 5568, 7599, 4867, 7911, 4481, 8999, 7986], [139, 5542, 345, 6268, 2159, 6300, 3198, 2870, 8302, 4209, 7102, 754, 4027, 7682], [4676, 4908, 1741, 6733, 4558, 9621, 5985, 8621, 2618, 2986, 3965, 8443, 5115, 9241, 5835], [3347, 3265, 5978, 1523, 6942, 2528, 1533, 2610, 6567, 4378, 5714, 3113, 6932, 7003, 605, 4705], [8795, 9979, 6347, 7427, 2100, 7956, 8368, 4760, 1505, 5429, 1147, 6855, 6284, 3544, 2171, 1235, 3545]]
#all_keys = [[0],[0], [0, 784], [0, 772, 390], [0, 789, 398, 450], [0, 497, 560, 196, 765], [0, 752, 324, 225, 839, 454], [0, 517, 657, 57, 420, 801, 987], [0, 812, 671, 988, 46, 911, 414, 225], [0, 200, 623, 180, 173, 455, 942, 883, 379], [0, 75, 594, 842, 271, 865, 288, 251, 215, 776], [0, 340, 371, 390, 304, 429, 702, 303, 339, 532, 175], [0, 305, 332, 538, 83, 546, 535, 876, 726, 553, 582, 63], [0, 986, 931, 45, 528, 42, 592, 249, 652, 779, 363, 61, 513], [0, 881, 216, 92, 975, 112, 816, 736, 111, 790, 845, 185, 567, 519], [0, 252, 468, 224, 630, 68, 592, 704, 729, 846, 444, 984, 144, 326, 521], [0, 934, 890, 506, 789, 729, 408, 56, 952, 650, 65, 892, 463, 660, 736, 207], [0, 799, 919, 876, 138, 987, 291, 199, 584, 742, 261, 645, 519, 960, 320, 261, 272]]


def generate_key(length):
    keyseq = None
    while not keyseq:
        nums = [0]+[randint(0, 1000) for j in range(length-1)]
        #print(nums)
        res = build_master(nums)
        if res is not None:
            print("FOUND",nums)
            keyseq = nums
    return keyseq

if all_keys is None:
    all_keys = [[0]]
    for slen in range(2,18):
        all_keys.append(generate_key(slen))
    print(all_keys)


def inverse(fres, hfunc):
    ### This one undoes hfunc suffix
    for j in range(len(hfunc)-1,-1,-1):
        if not hfunc[j]:
            fres -= 1
            fres += MOD
            fres %= MOD
    return fres






BLOCKSIZE = 16
n = int(input())

blocks = [0 for i in range(n+1)]
div_blocks = [blocks[i:i+BLOCKSIZE] for i in range(0, len(blocks),BLOCKSIZE)][::-1]

#print(div_blocks)

known = 0
cur_ind = len(div_blocks)-1

def query(cur_ind):
    out = list(div_blocks)
    for j in range(cur_ind+1, len(div_blocks)):
        for k in range(len(div_blocks[j])):
            out[j][k] = 1

    chosen_key = all_keys[len(div_blocks[cur_ind])]
    #print(chosen_key)
    out[cur_ind] = chosen_key
    print("?", end=" ")
    for k in out:
        print(*k, end=" ")
    print()
totadds = 0
invs = []
while cur_ind > 0:
    ### Query again
    query(cur_ind)

    result = int(input())

    for func in invs:
        result = inverse(result, func)

    lookup = build_master(all_keys[BLOCKSIZE])
    #assert len(lookup.keys()) == pow(2, len(div_blocks[cur_ind])-1)
    hfunc = lookup[result]
    #print("FOUND", hfunc)
    totadds += list(hfunc).count(0)
    invs.append(hfunc)

    cur_ind -= 1
print("!", end=" ")

for i in invs[::-1]:
    for k in i:
        if k == 0:
            print("+", end="")
        else:
            print("x", end="")
print()