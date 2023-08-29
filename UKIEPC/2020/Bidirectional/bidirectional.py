
def smaller_odd(n):
    if str(n) == str(n)[::-1]:
        return str(n)
    assert len(str(n))%2==1
    mid = len(str(n))//2
    nstr = str(n)
    if nstr[mid] != "0":
        return nstr[:mid]+str(int(nstr[mid])-1)+nstr[:mid][::-1]
    else:
        for i in range(1, mid+1):
            l,r = nstr[mid-i], nstr[mid+i]
            if l != r:
                ### Set to minimum
                chosen = min(l,r)

                fhalf = nstr[:mid-i]+chosen
                res = fhalf + ((2*i-1)*"0")+fhalf[::-1]
                if int(res) != 0:
                    return res
                return smaller_even(n-1)
        raise RuntimeError()
def smaller_even(n):
    if n <= 100:
        if n==10:
            return "9"

        for j in range(99,-1,-1):
            if str(j) == str(j)[::-1] and j <= n:
                return str(j)
    if str(n) == str(n)[::-1]:
        return str(n)
    r = len(str(n))//2
    l = r-1
    res = list(str(n))
    done = 0
    while l > 0:
        if res[l] == res[r] == "0":
            l -= 1
            r += 1
            done += 1
            continue
        else:
            done += 1
            #### Reflect up to L
            return str(n)[:l] + (2*done)*"0"+str(n)[:l][::-1]
    #print("FAILED", n)
    return smaller(n-10)

def smaller(n):
    if len(str(n))%2 == 0:
        return smaller_even(n)
    else:
        return smaller_odd(n)


def solve(num):
    numc = int(num)
    ans = []
    while num:
        ne = smaller(num)
        #print(num, ne)
        assert ne == ne[::-1]
        num -= int(ne)
        ans.append(int(ne))
    print(len(ans))
    for k in ans:
        print(k)
    assert sum(ans) == numc and len(ans) <= 10

n = int(input())
solve(n)
