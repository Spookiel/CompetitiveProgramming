
look = {"R":(1,0), "U":(0,1), "D":(0,-1), "L":(-1,0)}
oppo = {"L":"R", "R":"L", "D":"U", "U":"D"}
from random import randint, random


s = input()

if len(s) >= 3:
    if s[-3] == s[-1] and s[-1] == oppo[s[-2]]:
        print("impossible")
        exit()

def gen_board():
    walls = set()

    for j in range(-100, 100):
        for k in range(-100, 100):
            if random() < 0.05:
                walls.add((j, k))
    return walls


def next_pos(bx, by, d):
    dx,dy = look[d]
    return bx+dx, dy+by
def check(walls):

    seen = set()
    bx, by = 10,10
    seen.add((bx, by))

    for ind, move in enumerate(s):
        #print(move)

        if (bx, by) in walls:
            return False
        cnt = 0
        while next_pos(bx, by, move) not in walls:
            bx, by = next_pos(bx, by, move)
            seen.add((bx, by))
            cnt += 1
            if cnt >= 600:
                #print("FAILED TOO MANY ITERATIONS")
                return False

    cnt = 0
    for x,y in seen | walls:
        if x - bx == 0 and y - by == 0:
            #print("FAILED HERE")
            cnt += 1
    if cnt != 1:
        return False
    # print(seen,walls)
    # print(bx, by)
    return True, bx, by

while True:
    walls = gen_board()

    res = check(walls)
    if res:
        #print(res)
        _, bx, by = res
        #print("ENDED", bx, by)
        print(10-bx,10-by)
        print(len(walls))
        for x,y in walls:
            print(x-bx,y-by)
        break
