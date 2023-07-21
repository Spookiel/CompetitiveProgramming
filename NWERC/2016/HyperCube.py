
n,a,b = input().split()
n = int(n)

def calc(s):

    s = s[::-1]
    ind = 0
    for i, j in enumerate(s):
        if i == 0:
            #print("REACHED", int(j))
            ind = int(j)
            continue
        if j == "0":
            continue
        elif j == "1":
            ind = 2**(i+1)-ind-1

    return ind


r1 = calc(a)
r2 = calc(b)
print(int(abs(r2-r1)-1))

