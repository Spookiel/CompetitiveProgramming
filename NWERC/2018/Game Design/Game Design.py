


look = {"R":(1,0), "U":(0,1), "D":(0,-1), "L":(-1,0)}
oppo = {"L":"R", "R":"L", "D":"U", "U":"D"}
sign = {"L": -1, "R":1, "U":1, "D":-1}
walls = set()


def check_hor_range(y, sx, ex, walls):
    if sx < ex:
        for i in range(sx, ex+1):
            if (i, y) in walls:
                return i
    else:
        for i in range(sx, ex, -1):
            if (i, y) in walls:
                return i

    return ex
def check_ver_range(x, sy, ey, walls):
    if sy < ey:
        for i in range(sy, ey+1):
            if (x, i) in walls:
                return i
    else:
        for i in range(sy, ey, -1):
            if (x,i) in walls:
                return i
    return ey
def next_wall(bx, by, dir):
    dx, dy = look[dir]
    return bx+dx, by+dy

s = input()

if len(s) >= 3:
    if s[-3] == s[-1] and s[-2] == oppo[s[-1]]:
        print("impossible")
        exit()
#print(len(s))

bx, by = 0,0

bounds = 2

walls = set()
for j in range(len(s)):
    if s[j] == "U" or s[j] == "D":
        ny = sign[s[j]]*bounds*(j+1)

        acy = check_ver_range(bx, by, ny, walls)
        walls.add((bx, acy))
        by = sign[s[j]]*-1 + acy
    else:
        nx = sign[s[j]]*bounds*(j+1)

        acx = check_hor_range(by, bx, nx, walls)

        walls.add((acx,by))
        bx = sign[s[j]]*-1 + acx

print(-bx, -by)
print(len(walls))
for x,y in walls:
    print(x-bx, y-by)


# for y in range(40,-40,-1):
#     for x in range(-40, 40):
#         cx,cy = x+bx, y+by
#         if cx == 0 and cy == 0:
#             print("S", end="")
#         elif (cx,cy) in walls:
#             print("#", end="")
#         elif x == 0 and y == 0:
#             print("E", end="")
#         else:
#             print(".", end="")
#     print(y)


