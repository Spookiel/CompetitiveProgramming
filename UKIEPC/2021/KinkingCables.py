from math import sqrt
def dist(p,q):
    return sqrt(sum([pow(p[i]-q[i],2) for i in range(2)]))
n,m = list(map(int, input().split()))
l = float(input())


"""
Strategy is:

Go out to right corner and go up one, back to (0,1)
then back to (n, 1) and repeat until don't have enough wire left to 
do a full one of these.
Then just go out enough so you can get back to the y axis at (n, YCOORD)
and finish by moving up to the end. Do a bit of maths to work out the coords.

"""

# Deal with some special cases first
# Don't have enough cable to go out to right corner

if l <= n+m:
    ### Either diagonal

    if l*l == n*n+m*m:
        # Just the diagonal
        print(2)
        print(0,0)
        print(n,m)

    else:
        # Must be slightly longer
        # Just make a kink at x = 0
        print(3)
        y = (l*l-n*n-m*m)/(2*l-2*m)
        print(0,0)
        print(0, y)
        print(n,m)
    exit()
ans = [(0,0), (n,0)]

left = l - m - n  # Length left for the exciting method
for num_full in range(0,m,2):
    width_last = (left-num_full*n)/2
    if width_last < 0 or width_last > n:
        continue
    d = m-num_full-2
    if d < 0:
        continue
    lasty = 0
    # Found valid answer
    for j in range(num_full):
        direction = j%2 # 0 is for left

        ans.append((n if not direction else 0, lasty+1)) # Go up one
        ans.append((n if direction else 0, lasty+1)) # Move in the direction
        lasty += 1

    ans.append((n, lasty+1))
    ans.append((n-width_last, lasty+1))
    ans.append((n-width_last, lasty+2))
    ans.append((n, lasty+2))
    ans.append((n,m))
    break
print(len(ans))
tot = 0
assert 2 <= len(ans) <= 500
last = (0,0)
for p in ans:
    print(*p)
    tot += dist(p, last)
    last = p
#print(tot, l, "HERE", abs(tot-l))
assert abs(tot-l) < 1e-5
