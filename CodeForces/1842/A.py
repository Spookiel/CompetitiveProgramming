

t = int(input())

for i in range(t):
    n,m = list(map(int, input().split()))
    x = sum(list(map(int, input().split())))
    y = sum(list(map(int, input().split())))

    if x == y:
        print("Draw")
    elif x > y:
        print("Tsondu")
    else:
        print("Tenzing")