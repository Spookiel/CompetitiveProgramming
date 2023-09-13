


### grid goes from -10 to 20
### grid goes from -10 to 20

SCALE = 10


n = int(input())

circs = []
for i in range(n):
    x,y,r = list(map(int, input().split()))
    circs.append((x,y,r))

DIM = 20*SCALE+10*SCALE
cnt = [[0 for i in range(DIM)] for j in range(DIM)]
for y in range(-10*SCALE, 20*SCALE):
    for x in range(-10*SCALE, 20*SCALE):
        for a,b,r in circs:
            if (x/SCALE-a)*(x/SCALE-a)+(y/SCALE-b)*(y/SCALE-b) <= r*r:
                cnt[y][x] += 1
                break
tot = 0
for i in cnt:
    for j in i:
        if j:
            tot += 1
print(tot/(SCALE*SCALE))
