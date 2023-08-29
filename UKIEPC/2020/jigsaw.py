

c,e,m = list(map(int, input().split()))

if c == 4:
    #print(int((m**0.5))+2)
    for f in range(1, int((m**0.5))+2):
        #print(f, m)
        if m%f == 0:
            h = f+2
            if h == 0:
                continue
            #print(h)
            w = (e+m+4)//h
            if 2*(w-2)+2*(h-2) == e and c == 4 and (w-2)*(h-2) == m and h >= 2 and w >= 2:
                print(min(w,h), max(w,h))
                exit()
    if m == 0:
        if e == 0:
            print(2,2)
        elif e%2 == 0:
            print(2,2+e//2)
        else:
            print("impossible")
    else:
        print("impossible")
else:
    print("impossible")