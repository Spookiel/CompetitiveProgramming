
def dist(p,q):
    return ((p[0]-q[0])*(p[0]-q[0])+(p[1]-q[1])*(p[1]-q[1]))**0.5
nums = list(map(int, input().split()))

a,b = nums[:4], nums[4:]
a1,a2,b1,b2 = a[:2], a[2:], b[:2], b[2:]


best = max(dist(a1, b1), dist(a1, b2))
best = max(best, dist(a2, b1))
best = max(best, dist(a2, b2))
print(best)