


from math import asin, acos, sin, cos, atan2, pi, sqrt
n = int(input())

coords = [list(map(int, input().split())) for i in range(n)]

EPS = 1e-8

#print(list(map(tuple, coords)))


def gen_poly(p, k):
    r = sqrt(p[0]*p[0]+p[1]*p[1])
    theta = atan2(p[1], p[0])
    points = []

    for i in range(k):
        x = r*cos(theta+ 2*i*pi / k)
        y = r*sin(theta + 2*i*pi / k)
        points.append((x,y))
    return points



def get_ang(p1, p2, p3):
    a,b = p2[0]-p1[0], p2[1]-p1[1]
    c,d = p3[0]-p1[0], p3[1]-p1[1]


    cosang = (a*c+b*d) / (sqrt(a*a + b*b)*sqrt(c*c+d*d))

    try:
        res = acos(cosang)
    except:
        res = acos(round(cosang(15)))
    return res

def check_in(v, p):

     ### Duplicate last to make loop easy
     ans = False
     for a, b in zip(v, v[1:] + v[:1]):
         if (a[1] < p[1]) != (b[1] < p[1]):
             if a[0] + (b[0] - a[0]) * (p[1] - a[1]) / (b[1] - a[1]) < p[0]:
                 ans = not ans
     return ans
        



def shoelace(points):
    tot = 0

    for i in range(len(points)-1):
        tot += points[i][0]*points[i+1][1]
        tot -= points[i+1][0]*points[i][1]
    return tot/2


def bin_search(coords, size, inside=True):


    low = 0.001
    high = 10000000

    ans = None
    while abs(high-low) > EPS:
        mid = (low+high)/2

        #print(low, mid, high)

        points = gen_poly((mid, 0), size)
        points.append(points[0])
        assert len(points) == size+1
        flag = True
        for c in coords:
            if check_in(points, c) != inside:
                flag = False
                break
        #print(len(points), size)
        assert len(points) == size+1
        if flag:
            ### This one is valid so make it bigger
            if not inside:

                ans = points
                low = mid
            else:
                high = mid
        else:

            if not inside:
                high = mid
            else:
                ans = points
                low = mid
    return ans


ans = None
res = 0
for size in range(3, 9):
    outer = bin_search(coords, size)
    inner = bin_search(coords, size, False)

    # print(size)
    # print(len(outer), list(map(lambda x: (round(x[0], 3), round(x[1],3)), outer)))
    # print(len(inner), list(map(lambda x: (round(x[0], 3), round(x[1],3)), inner)))
    if not inner or not outer:
        #print("FAILED", size)
        continue
    r = shoelace(inner)/shoelace(outer)

    if r > res:
        res = r
        ans = size
print(ans,res)




