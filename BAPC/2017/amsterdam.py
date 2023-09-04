
from math import pi
m,n,r = list(map(float, input().split()))

sx,sy, ex,ey = list(map(int, input().split()))

RING_WIDTH = r/n


def direct(x,y, tx,ty):
    if y == 0:
        ### Go through centre
        return ty*RING_WIDTH

    ### X is which segment, Y is which ring

    arc_length = 2*pi*y*RING_WIDTH / (2*m)

    tot_circ = abs(tx-x)*arc_length
    #print(tot_circ, abs(tx-x), arc_length)
    return tot_circ+abs(y-ty)*RING_WIDTH



best = 99999999

for ycoord in range(sy+1):
    tot = ycoord*RING_WIDTH + direct(sx, sy-ycoord, ex, ey)
    best = min(tot, best)
print(best)
