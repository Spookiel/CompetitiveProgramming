
from math import sqrt
import sys
from random import randint


n = int(input())

U = 1
def query():
    global n
    ### First check the ball isn't at one of the center circle locations

    a = randint(1, 100)
    b = randint(1, 100)



    print(a,b)
    sys.stdout.flush()
    r1s = int(input())
    if r1s == 0:
        n -= 1
        return
    print(a+1,b)
    sys.stdout.flush()
    r2s = int(input())
    if r2s == 0:
        n -= 1
        return

    ### Use the two distances to the cirlces to triangulate this point

    x = (r1s-r2s+1+2*a)/2
    #print(x, "DEBUG")
    y = sqrt(r1s-(x-a)*(x-a))

    print(int(x),int(y+b))
    sys.stdout.flush()
    dist = int(input())
    if dist == 0:
        n -= 1
        return
    print(int(x),int(b-y))
    dist = int(input())
    if dist == 0:
        n -= 1
        return


while n:
    query()
