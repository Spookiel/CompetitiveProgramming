

n = int(input())



top = list(map(int, input().split()))
bot = list(map(int, input().split()))


def check(w, top, bot):
    comptop = []
    compbot = []

    for i in top:
        if i > w:
            comptop.append(i)
    for i in bot:
        if i > w:
            compbot.append(i)
    can = len(compbot)%2 == 0 and len(comptop)%2 == 0
    for j in range(0, len(compbot)-1, 2):
        can &= compbot[j] == compbot[j+1]
    for j in range(0,len(comptop)-1,2):
        can &= comptop[j] == comptop[j+1]
    # print(compbot)
    # print(comptop)
    return can

low = 0
high = 100000000000

while low < high:
    mid = (low+high)//2
    #print(low, mid, high, check(mid, top, bot))
    if check(mid, top, bot):
        high = mid
    else:
        low = mid+1

print(low)
